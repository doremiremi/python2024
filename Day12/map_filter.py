#map(어떻게/무엇을) - 변경 치환해주는 함수

# numList =[1, 2, 3, 4, 5]

# def square(x):
#     return x**2

# a = map(lambda x:x**2,numList)
# print(list(a))
#
# b = map(lambda x:x+100,numList)
# print(list(b))
# c = map(lambda x:x**2+100,numList)
# print(list(c))
#
#
# coffeePriceList = [2000,3000,3500,4000]
# d = map(lambda x:str(x+1000)+'원',coffeePriceList)
#
# print(list(d))
#
# fruits = ['apple','banana','mango','avocado']
# e = map(lambda x:len(x),fruits)
# print(list(e))

#filter(어떻게,무엇을) 컷,필터

# numList = [1,2,3,4,5,6,7,8,9,10]
# # filter(lambda x: x >5,numList)
#
# a = filter(lambda x:x % 2 == 0,numList)
# print(list(a))
#
fruits = ['apple','banana','mango','avocado']
# b = filter(lambda x: 'o' in x, fruits)
# print(list(b))

c = filter(lambda x:len(x)>=6,fruits)
d = map(lambda x:x+'👳‍♂️',c)
print(list(d))
