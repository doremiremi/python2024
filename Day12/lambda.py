# #간결하고 이름이 없는 안줄함수
# plus = lambda a,b: a+b
# resulta = plus(5,7)
# print(resulta)
#
# minus =lambda a,b: a-b
# resultm = minus(7,5)
# print(resultm)
#
# mult = lambda  a,b: a*b
# resultmt = mult(3,3)
# print(resultmt)

#callback 함수
def hello(some):
    print("안녕")
    some()


def bye():
    print('잘가')

hello(bye)

eggs = ['🥚''🥚''🥚']
def cookEggs(eggs, index,recipe):
    recipe(eggs,index)

def makefry(eggs,index):
    eggs[index] = '🍳'

def makesandwich(eggs,index):
    eggs[index] = '🥪'

cookEggs(eggs,index:0,makefry)



