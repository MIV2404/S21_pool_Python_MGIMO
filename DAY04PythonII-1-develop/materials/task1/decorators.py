from num2words import num2words


def decor_num2words(func):
    def inner(text : str):
        # Напиши код, который позволяет заменять в тексте численные значения (1, 2, 1 000 000) на текст (one, two, one million)
        # Используй библиотеку num2words
        # Тебе потребуется отфильтровать текст и найти только те литералы, которые являются числами 
        # Проверка на цифры/числа есть в Python'e. Найди её и воспользуйся
        text_filtered = ...
        # Затем текст попадает в другую функцию, не изменяй текст, который был на входе!
        # Используй новую переменную - text_filtered
        return func(text_filtered)
    return inner

@decor_num2words
def get_tokens(text : str):
    # Раздели текст на отдельные слова (токены)
    pass

@decor_num2words
def get_unique_tokens(text : str):
    # Раздели текст на отдельные слова (токены)
    # Но все слова должны быть уникальными. Никаких повторений!
    pass

@decor_num2words
def remove_punctuation_marks(text : str):
    # Убери все пунктуационные знаки из текста
    # Мы рекомендуем использовать такой набор знаков '.,?!;-'
    pass


nlp_text = "30 days has September,\
    April, June and November.\
    February has 28 alone.\
    All the rest have 31,\
    But leap year coming once in 4,\
    Gives February 1 day more.\
    ...\
    8,000,000,000 live on earth.\
    Why not? There is room to space.\
    And our views on this or that\
    Are different here and there.\
    But we are all for honest work,\
    We love the same blue sky\
    In Minsk, Moscow and Beijing -\
    So keep our friendship high !"


# Выведи
# 1) Значение переменной filtered_text
# 2) Набор токенов
# 3) Размер набора токенов
# 4) Размер набора уникальных токенов
