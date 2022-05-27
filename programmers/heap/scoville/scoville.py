import heapq

def solution(scoville, K):
    mix = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        after = heapq.heappop(scoville)+2*heapq.heappop(scoville)
        heapq.heappush(scoville, after)
        mix+=1
    if scoville[0] >= K: return mix
    return -1