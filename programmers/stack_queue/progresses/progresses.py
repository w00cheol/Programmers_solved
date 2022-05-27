def solution(progresses, speeds):
    answer = []
    day = cnt = 0
    lenP = len(progresses)
    for i in range(lenP):
        progresses[i] = -((-100+progresses[i])//speeds[i])
    while lenP:
        if day >= progresses[0]:
            del progresses[0]
            lenP = lenP - 1
            cnt = cnt + 1
            if lenP == 0: answer.append(cnt)
            continue
        elif cnt: answer.append(cnt)
        cnt = 0
        day = day + 1
    return answer