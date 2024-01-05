#1.첫번째 정수와 두번째 정수를 받고 결과를 a의 b제곱 결과를 나타내기

int_a = int(input("첫번째 정수를 입력하세요:"))
int_b = int(input("두번째 정수를 입력하세요:"))
int_res = int_a**int_b
print(f"결과는 {int_res}입니다")

#2.엔화계산기 원화를 받으면 엔으로 환전되는 프로그램

won = float(input('Won:'))
yen = float(won*0.11)

print(f"={yen}yen")


#다른방법
#yen을 변수로 두고 결과에서 won/yen 하기