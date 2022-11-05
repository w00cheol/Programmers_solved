import heapq as hq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    works = [-work for work in works]
    hq.heapify(works)

    for _ in range(n):
        solve = hq.heappop(works)
        hq.heappush(works, solve + 1)

    for work in works:
        answer += work ** 2

    return answer