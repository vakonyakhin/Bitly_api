# Учебный проект. Сокращение ссылок с помощью Bit.ly
Данный код позволяет создавать сокращенные ссылки используя 
[bit.ly API](https://dev.bitly.com/api-reference).

## Как установить
Python3 уже должен быть установлен. Рекомендуется использовать venv для изоляции проекта

Затем используйте pip/poetry для установки зависимостей

    python3 -m poetry install

или

    pip install -r requirements.txt

## Цель проекта
В рамках изучения библиотеки requests

## Пример запуcка из командной строки: 
**Для запуcка необходимо получить токен в личном кабинете на сайте bit.ly - https://bitly.is/accesstoken. Для скрытия токена используется .env файл с переменной BT_TOKEN**

    from dotenv import load_dotenv
    
    load_dotenv()
    TOKEN = os.environ['BT_TOKEN']
    
Для запуска программы используйте ссылку:

    python main.py ya.ru

или

    python main.py bit.ly/3wCjHBK

## Описание аргументов:
 - url - Название ссылки для сокращения или bitlink для получения статистики кликов.

**Параметр обязателен для заполнения**
