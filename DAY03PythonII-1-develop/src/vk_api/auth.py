import vk

def GET_TOKEN():
    # Допиши код
    # В файле materials/token.txt лежит токен (если такого файла нет прочти информацию в materials/README.md)
    # Прочитай файл и верни токен (строка)
    with open('../token.txt', 'r', encoding='utf-8') as file:
        token = file.readline()
    return token

# print(GET_TOKEN())

if __name__ == '__main__':
    api = vk.API(access_token=GET_TOKEN(), v='5.131')
    print(api.users.get(user_ids='1'))
# Выведи информацию на экран по примеру из документации
# https://vk.readthedocs.io/en/latest/usage.html#api-method-request-example
# Можешь вывести информацию о Павле Дурове либо о себе 8)
