#함수:코드를 모아놓은 묶음
#파이썬 내장함수:print,len,int etc.

#파이썬 커스터마이즈 함수
# def add(x,y):
#     result = x + y
#     return result
# a= add(5,10)
# print(a)
#
# def sub(x,y):
#     result = x - y
#     return result
#
# def multiply(x,y):
#     result = x * y
#     return result

def oddEven(x):

    if x % 2 == 0:
        return  '짝수입니다'
    else:
        return '홀수입니다'


a = oddEven(5)
print(a)

def makeListDict(xList,yList,xKey='item',yKey='price'):
   return [{xKey:x, yKey: y} for x, y in zip(xList,yList)]

breads = ['소금빵','보름달','단팥빵','앙버터','마카롱']
prices = [2500,1000,2400,4500,3000]

result = makeListDict(breads,prices,'빵','가격')
print(result)
