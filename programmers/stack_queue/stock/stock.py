'''
=알고리즘
time 과 index 는 같다.
stack이 비어있으면 prices의 다음 index 추가
stack의 마지막 값을 max values' index (=the time that max is appered) 로 간주
다음 prices[index] 값이 stack의 마지막 값과 같거나 더 크면 append
더 작으면 time - stack.pop() 이 버틴 시간. 이걸 answer.append()
더 작지 않을 때까지 Line8 을 계속 반복
time이 lenP 에 도달할때 stack 에 남은 값들은 끝까지 버틴 것이기 때문에 time에서 index 빼서 출력
=시간복잡도
O(n)
'''

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    time = 0
    
    while time < len(prices):
        while stack and prices[time] < prices[stack[-1]]:
            appeared_time = stack.pop()
            answer[appeared_time] = time - appeared_time
            
        stack.append(time)
        time += 1
    
    time -= 1
    while stack:
        appeared_time = stack.pop()
        answer[appeared_time] = time - appeared_time
        
    return answer