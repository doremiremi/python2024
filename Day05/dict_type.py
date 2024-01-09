# #key-value
# #key는 중복이 안됨,문자 type가능
# zodiac ={
#     1.'쥐'
#     2.'소'
#     3.'범'
#     4.'토끼'
#     5.'용'
# }
#
# mbti = {
#     'e':'외향적',
#     'i':'내향적',
#     's':'직관적',
#     'n':'직관적',
#     'f':'감성적',
#     't':'이성적',
#     'j':'계획적',
#     'p':'즉흥적'
#
# }
# usermbti = input("mbti를 입력하세요:")
# print(f"당신의 성향은 {mbti[usermbti[0]]}이고 {mbti[usermbti[1]]}이며 {mbti[usermbti[2]]}이고 {mbti[usermbti[3]]}입니다")

instagram = {
    "신촌맛집":['싸다김밥','신촌순댓국','서브웨이'],
    "서강대맛집":{
        "서강대학식":['한식정식','오늘의치돈','육회덮밥']
    }
}
print(instagram["신촌맛집"][2])
print(instagram["서강대맛집"]["서강대학식"][1])