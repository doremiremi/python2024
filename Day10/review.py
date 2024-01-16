#1
a = [i for i in range(1,21) if i %2 ==0]
#[i for i in range(1,21) if i% 2 == 0]
#2
b1 = [1,2,3,4,5,6,7,8,9,10]
b = [i for i in b1 if i > 5]
#3
fruits = ["apple","banana","cherry","date"]
firstLetters = [i[0] for i in fruits]

#4
fruituppers = [i.upper() for i in fruits]