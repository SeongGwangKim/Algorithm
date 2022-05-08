import sys
input = sys.stdin.readline

T = int(input().strip())


for _ in range(T):
    temp = int(input())
    temp_list = [list(map(int, input().split())) for _ in range(temp)]
    temp_list.sort(key=lambda a: a[0])

    cnt = 1

    min = temp_list[0][1]

    for i in range(1, temp):
        if temp_list[i][1] < min:
            min = temp_list[i][1]
            cnt += 1
    print(cnt)



