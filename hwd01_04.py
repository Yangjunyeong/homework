s = input('숫자를 입력해주세요 : ')

a = int(s)
b = 0
while (a > 0):
    b = b + a % 10
    a = a // 10

print(b)

#각 자릿수 합을 구하기
