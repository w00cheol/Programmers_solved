from collections import defaultdict

def solution(arrows):
    answer = 0
    
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    x, y = 0, 0
    
    visit = defaultdict(set)
    visit[(x, y)].add((dx[arrows[0]], dy[arrows[0]]))
    visit[(x + dx[arrows[0]], y + dy[arrows[0]])].add((-dx[arrows[0]], -dy[arrows[0]]))
    
    for i in arrows:
        x += dx[i]
        y += dy[i]
        if (x, y) in visit:
            if (-dx[i], -dy[i]) not in visit[(x, y)]:
                answer += 1
        visit[(x, y)].add((-dx[i], -dy[i]))
        visit[(x-dx[i], y-dy[i])].add((dx[i], dy[i]))
        
        
        x += dx[i]
        y += dy[i]
        if (x, y) in visit:
            if (-dx[i], -dy[i]) not in visit[(x, y)]:
                answer += 1
        visit[(x, y)].add((-dx[i], -dy[i]))
        visit[(x-dx[i], y-dy[i])].add((dx[i], dy[i]))
    
    return answer