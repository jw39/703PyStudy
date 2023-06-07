
import requests
from bs4 import BeautifulSoup

# 웹 페이지의 URL
url = "https://www.example.com"

# requests를 사용하여 웹 페이지의 HTML 코드를 가져옴
response = requests.get(url)
html = response.content

# BeautifulSoup을 사용하여 HTML 코드를 파싱
soup = BeautifulSoup(html, "html.parser")

# 제목 태그와 내용 태그를 찾아서 텍스트만 추출하여 출력
title = soup.title.text
content_title = soup.find("h1").text
content_text = soup.find("p").text

print("Title:", title)
print("Content Title:", content_title)
print("Content Text:", content_text)

