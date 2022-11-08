from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    time = 0
    
    while truck_weights:
        time += 1
        bridge_weight -= bridge.popleft()
        
        if bridge_weight + truck_weights[0] <= weight:
            truck_weight = truck_weights.popleft()
            bridge.append(truck_weight)
            bridge_weight += truck_weight
        else:
            bridge.append(0)
        
    while bridge_weight > 0:
        time += 1
        bridge_weight -= bridge.popleft()
        
    return time