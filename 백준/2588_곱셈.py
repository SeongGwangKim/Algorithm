A = 472
B = 385

for i in range(1, 4):
    # print(i)
    print(B//(10**i))
    B = B - (B//(10**i))*(10**i)
    print('=====')
