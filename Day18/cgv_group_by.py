import pandas as pd
df = pd.read_csv('cgv.csv')

# #데이터 프레임의 멤버 변수
# print(df.shape)#행과 열의 수
# print(df.index)#행 정보
# print(df.columns)#열 정보
# print(df.values)#데이터
# #데이터프레임의 멤버 함수
# print(df.head(20))#위에서 20개 가져오기
# print(df.tail(20))#뒤에서 20개 가져오리
# print(df.describe())#전체 데이터 요약본
# group_by_movies=df.groupby('movies')
# ages_group_by_movies = group_by_movies['ages'].value_counts()
# print(ages_group_by_movies)
#
#
# group_by_times = df.groupby('Times')
# drinks_group_by_times = group_by_times['drinks'].value_counts()
# print(drinks_group_by_times)
#
# group_by_ages =df.groupby('ages')
# payments_group_by_ages = group_by_ages['payments'].value_counts()
# print(payments_group_by_ages)
#
# group_by_movies =df.groupby('movies')
# payments_group_by_movies = group_by_movies['payments'].value_counts()
# print(payments_group_by_movies)
#
# group_by_times =df.groupby('Times')
# movies_group_by_times = group_by_times['movies'].value_counts()
# print(movies_group_by_times)

group_by_times =df.groupby('Times')
movies_group_by_times = group_by_times['movies'].value_counts()
print(movies_group_by_times)

#x대별로 가장인기있는 y
popular_movies = df.groupby('Times')['movies'].value_counts().groupby(level=0).head(1)

#중간에 times와 movies만 다른걸로 바꿔주면댐
#함수화 해보기
def most_x_to_y(x,y):
    return df.groupby(x)[y].value_counts().groupby(level=0).head(1)

print(most_x_to_y('ages','Times'))