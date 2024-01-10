# #제어문
# num = int(input("정수 입력:"))
#
# if num > 0:
#     print("양의 정수 입니다")
# elif num == 0:
#     print("0입니다")
# else:
#     print("0또는 음의 정수 입니다")

#유저에게 영어점수를 입력받고
#100~90 A
#90~80  B
#80~70 C
#70 재수강입니다

# score = int(input("영어점수를 입력해보시죠?:"))
#
# if score >= 90:
#     print("A입니다")
# elif score >=80:
#     print("B입니다")
# elif score >= 70:
#     print("C입니다")
# else:
#     print("축하드립니다 재수강입니다")

#유저에게 정수를 입력받고
#양의 홀수인지,양의 짝수인지

# num = int(input("정수를 입력해주세요:"))
# result = num % 2
# if num > 0:
#     if result == 1:
#         print("입력하신 정수는 양의 홀수 입니다")
#     else:
#         print("입력하신 정수는 양의 짝수입니다")
#
# if num == 0:
#     print("입력하신 정수는 0입니다")
#
# if num < 0:
#     if result ==1:
#         print("입력하신 정수는 음의 홀수 입니다")
#
#     else:print("입력하신 정수는 음의 짝수 입니다")

password = input("비밀번호 입력:")
# num = len(password)
#
# if num < 8:
#     print("비밀번호 재설정!")
#
# else:
#     print("비밀번호가 설정되었습니다")
if len(password) >= 8:
    if '!' not in password:
        print("비밀번호가 설정안댐")
        #password.count('!')==0
    else:
        print("비밀번호가 설정되엇ㅇㅇ")
else:
    print("비밀번호가 8글자 이하입니다")