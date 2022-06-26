# 과제

# 계산기 만들기
# 클래스 + 함수 강의에서 무조건 나오는 과제.
# class 명은 cal, 덧셈함수 add, 뺄셈함수 sub 두개만 만들어보기

#답안지
class cal():
    def __init__(self, num):
        self.num = num

    def add_1(self, num2):
        self.num += num2
        return self.num

    def sub_1(self, num2):
        self.num -= num2
        return self.num

exam_cal = cal(3)
print(exam_cal.add_1(4))
print(exam_cal.sub_1(2))


print("="*20)
'''
f = open('test.txt','r',encoding='utf8')
line = f.readlines()
f.close()


f = open('test.txt','r',encoding='utf8')
line = f.readlines()
f.close()

print(line) 
# 받아온 결과의 \n를 없애본다.
#결과  ['이름:이상훈', '지역:서울', '나이:32', '성별:남']

# 과제1)
temp = []
with open('test.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        temp.append(line)

print(temp)

# 과제2)
temp2 = []
with open('test.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(":")
        temp2.append(list(line))

print(temp2)
'''
# 과제3)
temp3 = []
with open('test.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(":")
        temp3.extend(line)

print(temp3)

# 과제
# 예외처리 구문에서 pass와 continue의 차이점을 서술하시오

# 답안 :
# pass는 다음을 실행하지만
# continue는 다음 loop로 넘어가 실행한다.

#과제
# 아래 배열에서 두번째 행중 5이상인 숫자의 배열만 선택하시오
import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9]])

a = x[1][x[1]>=5]
print(a)
#답안
x[1][x[1]>=5]

#과제 : date 에 저장된 각 월말 마다 시가총액(market_cap) 1등부터 5등까지 기업들을 모아보시오.
#Hint1. For Loop 사용
#Hink2. 저장을 위해 save_data = pd.DataFrame()  으로 비어있는 데이터프레임을 생성
#Hink3. pd.merge()를 활용하여 dataframe을 합치는 식으로 데이터 저장
#   df1 =  pd.merge([df1,df2])



#답안
import pandas as pd
data = pd.read_csv("dg_csv_kospi_201912301.csv")
date = data['trd_date'].unique()
save_data = pd.DataFrame()
for i in range(len(date)):
    first_data = data[data['trd_date']==date[i]]
    second_data = first_data.sort_values(by=['market_cap'],ascending=[False])
    save_data = pd.concat([save_data,second_data.iloc[:5,:]])