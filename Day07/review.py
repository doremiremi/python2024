#홀수인지 짝수인지
num = int(input("정수를 입력해주세요:"))
if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

#알파벳탐지기
alp = input("문자 한 개를 입력해주세요. 알파벳인지 아닌지 알려드림><:")
if alp.isalpha():
    print("알파벳입니다")
else:
    print("알파벳 아님")

#비밀번호 설정 프로그램

pw = input("설정하실 비밀번호를 입력하세요:")
if len(pw) < 10:
    print("비밀번호는 10자리 이상이어야 합니다리")
elif pw.isalnum() or ('!' in pw or '@' in pw or '#' in pw):
    print("영어와 숫자를 꼭 포함해주시조")
else:
    if not ('!' in pw or '@' in pw or '#' in pw):
        print("특수문자를 !@# 포함해주세요")
    else:
        print("비밀번호 설정 완료")

#버스 요금 계산기

 bus = {
     1:{
     'name':'시내버스',
    'price':1200
     },

     2':{
         'age':[],
         'discount'
     }
}
bus_choice = int(input(f"버스를 선택하세요![1.시내버스 -1200원, 2.광역버스-2000원"))
age = int(input("나이를 입력하세요:"))

if age <= 7 or 65 <= age:
    print("무료입니다")
elif 8 <= age and age <= 19:

else:
  print(f"{bus[bus_choice]['name']}의 {bus[bus_choice]['price'] * 0.7}가격입니다")


