import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cgv.csv')
drinks_by_movies = df.groupby('movies')['drinks'].value_counts()
normal_time_snack=drinks_by_movies['웡카']

plt.rcParams['font.family'] = 'Malgun Gothic'#폰트설정
normal_time_snack.plot.pie(autopct='%1.1f%%')#plot.pie()파이 그래프.autopct =소수점자리
plt.show()#보여주기
ㅍ