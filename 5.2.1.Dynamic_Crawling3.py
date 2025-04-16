from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

#[CODE 1]
def CoffeeBean_store(result):

    wd = webdriver.Chrome()

    wd.get("https://www.coffeebeankorea.com/store/store.asp")
    wd.execute_script("storePop2(1)")
    time.sleep(1)  # 스크립트 실행할 동안 1초 대기

    html = wd.page_source
    soupCB1 = BeautifulSoup(html, 'html.parser')

    store_list = soupCB1.select("div.store_txt")
    for store in store_list:
        try:
            store_name = store.select("p.name > span")[0].next
            print(store_name)

            store_address = store.select("p.address > span")[0].string
            store_phone = store.select("p.tel > a")[0].string
            result.append([store_name, store_address, store_phone])
        except:
            continue
    return

def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)  # [CODE 1]

    CB_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding = 'utf8', mode = 'w', index = True)

if __name__ == '__main__':
    main()
