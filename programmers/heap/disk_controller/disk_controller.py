import heapq
def solution(jobs):
    answer = complete = time = working = 0
    todo = sorted(jobs)
    waiting = []
    complete += todo[0][0] + todo[0][1]
    working = [(heapq.heappop(todo))[0]]
    while todo or waiting or working:
        while todo and todo[0][0] == time:
            heapq.heappush(waiting, [todo[0][1],todo[0][0]])
            heapq.heappop(todo)
        if time == complete: answer += time - working.pop()
        if time >= complete and waiting:
            working.append(waiting[0][1])
            complete = time + (heapq.heappop(waiting))[0]
        time += 1
    return answer//len(jobs)