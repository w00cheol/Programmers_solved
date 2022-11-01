def solution(n, lost, reserve):
    L = list(set(lost)-set(reserve))
    R = set(reserve)-set(lost)
    
    for l in L:
        if l-1 in R:
            R.remove(l-1)
        elif l+1 in R:
            R.remove(l+1)
        else: n -= 1
        
    return n