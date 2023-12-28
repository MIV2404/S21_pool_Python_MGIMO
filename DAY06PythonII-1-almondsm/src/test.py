import requests
import telebot
from telebot import types
from time import strftime
from dotenv import load_dotenv
import os
import base64
import sys
import json

load_dotenv()

TOKEN_CORTEX = os.getenv('TOKEN_CORTEX')
TOKEN_STABILITY = os.getenv('TOKEN_STABILITY')
TOKEN_TG = os.getenv('TOKEN')
PROMPT = "random picture"
user_language = {}


def check_tokens() -> bool:
    """Проверка наличия всех необходимых токенов"""
    are_all_tokens = True
    TOKENS = {'TOKEN_TG': TOKEN_TG,
                'TOKEN_CORTEX' : TOKEN_CORTEX,
                'TOKEN_STABILITY' : TOKEN_STABILITY
              }
    for token in TOKENS.values():
        if not token:
            are_all_tokens = False
    return are_all_tokens


def response_parser(response: requests) -> str:
    """Парсинг ответа полученного от кортекс"""
    response = response.json().get('data').get('outputs')
    return response[0].get('text')


def log_response(message: str) -> None:
    """Логирует запрос и время его получения"""
    time_of_response = strftime("%Y/%m/%d, %H:%M:%S")
    with open('log_response.txt', 'a+') as file:
        file.writelines(f"{time_of_response}   {message}\n")


def get_response_from_cortex(bot, chat_id: int, message: str) -> str:
    """POST запрос к нейросети для перевода текста"""
    url = 'https://api.textcortex.com/v1/texts/translations'

    payload = {
        "source_lang": "ru",
        "target_lang": "en",
        "text": message
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_CORTEX}"
    }
    try:
        response = requests.request("POST", url, json=payload, headers=headers)
    except ConnectionError:
        print("Incorrect url")

    if response.status_code != 200:
        bot.send_message(chat_id, 'невозможно перевести текст')
        raise Exception('Non-200 response: ' + str(response.text))

    return response_parser(response)


def get_response_from_stability(bot, chat_id: int, message: str) -> None:
    """Делает пост запрос к нейросети для генерации картинки"""
    ENNGINE_ID = 'stable-diffusion-v1-6'
    domain = 'https://api.stability.ai'
    link = f'{domain}/v1/generation/{ENNGINE_ID}/text-to-image'

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN_STABILITY}"
    }

    payload = {
        "text_prompts": [
            {
                "text": message
            }
        ],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30,
    }
    
    try:
        response = requests.post(
            link,
            headers=headers,
            json=payload,
        )
    except ConnectionError:
        print("Incorrect url")
    if response.status_code == 200:
        data = response.json()
        with open(f'./image.png', 'wb') as file:
            file.write(base64.b64decode(data["artifacts"][0]["base64"]))
        send_foto(bot, chat_id)
        # os.remove('./image.png')
    elif response.json()['message'] == 'Invalid prompts detected':
        bot.send_message(chat_id, 'Ошибка запроса, проверьте настройки языка \
и содержимое запроса')
    elif response.status_code != 200:
        raise Exception('Non-200 response: ', response.status_code)


def send_foto(bot, chat_id:int )-> None:
    """Отправка картинки пользователю"""
    with open(f"./image.png", 'rb') as photo:
        bot.send_photo(chat_id, photo)
    os.remove("./image.png")


def create_setup_dict():
    """Создание словаря хранящего настройки пользователей"""
    try:
        with open('users_settings.json', 'r') as file:
            if os.path.getsize('users_settings.json') != 0:
                user_language_json = file.read()
        user_language = json.loads(user_language_json)
    except FileNotFoundError:
        file = open('users_settings.json', 'w')
        file.close()


def update_file():
    """Обновление файла хранящего настройки пользователей"""
    with open('users_settings.json', 'w') as file:
        user_language_json = json.dumps(user_language)
        file.write(user_language_json)


def main():
    """Основная логика работы бота"""
    # проверить все токены если их нет, то завершить программу
    if not check_tokens():
        sys.exit('В локальном окружении нет необходимых токенов')
    bot = telebot.TeleBot(TOKEN_TG)

    create_setup_dict()

    @bot.message_handler(commands=['start', 'help', 'language', 'random'])
    def handle_commands(message):
        chat_id = message.from_user.id
        if message.text == '/start':
            user_language.setdefault(chat_id, "english")
            update_file()
            set_language(message)
            set_random(message)
        elif message.text == '/help':
            bot.send_message(chat_id, '/language - выбрать язык \n'
                             '/help - получить справку \n')
        elif message.text == '/language':
            set_language(message)

    def set_language(message):
        """Функция для отправки inline клавиатуры выбора языка"""
        chat_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('English', callback_data='english')
        btn2 = types.InlineKeyboardButton('Русский', callback_data='russian')
        markup.add(btn1, btn2)
        bot.send_message(
            chat_id, "Выберете язык. Select a language", reply_markup=markup)
    
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback_query(call):
        """Обработчик callback-запросов"""
        chat_id = call.message.chat.id
        global user_language  # <---- !!!!!!!!!!!!!!!!!!!!!!!!!
        if call.data == 'english':
            user_language[chat_id] = 'english'
            bot.send_message(chat_id, "Welcome!")
        elif call.data == 'russian':
            user_language[chat_id] = 'russian'
            bot.send_message(chat_id, 'Добро пожаловать!')
        update_file()

        # Убираем inline клавиатуру после выбора языка
        bot.edit_message_reply_markup(
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=None
        )

    @bot.message_handler(commands=['random'])
    def set_random(message):
        """Обработчик команды /random"""
        chat_id = message.from_user.id
        language = user_language.get(
            chat_id, 'english')  # По умолчанию английский
        button_text = "I'll get lucky!" if language == 'english' else "Мне повезет!"

        reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(button_text)
        reply_markup.add(btn1)

        if language == 'english':
            message_text = "if you want get random picture, press the button" 
        else:
            message_text = 'Чтобы получить случайное изображение нажмите кнопку'

        bot.send_message(chat_id, message_text, reply_markup=reply_markup)

    @bot.message_handler(
            func=lambda message: message.text in ["Мне повезет!", "I'll get lucky!"])
    def handle_random_image(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Подождите, генерирую картинку...')
        get_response_from_stability(bot, chat_id, PROMPT)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        """Перовод текста, если это необходимо. Вызов ф-и генерация картинки"""
        chat_id = message.from_user.id
        log_response(message.text)

        # если язык не англ, то вызываем перевод
        if user_language.get(chat_id) != 'english':
            response_from_cortex = get_response_from_cortex(
                bot, chat_id, message.text
                )
        else:
            response_from_cortex = message.text
        bot.send_message(chat_id, 'Подождите, генерирую картинку...')
        get_response_from_stability(bot, chat_id, response_from_cortex)

    bot.infinity_polling()


if __name__ == '__main__':
    main()
