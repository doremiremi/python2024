# #일본여행 계획프로그램
# plan = input("쉼표를 기준으로 일본여행 계획을 입력하세요:")
# plansplit = plan.split(',')
# print(f" 일본여행리스트는 {plansplit}입니다)")

#뉴스기사 단어찾기 프로그램
# news = """The deal became one of the most lucrative partnerships in sports history as Woods dominated the world of golf for more than a decade to put him second on the list of men's major champions, three behind leader Jack Nicklaus.
#
# Becoming one of the world's most famous sport stars, Woods signed further, multiple deals with Nike over his career, including a 10-year contract in that was worth a reported $200m.
#
# Tim Derdenger, an associate professor of marketing and strategy at Carnegie Mellon's Tepper School of Business in the US, told the BBC the long-term partnership between Woods and Nike was "a win-win for everybody".
#
# In 2013, the academic was part of a research team which looked at the impact of Woods on the sales of Nike golf balls, which he switched to using in 2000.
#
# Prof Derdenger said while Woods was paid $200m (£157m) to be sponsored by Nike over a 10-year period, the research found that Nike recovered 60% of the investment in sales of its golf balls in the US alone.
#
# He said when Woods first turned professional in 1996, Nike "didn't have a strong prominent position in the golf industry" and so struck gold when it launched the brand's golf line with the upcoming star.
#
# "What better person in hindsight to then bring out this phenomenal teenage, generational player to then launch their golf brand and apparel brand for Nike? He is golf, he is that person that brought the game to a massive amount of people over the last 25 years," said Prof Derdenger.
#
# "This was sort of the MO (modus operandi) for Nike and it still is to this day is to go out and find these athletes that are generational, or some of the best of their time, and build brands around them to help them drive sales of Nike products.""""
# print(news)
# word = input("찾으실 단어를 입력해주세요")
# word_num = news.find(word)
#
# print(f"찾으신 {word}의 수는 총{word_num}개 입니다")
#
# #스타벅스 메뉴 선택 프로그램
# coffee = [4000, 5000, 5500]
# cake = [5000, 6000, 5500]
# coffee_chosen = int(input("원하시는 커피의 번호를 입력해주세요:메뉴 좌라락"))-1
# cake_chosen = int(input("원하시는 케익의 번호를 입력해주세요: 메뉴 좌라락"))-1
# print(f"고르신 커피와 케익의 값은{coffee[coffee_chosen] + cake[cake_chosen]}입니다")

#좋아하는 커피 브랜드 저장 프로그램
brand = input("좋아하는 커피 브랜드 세개를 입력해주세요(쉼표기준):").split(',')
brand[0] = brand[0].capitalize()
brand[1] = brand[1].capitalize()
brand[2] = brand[2].capitalize()
print(brand)


