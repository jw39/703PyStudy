from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def coffee_products(result):
    for page in range(1, 3):
        coffee_url = 'https://cheongjadabang.com/category/%EC%9D%8C%EB%A3%8C/58/?page={}'.format(page)
        print(coffee_url)
        html = urllib.request.urlopen(coffee_url)
        soupCoffee = BeautifulSoup(html, 'html.parser')
        product_items = soupCoffee.find_all('li', class_='xans-record-')
        for item in product_items:
            product_name = item.find_all('span', style='font-size:17px;color:#333333;')
            product_nutrient = item.find_all('span', style='font-size:12px;color:#555555;')
            if product_name and product_nutrient:
                product_n1 = product_nutrient[0].text
                product_n2 = product_nutrient[1].text
                product_n3 = product_nutrient[2].text
                product_n4 = product_nutrient[3].text
                product_n5 = product_nutrient[4].text
                result.append([product_name[0].text, product_n1, product_n2, product_n3, product_n4, product_n5])  # 수정
    return

def main():
    result = []
    print('coffee products crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    coffee_products(result)  
    
    coffee_tbl = pd.DataFrame(result, columns=['Name', 'Calories', 'Fat', 'Sodium', 'Protein', 'Caffeine'])
    coffee_tbl.to_csv('coffee.csv', encoding='utf-8-sig', mode='a', index=True)
    del result[:]
    

if __name__ == '__main__':
    main()

