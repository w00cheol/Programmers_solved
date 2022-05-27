from collections import Counter

def solution(clothes):
    answer = 1
    dic =  list(Counter([i[1] for i in clothes]).values())
    for i in range(len(dic)):
        answer = answer * (dic[i]+1)
    return answer-1