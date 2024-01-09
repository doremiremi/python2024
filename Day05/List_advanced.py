#
# #+:str+str(문자연결연산)/list+list(리스트 연결 연산)
# cofffee =['아메리카노','라떼','바닐라라떼']
# cookie = ['화이트 쿠키','녹차 쿠키','오레오 쿠키']
# menu = coffee + cookie
# print(menu)
#
# #*:str*int(str을 n번 연산)/list도 같음
# double_menu = menu * 2
# print(double_menu)
#
# #in 연산자:Boolean 타입 변환
# print('디카페인' in menu)
#
# #[:] 슬라이싱 연산자
# new menu = menu[1:4]



# 리스트 기능
#1.리스트의 길이기능:len()
store = ['cu', 'gs', 'seven', 'ministop']
print(len(store))

#리스트 추가[맨뒤]: append(무엇을)
store.append('emart24')
print(store)
#리스트 추가[몇번째]: insert(몇번째,무엇을)
store.insert(1,'familymart')

#리스트 제거:remove(무엇을)
store.remove('cu')

#리스트 해당아이템 위치 찾기: index(무엇을)
print(store.index('ministop'))

#리스트에 해당아이템 몇개 세기:cound(무엇을)
print(store.count('emart24'))

#리스트를 추가:extend(리스트) +같은 역할
newStore = ['storyway','buytheway']
store.extend(newStore)

#리스트 정렬: sort() /sort(reverse=True)
store.sort()
store.sort(reverse=True)