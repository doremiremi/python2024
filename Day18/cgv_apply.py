import pandas as pd
#apply 새로운 열을 만들기

df= pd.read_csv('cgv.csv')

# def recommendPopcornForSenior(row):
#     if row['ages'] == 50 and row['snacks'] == '일반팝콘':
#         return '할인대상'
#     else:
#         return '할인없음'


# def recommendEarlybirdForCheckcard(row):
#     if row['Times'] == '조조' and row['payments'] == '체크카드':
#         return '조조할인대상'
#     else:
#         return '조조할인없음'
# df['조조 이벤투'] = df.apply (recommendEarlybirdForCheckcard,axis=1)
# # df['50대 할인 이벤트'] = df.apply(recommendPopcornForSenior,axis=1)
# print(df)

def ComboEvent(row):
    if row['snacks'] == '일반팝콘' and row['drinks'] == '제로콜라':
        return '제로 콤보 세트'
    else:
        return '해당없음'
df['제로콜라이벤트'] = df.apply (ComboEvent,axis=1)
# df['50대 할인 이벤트'] = df.apply(recommendPopcornForSenior,axis=1)
print(df)