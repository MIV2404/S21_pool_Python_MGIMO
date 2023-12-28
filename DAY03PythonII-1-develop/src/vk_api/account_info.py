import vk
from auth import GET_TOKEN

def get_info(token):
    api = vk.API(access_token=token, v='5.131')
    info = api.account.getProfileInfo()

    dct = {'full_name': info['first_name'] + ' ' + info['last_name'],
            'sex': ['не указан', 'женский', 'мужской'][info['sex']],
            'relation' : ['не указано', 'не женат/не замужем', 'есть друг/есть подруга', 'помолвлен/помолвлена', 'женат/замужем', 'всё сложно', 'в активном поиске', 'влюблён/влюблена', 'в гражданском браке'][info['relation']],
            'bdate' : info['bdate'],
            'home_town' : info['home_town'],
            'country' : info['country']['title'],
            'status' : info['status'],
            'phone' : info['phone'],
            'id' : info['id']}
    return dct

if __name__ == '__main__':

    dct = get_info(GET_TOKEN())
    print(f'''ФИО: {dct['full_name']}
    Пол: {dct['sex']}
    Семейное положение: {dct['relation']}
    Дата рождения: {dct['bdate']}
    Родной город: {dct['home_town']}
    Страна: {dct['country']}
    Статус: {dct['status']}
    Номер телефона: {dct['phone']}''')

# Выведи информацию о текущем пользователе (ФИО, дата рождения, место жительства и т.д.),
# используй авторизацию и методы, описанные в документации
# https://dev.vk.com/ru/method (<- Документация)
