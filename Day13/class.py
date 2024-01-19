# #객체 && class
#
# price -> int/float
# name -> str
# height->float
# coffee->coffeename=str,coffeeprice = int,hasShot =bool
# (struct 구조체[변수모음/명사/상태]+function[동사/동작])->classmethod
#
# 어떤 프로그램인지 미리 기획이 완성이 되어야
# 클래스를 만들수있습니다
#
# 펫보험 클래스
# dog->owner,name,age,breed,surgeryList...
# dog->changeOwnername,addAge,addsurgery...
#
#
# 강아지 키우기 클래스
# dog->hp,skill,skill...
# dog->takethemwalk...

class Car:
    def __init__(self,b, n, c):
        self.brand = b
        self.name = n
        self.color = c
    def introduce(self):
        print(f"차의 이름은 {self.name}이고 차브랜드는 {self.brand},색깔은{self.color}")
    def horning(self):
        print("경적빵빵쓰~")

    def driving(self):
        print("부뤵부뤵")

a = Car('현대','k5','검은색')
b = Car('기아','모닝','보라색')
a.introduce()
b.introduce()

# 절차 지향 프로그래밍 -> 객체 지향 프로그래밍(OOP)
# 절차[연산자지향] 지향(위에서 아래루)
# 유지보수 힘듦/결과예측 불가
#
# 객체[object지향] 지향() object[str,int,float...]
# 유지보수 가능/결과예측