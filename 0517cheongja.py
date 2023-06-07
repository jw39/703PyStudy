# from bs4 import BeautifulSoup
# import urllib.request
# import pandas as pd

# def crawl_coffee_info():
#     coffee_url = 'https://cheongjadabang.com/product/list.html?cate_no=58&page=1#none'
#     html = urllib.request.urlopen(coffee_url)
#     soup = BeautifulSoup(html, 'html.parser')
#     coffee_list = soup.find_all('li', class_='item xans-record-')
#     result = []

#     for coffee in coffee_list:
#         coffee_name = coffee.find('p', class_='name').text
#         coffee_calories = coffee.find('li', class_='calories').text.split(':')[1].strip()
#         coffee_fat = coffee.find('li', class_='fat').text.split(':')[1].strip()
#         coffee_sodium = coffee.find('li', class_='sodium').text.split(':')[1].strip()
#         coffee_protein = coffee.find('li', class_='protein').text.split(':')[1].strip()
#         coffee_caffeine = coffee.find('li', class_='caffeine').text.split(':')[1].strip()

#         result.append([coffee_name, coffee_calories, coffee_fat, coffee_sodium, coffee_protein, coffee_caffeine])

#     return result

# def main():
#     coffee_info = crawl_coffee_info()
#     coffee_df = pd.DataFrame(coffee_info, columns=['Name', 'Calories', 'Fat', 'Sodium', 'Protein', 'Caffeine'])
#     coffee_df.to_csv('coffee_info.csv',encoding='cp949', index=False)
#     print('Coffee information saved to coffee_info.csv')

# if __name__ == '__main__':
#     main()


from bs4 import BeautifulSoup
import requests
import pandas as pd

def crawl_coffee_info():
    coffee_url = 'https://cheongjadabang.com/product/list.html?cate_no=58&page=1#none'
    response = requests.get(coffee_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    coffee_list = soup.find_all('li', class_='xans-record-')
    result = []  # 결과를 저장할 리스트

    for coffee in coffee_list:
        coffee_name = coffee.find('div', id='eListPrdImage').text.strip()
        coffee_td = coffee.find_all('tbody')
        for store in coffee_td.find_all('tr'):
            if len(store) <= 5:
                break
            coffee_td = coffee.find_all('td' , class_='info_text')
        coffee_calories = coffee_td[0].text.strip()
        coffee_fat = coffee_td[1].text.strip()
        coffee_sodium = coffee_td[2].text.strip()
        coffee_protein = coffee_td[3].text.strip()
        coffee_caffeine = coffee_td[4].text.strip()

        result.append([ coffee_calories, coffee_fat, coffee_sodium, coffee_protein, coffee_caffeine])

    return result

def main():
    coffee_info = crawl_coffee_info()
    coffee_df = pd.DataFrame(coffee_info, columns=['Name', 'Calories', 'Fat', 'Sodium', 'Protein', 'Caffeine'])
    coffee_df.to_csv('0517cheongja_info.csv', encoding='utf-8-sig', index=False)
    print('Coffee information saved to coffee_info.csv')

    print('Crawling result:')
    for row in coffee_info:
        print(row)

if __name__ == '__main__':
    main()







# # from bs4 import BeautifulSoup
# # import requests
# # import pandas as pd

# # def crawl_coffee_info():
# #     coffee_url = 'https://cheongjadabang.com/product/list.html?cate_no=58&page=1#none'
# #     response = requests.get(coffee_url)
# #     soup = BeautifulSoup(response.text, 'html.parser')
# #     coffee_list = soup.find_all('li', class_='xans-record- ')
# #     result = []  # Result list to store information

# #     for coffee in coffee_list:
# #         coffee_td = coffee.find('tbody')
# #         coffee_rows = coffee_td.find_all('tr')

# #         coffee_info = []
# #         for row in coffee_rows:
# #             coffee_td = row.find_all('td', class_='info_text')
# #             coffee_info.extend([td.text.strip() for td in coffee_td])

# #         result.append(coffee_info)

# #     return result

# # def main():
# #     coffee_info = crawl_coffee_info()
# #     column_names = ['Calories', 'Fat', 'Sodium', 'Protein', 'Caffeine']
# #     coffee_df = pd.DataFrame(coffee_info, columns=column_names)
# #     coffee_df.to_csv('coffee_info.csv', encoding='utf-8-sig', index=False)
# #     print('Coffee information saved to coffee_info.csv')

# #     print('Crawling result:')
# #     for row in coffee_info:
# #         print(row)

# # if __name__ == '__main__':
# #     main()


# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# def crawl_coffee_info():
#     coffee_url = 'https://cheongjadabang.com/product/list.html?cate_no=58&page=1#none'
#     response = requests.get(coffee_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     coffee_list = soup.find_all('li', class_='xans-record-')
#     result = []  # 결과를 저장할 리스트

#     for coffee in coffee_list:
#         coffee_name = coffee.find('strong', class_='name').text.strip()
#         coffee_specs = coffee.find_all('strong', class_='title')
#         coffee_values = coffee.find_all('span', style='font-size:12px;color:#555555;')

#         coffee_calories = coffee_values[0].text.strip()
#         coffee_fat = coffee_values[1].text.strip()
#         coffee_sodium = coffee_values[2].text.strip()
#         coffee_protein = coffee_values[3].text.strip()
#         coffee_caffeine = coffee_values[4].text.strip()

#         result.append([coffee_name, coffee_calories, coffee_fat, coffee_sodium, coffee_protein, coffee_caffeine])

#     return result

# def main():
#     coffee_info = crawl_coffee_info()
#     coffee_df = pd.DataFrame(coffee_info, columns=['Name', 'Calories', 'Fat', 'Sodium', 'Protein', 'Caffeine'])
#     coffee_df.to_csv('coffee_info.csv', encoding='utf-8-sig', index=False)
#     print('Coffee information saved to coffee_info.csv')

#     print('Crawling result:')
#     for row in coffee_info:
#         print(row)

# if __name__ == '__main__':
#     main()
