from math import sqrt, floor

def solution(begin, end):
    answer = []
    
    if begin == 1:
        answer.append(0)
        begin = 2
    
    for n in range(begin, end + 1):
        if n % 2 == 0 and n // 2 <= 10000000:
            answer.append(n // 2)
        else:
            answer.append(1)
            
            for i in range(2, floor(sqrt(n)) + 1):
                if n % i == 0 and n // i <= 10000000:
                    answer[-1] = n // i
                    break
            
    return answer