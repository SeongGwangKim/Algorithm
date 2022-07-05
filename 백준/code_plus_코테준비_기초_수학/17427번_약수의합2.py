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

# 1부터 N까지 N에서 i로 나눈 몫에 i를 곱한다.
'''
ex) N = 10
10 : 1 2     5         10
 9 : 1   3           9 
 8 : 1 2   4       8
 7 : 1           7
 6 : 1 2 3     6
 5 : 1       5
 4 : 1 2   4
 3 : 1   3
 2 : 1 2
 1 : 1

1 : 10개
2 :  5개
3 :  3개
4 :  2개
5 :  2개
6 :  1개
7 :  1개
8 :  1개
9 :  1개
10 : 1개
cf)

10//1 * 1 = 1 * 10 : 1이 10개
10//2 * 2 = 5 * 2 : 5가 2개 -> 10의 약수 중 5, 5의 약수 중 5
10//3 * 3 = 3 * 3 : 3이 3개 -> 9의 약수 중 3, 6의 약수 중 3, 3의 약수 중 3
10//4 * 4 = 2 * 4 : 2가 4개 -> 10의 약수 2, 8의 약수 2, 4의 약수 2, 2의 약수 2
'''
import sys

input = sys.stdin.readline
N = int(input())
ans = 0
for i in range(1, N+1):
    ans += (N//i)*i
print(ans)