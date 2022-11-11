from collections import deque

def solution(maps):
    def bfs(y, x):
        q = deque()
        q.append((y, x, 1))
        
        while q:
            y, x, distance = q.popleft()
            
            if y == len(maps)-1 and x == len(maps[0])-1:
                return distance
            
            if maps[y][x] == 0:
                continue
            maps[y][x] = 0
            
            if y+1 < len(maps):
                q.append((y+1, x, distance+1))
            if x+1 < len(maps[0]):
                q.append((y, x+1, distance+1))
            if y-1 >= 0:
                q.append((y-1, x, distance+1))
            if x-1 >= 0:
                q.append((y, x-1, distance+1))
        
        return -1
    
    return bfs(0, 0)