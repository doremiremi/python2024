try:
    num = int(input("숫자를 입력하세요:"))
    result = 10 / num
    print(f"결과는{result}")

except ValueError:
    print("제발 숫자를 입력하세요")
except ZeroDivisionError:
    print("0으로 못나눔")
#except Exception: 부모클래스라서 이렇게만 적어도됨
else:
    print("에러가 없어요 추카포카")#에러가 없는경우 출력
finally:
    print("상관 없으니 보여주라")#에러 여부 상관없이 출력