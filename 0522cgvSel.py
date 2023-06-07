#정적 1 select

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def crawl_movie_chart(result):
    CGV_url = 'http://www.cgv.co.kr/movies/pre-movies.aspx'
    html = urllib.request.urlopen(CGV_url)
    soup = BeautifulSoup(html, 'html.parser')
    
    movie_list = soup.select('div.box-contents') 
    #div.box-contents를 선택하여 영화 리스트를 가져옴
    for movie in movie_list:
        movie_title = movie.select_one('strong').text.strip()
        #strip()  문자열에서 양쪽에 위치한 공백 제거
        movie_release = movie.select_one('span.txt-info').text.strip()
        movie_genre = movie.select_one('em.dday')
        #값이 존재하면 해당 텍스트를 가져오고, 없으면 빈 문자열로 처리
        if movie_genre is not None:
            #dday의 값이 있는지 확인
            movie_genre = movie_genre.text.strip()
            #정보가 있는 경우에만 strip() 함수 사용해 양쪽 공백 제거
        else:
            movie_genre = ''
        release_date = movie_release.split()[0]
        #movie_release.split()[0]는 개봉 날짜 정보인 "2023-05-30" 부분을 추출하기 위해 사용
        movie_ticket = movie.select_one('span').text.strip()
        result.append([movie_title, release_date, movie_genre, movie_ticket])
        
        
def main():
    result = []
    print('CGV pre-movies crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    crawl_movie_chart(result)
    cgv_tbl = pd.DataFrame(result, columns=('영화 이름', '개봉 날짜', 'D-DAY', '예매율'))
    cgv_tbl.to_csv('cgv_pre_movies2.csv', encoding='cp949', index=True)
    
    #print('Data saved to cgv_pre_movies.csv')
    print('Crawling result:')
    for row in result:
        print(row)

if __name__ == '__main__':
    main()
