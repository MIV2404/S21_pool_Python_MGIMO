from bs4 import BeautifulSoup
import requests


# Используй функцию из прошлого задания, чтобы получить html-текст страницы согласно варианту из файла variants.md
def get_html_code(link):
    headers = {'User-Agent': "PostmanRuntime/7.32.3",
                'referer': 'https://www.google.com/'}
    # Используй функцию с прошлого задания
    pass

link = ...  # Используй ссылку и задание согласно варианту из файла materials/variants.md

# Обработай полученный текст с помощью объекта BeautifulSoap
soup = BeautifulSoup(get_html_code(link), 'html.parser')
# Выведи DOM-дерево

# Изучив дерево, определи теги, необходимые для решения задачи согласно варианту


# Важно!
# Тебе могут помочь методы: find(), find_all(), unwrap() и другие
# Также почитай про parent тэг в документации BeautifulSoap 
# https://beautiful-soup-4.readthedocs.io/en/latest/
