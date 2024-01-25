import pandas as pd

data = {
    'age':[30,40,50,40,50],
    'name':['a','b','c','d','e'],
    'gender':['m','f','f','m','f']
}
df = pd.DataFrame(data)
#class 변수+함수
#dataframe =변수
# print(df)
# #shape 행과 열의 수를 돌려줌
# print(df.shape)
# #index 행
# print(df.index)
# #column 열
# print(df.columns)
# #values 데이터[list]
# # (리스트 타입이기 때문에 몇번째의 데이터를 알고싶을때 print(df.values[0]해도 댐ㅇㅇ)
# print(df.values)
# #해당 열 뽑기
# print(df['age'])
# print(df[['age','name']]) #그중 몇개의 콜럼만 보고싶다? []하나 더 써야됨ㅋ..
#해당열 뽑기[조건] ex)데이터에서 age가 30인 이상인 사람만 뽑아죠
print(df[df['age']>30])
fdf = df[df['gender']=='f'][df['age']==40]
# f_40_df = fdf[df['age']==40] 이렇게도 가능
# print(f_40_df)

#행뽑기
print(df.loc[0,'name'])