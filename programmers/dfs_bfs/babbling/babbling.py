def solution(babbling):
    global answer
    answer = 0
    
    def dfs(string):
        if not string:
            global answer
            answer += 1
            return
        
        if len(string) >= 2 and string[0:2] == "ye" or string[0:2] == "ma":
            dfs(string[2:])
        if len(string) >= 3 and string[0:3] == "woo" or string[0:3] == "aya":
            dfs(string[3:])
        
        return
                
    for i in babbling:
        dfs(i)
    
    return answer