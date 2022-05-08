import sys

input = sys.stdin.readline

grade_list = []

for i in range(8):
    grade_list.append((int(input().strip()), i))

grade_list.sort(key=lambda a: -a[0])

answer_sum = 0
answer_list = []
for j in range(5):
    answer_sum += grade_list[j][0]
    answer_list.append((grade_list[j][1]+1))

answer_list.sort()
print(answer_sum)
for k in answer_list:
    print(k, end=' ')