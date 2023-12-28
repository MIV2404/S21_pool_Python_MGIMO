from num2words import num2words


def decor_num2words(func):
    def inner(text : str):
        # Напиши код, который позволяет заменять в тексте численные значения (1, 2, 1 000 000) на текст (one, two, one million)
        # Используй библиотеку num2words
        # Тебе потребуется отфильтровать текст и найти только те литералы, которые являются числами 
        # Проверка на цифры/числа есть в Python'e. Найди её и воспользуйся
        lst_text = text.split()
        for n, word in enumerate(lst_text):
            str_add = ""
            for chunk in word.split(','):
                if chunk.isdigit():
                    str_add += chunk
            if str_add:
                lst_text[n] = num2words(int(str_add))
            if lst_text[n].isdigit():
                lst_text[n] = num2words(int(lst_text[n]))
            if word[-1] == ',' and word[-2].isdigit():
                lst_text[n] = num2words(int(word[:-1])) + ','
        text_filtered = ' '.join(lst_text)
        # Затем текст попадает в другую функцию, не изменяй текст, который был на входе!
        # Используй новую переменную - text_filtered
        return func(text_filtered)
    return inner

@decor_num2words
def get_tokens(text : str):
    # Раздели текст на отдельные слова (токены)
    return remove_punctuation_marks(text).split()

@decor_num2words
def get_unique_tokens(text : str):
    # Раздели текст на отдельные слова (токены)
    # Но все слова должны быть уникальными. Никаких повторений!
    result = {k: None for k in get_tokens(text)}
    result = list(result.keys())
    return result

@decor_num2words
def remove_punctuation_marks(text : str):
    # Убери все пунктуационные знаки из текста
    # Мы рекомендуем использовать такой набор знаков '.,?!;-'
    result = ""
    for symbol in text:
        if symbol in '.,?!;-':
            continue
        result += symbol
    return result

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

@decor_num2words
def print_ret(text: str):
    return text

print(print_ret(nlp_text)) # Значение переменной filtered_text
# print()
# print(remove_punctuation_marks(nlp_text))
print(get_tokens(nlp_text)) # Набор токенов
print(len(get_tokens(nlp_text))) # Размер набора уникальных токенов
print(len(get_unique_tokens(nlp_text))) # Размер набора уникальных токенов

# Выведи
# 1) Значение переменной filtered_text
# 2) Набор токенов
# 3) Размер набора токенов
# 4) Размер набора уникальных токенов
