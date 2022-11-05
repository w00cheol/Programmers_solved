def solution(A, B):
    A.sort()
    B.sort()
    
    answer = 0
    a_runner = 0
    b_runner = 0
    
    while b_runner < len(A):
        if B[b_runner] <= A[a_runner]:
            b_runner += 1
            continue
        
        a_runner += 1
        b_runner += 1
        answer += 1
        
    return answer