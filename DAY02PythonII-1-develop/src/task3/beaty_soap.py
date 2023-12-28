from bs4 import BeautifulSoup
from requests import get as get_req


# Используй функцию из прошлого задания, чтобы получить html-текст страницы согласно варианту из файла variants.md
def get_html_code(link):
    headers = {'User-Agent': "PostmanRuntime/7.32.3",
                'referer': 'https://www.google.com/'}
    # Используй функцию с прошлого задания
    res = get_req(link, headers=headers)
    # Вызывай get запрос с параметром headers=headers
    if res.status_code == 200:  # проверь результат
        return(res.text)
    else:    # вызови ошибку
        raise RuntimeError

link = "https://web.archive.org/web/20230903112115/https://iz.ru/news" # Используй ссылку и задание согласно варианту из файла materials/variants.md
site = "https://web.archive.org"

# Обработай полученный текст с помощью объекта BeautifulSoap
soup = BeautifulSoup(get_html_code(link), 'html.parser')
# Выведи DOM-дерево
print(soup.prettify(), end='\n')
# Изучив дерево, определи теги, необходимые для решения задачи согласно варианту
# search = BeautifulSoup.find_all(soup, class_ = 'node__cart__item')
# search = BeautifulSoup.find_all(search, 'a')
# print(search)

dct = {}

for n, link in enumerate(soup.find_all('div', {'class':"node__cart__item show_views_and_comments"})):
    block_a = link.find_all('a')[1]
    news = block_a.find('span').text
    theme = link.find_all('a')[0].text
    link_news = site + block_a.attrs['href']
    dct[theme] = dct.get(theme, []) + [[news, link_news]]

for theme, content in dct.items():
    print(theme)
    # print(v)
    for news in content:
        print('-', news[0], '\n  ', news[1])
 
# Важно!
# Тебе могут помочь методы: find(), find_all(), unwrap() и другие
# Также почитай про parent тэг в документации BeautifulSoap 
# https://beautiful-soup-4.readthedocs.io/en/latest/
