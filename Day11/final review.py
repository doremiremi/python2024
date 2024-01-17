movie = {
    1:{
        'movie':'액션영화',
        'price':12000
    },
    2:{
        'movie':'로맨틱 코미디',
        'price':10000
    },
    3:{
        'movie':'다큐멘터리',
        'price':11000
    }

}
food = {
    1:{
        'name':'팝콘세트',
        'price':6000
    },
    2:{
        'name':'스낵콤보',
        'price':8000
    },
    3:{
        'name':'건강팩',
        'price':7000
    }
}

movieChoice = input("영화번호를 선택해주세요[1.액션영화,2로맨틱코메디영화,3.다큐멘터리]")
foodChoice = input("스낵을 선택해주세요[1.팝콘세트,2.스낵콤포,3.건강팩")
seatChoice = input("좌석을 선택해주세요[1.일반,2.프리미엄좌석,3.vip좌석")
age = input("나이를 입력하세요:")

if seatChoice == 1:
    if age < 18:
        print(f"{movie[movieChoice]['name']}와/과 {food[foodChoice]['name']}의 가격은 {movie[movieChoice]['price']+food[foodChoice]['price']*0.8}입니다")

    elif 18 <= age and age<65:
        print(f"{movie[movieChoice]['name']}와/과 {food[foodChoice]['name']}의 가격은 {movie[movieChoice]['price'] + food[foodChoice]['price'] }입니다")
    else:
        print(f"{movie[movieChoice]['name']}와/과 {food[foodChoice]['name']}의 가격은 {movie[movieChoice]['price'] + food[foodChoice]['price'] * 0.85}입니다")



elif seatChoice == 2:
    if age < 18:
        print(
            f"{movie[movieChoice]['name']}와/과 {food[foodChoice]['name']}의 가격은 {movie[movieChoice]['price'] + food[foodChoice]['price'] * 0.8+5000}입니다")

    elif 18 <= age and age < 65:

    else:
        print(
            f"{movie[movieChoice]['name']}와/과 {food[foodChoice]['name']}의 가격은 {movie[movieChoice]['price'] + food[foodChoice]['price'] * 0.85+5000}입니다")