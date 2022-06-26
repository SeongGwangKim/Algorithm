
for j in range(5, 0, -1):
    print("*" * j)

print("="*10)
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print("")

print("="*10)
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

print("="*10)

for i in range(5, 0, -1):
    print("{:>5}".format("*"*i))

print("="*10)

for i in range(4):
    for j in range(i+1):
        print(" "*(4-i) + "*"*(j+1), end="")
    print("")