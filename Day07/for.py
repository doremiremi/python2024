#
# num = int(input("몇번까지 보실래요?"))+1
# for x in range(num): #0-9까지 나옴
#     if x % 2 ==0:
#      print(x)
# print("끝")


#유저에게 정수를 입력받고 해당 수의 공배수:

# num = int(input("정수를 입력하세요"))
# for x in range(1001):
#     if x % num == 0:
#         print(x)
# print("끝")
# sum = 0
# for x in range(11):
#     sum += x
# print(sum)

# 유저에게 n의 정수를 받고,m의 정수를 받으면
# 0~n 까지의 m의 공배수의 총합을 나타내는 프로그램

# n = int(input("몇번째까지"))+1
# m = int(input("공배수:"))
# sum =0
#
# for x in range(n):
#     if x % m == 0:
#         sum += x
# print(f"총합:{sum}")

import random

num = random(0,10000)
