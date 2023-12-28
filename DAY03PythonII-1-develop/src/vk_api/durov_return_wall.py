import vk
from auth import GET_TOKEN
from account_info import get_info
import requests

api = vk.API(access_token=GET_TOKEN(), v='5.131')

# публикация поста текста на стену
post_massage = api.wall.post(message="Hello_World!\nI'm testing VK_API")

# публикация фото на стену
info = api.photos.getWallUploadServer()
url = info['upload_url']
req = requests.post(url, files={'file': open('src/hw.png', 'rb')})
id = get_info(GET_TOKEN())['id']
save_wall_photo = api.photos.saveWallPhoto(user_id = id, v='5.131',
                                           photo=req.json()['photo'],
                                           server=req.json()['server'],
                                           hash=req.json()['hash'])
saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
api.wall.post(owner_id=id, v='5.131', attachments=saved_photo)

# Опубликуй пост на своей странице
# Например, "Учу Python вместе с друзьями! VkAPI - мощь! #PythonProof"
# И второй пост, содержащий какой-либо медиа-контент (фото, гифка и др.)
# используй авторизацию и методы, описанные в документации
# https://dev.vk.com/ru/method (<- Документация)
