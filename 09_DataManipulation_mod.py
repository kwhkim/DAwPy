# -*- coding: utf-8 -*-
# %% [markdown]
# 문제는 어떤 작업을 하려는 것이며,
# 그 작업이 어떤 데이터 구조에 적합하게 하기 위해
# 어떤 함수를 쓰게 된다는 것?


# %%
# https://towardsdatascience.com/avoiding-apply-ing-yourself-in-pandas-a6ade4569b7f

import pandas as pd
import numpy as np

df_len = 1000

test_df = pd.DataFrame(
    {
        "cat_column": np.random.choice(["a", "b", "c"], size=df_len),
        "float_col1": np.random.random(size=df_len),
        "float_col2": np.random.random(size=df_len),
    }
)

# %%
test_df


# %%
def trig_transform(x):
    return np.log(np.cos(x) + 5)


# %%
test_df['float_col1'].apply(trig_transform) 
# series에 apply를 하면, element-wise하게 function을 적용하고,
# 실패하면 pd.Series를 넘긴다?

# %%
trig_transform(test_df['float_col1']) 
# 그러게.. column을 바로 집어 넣으면 되는데, 왜 .apply()?

# %%
## Apply a function to each row of a data frame
# https://towardsdatascience.com/apply-function-to-pandas-dataframe-rows-76df74165ee4

## Apply, applymap, map for DF and Series
# https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas


# df.query

# %%
import numpy as np
import pandas as pd

# %%
df = pd.DataFrame(np.random.randn(30, 3), columns=['a','b','c'])
df_filtered = df.query('a > 0').query('0 < b < 2')

# %%
df['place.like'] = df.b


# %%
df

# %%
df.query('`place.like` < 0')
# %%
#


# %%
df = pd.DataFrame({'a':[1,3,2,3,3,2,1], 
                   'b':'abcbbca', 
                   'c':np.random.normal(0,1,7),
                   'd':np.random.normal(3,1,7)}, 
                  index = [1,3,2,2,3,2,3])

# %%
df

# %%
type(df.groupby('a'))

# %%
type(df.a.groupby(level=0))

# %%
df[['c', 'd']].apply(np.mean)

# %%
df[['c', 'd']].apply([np.mean, np.sum]) # 두 함수를 각각 적용

# %%
df[['c', 'd']].apply(lambda x: x+1)

# %%
df2 = df[['c', 'd']].apply([lambda x: x+1, lambda x: x-1])
df2
# 왜 위의 .apply([np.mean, np.sum])과 다른가?

# %%
df2[[('c', '<lambda>')]]

# %%
func1 = lambda x: x+1
func2 = lambda x: x-1

# %%
func1.__name__, func2.__name__

# %%
df[['c', 'd']].apply([func1, func2]) 
# 여기서 function은 transform의 역할을 하기 때문에 
# 행으로 옮기면 multiindex로 표기해야 함

# %%
func1.__name__ = 'func1'
func2.__name__ = 'func2'

# %%
df[['c', 'd']].apply([func1, func2])

# %%

# %%
Y1 = df[['c', 'd']].apply(lambda x: np.quantile(x, [0.5, 0.9]))
Y1, type(Y1)

# %%
Y2 = df[['c', 'd']].apply(lambda x: [np.quantile(x,0.5), np.quantile(x,0.9)])
Y2, type(Y2)

# %%
df

# %%
Y3 = df[['c', 'd']].apply([lambda x: [np.quantile(x,0.5), np.quantile(x,0.9)],
                           lambda x: [np.quantile(x,0.1), np.quantile(x,0.2)]])
Y3, type(Y3)
# ??? 위의 Y2와 굉장히 다름. 이유는?

# %%
Y4 = df[['c', 'd']].apply([lambda x: np.quantile(x,[0.5, 0.9]),
                           lambda x: np.quantile(x,[0.1, 0.2])])
Y4, type(Y4)

# %%
df[['c', 'd']].transform(lambda x: x+1)

# %%
df.c.apply(np.mean)

# %%
df.d.apply(np.sum)

# %%
df.c.agg(np.mean)

# %%
df.d.agg(np.sum)


# %%
## groupby 류 속도 비교
x="""Animal   FeedType   Amount(kg)
Animal1     A         10
Animal2     B         7
Animal3     A         4
Animal2     A         2
Animal1     B         5
Animal2     B         6
Animal3     A         2
"""
with open('datAnimal.csv', 'w+') as f:
    f.write(x)
# -

# %%
dat = pd.read_csv('datAnimal.csv', delimiter='\s+')
# delimiter에 re를 쓸 수 있다!!!???

# %%
# ?pd.read_csv

# %%
dat

# %% [markdown]
# https://stackoverflow.com/questions/20905713/equivalent-of-rs-tapply-in-python-pandas


# %%
import timeit
start_time1 = timeit.default_timer()
x1 = dat.groupby(['Animal','FeedType'])['Amount(kg)'].sum()
elapsed_groupby = timeit.default_timer() - start_time1

# %%
# #?dat.pivot_table

# %%
start_time2 = timeit.default_timer()
x2 = dat.pivot_table(index='Animal', columns='FeedType',values='Amount(kg)',aggfunc=sum)
elapsed_pivot = timeit.default_timer() - start_time2

# %%
start_time3 = timeit.default_timer()
x3 = dat.pivot_table(index=['Animal', 'FeedType'], values='Amount(kg)',aggfunc='sum')
elapsed_pivot2 = timeit.default_timer() - start_time2

# %%
print ('elapsed_groupby: ' + str(elapsed_groupby))
print ('elapsed_pivot: ' + str(elapsed_pivot))
print ('elapsed_pivot2: ' + str(elapsed_pivot2))

# %%
print(x1)
print(x2)
print(x3)

# %%
