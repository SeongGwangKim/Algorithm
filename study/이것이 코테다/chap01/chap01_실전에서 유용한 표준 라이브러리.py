'''
itertools : 순열 조합 라이브러리
heapq : heap 자료 구조 제공, 우선 순우 ㅣ큐
bisect : 이진 탐색 기능
collections : 덱, 카운터 등 자료 구조 포함
math : 제곱근 등등
'''

# 내장 함수
'''
sum()
min()
max()
eval()
sorted() : 리스트 등에서 정렬을 해주는 함수
'''
result = eval("(3+5)*7")
print(result)

result2 = sorted([9, 1, 8, 5, 4])
reverse_result2 = sorted([9, 1, 8, 5, 4], reverse=True)
print(result2)
print(reverse_result2)

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
result3 = sorted(array, key=lambda x: x[1], reverse=True)
print(result3)

# 최대 공약수와 최소 공배수 구하기
import math

def lcm(a, b):
    return a * b // math.gcd(a,b)

print(math.gcd(21, 14))
print(lcm(21, 14))