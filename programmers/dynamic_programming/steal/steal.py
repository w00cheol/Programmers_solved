def solution(money):
    lenM = len(money)
        
    answer1 = [0]*lenM
    answer1[0] = 0
    answer1[1] = money[1]
    for i in range(2, lenM):
        answer1[i] = max(answer1[i-1], answer1[i-2]+money[i])
        
    answer2 = [0]*lenM
    answer2[0] = money[0]
    answer2[1] = max(money[0], money[1])
    money[-1] = 0
    for i in range(2, lenM):
        answer2[i] = max(answer2[i-1], answer2[i-2]+money[i])
    return max(answer1[-1], answer2[-1])