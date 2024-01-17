words = ["apple","banana","cherry","date","elderberry","fig"]
filter = [i for i in words if i.count('a') and len(i) > 5]
print(filter)


numbers = [30,55,20,75,40,90,10,65]
num = [i for i in numbers if (int(i)) > 50 ]
print(num)




def plusminus(a,b,flag):
    if flag:
        return a + b
    else:
        return a - b

# a = int(input("정수 입력:"))
# b = int(input("정수 입력:"))
# flag = bool()
# def true(a,b):
#    a + b
#
# def false(a,b):
#     a - b
