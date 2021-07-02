from bs4 import BeautifulSoup

with open("books.xml", "r", encoding="utf8") as f:
    booksxml = f.read()  # - 파일을 문자열로 읽기


# - BeautifulSoup 객체 생성 : lxml parser를 이용해 데이터 분석
soup = BeautifulSoup(booksxml, "lxml")

for title in soup.find_all("title"):
    print(title.get_text())  # -  태그를 찾는 find_all 함수 이용

