#파이썬 프로그램 만들기:1.데이터분석(pandas) 2.인공지능(tensorflow,keras) 3.웹서버(django,flask)
#크롤링->웹사이트 정보 가져오기
from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/sise/"

response = requests.get(url)
response.encoding = 'cp949'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

itemList = soup.find(id="popularItemList")
liList = itemList.find_all('li')
stockList = []
for i in liList:
    stockList.append({'company':i.find('a').text,'price':i.find('span').text})
print(stockList)

