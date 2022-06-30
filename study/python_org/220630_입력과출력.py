yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
# {:-9} 9칸 배정
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

print('='*20)

s = 'Hello, world.'
str(s)

repr(s)

str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
print('='*20)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
# repr()은 \ 즉, 이스케이프 문자도 문자 취급을 하여 출력한다. 또한 코테이션으로 감싸져서 출력이 된다.(" ' ~ ' ")
hellos = repr(hello)
helloos = str(hello)
print(hellos)
print(helloos)

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))