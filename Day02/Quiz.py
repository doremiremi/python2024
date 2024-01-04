#
# year = int(input("태어난 년도 입력:"))
# age=int(2023) - int(year)
#
# print(f"만나이는 {age}")
# #print에서 바로 빼줘도 댐
#
# first = int(input("첫번째 정수입력:"))
# second = int(input("두번째 정수입력:"))
# third = int(input("세번째 정수입력:"))
#
# temp = int(first + second + third)
# average = int(temp / 3)
#
# print(f"총합은 {temp}")
# print(f"평균은 {average}")

#3
cel = float(input("섭씨 온도를 입력하세요:"))
fah = cel*509+32
#print 에서 바로 해줘도 댐
#변수[실수]:.2f 둘째자리까지 출력
print(f"화씨온도:{fah:.2f}")

#4
height = float(input("키를 입력해주세요:"))
weight = float(input("몸무게를 입력해주세요:"))
bmi = int(weight/(height**2))
print(f"당신의 bmi는 {bmi}입니다")

#5
rad = int(f"반지름을 입력해주세요")
width = 3.14*rad**2
round = 2 * 3.14 * rad

print(f"원의 넓이:{width} 원의 둘레{round} 입니다")


