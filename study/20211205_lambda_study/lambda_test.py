pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

pairs.sort(key=len)
for pair in pairs:
    print(pair)

print('-----------------------------------')
num_list = [15, 22, 8, 79, 10]
num_list.sort()
print(num_list)

print('-----------------------------------')
num_list02 = [15, 22, 8, 79, 10]
num_list02
print(num_list02.sorted())