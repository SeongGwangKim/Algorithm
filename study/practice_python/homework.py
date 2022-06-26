#과제(1)
#  x = 5.0, y = 3 을 입력하고, 결과창으로
# "x + y = 8.0 입니다" 를 출력하는 함수 작성
x=5.0
y=3

#답안지
print("""x + y = {0}""".format(x+float(y)))

print('='*20)
#과제(2)
# x = "than3k"
# y = "yo97u"
# x와 y를 위와 같이 선언한 후에, 강의에서 학습한 함수를 사용하여 "thank you"를 출력해본다.


# 답안지
x = "than3k"
y = "yo97u"

x = x.split('3')
x = ''.join(x)
y = y.split('97')
y = ''.join(y)
print(x, y)

x = "than3k"
y = "yo97u"
print(x.replace("3",""), y.replace("97",""))

print('='*20)
# 과제
# 리스트를 다음과 같이 선언한 후에 lst1 = [1,2,3,4,5,6,7,8,9,10]
# lst2 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5] 의 결과가 나오도록 한줄 코딩을 해본다.
lst1 = [1,2,3,4,5,6,7,8,9,10]

#답안지
lst2 = lst1[5:] + lst1[:5]
print(lst2)

print('='*20)
# 과제
# 튜플은 값을 변경할 수 없는것이 가장 큰 특징이다.
# 하지만 만약 튜플의 값을 변경해야 한다면 ??
# tpl = (0,1,2,3) 을 선언 한 다음, tpl = (0,1,2,3,4)로 수정해본다.
# 힌트는 list를 이용하는 것
tpl = (0,1,2,3)

# 답안지
tpl = list(tpl)
tpl.append(4)
tpl = tuple(tpl)
print(tpl)

print('='*20)
# <<<<과제>>>>
# 아래 list를 a라는 dictionary에 1번 : 이정재, 2번: 박해수 식으로 딕셔너리를 만들어보자
name = ['이정재', '박해수', '오영수', '위하준', '정호연', '허성태', '미주령']

# 답안지
a = dict()
for i, j in enumerate(name):
    a["{0}번".format(i+1)] = j
print(a)

# 첫번째 방법
a = dict()
b = []
for i in range(1, len(name) + 1):
    b.append("{}번".format(i))

for i in range(0, len(name)):
    a[b[i]] = name[i]

# 두번째 방법
a = dict(zip(b, name))