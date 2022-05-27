def solution(routes):
    answer = i = 0
    routes.sort()
    lenR = len(routes)
    while i < lenR:
        cnt = 1
        end = routes[i][1]
        while i+cnt < lenR and end >= routes[i+cnt][0]:
            end = min(end, routes[i+cnt][1])
            cnt += 1
        i += cnt
        answer += 1
    return answer