from bs4 import BeautifulSoup
import requests

url = "https://www.musinsa.com/ranking/best?u_cat_cd=001"

response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#item_title,list_info,price

companies = soup.find_all("p",class_="item_title")
companyList = []
for i in companies:
    companyList.append(i.text.strip())
# print(companyList)
infos = soup.find_all("p",class_="list_info")
infosList = []
for i in infos:
    infosList.append(i.text.strip())
# print(infosList)

prices = soup.find_all("p",class_="price")
pricesList = []
for i in prices:
    pricesList.append(i.text.strip().replace(" ","").split("\n")[0])
# print(pricesList)

result = [{'회사':c,'이름':i, '가격':p} for (c,i,p) in zip(companyList,infosList, pricesList)]
print(result)