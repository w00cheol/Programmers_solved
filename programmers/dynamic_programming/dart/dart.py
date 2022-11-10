import heapq

def solution(target):
    memo = {0: [0, 0]}

    def dp(score):
        if score in memo:
            return memo[score]

        temp = []
        if score - 50 >= 0:
            count, s_b = dp(score - 50)
            heapq.heappush(temp, [count + 1, -(s_b + 1)])

        for i in range(1, 21):
            if score - 3*i >= 0:
                count, s_b = dp(score - 3*i)
                heapq.heappush(temp, [count + 1, -s_b])
            if score - 2*i >= 0:
                count, s_b = dp(score - 2*i)
                heapq.heappush(temp, [count + 1, -s_b])
            if score - i >= 0:
                count, s_b = dp(score - i)
                heapq.heappush(temp, [count + 1, -(s_b + 1)])

        memo[score] = [temp[0][0], -temp[0][1]]

        return memo[score]
    
    skip = 0
    while target > 300:
        target -= 60
        skip += 1

    answer = dp(target)
    return [answer[0] + skip, answer[1]]