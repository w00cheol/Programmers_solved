def solution(n, costs): # prim's algorithm
    costs.sort(key = lambda x: x[2])
    island = set((costs[0][0], costs[0][1]))
    answer = costs[0][2]
    
    while len(island) < n:
        for i in range(len(costs)):
            if costs[i][0] in island and costs[i][1] in island:
                continue
            elif costs[i][0] not in island and costs[i][1] not in island:
                continue

            answer += costs[i][2]
            island.add(costs[i][0])
            island.add(costs[i][1])
            costs.pop(i)
            break
            
    return answer