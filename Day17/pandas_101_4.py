import pandas as pd
import matplotlib.pyplot as plt
import random
#matplotlib
#pyplot 그래프화 도구모음

# x = [1,2,3,4,5]
# y = [20,25,30,35,40]
# plt.plot(x,y)
# plt.show()

x =[random.randint(0,10) for i in range(100)]
y =[random.randint(0,100) for i in range(100)]
plt.plot(x,y)
plt.show()

#그래서 아까 만들었던 커피 데이터에서 나이와 커피선호도에 관련해 그래프를 만들수도 있음