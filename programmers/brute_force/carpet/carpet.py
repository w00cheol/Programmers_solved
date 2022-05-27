def solution(brown, yellow):
    num = brown + yellow
    for i in range(3, int(num**1/2)+1): 
        if num%i == 0 and (num//i-2)*(i-2) == yellow: return [num//i, i]