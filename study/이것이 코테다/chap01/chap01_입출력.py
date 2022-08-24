# 기본 입출력
'''
data = input()
data02 = int(input())
a, b = map(int, input().split())
data03 = list(map(int, input().split()))

print(data)
print(data02)
print(a, b)
print(data03)


n = int(input())
data = list(map(int, input().split()))

print(n)
print(data)


# 빠른 입출력
import sys

input = sys.stdin.readline
data = input().strip()

print(data)
'''
# 연속 출력
print("가나다", end=' ')
print("라마바")

# 문자열에서 삽입 시 주의 사항
'''
','(콤마)는 연속 출력 가능하나 콤마 전에 띄어쓰기가 들어간다.
'+'는 문자열 출력 시 str 속성으로 변경해주어야 출력이 가능하다.
print("정답은" + answer + "입니다.")
'''
answer = 7
print("정답은", answer, "입니다.")
print("정답은" + str(answer) + "입니다.")

# f-string : f 옵션을 사용하여 문자열 안에서 {변수명}으로 출력
print(f"정답은 {answer}입니다.")