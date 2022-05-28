answer = []

def dfs(tickets, route):
    if not tickets:
        global answer
        if not answer:
            answer = route
        return
    
    for i in range(len(tickets)):
        if tickets[i][0] == route[-1]:
            plan = route[::]
            plan.append(tickets[i][1])
            dfs(tickets[:i]+tickets[i+1:], plan)

def solution(tickets):
    tickets.sort()
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            dfs(tickets[:i]+tickets[i+1:], tickets[i])
    return answer