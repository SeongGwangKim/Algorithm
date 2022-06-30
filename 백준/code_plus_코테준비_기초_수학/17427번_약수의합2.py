'''
import sys

input = sys.stdin.readline

N = int(input())
ans = 0


def res(i):
    temp = 0
    for j in range(1, i+1):
        if i % j == 0:
            temp += j
    return temp


for i in range(1, N+1):
    ans += res(i)

print(ans)

'''
import sys

input = sys.stdin.readline
N = int(input())
sum = 0

for i in range(1, N+1):
  sum += (N//i)*i
print(sum)