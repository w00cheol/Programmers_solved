import heapq
from collections import deque

def solution(jobs):
    jobs = deque(sorted(jobs))
    lenJobs = len(jobs)
    waiting = []
    total = 0
    
    while jobs or waiting:
        if waiting: # if any task should be started instantly
            cost, start = heapq.heappop(waiting)
            finish += cost
        else: # nothing to do for now
            cost, start = jobs.popleft()[::-1]
            finish = start + cost
            
        total += finish - start
        
        # while process is running,
        # recieve and rank other tasks in order of cost
        while jobs and jobs[0][0] <= finish:
            heapq.heappush(waiting, jobs.popleft()[::-1])
            
    return total // lenJobs