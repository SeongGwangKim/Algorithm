def foo(name,  **kwargs):
    print(name)
    return 'name' in kwargs

value = foo('oliver', **{'name' : 2})

print(value)