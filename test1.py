
from bs4 import BeautifulSoup
import requests
import pandas as pd

def crawl_coffee_info():
    coffee_url = 'https://cheongjadabang.com/product/list.html?cate_no=58&page=1#none'
    response = requests.get(coffee_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    coffee_list = soup.find_all('li', class_='xans-record-')
    result = []

    for coffee in coffee_list:
        coffee_name = coffee.find('strong', class_='name').text.strip().split(' : ')[-1]
        coffee_calories = coffee.find('th', text='칼로리(kcal/100g)').find_next('td', class_='info_text').text.strip()
        coffee_fat = coffee.find('th', text='포화지방(g)').find_next('td', class_='info_text').text.strip()
        coffee_sodium = coffee.find('th', text='나트륨(mg)').find_next('td', class_='info_text').text.strip()
        coffee_protein = coffee.find('th', text='단백질(g)').find_next('td', class_='info_text').text.strip()
        coffee_caffeine = coffee.find('th', text='카페인(mg)').find_next('td', class_='info_text').text.strip()

        result.append([coffee_name, coffee_calories, coffee_fat, coffee_sodium, coffee_protein, coffee_caffeine])

    return result

def main():
    coffee_info = crawl_coffee_info()
    coffee_df = pd.DataFrame(coffee_info, columns=['Name', 'Calories', 'Fat', 'Sodium', 'Protein', 'Caffeine'])
    coffee_df.to_csv('coffee_info.csv', encoding='utf-8-sig', index=False)
    print('Coffee information saved to coffee_info.csv')

if __name__ == '__main__':
    main()
