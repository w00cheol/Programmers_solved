def alphabet(s):
    count = 0
    for i in s:
        count += min(ord(i)-ord('A'), ord('Z')-ord(i)+1)
    return count

def solution(name):
    minimum = 1000
    rmA = list(filter(lambda x: x[1]!='A', enumerate(name[::])))
    nums = list(map(lambda y: y[0], rmA))
    alpha = list(map(lambda y: y[1], rmA))
    lenName = len(name)
    lenNums = len(nums)
    if lenNums == 0: return 0
    elif lenNums == 1:
        return min(nums[0], lenName-nums[0]) + alphabet(name[nums[0]])
    else:
        minimum = min(lenName-nums[0], nums[-1])
        for i in range(lenNums-1):
            a = nums[i]
            b = nums[i+1]
            minimum = min(minimum, 2*a + (lenName-b), a + 2*(lenName-b))
    return minimum + alphabet(alpha)