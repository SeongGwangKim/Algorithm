Score = [85, 90, 80, 75, 95]
print(Score[3])

import pandas as pd
dictionary = {"성별":"남자", "이름":"이상훈","지역":"서울","나이":"32"}
exam = pd.Series(dictionary)
print(exam.loc['이름':'나이'])
print(exam.iloc[1])