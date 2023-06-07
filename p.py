import pandas as p
#import pandas -> pd=pandas.read...
#import pandas as 를 사용하면 원하는 이름으로 변경 가능/pandas를 부를 때 마다 지정한 이름으로 부를 수 있다
#from pandas import read_excel => read_excel()

pd = p.read_excel('D:/panda203033/TEST.xlsx')
print(pd) 

print(pd[0:2])
# print(type(pd))
pd1 = pd[0:2]

pd1.to_excel('D:/panda203033/test1.xlsx') 
#pd1에다가 pd[0:2]의 값을 넣고, panda203033 위치에 test1.xlsx 파일로 추가한다 라는 의미