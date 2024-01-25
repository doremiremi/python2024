import pandas as pd
from faker import Faker
import random
faker = Faker('ko_KR')
print(faker.name())
#한번 만들어진건 쓸필요없음~~
# coffeeList = ['아메리카노','라떼','바닐라','모카','민초']
# data = {
#     'name':[faker.name() for i in range(30)],
#     'age':[random.randint(20,61) for i in range(30)],
#     'coffee':[random.choice(coffeeList) for i in range(30)]
# }
# print(data)
#
# df = pd.DataFrame(data)
# df.to_csv(f'dummy_data.csv',index=False)
