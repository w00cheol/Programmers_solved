def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    offset = [rocks[0]]
    for i in range(1, len(rocks)):
        offset.append(rocks[i]-rocks[i-1])
    m = 1
    M = distance
    while m < M:
        cnt = 0
        medium = (m+M)//2
        copied = offset[::]
        for i in range(len(copied)-1):
            if copied[i] < medium:
                copied[i+1] += copied[i]
                cnt += 1
        if copied[-1] < medium:
            cnt += 1
        if cnt <= n:
            answer = max(answer, medium)
            m = medium + 1
        else:
            M = medium
    return answer