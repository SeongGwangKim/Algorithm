# 함수
def operator(a, b):
    add_var = a+b
    subtract_var = a-b
    multiply_var = a*b
    divide_var = a//b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(f"각각의 값은 {a}, {b}, {c}, {d}이다.")

# 람다
print((lambda a, b: a+b)(3, 7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
# 위와 같은 형태
print(sorted(array, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result))