words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for i in range(1,len(words)):
    if words[i-1][-1] != words[i][0]:
        print(f'{i+1}번 탈락')
        break
    else:
        ban_wd = list(word for word in words if words.index(word) < i)
        if words[i] in ban_wd:
            print(f'{i+1}번 탈락')
            break
