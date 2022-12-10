def solution(k, ranges):
    def makeHailSequence(k):
        while k != 1:
            if k % 2 == 0:
                k = k // 2
                sequence.append(k)
            else:
                k = k * 3 + 1
                sequence.append(k)
                
        return len(sequence)
                
    def hailIntegral(start, end):
        if start > end:
            return -1.0
        
        area = 0
        for i in range(start, end):
            area += (sequence[i] + sequence[i + 1]) / 2
            
        return area

    sequence = [k]
    len_s = makeHailSequence(k)
    
    answer = []
    for r in ranges:
        answer.append(hailIntegral(r[0], len_s + r[1] - 1))
        
    return answer