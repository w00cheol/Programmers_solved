from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    rank = 0
    
    while q:
        loc, priority = q.popleft()
        
        if any(priority < work[1] for work in q):
            q.append((loc, priority))
        else:
            rank += 1
            if loc == location:
                return rank