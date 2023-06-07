# from bs4 import BeautifulSoup
# import urllib.request
# import pandas as pd
# import datetime
# from selenium import webdriver
# import time

# # Chrome 웹 드라이버 경로 설정
# webdriver_path = 'WebDriver 설치 경로/chromedriver.exe'

# def crawl_movie_chart(result):
#     # Chrome 웹 드라이버 실행
#     driver = webdriver.Chrome(webdriver_path)

#     # CGV 사이트 접속
#     driver.get('http://www.cgv.co.kr/movies/pre-movies.aspx')

#     # 페이지 로딩을 위한 대기 시간 (원하는 시간으로 조정)
#     driver.implicitly_wait(5)

#     # 페이지 소스코드 가져오기
#     html = driver.page_source

#     # BeautifulSoup으로 파싱
#     soup = BeautifulSoup(html, 'html.parser')

#     # 영화 목록 가져오기
#     movie_list = soup.find_all('div', class_='box-contents')
#     for movie in movie_list:
#         movie_title = movie.find('strong').text.strip()
#         movie_genre = movie.find('span', class_='txt-info').text.strip()
#         movie_release = movie.find('em', class_='dday')
#         if movie_release is not None:
#             movie_release = movie_release.text.strip()
#         else:
#             movie_release = ''
#         result.append([movie_title, movie_genre, movie_release])

#     # 웹 드라이버 종료
#     driver.quit()

# def main():
#     result = []
#     print('CGV pre-movies crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
#     crawl_movie_chart(result)
#     cgv_tbl = pd.DataFrame(result, columns=('title', 'genre', 'release'))
#     cgv_tbl.to_csv('cgv_pre_movies.csv', encoding='utf-8-sig', index=False)
#     print('Crawling result saved to cgv_pre_movies.csv')

# if __name__ == '__main__':
#     main()

""" 

""" """ 

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time


# Chrome 웹 드라이버 경로 설정
webdriver_path = 'WebDriver 설치 경로/chromedriver.exe'

def crawl_movie_chart(result):
    # Chrome 웹 드라이버 실행
    driver = webdriver.Chrome(webdriver_path)

    # CGV 사이트 접속
    driver.get('http://www.cgv.co.kr/movies/pre-movies.aspx')

    # 페이지 소스코드 가져오기
    html = driver.page_source

    # BeautifulSoup으로 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 영화 목록 가져오기
    movie_list = soup.find_all('div', class_='box-contents')
    for movie in movie_list:
        movie_title = movie.find('strong').text.strip()
        movie_genre = movie.find('span', class_='txt-info').text.strip()
        movie_release = movie.find('span', class_='txt-num')
        if movie_release is not None:
            movie_release = movie_release.text.strip()
        else:
            movie_release = ''
        result.append([movie_title, movie_genre, movie_release])

    # 웹 드라이버 종료
    driver.quit()

def main():
    result = []
    print('CGV pre-movies crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    crawl_movie_chart(result)
    cgv_tbl = pd.DataFrame(result, columns=('title', 'genre', 'release'))
    cgv_tbl.to_csv('cgv_pre_movies.csv', encoding='utf-8-sig', index=False)
    print('Crawling result saved to cgv_pre_movies.csv')

if __name__ == '__main__':
    main()
 """

# from bs4 import BeautifulSoup
# from selenium import webdriver
# import pandas as pd

# # Chrome 웹 드라이버 경로 설정
# webdriver_path = 'WebDriver 설치 경로/chromedriver.exe'

# def crawl_movie_chart(result):
#     # Chrome 웹 드라이버 실행
#     driver = webdriver.Chrome(webdriver_path)

#     # CGV 사이트 접속
#     driver.get('http://www.cgv.co.kr/movies/pre-movies.aspx')

#     # 페이지 소스코드 가져오기
#     html = driver.page_source

#     # BeautifulSoup으로 파싱
#     soup = BeautifulSoup(html, 'html.parser')

#     # 영화 목록 가져오기
#     movie_list = soup.find_all('div', class_='box-contents')
#     for movie in movie_list:
#         movie_title = movie.find('strong').text.strip()
#         movie_genre = movie.find('span', class_='txt-info').text.strip()
#         movie_release = movie.find('span', class_='txt-num').text.strip() if movie.find('span', class_='txt-num') else ''
#         result.append([movie_title, movie_genre, movie_release])

#     # 웹 드라이버 종료
#     driver.quit()

# def main():
#     result = []
#     print('CGV pre-movies crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
#     crawl_movie_chart(result)
#     cgv_tbl = pd.DataFrame(result, columns=('영화 이름', '개봉날짜', 'd-day'))
#     cgv_tbl.to_csv('cgv_pre_movies.csv', encoding='utf-8-sig', index=False)
#     print('Crawling result saved to cgv_pre_movies.csv')

# if __name__ == '__main__':
#     main()


from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# Chrome 웹 드라이버 경로 설정
webdriver_path = 'WebDriver 설치 경로/chromedriver.exe'

def crawl_movie_chart(result):
    # Chrome 웹 드라이버 실행
    driver = webdriver.Chrome(webdriver_path)

    # CGV 사이트 접속
    driver.get('http://www.cgv.co.kr/movies/pre-movies.aspx')

    # 페이지 소스코드 가져오기
    html = driver.page_source

    # BeautifulSoup으로 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 영화 목록 가져오기
    movie_list = soup.find_all('div', class_='box-contents')
    for movie in movie_list:
        movie_title = movie.find('strong').text.strip()
        movie_genre = movie.find('span', class_='txt-num').text.strip() if movie.find('span', class_='txt-num') else ''
        movie_release = movie.find('span', class_='txt-info').text.strip()
        result.append([movie_title, movie_genre, movie_release])

    # 웹 드라이버 종료
    driver.quit()

def main():
    result = []
    print('CGV pre-movies crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    crawl_movie_chart(result)
    cgv_tbl = pd.DataFrame(result, columns=('영화 이름', '개봉날짜', 'd-day'))
    cgv_tbl.to_csv('cgv_Driver.csv', encoding='utf-8-sig', index=False)
    print('Crawling result saved to cgv_pre_movies.csv')

if __name__ == '__main__':
    main()
