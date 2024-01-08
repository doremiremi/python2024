#1.정삼각형의 넓이와 둘레를 계산하는 프로그램
height = int(input("높이 입력:"))
side = int(input("한변의 길이 입력:"))
print(f"정삼각형의 넓이는 {height*side*0.5}둘레는 {side*3}")


#2. 운동순서 만들기 프로그램
a = input("운동 입력:")
b = input("운동 입력:")
c = input("운동 입력:")
print(f"운동 순서:{a}->{b}->{c}")

#3.영화리스트 팝콘리스트 음료리스트를 보여줘서 선택한 후 조합을 보여주는 프로그램
list_movie = ["서울의 봄", "위시", "노량"]
list_popcorn = ["팝콘", "치즈팝콘", "캬라멜 팝콘"]
list_drinks = ["콜라", "제로콜라", "스프라이트"]

int_movie = int(input("영화 번호 고르기 1번: 서울의 봄 2번: 위시 3번: 노량"))-1
int_popcorn = int(input("팝콘 번호 고르기[1번:팝콘 2번: 치즈팝콘 3번:캬라멜 팝콘]:"))-1
int_drinks = int(input("음료 번호 고르시오[1번:콜라 2번:제로 콜라 3번:스프라이트]:"))-1

print(f"고르신 영화는 {list_movie[int_movie]}이며 팝콘은 {list_popcorn[int_popcorn]} 그리고 음료는 {list_drinks[int_drinks]}입니다.")