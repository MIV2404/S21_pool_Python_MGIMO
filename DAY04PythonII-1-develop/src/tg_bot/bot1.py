import telebot

def GET_TOKEN():
    with open('../token_bot.txt', 'r', encoding='utf-8') as file:
        token = file.readline()
    return token

# Выполни несколько заданий в одном файле
# Ты будешь постепенно добавлять функционал в своего бота!

# ЗАДАНИЕ #1
# Заведи телеграмм бота (обратись, но с УВАЖЕНИЕМ, к @BotFather). Он, возможно, выдаст тебе токен
# Никому не передавай свой токен. Добавь его в файл token.txt. НЕ ЗАБУДЬ УДАЛИТЬ ФАЙЛ ПЕРЕД ОТПРАВКОЙ ЗАДАНИЯ В УДАЛЁННЫЙ РЕПОЗИТОРИЙ!
# Сделай так чтобы бот обрабатывал базовую команду /start и что-то отвечал "Готов!" или иное. Это будет "активацией" бота
# Напиши бота-пересмешника, который возвращает тот текст, который ввёл пользователь
# Например, Пользователь ввёл "Привет", бот ответил "Привет". Пользователь спросил "Как дела?", бот в ответ "Как дела?"
bot = telebot.TeleBot(GET_TOKEN())

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message,  "Привет!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()