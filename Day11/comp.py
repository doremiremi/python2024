# comprehension
# for문의 심화라고 읽고 단축버전
#
# for i in range(10):
#     print(i)
#
# [i for i in range(10)]:0~9
# [i for i in "snow"]'s','n','o','w'
#
# 필터링
# [i for i in range(10) if i % 2 ==0]0~9중 짝수 모음
#
# fruits =['apple','banana','mango']
# [i for i in fruits if i.count('b')>0 or 'b' in i]
#
# 맵핑[변환/치환]
# ['😻'if i % 2 == 0 else '🐭' i for i in range(10)]
#
# dict
# coffee = ['아메리카노','라떼','힘들다커피']
# price = [5000,3000,4000]
# zip화
# list안에 dict
# [{'커피':c,'가격':p} for c,p in zip(coffee,price)]
# dict안에 dict
# {i:{'커피':c,'가격':p} for i,(c,p) in enumerate(zip(coffee,price))}

