N, M = map(int, input().split())

for i in range(N//2):
    print('-' * ((M-(2*i+1)*3)//2) + '.|.'*(2*i + 1) + '-' * ((M-(2*i+1)*3)//2))

print('-'*((M-7)//2) + 'WELCOME' + '-'*((M-7)//2))

for i in range((N//2 - 1), -1, -1):
    print('-' * ((M-(2*i+1)*3)//2) + '.|.'*(2*i + 1) + '-' * ((M-(2*i+1)*3)//2))

for i in range((N//2 - 1), -1, -1):
    print(i)

print((N//2 - 1))