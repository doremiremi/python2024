#가변 매개 변수
# def makePizza(*toppings):
#     print("다음피자는 아래의 토핑이 들어갑니다.")
#     for i in toppings:
#         print(i)
#
# makePizza("pineapple")
# makePizza(*toppings:"pineapple","cheese")
# makePizza(*toppings:"pineapple","cheese", "mushroom")



#['닭','돼지','소']=zodiac(1993,1995,1997)



def zodiac(*years):
    sign = ['닭', '개', '돼지', '쥐', '소', '범', '토끼', '용', '뱀', '말', '양', '원숭이', '닭']
    # newList = []
    # for i in years:
    #     newList.append(sign[i-1993])
    # return newList
    return [sign[i-1993] for i in years]
a = zodiac(1993,1994)
print(a)