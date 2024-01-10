# megastudy = {
#     'python' : [1,2,3],
#     'java' :
# }

#set(집합) 중복안댐

a = {1,2,3,1,2,3,1,2,3}
b =set([1,2,3,4,1,2,3])
b.add(1)#소용없지라
b.add(5)#
b.discard(3)#3을 빼줌
print(b)
b.clear()#싸그리싹싹 비워줌
print(a)
