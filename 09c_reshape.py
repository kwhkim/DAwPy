# -*- coding: utf-8 -*-
# %% [markdown]
#
# ## 세로형/가로형 변환

# %%


# %% [raw] language="R"
# #install.packages('tidyr')`

# %% [raw] language="R"
# #데이터준비
# library(dplyr)
# library(tidyr)
# mtcars$name = rownames(mtcars); rownames(mtcars) = NULL
# mtcars %>% select(name, mpg, cyl, disp) -> mtcars01
# head(mtcars01, 4)


# %%
import numpy as np
import pandas as pd
#from pydataset import data
#mtcars = data('mtcars')
mtcars = pd.read_csv('dataset/pydataset/mtcars.csv', index_col=0)

# %%
mtcars.head()

# %%
mtcars01 = mtcars.copy()
#mtcars01.reset_index(drop=True)
#mtcars01.rename(columns = {'index':'name'}, inplace=True)
#mtcars01.rename({'index':'name'}, axis=1, inplace=True) # 위와 동일한 역할
#mtcars01.rename({'index':'name'}, axis='columns', inplace=True) # 위와 동일한 역할
mtcars01.head()

# %%
# inplace = True를 안 쓰면
mtcars01 = mtcars.copy()
mtcars01 = mtcars01.reset_index().rename(columns = {'index':'name'})
mtcars01.head()

# %%
columns = ["name","mpg","cyl","disp"] 
mtcars01= mtcars01[columns]
mtcars01.head()

# %%
# %% [markdown]
# ## 9.3.1 패키지 tidyr을 활용한 세로형/가로형 변환

# %% [raw] language="R"
# mtcars01 %>% gather(key='key', value='value', mpg, cyl, disp) -> mtcarsLong
# head(mtcarsLong, 4)


# %%
mtcarsLong = pd.melt(mtcars01, id_vars=["name"]) 
# "name"열을 제외한 모든 열을 variable, value 열로 표시하라
mtcarsLong.head()

# %% [raw] language="R"
# mtcarsLong %>% spread(key='key', value='value') -> mtcars02
# head(mtcars02,4)


# %%
mtcars02 = mtcarsLong.pivot(index="name", columns="variable", values="value")
mtcars02.head()

# %%
mtcars02 = mtcarsLong.pivot(index="name", columns="variable", values="value").reset_index()
mtcars02.head()

# %%
mtcars02.index.name, mtcars02.index

# %%
mtcars02.columns.name
# !!! ??? 근데 컬럼에 이름을 붙여줄 이유가 있을까?
# 여러 방식으로 컬럼을 설정할 수 있다면... level과 같은 의미...?
#
# mtcars02.columns는 immutable이므로 다른 변수에 저장될 수도 있어서?

# %%
x = mtcars02.columns

# %%
x

# %% [markdown]
# 위의 변수 `x`를 다시 데이터프레임 생성 시에 사용할 수도 있다.

# %% [raw] language="R"
# all.equal(mtcars01, mtcars02)


# %%
mtcars01.equals(mtcars02)

# %% [raw] language="R"
# all.equal(mtcars01 %>% arrange(name), 
#           mtcars02 %>% select(name, mpg, cyl, disp) %>% arrange(name))


# %%
mtcars01.head(), mtcars02[['name', 'mpg', 'cyl', 'disp']].head()

# %%
mtcars02.columns.name = None

# %%
mtcars01.sort_values('name').head(), mtcars02[['name', 'mpg', 'cyl', 'disp']].sort_values('name').head()

# %%
# # #mtcars01.sort_values?

# %%
#mtcars01 = mtcars01.sort_values('name')
#mtcars01.sort_values('name', inplace=True) # 인덱스가 바뀜
mtcars01.sort_values('name', inplace=True)
mtcars01.reset_index(drop=True, inplace=True)

# %%
mtcars02b = mtcars02[['name', 'mpg', 'cyl', 'disp']].sort_values('name').astype({'cyl':int})

# %%
mtcars02b.info()

# %%
mtcars01.info()

# %%
mtcars01.index

# %%
mtcars02b.index

# %%
mtcars02b.reset_index(drop=True, inplace=True)
mtcars01.equals(mtcars02b)

# %%
mtcars02b.reset_index(drop=True, inplace=True)
mtcars02b.index

# %%
mtcars01.info()

# %%
mtcars02b.info()

# %%
mtcars01.equals(mtcars02b)

# %% [markdown]
# ## 9.3.2 패키지 reshpae2의 활용

# %% [raw] language="R"
# #install.packages('reshape2')

# %% [raw] language="R"
# library(reshape2)
# mtcarsLong <- mtcars %>% select(am, name, mpg, cyl, disp) %>%
#   gather(-name, -am, 
#          mpg, cyl, disp, 
#          key='key', value='value', 
#          factor_key=TRUE) 
# head(mtcarsLong)

