def solution(n, s):
    avg = s // n
    if avg == 0:
        return [-1]
    
    answer = [avg for _ in range(n)]
    for i in range(n-1, n-s%n-1, -1):
        answer[i] += 1
    
    return answer