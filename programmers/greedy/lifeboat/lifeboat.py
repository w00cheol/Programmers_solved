def solution(people, limit):
    i = 1
    cnt = 0
    j = -1
    people.sort()
    while i+j <= (len(people)-1):
        cnt += 1
        sum = people[-i]
        i += 1
        while sum+people[j+1] <= limit:
            sum += people[j+1]
            j += 1
    return cnt