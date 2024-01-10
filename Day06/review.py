#뉴스 기사에서 가장긴단어 찾기
# article = """A fifth and final batch of court documents relating to sex offender Jeffrey Epstein has been released.
#
# Among the 1,400 pages of records are depositions with Epstein and his former girlfriend Ghislaine Maxwell.
#
# This last trove shows Epstein refused hundreds of times to answer lawyers' questions, including about alleged blackmail of famous men.
#
# The documents have been released as part of a lawsuit brought by sex-trafficking victim Virginia Giuffre.
#
# The legal action, filed in 2015, was settled in 2017. Maxwell has since been jailed for 20 years for helping Epstein abuse young girls. She is appealing against her conviction.
#
# The court records contain a transcript of Epstein's 2016 sworn deposition in which he repeatedly invoked his fifth amendment constitutional right against self-incrimination.
#
# Under questioning, a lawyer for Ms Giuffre asked Epstein whether she had been told to provide a "detailed report" about her alleged sexual encounters with powerful men such as Prince Andrew.
#
# The attorney asked whether this was intended to be used as "blackmail material".
#
# Epstein refused to answer any of the questions, repeatedly responding by saying just the word "fifth" over 500 times."""
# wordList =article.split()
# wordList.sort()



#영화 예매 프로그램(dict활용)



cgv = {
    'movie':{
        'movieList':['1.액션 영화','2.로맨틱 코메디','3.공포영화'],
        'moviePrice':[10000,8000,9000]
    },
    'popcorn':{
        'popcornList':['1.치즈 팝콘','2.카라멜 팝콘','3.일반팝콘'],
        'popcornPrice':[6000,5000,5000]
    }
}

movie_choice = int(input(f"영화를 고르세요[{cgv['movie']['movieList']}:"))-1
popcorn_choice = int(input(f"팝콘을 고르세요[{cgv['popcorn']['popcornList']}:"))-1

# print(f"선택한 영화:{cgv['movie']['movieList'][movie_choice]}, 선택한 팝콘:{cgv['popcorn']['popcornList'][popcorn_choice]},총 금액:{cgv['movie']['moviePrice'][movie_choice] + ['popcorn']['popcornPrice'][popcorn_choice]}")