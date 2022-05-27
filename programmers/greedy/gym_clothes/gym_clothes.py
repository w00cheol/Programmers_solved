def solution(n, lost, reserve):
    count = 0
    L = list(sorted(set(lost)-set(reserve)))
    R = list(sorted(set(reserve)-set(lost)))
    for i in range(len(L)):
        if L[i]-1 in R:
            R.remove(L[i]-1)
        elif L[i]+1 in R:
            R.remove(L[i]+1)
        else: count += 1
    return n - count