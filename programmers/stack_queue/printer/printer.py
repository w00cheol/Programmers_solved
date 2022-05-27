def solution(priorities, location):
    index = []
    printer = []
    re = j = 0
    lenP = len(priorities)
    for _ in range(lenP):
        index.append(_)
    while j < lenP-1:
        re = 0
        for i in index[j+1:]:
            if priorities[index[j]] < priorities[i]:
                index.append(index[j])
                del index[j]
                re = 1
                break
        if not re:
            printer.append(index[j])
            j += 1
    printer.append(index[j])
    return printer.index(location)+1