from collections import deque

def solution(n, edge):
    q = deque()
    q.append([1, 0]) # it means that distance to node.1 (from node.1) is 0

    visit = [False for _ in range(n)] # check visited nodes
    visit[0] = True
    
    distance = [2e9 for _ in range(n)] # initialize all the distance of node
    distance[0] = 0
    
    graph = [[] for _ in range(n+1)]
    for i in range(len(edge)): #O(N)
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
        
    while q: #O(N)
        now = q.popleft()
        distance[now[0]-1] = now[1]
        for i in graph[now[0]]:
            if visit[i-1] == False:
                q.append([i, now[1]+1])
                visit[i-1] = True
                
    return distance.count(max(distance))