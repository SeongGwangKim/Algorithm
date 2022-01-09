class Solution:
    def solution(self, code, message):
        listTemp = []
        code = "abcdefghijklmnopqrstuvwxyz"
        answer = code
        if message.isdigit() == True:
            temp = int(len(message) / 2)

            for i in range(0, temp):
                temp01 = int(message[i * 2: i * 2 + 2]) + 96
                listTemp.append(chr(temp01))

            answer = ''.join(str(e) for e in listTemp)

        else:
            list(message)

            for trans in list(message):

                if 0 < ord(trans) - 96 < 10:
                    listTemp.append(str((ord(trans) - 96)).zfill(2))

                else:
                    listTemp.append((ord(trans) - 96))

            answer = ''.join(str(e) for e in listTemp)

        return answer

code = "abcdefghijklmnopqrstuvwxyz"
message = "test"
#Solution.solution(code, message)

'''
listTemp = []
list(message)
for trans in list(message):
    listTemp.append(((ord(trans))-96))
print(listTemp)
print(''.join(str(e) for e in listTemp))
'''

'''
print('-------------------------')
listTemp = []
temp = int(len(message)/2)

for i in range(0, temp):
    temp01 = int(message[i*2: i*2 + 2])+96
    listTemp.append(chr(temp01))

print(listTemp)
#print(''.join(str(e) for e in listTemp))
'''
t = 20
e = 05 = 5
s = 19
t = 20
test -> 20051920


list(code)

print(Solution.solution(code, message))
