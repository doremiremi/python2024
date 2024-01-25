import pandas as pd
df = pd.read_csv('cycle.csv', encoding='cp949')
startList = df['시작_대여소명'].tolist()
places = {}
for i in startList:
    dong = i.split('_')[0]
    if dong in places:
        places[dong] += 1
    else:
        places[dong] = 1
print(places)