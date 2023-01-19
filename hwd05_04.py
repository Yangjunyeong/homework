# fn_d(91) 
# 출력 예시 
# 101

def fn_d(n):
    b = 0
    m = n
    while m > 0:
        b = b + m % 10
        m = m // 10
    return b + n

def is_selfnumber(n):
    l = len("n")
    key = 0
    for num in range(n - l * 9,n):
        if fn_d(num) == n:
            key = 1
    if key == 1:
        return False
    else:
        return True

print(is_selfnumber(int(input())))







