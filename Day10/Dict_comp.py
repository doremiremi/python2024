# normalpopcorn = {
#
#         'name':'일반팝콘'
#
# }

coffee = ['아메리카노', '라떼', '바닐라']
price = [2500, 3000, 3500]
caffeine = [200,150,50]
#zipper
# zipped = zip(coffee, price)
# print(list(zipped))

# result = [{'이름':name, '가격':price, '카페인':caffeine} for name, price,caffeine in zip(coffee,price,caffeine)]
# print(result)
#
# coffee = ['아메리카노', '라떼', '바닐라']
# for index,item in enumerate(coffee):
coffee = ['아메리카노', '라떼', '바닐라']
price = [2500, 3000, 3500]
a = {index:{'이름':coffee,'가격':price} for index,(coffee,price) in enumerate(zip(coffee,price))}
