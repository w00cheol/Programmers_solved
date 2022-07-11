def solution(record):
    answer = []
    dic = {}
    for i in range(len(record)):
        index1 = record[i].find(' ')
        task = record[i][:index1]
        if task == 'Leave':
            answer.append(record[i][index1+1:] + ' ' + task)
        else:
            index2 = record[i][index1+1:].find(' ')
            uid = record[i][index1+1:index1+index2+1]
            name = record[i][index1+index2+2:]
            dic[uid] = name
            if task == "Enter":
                answer.append(uid + ' ' + task)
    for i in range(len(answer)):
        index1 = answer[i].find(' ')
        if answer[i][index1+1:] == 'Enter':
            answer[i] = dic[answer[i][:index1]] + '님이 들어왔습니다.'
        else:
            answer[i] = dic[answer[i][:index1]] + '님이 나갔습니다.'
    return answer