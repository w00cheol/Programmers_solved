answer = 1e9
dic = {}
def dp(number, cnt):
    global answer
    if number in dic:
        answer = min(answer, cnt+dic[number])
        return
    if cnt >= 8 or number < 1: return
    for i in dic:
        dp(number - i, cnt+dic[i])
        dp(number + i, cnt+dic[i])
        if number % i == 0: dp(number//i, cnt+dic[i])
        dp(number * i, cnt+dic[i])

def solution(N, number):
    one = str(1)
    N = str(N)
    for i in range(1, 6):
        dic[int(one*i)] = i+1
        dic[int(N*i)] = i
    dp(number, 0)
    if answer > 8: return -1
    return answer