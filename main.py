import os
from argparse import ArgumentParser
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def create_parser():
    parser = ArgumentParser(description='Сокращение ссылкок и вывод статистики кликов')
    parser.add_argument('url', help='ссылка для анализа')

    args = parser.parse_args()
    return args


def shorten_url(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    payload = {'long_url': url}
    base_url = 'https://api-ssl.bitly.com/v4/bitlinks/'

    response = requests.post(base_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = {
        'unit': 'month',
        'units': '-1',
    }

    url_domain = urlparse(url).netloc
    url_path = urlparse(url).path
    base_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    url = f'{base_url}{url_domain}{url_path}/clicks/summary'

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def check_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    url_domain = urlparse(url).netloc
    url_path = urlparse(url).path
    base_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    url = f'{base_url}{url_domain}{url_path}'

    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    
    token = os.environ['BT_TOKEN']
    args = create_parser()
    check_link = check_bitlink(token, args.url)
    try:
        if check_link:
            print('Количество кликов по ссылке: ', count_clicks(token, args.url))
        else:
            scheme = urlparse(args.url).scheme
            if not scheme:
                url = f'http://{args.url}'
            print('Сокращенная ссылка:', shorten_url(token, url))
    except requests.exceptions.HTTPError:
        print('Cсылка введена некорректно')


if __name__ == '__main__':
    main()
