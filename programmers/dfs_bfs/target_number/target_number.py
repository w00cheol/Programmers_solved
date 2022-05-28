answer = 0
def dfs(numbers, target, now = 0):
    if len(numbers) == 1:
        last = numbers[0]
        if now + last == target or now - last == target:
            global answer
            answer += 1
        return
    
    new = numbers.pop()
    dfs(numbers[::], target, now + new)
    dfs(numbers[::], target, now - new)

def solution(numbers, target):
    dfs(numbers, target)
    return answer