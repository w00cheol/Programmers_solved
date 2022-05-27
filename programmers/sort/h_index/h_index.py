def solution(citations):
    answer = i = 0
    citations.sort()
    if citations[-1] == 0:
        return 0
    while citations[i] <= len(citations[i:]):
        answer = citations[i]
        i += 1
    for j in range(answer+1, citations[i]):
        if j <= len(citations[i:]): answer += 1
        else: return answer