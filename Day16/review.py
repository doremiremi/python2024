#
#
# def solution(eng):
#     num = ""
#     if 'one' in eng:
#         num += '1'
#     elif 'two' in eng:
#         num += '2'
#     elif 'three' in eng:
#         num += '3'
#     elif 'four' in eng:
#         num += '4'
#     elif 'five' in eng:
#         num += '5'
#     elif 'six' in eng:
#         num += '6'
#     elif 'seven' in eng:
#         num += '7'
#     elif 'eight' in eng:
#         num += '8'
#     elif 'nine' in eng:
#         num += '9'
#  return num
# a = input("숫자를 영어 문자열로 입력하세요:")
# solution(a)
# print(num)

def solution(numbers):
    numList = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for index, item in enumerate(numList):
        numbers = numbers.replce(item,str(index))
    return int(numbers)
