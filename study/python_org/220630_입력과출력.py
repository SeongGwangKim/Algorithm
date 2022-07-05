yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
# {:-9} 9칸 배정
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

print('='*50)

s = 'Hello, world.'
str(s)

repr(s)

str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
print('='*50)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
# repr()은 \ 즉, 이스케이프 문자도 문자 취급을 하여 출력한다. 또한 코테이션으로 감싸져서 출력이 된다.(" ' ~ ' ")
hellos = repr(hello)
helloos = str(hello)
print(hellos)
print(helloos)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))
print(type(repr((x, y, ('spam', 'eggs')))))

print('='*50)
import math

# 포맷 문자열 문자 f를 활용하여 문자열에 {value}를 통해 출력이 가능.
print(f'The value of pi is approximately {math.pi:.3f}.')

print('='*50)
# 포맷 문자열 문자 f를 사용하고 {} 사이에 {:문자폭숫자}로 사용하여 문자폭을 지정할 수 있다.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print('='*50)
animals = 'eels'
# 포맷 문자열 문자 f 괄호 안 value 뒤에 '!a'는 ascii()를, '!s'는 str()을, '!r'는 repr()을 적용한다.
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!s}.')
print(f'My hovercraft is full of {animals!r}.')

print('='*50)
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
print('same = ')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print('='*50)
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('='*50)
# .ljust()  .rjust()  .center() 각각 좌측 정렬, 우측 정렬, 중앙 정렬
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))