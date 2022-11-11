def solution(s):
    status = 0
    
    for parenthesis in s:
        if parenthesis == ')':
            status -= 1
            if status < 0:
                return False
        else:
            status += 1

    return True if status == 0 else False