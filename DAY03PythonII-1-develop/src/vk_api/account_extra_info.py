import vk
from auth import GET_TOKEN

api = vk.API(access_token=GET_TOKEN(), v='5.131')
groups = api.groups.get(extended=1)
groups_count = groups['count']
friends =  api.friends.get(fields='photo_200_orig')
friends_count = friends['count']
# print(friends)

print(f'Количество групп: {groups_count}')

for n, group in enumerate(groups['items'], start=1):
    link = 'https://vk.com/club' + str(group["id"]) + '?from=quick_search'
    print(f'''{n} Название группы: {group["name"]}
    Ссылка на группу: {link}
    Ссылка на фото группы:  {group["photo_200"]}''')

print(f'Количество друзей: {friends_count}')

for n, friend in enumerate(friends['items'], start=1):
    full_name = friend['first_name'] + friend['last_name']
    link = 'https://vk.com/id' + str(friend["id"])
    print(f'''{n} {full_name}
    Ссылка на профиль: {link}
    Ссылка на фото:  {friend["photo_200_orig"]}''')

# Выведи информацию СВЯЗАННУЮ с текущим пользователем (Кол-во и список его групп, друзей. Фото и ссылки на них),
# используй авторизацию и методы, описанные в документации
# https://dev.vk.com/ru/method (<- Документация)
