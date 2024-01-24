

def solution(phone_num):
      newNumber = ""
      for index,item in enumerate(phone_num):
        if len(phone_num) - 4 > index:
            newNumber += "*"
        else:
            newNumber += item
      return newNumber

a = solution("01057054620")
print(a)
            