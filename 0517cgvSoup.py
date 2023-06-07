#정적 2


from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def crawl_movie_chart(result):
    CGV_url = 'http://www.cgv.co.kr/movies/pre-movies.aspx'
    html = urllib.request.urlopen(CGV_url)
    soup = BeautifulSoup(html, 'html.parser')
    
    
    movie_list = soup.find_all('div', class_='box-contents')
    for movie in movie_list:
        movie_title = movie.find('strong').text.strip()
        movie_release = movie.find('span', class_='txt-info').text.strip()
        movie_genre = movie.find('em', class_='dday')
        if movie_genre is not None:
            movie_genre = movie_genre.text.strip()
        else:
            movie_genre = ''
        # Separate the date and value inside the <em> tag
        release_date = movie_release.split()[0]
        movie_ticket = movie.find('span').text.strip()
        
        
        result.append([movie_title, release_date, movie_genre, movie_ticket])

def main():
    result = []
    print('CGV pre-movies crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    crawl_movie_chart(result)
    cgv_tbl = pd.DataFrame(result, columns=('영화 이름', '개봉 날짜','D-DAY','예매율'))
    cgv_tbl.to_csv('cgv_pre_movies1.csv', encoding='cp949', index=True)
    
    #print('Data saved to cgv_pre_movies.csv')
    print('Crawling result:')
    for row in result:
        print(row)
        
    

if __name__ == '__main__':
    main()
