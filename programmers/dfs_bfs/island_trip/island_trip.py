import sys
sys.setrecursionlimit(10 ** 5)

def solution(maps):
    def dfs(r, c):
        if r < 0 or r >= len(maps) or c < 0 or c >= len(maps[0]):
            return 0
        if maps[r][c] == 'X':
            return 0
        
        food = int(maps[r][c])
        maps[r][c] = 'X'
        
        food += dfs(r, c + 1)
        food += dfs(r + 1, c)        
        food += dfs(r, c - 1)
        food += dfs(r - 1, c)
        
        return food
    
    answer = []
    
    for r in range(len(maps)):
        maps[r] = list(maps[r])
    
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            foods = dfs(r, c)
            if foods > 0:
                answer.append(foods)
    
    return sorted(answer) if answer else [-1]