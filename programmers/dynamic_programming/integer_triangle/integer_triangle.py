def solution(triangle):
    answer = 0
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i+1])):
            if j == 0: triangle[i+1][0] += triangle[i][0]
            elif j == len(triangle[i]): triangle[i+1][-1] += triangle[i][-1]
            else:
                triangle[i+1][j] += max(triangle[i][j-1], triangle[i][j])
    return max(triangle[-1])