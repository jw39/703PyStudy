import pandas as pd
import numpy as np
from pandas import read_excel #왜 read_excel 사라졌냐
# df = pd.DataFrame(data='', index='', columns='')


# 1. Create Pandas Dataframe
from IPython.display import display 
#ipython 안에 있는 클래스 이름 display이고, import는 메소드 이름


# Take a 2D array as input to your DataFrame 
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
display(pd.DataFrame(my_2darray))

# Take a dictionary as input to your DataFrame 
my_dict = {"a": ['1', '3'], "b": ['1', '2'], "c": ['2', '4']}
display(pd.DataFrame(my_dict))

# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
display(pd.DataFrame(my_df))

# Take a Series as input to your DataFrame
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
display(pd.DataFrame(my_series))

##########################

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))

# Use the `shape` property
print(df.shape)

# Or use the `len()` function with the `index` property
print(len(df.index))

list(df.columns)

####################
df = pd.DataFrame({"A":[1,4,7], "B":[2,5,8], "C":[3,6,9]})

# Use `iloc[]` to select a row
display(df.iloc[0])
display(df.loc[0])
# display(df.ix[0]) ix 안됨


# Use `loc[]` to select a column
display(df.loc[:,'A'])
display(df['A'])

# 특정 row, column을 선택하기
# display(df.ix[0]['A'])  ix 안됨
display(df.loc[0]['B'])