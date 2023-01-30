words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
#애너그램을 담을 빈 딕셔너리를 생성
Anagram = {}
# 반복문을 통해 단어를 정렬하여 키로 입력 받고 값에는 단어를 하나하나 넣어준다

for word in words:
    division_word = ''.join(sorted(word))
    # 딕셔너리[키] = 딕셔너리.get(키,[]) + [밸류에 넣고 싶은 값]
    # get에서 처음에 키값이 없을떄 빈 리스트를 가져오게 하고 
    # 그 뒤에 넣고 싶은 값 추가  
    Anagram[division_word] = Anagram.get(division_word,[]) + [word]

print(list(Anagram.values()))
