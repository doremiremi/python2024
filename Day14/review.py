# class Dog:
#     def __init__(self,n):
#         self.name = n
#
#
#     def intro(self):
#         print(f"저의 이름은 {self.name}입니다잉")
#
#
# a = Dog('비지')
# a.intro()
class BankAccount:
    def __init__(self, acocunt_number, owner_name):
        self.account_number = acocunt_number
        self.owner_name = owner_name
        self.balance = 0


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("금액을 잘못입력하였습니다")
            return False

    def withdraw(self, amount):
        if 0 < amount and amount < self.balance:
            self.balance -= amount
            return True
        else:
            print("금액을 잘못입력하였습니다.")
            return False

    def get_balance(self):
        return self.balance

    def get_account(self):
        return f"Accont: {self.account_number}, owner:{self.owner_name}, Balance:{self.balance}"

def bank_system():

    glaobalAccount = {}
    while True:
        print("은행계좌 시스템")
        print("1.계좌 개설")
        print("2.입금")
        print("3.출금")
        print("4.잔액조회")
        print("5.종료")
        systemNumber = input("선택:")

        if systemNumber == "1":
            account_number = input("계좌번호")
            owner_name = input("소유자 이름:")
            glaobalAccount[account_number] = BankAccount(account_number,owner_name)
            print("계좌 개설이 완료되었습니다")

        elif systemNumber == "2":
            account_number = input("계좌번호")
            amount = int(input("입금액:"))
            if account_number in glaobalAccount and glaobalAccount[account_number].deposit(amount):
                print("입금완료")
            else:
                print("입금 실패")

        elif systemNumber == "4":
            account_number = input("계좌번호:")
            if account_number in glaobalAccount:
                print(glaobalAccount[account_number].get_account())



