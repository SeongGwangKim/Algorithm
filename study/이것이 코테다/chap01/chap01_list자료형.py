# 리스트 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a)
print(a[0])
print(a[-1])

# 리스트 슬라이싱 : 배열[시작:끝] -> 시작부터 끝-1까지 출력 / a[1], a[2]
print(a[1:3])

# 리스트 컴프리헨션
array = [i for i in range(10)]
print(array)

array01 = [i for i in range(20) if i % 2 == 1]
print(array01)

m = 3
n = 4
array02 = [[0] * m for _ in range(n)]
print(array02)

'''
list()
list 함수 관련 메소드
1. append(추가할 값)
2. sort(), sort(reverse=True)
3. reverse()
4. insert(삽입할 위치 인덱스, 삽입할 값)
5. count(특정 값)
6. remove(특정 값)
'''

list_set = [1, 2, 3, 4, 5, 6, 6]
remove_set = {3, 6}

result = [i for i in list_set if i not in remove_set]
print(result)