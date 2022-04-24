'''
s = 'aacddefg'


def list_overlap_del(s):
    list_temp = []

    for i in range(len(s)):
        if i == 0:
            list_temp.append(s[i])
        elif list_temp[-1] != s[i]:
            list_temp.append(s[i])

    return list_temp
'''


def solution(n, m):
    cache = [-1] * 51
    cache[0] = 0
    cache[1] = 1

    for i in range(2, m + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    answer = 0

    for i in range(n, m + 1):
        answer = answer + cache[i]

    return answer

