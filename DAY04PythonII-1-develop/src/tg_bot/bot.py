import telebot
import random
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

users = {}

def GET_TOKEN():
    with open('../token_bot.txt', 'r', encoding='utf-8') as file:
        token = file.readline().strip()
    return token

bot = telebot.TeleBot(GET_TOKEN())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global users
    id = message.from_user.id
    users[id] = users.get(id, {})
    users[id]['age'] = users[id].get('age', None)

    bot.reply_to(message, "Привет!\n Я бот Super_bot_project\nесть команды:\n/age\n/name\n/predict\n/minigame\n/help")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/age':
        bot.reply_to(message, 'Введите Ваш возраст\nОн должен быть целым числом в диапазоне [5;150] лет')
        bot.register_next_step_handler(message, saver_age)
    elif message.text == '/name':
        bot.reply_to(message, 'Введите Ваше имя или псевдоним')
        bot.register_next_step_handler(message, saver_name)
    elif message.text == '/predict':
        bot.reply_to(message, predict_age(message))
    elif message.text == '/help':
        bot.reply_to(message, 'Есть команды:\n/age\n/name\n/predict\n/minigame\n/help')
    elif message.text == '/minigame':
        minigame(message)
    else:
        bot.reply_to(message, message.text)

def saver_age(message):
    global users
    id = message.from_user.id
    if message.text.isdigit() and 5 <= int(message.text) <= 150:
        users[id] = users.get(id, {})
        users[id]['age'] = int(message.text)
    else:
        bot.reply_to(message, 'Сказали же:\nВведите ваш возраст\nОн должен быть целым числом в диапазоне [5;150] лет\nЕсли хотите ввести возраст - повторите команду')

def saver_name(message):
    id = message.from_user.id
    if message.text:
        users[id] = users.get(id, {})
        users[id]['name'] = message.text

def predict_age(message):
    global users
    id = message.from_user.id
    name = users[id].get('name', '')
    if name:
        name = ', ' + name + ','
    if 'age' in users[id] and users[id]['age']:
        age = users[id]['age']
        current_year = 2023
        year = random.randint(current_year, current_year + 100)
        d_age = year - current_year
        age += d_age
        return f'Я вижу, вижу, что Вам{name} в {year} будет {age}!'
    return 'Для использования команды /predict\nсначала нужно ввести возраст\nкомандой /age'

def minigame(message):
    markup_start = InlineKeyboardMarkup(row_width=2)
    item_start = InlineKeyboardButton('Начать', callback_data='go')
    item_exit = InlineKeyboardButton('Прекратить', callback_data='stop')

    markup_start.add(item_start, item_exit)

    bot.send_message(message.chat.id, '''Добро пожаловать в игру!
    Ход игры:
    Загадайте целое число из диапазона [1;100]
    Я пытаюсь его отгадать - делаю предположение, а Вы отвечаете:
    нажатием кнопок <Больше>, <Меньше> или <Отгадал>
    Чтобы отгадать Ваше число мне потребуется не более 7 попыток
    Только давай играть честно
    Чтобы прекратить игру Вы можете воспользоваться кнопкой <Выйти>''',
    reply_markup=markup_start)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'go':
            process_game(call, 1, 100)
        elif call.data.startswith('hi_'):  # обработка кнопки "Больше"
            mid = int(call.data.split('_')[1])
            process_game(call, mid + 1, 100)
        elif call.data.startswith('low_'):  # обработка кнопки "Меньше"
            mid = int(call.data.split('_')[1])
            process_game(call, 1, mid - 1)

def process_game(call, left, right):
    if call.message:
        if left <= right:
            mid = (right + left) // 2

            markup = InlineKeyboardMarkup(row_width=2)
            item_h = InlineKeyboardButton('Больше', callback_data=f'hi_{mid}')  # передаем текущее предположение в callback_data
            item_l = InlineKeyboardButton('Меньше', callback_data=f'low_{mid}')  # передаем текущее предположение в callback_data
            item_a = InlineKeyboardButton('Отгадал', callback_data='accept')
            item_exit = InlineKeyboardButton('Выйти', callback_data='stop')
            markup.add(item_h, item_l, item_a, item_exit)
            bot.send_message(call.message.chat.id, f'Предполагаю, что число {mid}?', reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, '''Странно, но я не могу отгадать Ваше число
            при условии, что Вы меня не вводили в заблуждение
            Если хотите, можете попробовать сыграть снова''')

bot.polling()

# ЗАДАНИЕ #2
# После того как бот-пересмешник готов. Давай добавим новый функционал. Необходимо завести функции, которые обрабатывают команды:
# a) /age
# б) /name
# в) /help
# Первая предлагает пользователю ввести возраст (подумай как считать ответ и к какому типу его привести),
# вторая предлагает пользователю ввести имя (подумай как считать ответ)
# третья выводит информацию о всех командах, которые поддерживает бот
# Данные о пользователе будем запоминать в глобальную переменную users - словарь, где ключ - это ID пользователя, 
# а значение - словарь из двух элементов: age, name; которые соответствуют значениям, введённым пользователем
# Давай используем эти данные для новой функции
# будем обрабатывать команду /predict, которая будет выводить следующий текст:
# "Я вижу, вижу, что Вам, {name}, в {year} будет {age}!"
# где name - это имя пользователя,
# year - рандомный год (целое число!) в диапазоне от [текущий год; текущий год + 100]
# age - возраст пользователя в year году
# То есть для пользователя Имярек, которому в 2000 году 20 лет бот может выдать следующий результат:
# "Я вижу, вижу, что Вам, Имярек, в 2020 будет 40!"
# Обработать случай если /age, /name пустые! 


# Задание #3
# Давай перенесём команду /help в отдельное меню (Menu), как у @BotFather
# Посмотри в Интернете как создать такое меню (Подсказка: для решения задачи необходимо обратиться С УВАЖЕНИЕМ к Отцу всех ботов =])
# После создания меню перейдём к созданию нового интерактива с ботом - кнопки! (возможно тебе понадобится дополнительный модуль - используй конструкцию import ... или from ... import ...)
# Добавь новую команду (/minigame), чтобы поиграть с пользователем в угадайку: пользователь загадывает число от 1 до 100, а бот пытается отгадать
# Пусть каждый ответ бота имеет три inline кнопки: Больше, Меньше, Ответ
# И игра продолжается пока пользователь не нажмёт кнопку "Ответ" (подумай как бот должен отгадывать число, рандом тут может сыграть злую шутку!)


# Задание #4 
# Добавим дополнительные кнопки в интерфейс нашего бота (reply кнопки)
# Пусть при вводе команды /start бот здоровается с пользователем по никнейму в TG (first & last name пользователя)
# У бота должны отображаться (под строкой ввода текста) несколько кнопок:
# 1) Поздороваться в ответ (при нажатии бот отвечает пользователю, что у того хорошие манеры)
# 2) Что ты умеешь? (Выводит информацию о доступных командах и переводит в подменю, где команды заданы в виде кнопок)
# При нажатии на кнопку 2 меню меняется на иное:
# 1) набор кнопок, соответствующих командам /help, /minigame и др.
# 2) кнопка возврата в начальное меню

# Ты можешь вынести функцию пересмешника в отдельный блок (например, /mockingbird) либо оставить в основном блоке обработки сообщений
# НО не удаляй эту функциональность (а вот token.txt удали перед отправкой на удалённый репозиторий)
# Функциональность предсказателя также не убирай!

# Да прибудет с тобой сила, Python-разработчик!
