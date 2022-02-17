'''
# 내 풀이 : 정답은 맞췄으나 시간 초과...
N, P = map(int, input().split())
melody= [[] for i in range(7)]
cnt = 0


def AddMelody(row, fret):
    global cnt
    for i in range(1, 6):
        if i == row:
            if melody[i]:
                if melody[i][-1] < fret:
                    melody[i].append(fret)
                    cnt = cnt + 1
                elif melody[i][-1] > fret:
                    while fret < melody[i][-1]:
                        if len(melody[i]) == 1:
                            melody[i].pop()
                            cnt = cnt + 1
                            break
                        else:
                            melody[i].pop()
                            cnt = cnt + 1
                    if melody[i]:
                        if melody[i][-1] == fret:
                            break
                        else:
                            melody[i].append(fret)
                            cnt = cnt + 1
                    elif len(melody[i]) == 0:
                        melody[i].append(fret)
                        cnt = cnt + 1
            else:
                melody[i].append(fret)
                cnt = cnt + 1


for i in range(N):
    temp = list(map(int, input().split()))
    AddMelody(temp[0], temp[1])

print(cnt)
'''
# 해설
import sys

input = sys.stdin.readline
N, P = map(int, input().split())
stk = [[] for _ in range(7)]
answer = 0

for _ in range(N):
    line, p = map(int, input(). split())

    while stk[line] and stk[line][-1] > p:
        stk[line].pop()
        answer = answer + 1

    if stk[line] and stk[line][-1] == p:
        continue

    stk[line].append(p)
    answer = answer + 1

print(answer)