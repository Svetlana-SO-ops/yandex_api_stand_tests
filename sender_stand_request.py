# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests,который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests
# Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается
# из базового адреса сервиса и пути к его документации, оба определены в модуле
# конфигурации. Затем он выводит HTTP-статус код ответа от сервера, который указывает
# на результат выполнения запроса.

import data

# from requests.adapters import HTTPAdapter, Retry
# s = requests.Session()
# retries = Retry(total=5,
#                 backoff_factor=0.1,
#                 status_forcelist=[ 500, 502, 503, 504 ])
# s.mount('*', HTTPAdapter(max_retries=retries))


# Определяем функцию get_docs, которая не принимает параметров
def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


# Вызываем функцию get_docs и сохраняем результат в переменную response
response = get_docs()

# Выводим в консоль HTTP-статус код полученного ответа
# Например, 200 означает успешный запрос, 404 - не найдено и т.д.
# print(response.status_code)

# Импортируем необходимые библиотеки и модули
# import requests
# import configuration


#Определяем функцию get_logs, которая отправляет GET-запрос к серверу для получения логов
def get_logs():
    # Складываем базовый URL из конфигурационного файла и путь к основным логам,
    # чтобы сформировать полный URL для запроса.
    # Возвращает объект ответа, полученный от сервера после выполнения GET-запроса
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)


# Вызываем функцию get_logs и сохраняем ответ сервера в переменную response
# response = get_logs()

# Выводим в консоль HTTP-статус код ответа сервера. Коды состояния HTTP сообщают
# о результате выполнения запроса. Например, код 200 означает "OK", а 404 - "Не найдено".
# print(response.status_code)

# Выводим в консоль заголовки HTTP-ответа сервера.
# Заголовки могут содержать полезную информацию, например, тип содержимого ответа
# и используемые сервером технологии.
# print(response.headers)

# Импорт модуля requests для отправки HTTP-запросов
# import requests
# Импорт конфигурационного файла, который содержит настройки URL
# import configuration


# Функция для получения данных из таблицы пользователей
def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


# Выполнение функции и сохранение ответа в переменную response
response = get_users_table()

# Вывод статус-кода ответа сервера в консоль
# Статус-коды HTTP сообщают о результате выполнения запроса
print(response.status_code)

# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
# import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
# import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
# import data


# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    #    print("URL: " + configuration.URL_SERVICE + configuration.CREATE_USER_PATH)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(response.status_code)

# Функция response.json() позволяет получить тело ответа в формате JSON.
# Это полезно для извлечения данных, полученных в результате запроса,
# особенно когда сервер возвращает полезные данные в формате JSON.
# Здесь мы вызываем эту функцию и выводим полученный JSON в консоль для наглядности.
print(response.json())
