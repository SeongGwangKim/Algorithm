# 조건문

x = 85

if x >= 90:
    print("학점 A")
elif x >= 80:
    print("학점 B")
elif x >= 70:
    print("학점 C")
else:
    print("학점 F")

# 비교 연산자
'''
x == y
x != y
'''

# 논리 연산자
'''
x and y : 둘 다 True이어야 True
x or y : 둘 중 하나만 True이어도 True
not x
'''

# in, not in 연산자
'''
x in 리스트 : 리스트 안에 x가 있으면 True
x not in 문자열 : 문자열 안에 x가 들어 있지 않으면 True
'''

# pass 완벽한 작성 전에 테스트 할 때 주로 사용
x = 85

if x >= 90:
    pass
elif x >= 80:
    print("학점 B")
elif x >= 70:
    print("학점 C")
else:
    print("학점 F")

# 조건문 간소화
'''
score = 85

if score >= 80: result = "success"
else: result = "Fail"
print(result)
'''
score = 85

result = "Success" if score >= 80 else "Fail"
print(result)

# 수학의 부등식
'''
if x > 0 and x < 20:
    print("x는 0초과 20미만의 수")
'''
x = 15
if 0 < x < 20:
    print("x는 0초과 20미만의 수")

