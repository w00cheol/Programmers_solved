answer = 2e9

def dfs(now, target, words, cnt):
    if now == target:
        global answer
        answer = min(answer, cnt)
        return
    if not words: return
    lenWord = len(words[0])
    for i in range(len(words)):
        diff = 0
        for j in range(lenWord):
            if now[j] != words[i][j]:
                diff += 1
        if diff == 1:
            dfs(words[i], target, words[:i]+words[i+1:], cnt+1)

def solution(begin, target, words):
    dfs(begin, target, words, 0)
    if answer == 2e9: return 0
    return answer