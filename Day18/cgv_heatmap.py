import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cgv.csv')
#1.시간과 음료 그룹핑
#2.크기 계산 size()
#3.피벗 테이블화
table = df.groupby(['Times','drinks']).size().unstack(fill_value=0)
print(table)

plt.rcParams['font.family'] = 'Malgun Gothic'
sns.heatmap(table, cmap='coolwarm')
plt.show()