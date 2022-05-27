def solution(bridge_length, weight, truck_weights):
    time = 1
    cnt = 0
    onBridge = [0]
    howLong = {}
    trucks = list(enumerate(truck_weights))
    del trucks[0]
    lenT = len(truck_weights)
    for i in range(lenT): howLong[i] = 0
    while trucks:
        sum = 0
        time += 1
        for i in onBridge: howLong[i] += 1
        if howLong[onBridge[0]] == bridge_length:
            del onBridge[0]
            cnt += 1
        for i in onBridge: sum+= truck_weights[i]
        if sum+trucks[0][1] <= weight:
            onBridge.append(trucks[0][0])
            del trucks[0]
    return time+bridge_length