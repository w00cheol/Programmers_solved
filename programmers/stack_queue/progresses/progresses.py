from math import ceil

def solution(progresses, speeds):
    answer = []
    days = [ceil((100 - progresses[i]) / speeds[i]) for i in range(len(speeds))]

    runner = 0
    while runner < len(progresses):
        deploy = 0
        treshold = days[runner]
        
        while runner < len(progresses) and days[runner] <= treshold:
            deploy += 1
            runner += 1
        
        answer.append(deploy)
    
    return answer