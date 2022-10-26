
def solution(distance, rocks, n):
    max_of_min = 0
    rocks.sort()
    rocks.append(distance)
    
    # 출발지점과 첫 바위에 대한 간격 추가
    intervals = [rocks[0]]
    
    # 바위 간의 간격 저장
    for i in range(1, len(rocks)):
        intervals.append(rocks[i] - rocks[i-1])
        
    # 최소간격의 최소 경우와 최대 경우
    l, r = 0, distance
    
    # 바위 제거 수와 최소간격은 비례한다는 점을 두고,
    # 최소 간격의 모든 경우에 필요한 n을 찾는다.
    while l <= r:
        min_interval = (l+r) // 2
        remove = 0
        
        # 목표 최소간격을 넘기 위해 간격을 더해간다.
        collect = 0
        for i in range(len(intervals)):
            collect += intervals[i]
            
            # 아직 최소간격에 도달하지 못한다면, 바위를 지우고 간격을 더한다.
            if collect < min_interval:
                remove += 1
            else:
                collect = 0
        
        # n개 제거만으로 이 최소간격(min_interval)은 만들 수 없으니, 목표를 낮춘다.
        if remove > n:
            r = min_interval - 1
        # n개 이하로 이 최소간격(min_interval)을 만들 수 있다면,
        # 일단 정답에 저장 후, 목표를 더욱 높여본다.
        else:
            max_of_min = max(max_of_min, min_interval)
            l = min_interval + 1
    
    return max_of_min
