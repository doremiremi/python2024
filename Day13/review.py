#1

def reverseStr(my_string):
    strList = list(my_string) #[b,r,e,a,d ]
    strList.reverse() #[d,a,e,r,b]
    word = ""
    for i in strList:
        word += i
    return word




#2
todo_list = ["problem solving","practiceguitar","swim","studygraph"]
finished = ["true","false","true","false"]

def haveto_List(todoList,finishedList):

  return [todoList[index] for index, item in enumerate(finishedList) if not item]

# newList = []
    # for index,item in enumerate(finishedList):
    #     if not item:
    #         newList.append(todoList[index])
    # return newList 로 풀어서도 가능