# %% [raw] language="R"
# mtcarsWide <- 
#   mtcarsLong %>% spread(key='key', value='value') 
# head(mtcarsWide)

# %%
mtcars01 = mtcars.copy()
mtcars01 = mtcars01[['am', 'mpg', 'cyl', 'disp']].\
    reset_index().rename(columns = {'index':'name'})

# %%
mtcars01.head()

# %%
#mtcars01.pivot(index=['name', 'am'], columns = ['mpg', 'cyl', 'disp'], values=['mpg', 'cyl', 'disp'])
mtcarsLong = \
    pd.melt(mtcars01, 
            id_vars=["name", "am"], 
            value_vars = ['mpg', 'cyl', 'disp'], 
            var_name='key', value_name='value')  # 기본값: var_name='variable', value_name='value'
mtcarsLong.head()

# %%
# origin
#  label type  value
#0     x    a      1
#1     x    b      2
#2     x    c      3
#3     y    a      4
# equivalent of R spread

# 1. origin.pivot(index='label', columns='type')['value']
# 2. origin.pivot_table(values='value', index='label', columns='type')
# 3. origin.groupby(['label', 'type'])['value'].aggregate('mean').unstack()

# %%
#mtcarsLong.pivot(index=['name', 'am'], columns = 'key')

# %%
mtcarsLong.set_index(['name', 'am']).head()

# %%
# mtcarsLong.pivot(index = ['name', 'am'], columns = 'key') # ERROR
# print(pd.__version__)  # 1.1.4에서도 에러
dat2 = mtcarsLong.set_index(['name', 'am']).pivot(columns='key')
dat2.head()

# %%
dat2.columns

# %%
dat2.index[:3], dat2.index.names

# %%
mtcarsLong.\
    pivot_table(values='value', index=['name', 'am'], columns = 'key').head()

# %%
mtcarsLong.groupby(['name', 'am', 'key'])['value'].mean().unstack(level=2).head()

# %%
mtcarsWide = mtcarsLong.groupby(['am', 'name','key'])['value'].mean().unstack(level=2).reset_index()

# %%
mtcarsWide.head()

# %% [raw] language="R"
# mtcarsLong2 <- mtcars %>% select(am, name, mpg, cyl, disp) %>%
#   melt(id=c("am", "name"),
#        measure.vars = c("mpg", "cyl", "disp"),
#        variable.name = "key", value.name = 'value')
# mtcarsWide2 <- 
#   mtcarsLong2 %>% dcast(am + name ~ key) -> mtcarsWide2
#
# head(mtcarsLong2)

# %%
mtcarsLong2 = \
    pd.melt(mtcarsWide, 
            id_vars=['am', 'name'], 
            value_vars=['mpg', 'cyl', 'disp'], 
            var_name='key', value_name='value')
mtcarsLong2.head()

# %%
mtcarsLong.head()

# %% [raw] language="R"
# all.equal(mtcarsLong, mtcarsLong2)
# all.equal(mtcarsWide, mtcarsWide2)


# %%

# %% [raw] language="R"
# dcast(mtcarsLong2, am ~ key, fun.aggregate=mean)


# %%
mtcarsLong.groupby(['am', 'key']).agg('mean').unstack(1)

# %%
x = "a
b"

# %%
x ="""a
b"""

# %% [raw]
# a
# b

# %% [raw]
# a\nb

# %%
x = "a\nb"

# %%
print(x)

# %%
x

# %%
mtcarsLong.pivot_table(index=['am'], columns=['key'], aggfunc='mean').fillna(0)

# %% [raw] language="R"
# dcast(mtcarsLong2, name + am ~ key, fun.aggregate=mean) %>% head(5)


# %%
mtcarsLong.groupby(['name', 'am', 'key']).agg('mean').unstack(2).head()

# %%
mtcarsLong.pivot_table(index=['name', 'am'], columns=['key'], aggfunc='mean').\
    fillna(0).head()

# %% [raw] language="R"
# dcast(mtcarsLong2, key ~ am, fun.aggregate=mean)


# %%
mtcarsLong.groupby(['am', 'key']).agg('mean')

# %%
mtcarsLong.pivot_table(index=['am'], columns=['key'], aggfunc='mean').\
    stack().head()

# %% [raw] language="R"
# dcast(mtcarsLong2, . ~ am + key, fun.aggregate=mean)

# %%
#mtcarsLong.groupby(['am', 'key']).agg('mean').unstack().unstack()의 결과가 pd.Series이기 때문에
pd.DataFrame(mtcarsLong.groupby(['am', 'key']).agg('mean').unstack().unstack()).T

# %%
pd.DataFrame(mtcarsLong.pivot_table(columns = ['key', 'am'], aggfunc='mean')).T

# %% [raw] language="R"
# dcast(mtcarsLong2, am + key ~ ., fun.aggregate=mean)

# %%
mtcarsLong.groupby(['am', 'key']).agg('mean')

# %%

# %%

# %%

# %%

# %%

# %%
