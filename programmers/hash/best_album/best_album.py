def solution(genres, plays):
    answer = []
    dic = {}
    lenS = len(genres)
    for i in range(lenS):
        if dic.get(genres[i]): dic[genres[i]] += plays[i]
        else: dic[genres[i]] = plays[i]
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(dic)):
        sortPlays = {}
        for j in range(lenS):
            if genres[j] == dic[i][0]:
                sortPlays[j] = plays[j]
        sortPlays = sorted(sortPlays.items(), key=lambda x: x[1], reverse=True)
        answer.append(sortPlays[0][0])
        if len(sortPlays)>=2: answer.append(sortPlays[1][0])
    return answer