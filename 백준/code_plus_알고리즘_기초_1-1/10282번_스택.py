import sys
input = sys.stdin.readline

temp_list = []

N = int(input())

for _ in range(N):
    str = input().rstrip()
    if 'push' in str:
        p, num = str.split()
        temp_list.append(num)
    elif 'pop' in str:
        if temp_list:
            print(temp_list.pop())
        else:
            print(-1)
    elif 'size' in str:
        print(len(temp_list))
    elif 'empty' in str:
        if not temp_list:
            print(1)
        else:
            print(0)
    elif 'top' in str:
        if not temp_list:
            print(-1)
        else:
            print(temp_list[-1])


