#반목문(for)
#
# for x in "icecream":
#유저에게 대문자와 소문자가 섞인 단어를 받았을때-> 반대로 출력하는 프로그램

# user = input("대문자와 소문자가 섞인단어를 입력하세요:")
# word = ''
# for x in user:
#     if x.isupper():
#         word = word + x.lower()
#     else:
#         word = word + x.upper()
# print(word)

# user = input("단어를 입력하세요")
# word = ''
# for x in user:
#     if x == 'a' or x == 'e':
#         word = word
#     else:
#         word = word + x
# print(word)


#다른방법
# user = input("단어를 입력하세요")
# word = ''
# for x in user:
#      if x in 'aeiou':
#          pass
#      else:
#          word += x
# print(word)
#
# for x in [1,2,3,4,5]:
#     print(x ** 2)
#
# for x in ['사과','바나나','파인애플']:
#     print(x)
# length = []
# for x in ['사과','바나나','파인애플']:
#     length.append(len(x))
# print(length)
#
# odd = []
# evenSun = 0
# for x in [1,2,3,4,5,6,7,8,9,10]:
#     if x % 2 == 0:
#         evenSun += x
#     else:
#         odd.append(x)
#
# print(f"짝수:{evenSum}")
# print(f"홀수:{odd}")
import random
lIsT = []
for x in range(100):
    lIsT.append(random.randint(0,10001))
lIsT.sort()
    # if x % 2 == 0:

rabbitcarrotLst = []
for x in lIsT:
    if x % 2 ==1:
        rabbitcarrotLst.append('🍺')
    else:
        rabbitcarrotLst.append('🐮')
print(lIsT)
print(rabbitcarrotLst)


#for x in range(100)
# for x in 'apple' -> a p p l e
#for x in

device = ['아이폰','갤럭시','맥북']
for x,y 