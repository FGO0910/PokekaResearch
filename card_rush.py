# PRG1:ライブラリ設定
import json
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs

import get_html

CHROMEDRIVER = '/opt/chrome/chromedriver'
BASE_URL = 'https://www.cardrush-pokemon.jp/product-list'

with open('./card_rush.json') as f:
    card_list = json.load(f)
    
for card in card_list:
    # キーワードをURLにセット
    url = BASE_URL + '?keyword=' + card['keyword']
    # リクエストしてWebページのHTMLを取得
    html = get_html.get_html(url)

    # Beautifulsoupで要素取得
    soup = bs4(html, 'html.parser')
    items_list = soup.find_all('div', class_='item_data')
    for i, item in enumerate(items_list):
        text = item.find('span', class_='goods_name').text
        if '状態' in text:
            continue
        price = int(item.find('span', class_='figure').text.replace('円', '').replace(',', ''))
        img_src = item.find('img').get('src')
        print(text)
        print(price)
        print(img_src)