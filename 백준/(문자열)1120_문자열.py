import sys
input = sys.stdin.readline

A, B = map(str, input().split())
A_list = list(A)
B_list = list(B)

cnt_list = []

if len(A) == len(B):
    cnt = 0
    for i in range(len(A)):
        if A_list[i] != B_list[i]:
            cnt += 1
    print(cnt)
else:
    for i in range(len(B)-len(A)+1):
        cnt = 0
        for j in range(len(A)):
            if A_list[j] != B_list[i+j]:
                cnt += 1
        cnt_list.append(cnt)
    print(min(cnt_list))