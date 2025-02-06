# Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.
# from itertools import count

import requests

# params = {"q": "html"}
#
# response = requests.get("https://api.github.com/search/repositories", params=params)
# response_json = response.json()
#
# print(response.status_code)
# print(f'Количество репозиториев с html: {response_json["total_count"]}')


# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

# url = "https://jsonplaceholder.typicode.com/posts"
# params = {"userId": 1}
# response = requests.get(url, params=params)
# response_json = response.json()
# print(response.status_code)
# print(response_json)

# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа.
import json
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, data=data)

print(response.status_code)
print(json.dumps(response.json(), indent=3))