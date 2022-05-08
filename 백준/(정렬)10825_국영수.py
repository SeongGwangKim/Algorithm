import sys
input = sys.stdin.readline

N = int(input().strip())

grade_list = []

for _ in range(N):
    name, kor, eng, mat = map(str, input().split())
    grade_list.append((name, int(kor), int(eng), int(mat)))

grade_list.sort(key=lambda a: a[0])
grade_list.sort(reverse=True ,key=lambda a: a[3])
grade_list.sort(key=lambda a: a[2])
grade_list.sort(reverse=True ,key=lambda a: a[1])

for grade in grade_list:
    print(grade[0])