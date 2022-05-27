answer = set([])
def isSosu(n):
    if n == 0 or n == 1: return 0
    for i in range(2, (n+1)//2+1):
        if n%i == 0: return 0
    return 1

def recur(s, lenS, other, lenOther, n):
    if lenS == n:
        result = int(s)
        if isSosu(result):
            answer.add(result)
            return
    for i in range(lenOther):
        recur(s+other[i], lenS+1,  other[0:i]+other[i+1:], lenOther-1, n)
        
def solution(numbers):
    lenN = len(numbers)
    for i in range(lenN):
        recur('', 0, numbers, lenN, i+1)
    return len(answer)