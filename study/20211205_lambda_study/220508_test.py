s ='aabcbcd'
cnt = 0

while(True):
    if 'abc' in s:
        cnt += 1
        s = s.replace('abc', '')
        print(s)
    else:
        print('cnt = ', cnt)
        break