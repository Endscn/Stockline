# 정적인 크롤러
import urllib.request
from bs4 import BeautifulSoup

"""
pageNum은 페이지 넘기면서 찾아가는것
findAll 'img'=클래스 앞에 붙는 이름
mimg= 뒤에 붙는거
아래 for문에서 i.find(img) "src"를 어떻게 바꿔야하는지 알아봐야한다.
"""

# 접근할 페이지 번호
pageNum = 1

while pageNum < 2:
    url = "https://www.cnbc.com/dow-30/"
    fp = urllib.request.urlopen(url)
    source = fp.read();
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find("section")  # 이걸 사진있는 클래스로 바꿔준다.
    soup = soup.find("div")  # 이걸 사진있는 클래스로 바꿔준다.
    soup = soup.find("tbody")  # 이걸 사진있는 클래스로 바꿔준다.
    print(soup)

    pageNum += 1


# selenium 사용하기

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/bwang/Downloads/chromedriver")

driver.implicitly_wait(3)

driver.get("https://www.cnbc.com/dow-30/")

driver.implicitly_wait(3)

driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup = soup.find("section").find("div").find("div",class_="BasicTable-container")
soup = soup.find_all("tr", valign="middle")
symbolist = []
for i in range(len(soup)):
    tkSymbol = soup[i].find("td")
    tkSymbol = tkSymbol.find("div",class_="BasicTable-symbolName")
    tkSymbol = tkSymbol.text
    symbolist.append(tkSymbol)
    print(i+1,"번째",tkSymbol)
print(symbolist)

driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup = soup.find("section").find("div").find("div",class_="BasicTable-container")
soup = soup.find_all("tr", valign="middle")
symbolist = []
for i in range(len(soup)):
    tkSymbol = soup[i].find("td")
    tkSymbol = tkSymbol.find("div",class_="BasicTable-symbolName")
    tkSymbol = tkSymbol.text
    symbolist.append(tkSymbol)
    print(i+1,"번째",tkSymbol)
print(symbolist)

# 22년 6월 12일
# 1. 일단은 비슷한 그래프를 찾아주는 메커니즘은 대충 완성
# 2. 이미지 그래프를 받아서 데이터로 변경하는게 가능할까?
# 3. 2번이 안된다면 일단은 내가 고른 주식의 일부분이 다른 그래프의 일부, 즉, 일부와 일부의 만남을 판단할 수 있는지가 문제.
# 4. 오늘은 여기까지..