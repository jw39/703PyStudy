# from bs4 import BeautifulSoup
# import urllib.request
# import pandas as pd
# import datetime


# def coffee_chart(result):
#     for page in range(1, 3):
#         coffee_url = 'https://cheongjadabang.com/category/%EC%9D%8C%EB%A3%8C/58/?page={}'.format(page)
#         print(coffee_url)
#         html = urllib.request.urlopen(coffee_url)
#         soup = BeautifulSoup(html, 'html.parser')
#         coffee_list = soup.find_all('li', class_='xans-record-')
        
#         for coffee in coffee_list:
#             coffee_strong = coffee.find_all('strong')
#             coffee_Calories = coffee_strong[0].string
#             coffee_Fat = coffee_strong[1].string
#             coffee_Sodium = coffee_strong[2].string
#             coffee_Protein = coffee_strong[3].string
#             coffee_Caffeine = coffee_strong[4].string
#             result.append([coffee_Calories, coffee_Fat, coffee_Sodium, coffee_Protein, coffee_Caffeine])
        
#         # for coffee in coffee_list:
#         #     coffee_div = coffee.find('div')
#         #     if coffee_div is None:
#         #         continue
#         #     coffee_strong = coffee_div.find_all('strong')
#         #     if len(coffee_strong) >= 5:
#         #         coffee_Calories = coffee_strong[0].string
#         #         coffee_Fat = coffee_strong[1].string
#         #         coffee_Sodium = coffee_strong[2].string
#         #         coffee_Protein = coffee_strong[3].string
#         #         coffee_Caffeine = coffee_strong[4].string
#         #         result.append([coffee_Calories] +[coffee_Fat]+ [coffee_Sodium]+[coffee_Protein]+[coffee_Caffeine])
            
#         return
    
# def main():
#     result=[]
#     print('coffee chart crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
#     coffee_chart(result)
#     coffee_tbl = pd.DataFrame(result, columns=('Calories', 'Fat', 'Sodium', 'Protein', 'Caffeine'))
#     coffee_tbl.to_csv('coffee_info11.csv', encoding='utf-8', index=True)
        
#     print('Crawling result:')
#     for row in result:
#         print(row)
        
    

# if __name__ == '__main__':
#     main()

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


def coffee_chart(result):
    for page in range(1, 3):
        coffee_url = 'https://cheongjadabang.com/category/%EC%9D%8C%EB%A3%8C/58/?page={}'.format(page)
        print(coffee_url)
        html = urllib.request.urlopen(coffee_url)
        soup = BeautifulSoup(html, 'html.parser')
        coffee_list = soup.find_all('li', class_='xans-record-')
        for coffee in coffee_list:
            product_name = coffee.find('strong', class_='name')
            if product_name:
                product_name = product_name.get_text(strip=True)
                product_items = coffee.find_all('li', class_='xans-record-')
                product_nutrient = []
                for item in product_items:
                    nutrient_title = item.find('strong', class_='title')
                    if nutrient_title:
                        nutrient_title = nutrient_title.get_text(strip=True)
                        nutrient_value = item.find('span', class_='info_text')
                        if nutrient_value:
                            nutrient_value = nutrient_value.get_text(strip=True)
                        else:
                            nutrient_value = ''
                        product_nutrient.append((nutrient_title, nutrient_value))
                result.append([product_name] + [value for _, value in product_nutrient])

    return


def main():
    result = []
    print('coffee chart crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    coffee_chart(result)
    coffee_tbl = pd.DataFrame(result, columns=['Name', 'Calories', 'Fat', 'Sodium', 'Protein', 'Caffeine'])
    coffee_tbl.to_csv('coffee_info.csv', encoding='utf-8-sig', index=False)

    print('Crawling result:')
    for row in result:
        print(row)


if __name__ == '__main__':
    main()



