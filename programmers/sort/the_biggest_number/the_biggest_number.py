def solution(numbers):
    answer = ''.join(map(str, list(reversed(sorted(numbers, key=lambda mul: str(mul)*3)))))
    if answer[0] == '0': return '0'
    return answer