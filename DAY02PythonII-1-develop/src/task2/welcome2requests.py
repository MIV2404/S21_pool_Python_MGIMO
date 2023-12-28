from requests import get

# Допиши код
# Напиши get-запрос (HTTP GET) с использование ссылки (link) согласно варианту из файла materials/variants.md
# Проверь, что запрос вернул код OK
# И верни html-текст
# Если вернулась ошибка (не OK), то сообщи об этом пользователю и вызови ошибку (raise RuntimeError)
def get_html_code(link):
    # Это поможет тебе избежать некоторых ошибок
    headers = {'User-Agent': "PostmanRuntime/7.32.3",
                'referer': 'https://www.google.com/'}
    res = get(link, headers=headers)
    # Вызывай get запрос с параметром headers=headers
    if res.status_code == 200:  # проверь результат
        return(res.text)
    else:    # вызови ошибку
        raise RuntimeError

link = "https://web.archive.org/web/20230903112115/https://iz.ru/news"

print(get_html_code(link))
