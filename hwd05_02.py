# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
import calendar

# choice_month = int(input())
# choice_day = int(input())
end = 0
while end == 0:
        choice_year = int(input())
        if calendar.isleap(choice_year):
            print('윤년입니다. 연도를 다시 입력해주세요. ')
        else: 
            end = 1

print(calendar.calendar(choice_year))

choice_month = int(input())
choice_day = int(input())
if calendar.weekday(choice_year, choice_month, choice_day) == 0:
    print('#경고 월요일입니다.')
list_a = ['월', '화', '수','목','금','토','일']
lst = {'년' : choice_year, '월' : choice_month, '일' : choice_day, '요일' : f'{list_a[calendar.weekday(choice_year, choice_month, choice_day)]}요일'}

print(lst)




        

