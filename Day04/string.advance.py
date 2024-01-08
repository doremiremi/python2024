# # coffee = "americano" #str
# # #내장합스[int() str() float() bool() list() print() input()
# # #len():길이를 알려주는 기능
# # print(len(coffee)) #9
# # print(coffee.upper()) #대문자로 바꿔줌
# # print(coffee.lower())#소문자로 바꿔줌
# # print(coffee.capitalize()) #Americano
# # print(coffee.strip())#빈공간 americano 빈공간 인경우 [빈공간 없애기]
# # print(coffee.find('c')) #몇번째에 'c'가 있니? 5 없는 경우는 -1
# # print(coffee.replace('cano','can')) #왼쪽에서 오른쪽으로 바꾸기
# # print(coffee.count('a')) #a가 몇개인지 없으면 -1
# #
# #사용자로 부터 소문자 문자열을 입력받고 이를 모두 대문자로 변환
#
# # lower = input("소문자로 문자입력")
# # print(lower.upper())
#
# #찰리푸스 노래에서 left and right 단어가 몇번나오는지 세는 프로그램
#
# song = """"Left and right
# Left and right
# Left and right
# SEVENTEEN ha
# 잊지 말아야 해 출발선에 설 때
# 두 눈 부릅뜨고 고갤 들어
# Come on!
# 무릎 꿇고서 추진력을 얻고 나면
# 제일 먼저 baby 앞서갈래
# Come on!
# 친구들 불러 I'ma celebrate
# 아무도 못 말려 we party today
# 클라이맥스 달려 꼬리를 휘날려 또
# 알잖아 버펄로
# 레드 카펫 위를 뛰어
# 내일은 잘 나갈 거야 더
# 하물며 대기권을 뚫어 뚫어 뚫어 뚫어
# 웃어봐 더 하하하하
# 스무 번 더 하하하하 이것은
# 결승선을 넘을 때 세리머니
# 시원하게 yeh it goes like
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# 기분 좋을 때 걱정 없이
# 더 더 확실하게 follow me
# Yeah, it goes like
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# I run up, I run up, I run up, I run up
# 그 누구의 말도 안 들어
# 딴말을 떠들어 떠들어
# 어쩌고저쩌고 시끄러워 쉿 해
# 우리에게 필요한 건
# 달콤한 내일이잖아
# 헹가래 하늘 향해
# 위로 위로 위로 위로
# 달리고 달리고 달려봐도
# 도대체 언제 앞지르냐고
# 달리는 것만으로도 충분하다고 yeah, yeah, yeah
# 그럼 뭐 어쩌라고
# 안 뛰는 것도 방법이라고
# 아무렴 어때 yeah, yeah
# 웃어봐 더 하하하하
# 스무 번 더 하하하하 이것은
# 결승선을 넘을 때 세리머니
# 시원하게 yeah, it goes like
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# 기분 좋을 때 걱정 없이
# 더 더 확실하게 follow me
# Yeah, it goes like
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# 혼자가 아니라
# 우리 우리라서
# 겁낼 필요 없어 yeah, yeah
# 혼자가 아니라
# 우리 우리라서
# 또 걱정 없이 달리지 yeah, yeah
# So, uh, uh 열정의 세리머니
# 넷을 세고 go 해
# 하나 둘 셋 넷
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# 같이 가보자 걱정 없이
# 더 더 확실하게 follow me
# Yaeh, it goes like
# Left and right
# Left and right
# Left and right
# Rip it, rip it
# 하나 둘 셋 넷 둘 둘 셋 넷
# 셋 둘 셋 넷 넷 둘 셋 넷"""
#
# print(f"가사에서 left는 {song.count('Left')} right는 {song.count('right')}번 나왔습니다")
# print(f"가사의 길이는 {len(song)}")

# a = "mega"
# b = "study"
# c = a + b #+문자열 연결 연산자 결과:megastudy
# d = a * 3 #* 문자열 반복 연산자 결과:megamegamega
# e = a[0] #문자열 인덱싱 결과:m
# f = b[0:3] #[start:end]문자열 슬라이싱(end 제외) 결과:stu
# g = 'g' in a #"mega"에서 'g'가 있니? 결과: true or false
#
# title = "megastudy python programming"
# print(title.split())#빈공간 기준으로 str에서 list만들어주기
# title1 = "orange,apple,banana"
# print(title1.split(','))


# user한테 이메일주소르 ㄹ입력받고 ,[유저아이디, 도메인]
##split
# user = input("이메일 주소입력")
# a = user.split('@')
# b = a[1].split('.')
# print(a)
# print(b)
# a[1] = b[0]
# a.append(b[1])
# print(a)

#join
# word = ' '.join(['ice','cream']) # ice cream
#
# id = input("id입력:")
# domain = input("도메인 입력:")
# print('@'.join([id,domain]))

article = """US Secretary of State Antony Blinken says Palestinians must not be pressured into leave Gaza, and must be allowed to return to their homes once conditions allow.

Mr Blinken condemned statements by some Israeli ministers, who called for the resettlement of Palestinians elsewhere.

The US official was in Qatar on his latest Middle East tour.

His comments come following reports that dozens of people were killed at a refugee camp in northern Gaza.

Footage from Jabalia shows bodies lying in the rubble of a destroyed building - many of them women and children.

The Israeli military has not yet responded to the reports.

More than 60 Palestinians have reportedly also been killed in the past day in the southern city of Khan Younis.

The Jabalia camp has been hit several times since Israel began its war against Hamas following the unprecedented attack by Hamas gunmen on southern Israel on 7 October.

Some 1,200 people were killed - most of them civilians - and about 240 others taken hostage in the Hamas raids.

More than 22,000 people - mostly women and children - have been killed in Gaza, according to the Hamas-run health ministry. It has reported at least 113 deaths over 24 hours of Israeli bombardment.

Why are Israel and Hamas fighting in Gaza?
Israel says war expected to continue throughout 2024
"Palestinian civilians must be able to return home as soon as conditions allow," Mr Blinken said on Sunday. "They cannot, they must not be pressed to leave Gaza."

Israel's far-right Finance Minister Bezalel Smotrich has called for Palestinians to leave Gaza and make way for Israelis who could "make the desert bloom".

And National Security Minister Itamar Ben-Gvir this week issued a call "to encourage the migration of Gaza residents" as a "solution" to the crisis.

The official line from the Israeli government is that Gazans will eventually be able to return to their homes, though it has yet to outline how or when this will be possible.

Meanwhile, the situation in Gaza continues to deteriorate. Health officials said even medical facilities including hospitals are now unsafe.

Three international medical aid groups announced they were pulling out of the al-Aqsa hospital in central Gaza after Israel issued evacuation orders.

A representative of the United Nation's Office for the Coordination of Humanitarian Affairs (OCHA), told the BBC World Service's Newshour programme that they were "hugely concerned by this development".

"What it means is that a hospital that was already over-crowded and overloaded and well beyond its capacity is now without absolutely critical reinforcement to support it as it deals with an ever-increasing number of casualties," said Gemma Connell.

"""

# newarticle = article.replace('after','before')
# newarticle1 = newarticle.replace('it','😁').split()

newarticle = article.replace('after','before').replace('it','😁').split()

print(newarticle)