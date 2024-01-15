#for문 심화/축약 버전
#
# a = [i for i in range(1001)]
# print(a)

#0부터 100까지
# b = [i for i in range(101)]
# print(b)
#1부터 500까지
# c = [i for i in range(1,501)]
# print(c)

# d = [i for i in "megastudy"]
# print(d)
#
# e = [i*2 for i in range(1,101)]

# f =[i ** 2 for i in range(1,11)]
# print(f)
#
# g = [i+5 for i in range(1,11)]
# print(g)

#for 컴프리헨션 조건문
#1.if가 뒤에 있을 때는 filter 컷 역할
# fruits = ['apple','strawberry', 'mange','orange','melon']
# a = [i for i in fruits if i.count('r') == 1]
# b = [i for i in fruits if i.count('a') > 0]
# c = [i for i in fruits if len(i) >= 6] #6글자 이상인 단어들
# # print(b)
# # print(a)
# print(c)
# # a = [i for i in range(1,101) if i % 5 == 0]
# # print(a)
#
# #2.if- else 있을 때는 map 변환/치환 역할
#
# a = ['🍓'if i % 2 == 0 else i for i in range(1,101)]
# print(a)

#유저에게 n을 입력 받고 1-100까지 리스트를 출력을 하는데
#n의 배수만 당근을 표현해주고 나머지는 숫자로 표현하기
# usernum = int(input("정수입력:"))
# b = ['🥕'if i % usernum == 0 else i for i in range(1,101)]
# print(b)
# #fruits = ['apple','strawberry', 'mange','orange','melon']
# #fruits에서 5글자 이하이면 대문자로 바꿔서 출력하고 아니면 🐌로 출력하는 리스트만들기
#
# fruits = ['apple','strawberry', 'mange','orange','melon']
# c = [i.upper() if len(i) <= 5 else '🐌' for i in fruits ]
# print(c)

h = [i*j for i in range(1,4) for j in range(1,4)]
print(h)

g = [i+j for i in ["apple","banana"]for j in ["pie,""tanghuru"]]
print(g)