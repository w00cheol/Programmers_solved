def solution(nums):
    return min(len(nums)>>1, len(set(nums)))