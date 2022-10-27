def solution(N, number):
    global answer
    answer = 9
    puzzles = [0] + [int(str(N)*i) for i in range(1, 10)]
    
    def dfs(current_value, used):
        if current_value == number:
            global answer
            answer = used # used < answer always
            return
        
        for i in range(1, answer - used):
            dfs(current_value + puzzles[i], used + i)
            dfs(current_value - puzzles[i], used + i)
            dfs(current_value // puzzles[i], used + i)
            dfs(current_value * puzzles[i], used + i)
            
        return

    dfs(0, 0)
    
    return answer if answer <= 8 else -1
