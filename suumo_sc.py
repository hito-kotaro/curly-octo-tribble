import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
SEARCH_URL = os.getenv('SEARCH_URL')
PAGE_START = int(os.getenv('PAGE_START'))
PAGE_LIMIT = int(os.getenv('PAGE_LIMIT'))

EXPORT_CSV_PATH = "./result/"
EXPOR_FILE_PREFIX = "SUUMO_"
BASE = 'https://suumo.jp'

current_page = PAGE_START

# 結果を突っ込む配列
floor_list = []
rent_list = []
link_list = []
building_name_list = []
breadth_list = []

# 結果出力ファイルの名前を作る
dt_now = datetime.datetime.now()
date = (dt_now.strftime('%Y_%m_%d'))
export = EXPORT_CSV_PATH+EXPOR_FILE_PREFIX+date+".csv"

os.makedirs(EXPORT_CSV_PATH, exist_ok=True)
# htmlを取得してガチャガチャする関数
def fetch_html(url):
    # ここでhtmlを取得
    response = requests.get(url)
    html = BeautifulSoup(response.text,'html.parser')

    # 家賃を囲んでいるdivタグを取得
    rent_div = html.find_all('div', class_='detailbox-property-point')

    # 家賃を囲んでいるdivタグからテキストを取得
    for rent in rent_div:
        rent_list.append(rent.text)


    # 詳細ページのurlを囲んでいるaタグを取得
    link_href = html.find_all('a', class_='js-cassetLinkHref')

    # 詳細ページのurlを囲んでいるaタグからutlとテキスト(建物名)を抽出
    for link in link_href:
        # 先頭部分が抜けているので補完
        detail_url = BASE+link.get('href')
        link_list.append(detail_url)
        building_name_list.append(link.text)

    # 間取りを囲んでいるtrタグを取得
    floor_plan_tb = html.find_all('tr')

    # trタグから間取りと敷地面積のテキストを抽出
    for row in floor_plan_tb:
        for item in row.find_all('td',class_='detailbox-property-col detailbox-property--col3'):
            for floor in item.find_all('div'):
                if 'LDK' in floor.text:
                    floor_list.append(floor.text)
                elif 'm' in floor.text:
                    breadth_list.append(floor.text)

# 結果出力
def export_result():
    # ファイルオープン
    f = open(export, 'w')
    writer = csv.writer(f, lineterminator='\n')
    # if len(link_list) == len(floor_list) and len(link_list) == len(rent_list) and len(rent_list) == len(floor_list):
    length = len(link_list)
    column = "name","rent","layout","space","link"
    writer.writerow(column)
    i = 0
    while i < length:
        line = building_name_list[i],rent_list[i],floor_list[i],breadth_list[i],link_list[i]
        writer.writerow(line)
        i += 1
    
    print("Total",i)

    f.close()


if __name__ == "__main__":
    while PAGE_LIMIT >= current_page:
        list_page_url=f'{SEARCH_URL}{current_page}'
        time.sleep(1)
        fetch_html(list_page_url)
        print(f'fetch page:{current_page}')
        current_page += 1
    
    export_result()

