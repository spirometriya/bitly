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
    return response.json().get("link")


def count_clicks(token, link):
    parse_url = urlparse(link)
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_URL}{parse_url.netloc}{parse_url.path}/clicks/summary", headers=headers)
    response.raise_for_status()
    return response.json().get("total_clicks")


def is_bitlink(token, url):
    parse_url = urlparse(url)
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_URL}{parse_url.netloc}{parse_url.path}", headers=headers)
    if response.ok:
        return True


if __name__ == '__main__':
    load_dotenv()
    token = os.environ["BITLY_BEARER_TOKEN"]
    url = input()
    if not is_bitlink(token, url):
        try:
            url = shorten_link(token, url)
            print(f"Short url: {url}")
        except requests.HTTPError:
            print("Invalid url for shortening!")
    try:
        click_count = count_clicks(token, url)
        print(f"Your url was clicked {click_count} time(s)")
    except requests.HTTPError:
        print(f"Could not get the number of clicks for {url}")
