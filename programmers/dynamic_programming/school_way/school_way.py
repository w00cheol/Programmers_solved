def solution(m, n, puddles):
    graph = [-1 for _ in range(m*n)]
    graph[0] = 1
    graph[1] = 1
    graph[m] = 1
    for i in range(len(puddles)):
        graph[(puddles[i][0]-1) + (puddles[i][1]-1)*m] = 0
    for i in range(len(graph)):
        if graph[i] == -1:
            if i < m: graph[i] = graph[i-1]
            elif i % m == 0: graph[i] = graph[i-m]
            else: graph[i] = graph[i-m] + graph[i-1]
    return graph[-1]%1000000007