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

# angle = int(input("각도 입력:"))
#
# if angle < 90 :
#     print("예각입니다")
# elif angle == 90 :
#     print("직각입니다")
# elif angle == 180 :
#     print("평각입니다")
# elif 180 > angle > 90 :
#     print("둔각입니다.")

#테마파크 입장권과 놀이기구 이용패키지 선택 프로그램



# amusement_park = {
#    1:{
#        'ticketName': '일반입장권',
#        'ticketPrice': '50000'
#    },
#  2:{
#        'ticketName': '프리미엄입장권',
#        'ticketPrice': '75000'
#    },
#  3:{
#        'ticketName': 'VIP입장권',
#        'ticketPrice': '100000'
#    }
#
# }
# ticket = int(input("입장권 종류 번호 입력[1.일반입장권,2.프리미엄 입장권 3.VIP입장권]:"))
# age = int(input("나이 입력:"))
#
# if age < 12:
#     print(f"선택하신 티켓은 {amusement_park[ticket]['ticketName']}가격은 {amusement_park[ticket]['ticketPrice']}*0.5")
# elif age >= 65:
#     print(f"선택하신 티켓은 {amusement_park[ticket]['ticketName']}가격은 {amusement_park[ticket]['ticketPrice']}*0.7")
# else:
#     print(f"선택하신 티켓은 {amusement_park[ticket]['ticketName']}가격은 {amusement_park[ticket]['ticketPrice']}")
#

import random
num = []
for i in range(6):
     num.append(random.randint(1,10001))
num.sort()
print(num)


