lst_word = ['eat','tea','tan','ate','nat','bat']

def group_anagrams(lst):
    result = {}
    for h in lst:
        s = ''.join(sorted(h))
        result[s] = result.get(s,[]) + [h]
    
    print(result)

