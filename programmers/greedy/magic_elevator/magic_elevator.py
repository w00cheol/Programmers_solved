def solution(storey):
    answer, carry = 0, 0
    
    storey = list(map(int, str(storey)))
    idx = len(storey) - 1
    
    while idx >= 0:
        if storey[idx] == 10:
            if idx == 0:
                carry = 1
            else:
                storey[idx - 1] += 1
            continue
        
        if storey[idx] <= 4:
            answer += storey[idx]
            
        elif storey[idx] >= 6:
            answer += 10 - storey[idx]
            
            if idx == 0:
                carry = 1
            else:
                storey[idx - 1] += 1
            
        elif storey[idx] == 5:
            answer += 5
            has_to_up = False
            
            temp = idx
            while temp >= 0:
                if storey[temp] <= 4:
                    break
                elif storey[temp] >= 6:
                    has_to_up = True
                    break

                temp -= 1
            
            if temp == -1 and storey[0] == 5:
                has_to_up = True
            
            if has_to_up:
                storey[idx - 1] += 1
        
        idx -= 1
    
    return answer + carry