def solution(n, times):
    answer = 0
    lenT = len(times)
    M = n*times[0]
    m = 0
    while M > m:
        cnt = 0
        medium = (M+m)//2
        for i in range(lenT):
            cnt += medium//times[i]
        if cnt >= n:
            answer = medium
            M = medium
        else:
            m = medium+1
    return answer