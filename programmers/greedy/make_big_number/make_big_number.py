def solution(number, k):
    result=[number[0]]
    
    for n in number[1:]:
        while result and result[-1] < n and k > 0:
            result.pop()
            k -= 1
        result.append(n)
        
    return ''.join(result[:len(result)-k])