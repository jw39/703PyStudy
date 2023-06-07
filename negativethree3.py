from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import os

def negativethree_products(result):
    for page in range(1, 6):
        negativethree_url = 'https://negativethree.com/product/list.html?cate_no=68&page=%d' % page
        print(negativethree_url)
        html = urllib.request.urlopen(negativethree_url)
        soupNegativethree = BeautifulSoup(html, 'html.parser')
        product_items = soupNegativethree.select('li.block')
        for item in product_items:
            product_name = item.select_one('strong.name').text.strip()
            product_price_element = item.select('span[style="font-size:12px;color:#000000;"]')
            if product_price_element:
                product_price = product_price_element[0].string
                product_price2 = product_price_element[1].string
            else:
                product_price = 'N/A'
                product_price2 = 'N/A'
            result.append([product_name, product_price, product_price2])


def main():
    result = []
    print('NegativeThree products crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    negativethree_products(result)

    os.makedirs('./csv', exist_ok=True)

    negativethree_tbl = pd.DataFrame(result, columns=('product_name', 'price', 'price2'))
    negativethree_tbl.to_csv('negativethree3.csv', encoding='utf-8-sig', mode='a', index=True)
    del result[:]


if __name__ == '__main__':
    main()
