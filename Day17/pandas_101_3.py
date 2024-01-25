import pandas as pd

df = pd.read_csv('dummy_data.csv')
vanillaLover = df[df['coffee']=='바닐라'][df['age']>30]

#위에서 10개/뒤에서 10개
print(df.head(10))
print(df.tail(10))

#데이터의 요약본
print(df.describe())
#name 기준으로 정렬해주세요 (가나다순)
print(df.sort_values(by='name'))
#나이 순으로 정렬해주세요
print(df.sort_values(by='age'))
#커피이름순으로 정렬해주세요(가나다순)
print(df.sort_values(by='coffee'))


#데이터 변경
df['age'] = df['age'] // 10
print(df)

#groupby 데이터 특정 기준으로 그룹화
# groupedCoffee = df.groupby('coffee').mean()
# print(groupedCoffee)



