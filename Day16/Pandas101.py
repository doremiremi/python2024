#pandas-엑셀을 파이썬화
#판다스 데이터 타입: series,dataframe
#series: 엑셀에서 하나의 열
#dataframe: 엑셀 그자체[스프레드 시트]

import pandas as pd
from faker import Faker
# numList = [2,7,3,11,12]
# series =  pd.Series(numList)
# print(series.mean())

# coffee = ['Flatwhite','vanilla latte','americano','greentea latte','latte']
# series = pd.Series(coffee)
# print(series)

# coffeeData = {
#     "menu":['americano','latte','mocha','vanilla','mint'],
#     "price":[2500,3000,5000,2000,3000],
#     "caffeine":[120,180,150,200,150],
#
# }
#
# df = pd.DataFrame(coffeeData)
# df.to_csv('coffee.csv',index=False)#index=false (인덱스번호는 빼줘라)
fake = Faker()
# print(fake.name())
carData = {
    'carName':['k5','k7','avante','k3','tesla'],
     'onwer':[fake.name() for i in range(5)],
 }
print(carData)

df = pd.DataFrame(carData)
df.to_csv('car.csv',index=False)