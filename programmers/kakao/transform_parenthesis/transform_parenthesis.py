def solution(p):
    if p == '': return ''
    open_num, close_num, index = 0, 0, 0
    if p[0] == '(':
        open_num += 1
    else:
        close_num += 1
    ## 분리 불가능한 균형잡힌 문자열 찾기 (key = 마지막 인덱스 값)
    while open_num != close_num:
        index += 1
        if p[index] == '(':
            open_num += 1
        else:
            close_num += 1
    ## 시작이 '(' 이라면, 완벽한 괄호
    if p[0] == '(':
        return p[:index+1] + solution(p[index+1:])
    else:
        return '(' + solution(p[index+1:]) + ')' + ''.join(list(map(lambda x: '(' if x == ')' else ')', [i for i in p[1:index]])))