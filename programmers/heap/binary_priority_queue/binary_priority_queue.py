import heapq

def solution(operations):
    answer = []
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(answer, int(i[2:]))
        if i[0] == 'D' and answer:
            if i[2] == '1':
                target = -1
                for x in range(1, (len(answer)+1)//2):
                    if answer[-x] > answer[target]: target = -x
                del answer[target]
                heapq.heapify(answer)
            elif i[2] == '-':
                heapq.heappop(answer)
    if answer:
        return [max(answer), answer[0]]
    return [0,0]