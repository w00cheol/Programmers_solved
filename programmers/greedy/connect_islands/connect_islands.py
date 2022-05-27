def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    island = dict(map(lambda x: reversed(x), (enumerate(set(map(lambda x: x[0], costs))|set(map(lambda x: x[1], costs))))))
    for i in costs:
        if island[i[0]] != island[i[1]]:
            answer += i[2]
            m, M = min(i[0],i[1]), max(i[0],i[1])
            value1 = island[m]
            value2 = island[M]
            for i in island:
                if island[i] == value2: island[i] = value1
            cnt = 0
            for i in island:
                if island[i] == value1: cnt += 1
            if cnt == n: return answer