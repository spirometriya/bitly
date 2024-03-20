import argparse
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse

API_URL = "https://api-ssl.bitly.com/v4/bitlinks/"


def shorten_link(token, url):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"long_url": url}
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    if response.ok:
        return response.json().get("link")


def count_clicks(token, link):
    domain = urlparse(link).netloc
    path = urlparse(link).path
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_URL}{domain + path}/clicks/summary", headers=headers)
    response.raise_for_status()
    if response.ok:
        return response.json().get("total_clicks")


def is_bitlink(url):
    domain = urlparse(url).netloc
    return True if domain == "bit.ly" else False


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv("token")
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Any url')
    args = parser.parse_args()
    url = args.url
    if is_bitlink(url):
        try:
            click_count = count_clicks(token, url)
            print(f"По Вашей ссылке перешли {click_count} раз")
        except:
            print(f"Не удалось получить количество переходов для {url}")
    else:
        try:
            bitlink = shorten_link(token, url)
            print(f"Сокращенная ссылка: {bitlink}")
        except:
            print("Некорректная ссылка для сокращения!")
        try:
            click_count = count_clicks(token, bitlink)
            print(f"По Вашей ссылке перешли {click_count} раз")
        except:
            print(f"Не удалось получить количество переходов для {bitlink}")
