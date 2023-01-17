year = int(input("해를 입력하시오 > " ))

if year & 4 == 0 and year & 100 != 0:
    print("윤년")
elif year & 400 == 0:
    print("윤년")
else:
    print("윤년이 아님")


