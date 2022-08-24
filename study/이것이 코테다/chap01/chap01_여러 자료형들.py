## 문자열''
## 튜플()
## 사전{key:value}
## 집합{}


# 문자열
'''
+ 문자열 합함
* 문자열 여러 번 반복
문자열 객체는 안에 내용을 변경할 수 없음
'''

# 튜플 ()
'''
tuple()
한 번 선언된 값은 변경 불가
리스트보다 더 적은 양의 메모리를 사용

# 주로 사용할 경우
서로 다른 성질의 데이터를 묶어서 관리해야 할 때 사용
해싱의 키 값으로 데이터의 나열을 사용해야 할 때
리스트보다 메모리를 효율적으로 사용해야 할 때
'''

# 사전 {key:value}
'''
= hash table
dict()
keys() : 키만 출력
values() : 값만 출력
'''
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['복숭아'] = 'Peach'
'''
위와 같은 형태
data = {
    '사과' : 'Apple',
    '바나나' : 'Banana',
    '복숭아' : 'Peach'
}
'''

print(data)
# key값만 조회 사용 가능
if '사과' in data:
    print("사과 존재")

key_list = list(data.keys())
print(key_list)

value_list = list(data.values())
print(value_list)

print(data['사과'])

# 집합 자료형
'''
set([])
시간 복잡도 O(1)
중복 허용 x
순서 x
리스트 혹은 문자열을 이용해서 초기화 가능

# 집합 연산
1) 합집합 |
2) 교집합 &
3) 차집합 -

# 집합 함수 메소드
1) add(추가 할 값)
2) update([추가할 값들]) : 컴마로 구분
3) remove(제거할 값)

'''

set_data01 = set([1,1,2,2,3,3,4,4,5,5])
set_data02 = {1,1,2,2,3,3,4,4,5,5}

print(set_data01)
print(set_data02)
