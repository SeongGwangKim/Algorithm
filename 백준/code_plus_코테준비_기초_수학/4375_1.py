import sys
input = sys.stdin.readline

def add_count(n):
    num = 0
    i = 1
    while True:
      # 1 -> 11 -> 111 ... 쭉 1이 추가되면서 숫자 증가
      num = num * 10 + 1
      # n으로 num 값이 나누어 떨어 진다면 그 때 1이 더해진 횟수를 출력
      if num % n == 0:
        print(i)
        break
      else:
        i += 1

while True:
  # 입력되는 값이 없으면 stop
    try:
        n = int(input())
    except:
        break
    add_count(n)



