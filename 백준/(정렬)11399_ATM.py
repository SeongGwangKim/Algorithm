N = int(input())

array_list = list(map(int, input().split()))

array_list.sort(reverse=True)

answer = 0

for i in range(N):
    answer = answer + (i + 1) * array_list[i]

print(answer)