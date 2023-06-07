from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_coffee_info():
    base_url = 'https://cheongjadabang.com/product/list.html?cate_no=58&page='
    page_number = 1
    result = []

    while True:
        url = base_url + str(page_number) + '#none'
        print("Scraping:", url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        coffee_list = soup.find('ul', class_='prdList column5')
        if coffee_list is None:
            break

        for coffee in coffee_list.find_all('div'):
            name = coffee.find('strong', class_='name').text.strip()
            calorie = coffee.find('span', class_='calorie').text.strip()
            saturated_fat = coffee.find('span', class_='saturated-fat').text.strip()
            sugar = coffee.find('span', class_='sugar').text.strip()
            sodium = coffee.find('span', class_='sodium').text.strip()
            protein = coffee.find('span', class_='protein').text.strip()
            caffeine = coffee.find('span', class_='caffeine').text.strip()

            result.append([name, calorie, saturated_fat, sugar, sodium, protein, caffeine])

        page_number += 1

    return result

def main():
    print('Cheongjadabang coffee crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    coffee_info = scrape_coffee_info()
    coffee_df = pd.DataFrame(coffee_info, columns=['name', 'calorie', 'saturated fat', 'sugar', 'sodium', 'protein', 'caffeine'])
    coffee_df.to_csv('coffee_info.csv', encoding='utf-8-sig', index=False)
    print('Data saved successfully!')

if __name__ == '__main__':
    main()
