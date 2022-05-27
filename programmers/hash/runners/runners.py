def solution(participant, completion):
    key = 0
    dic = {}
    for i in participant:
        dic[hash(i)] = i
        key += hash(i)
    for i in completion:
        key -= hash(i)
    return dic[key]