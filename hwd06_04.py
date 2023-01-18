# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

lst_word = ['eat','tea','tan','ate','nat','bat']

def group_anagrams(lst):
    result = {}
    for h in lst:
        s = ''.join(sorted(h))
        result[s] = result.get(s,[]) + [h]
    return list(result.values())

print(group_anagrams(lst_word))



'''a = 'eat'
print(sorted(a))
print(''.join(['a','b','c']))
word_dict = {}
if 'aet' not in word_dict:
    word_dict['aet'] = ['eat']'''