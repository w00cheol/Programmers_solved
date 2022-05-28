def solution(n, computers):
    island = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if island[k] == island[i]: island[k] = island[j]
    return len(set(island))