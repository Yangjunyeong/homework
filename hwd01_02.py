score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm'] = 90
score['python'] = 85

total = sum(score.values())
print(total/len(score))

# 점수를 추가, 수정하고 평균구하기

