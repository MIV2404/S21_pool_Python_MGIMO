import telebot

# Выполни несколько заданий в одном файле
# Ты будешь постепенно добавлять функционал в своего бота!

# ЗАДАНИЕ #1
# Заведи телеграмм бота (обратись, но с УВАЖЕНИЕМ, к @BotFather). Он, возможно, выдаст тебе токен
# Никому не передавай свой токен. Добавь его в файл token.txt. НЕ ЗАБУДЬ УДАЛИТЬ ФАЙЛ ПЕРЕД ОТПРАВКОЙ ЗАДАНИЯ В УДАЛЁННЫЙ РЕПОЗИТОРИЙ!
# Сделай так чтобы бот обрабатывал базовую команду /start и что-то отвечал "Готов!" или иное. Это будет "активацией" бота
# Напиши бота-пересмешника, который возвращает тот текст, который ввёл пользователь
# Например, Пользователь ввёл "Привет", бот ответил "Привет". Пользователь спросил "Как дела?", бот в ответ "Как дела?"


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
