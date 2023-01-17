
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
cnt = list(map(str,orders.split(',')))
rr = set(cnt)

qw = [s for s in cnt if '아이스' in s] #리스트에서 일부를 추출해서 출력해줌 개사기....


print(f"아이스음료는 총 {len(qw)} 잔 입니다.")

for r in rr:
    print(f'{r}: {orders.count(r)}')



