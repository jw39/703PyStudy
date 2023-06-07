from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def crawl_movie_chart():
    CGV_url = 'http://www.cgv.co.kr/movies/pre-movies.aspx'
    html = urllib.request.urlopen(CGV_url)
    soup = BeautifulSoup(html, 'html.parser')
    movie_list = soup.find('li')
    result = []
    for movie in movie_list.find_all('div') :
        movie_strong = movie.find_all('strong')
        movie_em = movie.find_all('em')
        movie_title = movie_strong[0].string
        movie_genre = movie_strong[1].string
        movie_release = movie_em[0].string
        result.append([movie_title] + [movie_genre] + [movie_release])
    return result

def main():
    print('CGV pre-movies crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    result = crawl_movie_chart()
    cgv_tbl = pd.DataFrame(result, columns=('title', 'genre', 'release'))
    cgv_tbl.to_csv('cgv.csv', encoding='cp949', index=True)
    print(str(len(result)) + ' rows saved to cgv.csv.')
    
if __name__ == '__main__':
    main()
