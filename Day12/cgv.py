movie_names = ['액션 영화', '로맨틱 코미디', '다큐멘터리']
movie_prices = [12000, 10000, 11000]
popcorn_names = ['팝콘 세트', '스낵 콤보', '건강 팩']
popcorn_prices = [6000, 8000, 7000]
seatName = ['일반 좌석', '프리미엄 좌석', 'VIP 좌석']
seat_prices = [0, 5000, 10000]

def makeDict(name, price, key):
    return [{key: x, 'price': y} for x, y in zip(name, price)]


a = makeDict(movie_names,movie_prices,'movie')
b = makeDict(popcorn_names,popcorn_prices,'popcorn')
c = makeDict(seatName,seat_prices,'seat')

cgv = {
    1:a,
    2:b,
    3:c,
}

def selectList(target,index):
    for i in range(3):
        print(f"{i+1}.{cgv[index][i][target]} {cgv[index][i]['price']}")
    return int(input("번호 입력:")) - 1

movie = selectList('movie',1)
popcorn = selectList('popcorn',2)
seat = selectList('seat',3)
age = int(input("나이를 입력 하세요:"))
result = cgv[1][movie]['price'] + cgv[2][popcorn]['price'] + cgv[3][seat]['price']

if age >= 65:
    print(f"총 가격은 {result*0.85}")
elif age < 18:
    print(f"총 가격은 {result * 0.8}")
else:
    print(f"총 가격은 {result * 1}")