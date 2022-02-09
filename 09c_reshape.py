# -*- coding: utf-8 -*-
# %% [markdown]
# ## 가로형/세로형 변환

# %% [markdown]
# 가로형/세로형에 관한 이론은 [숨은원리 홈페이지의 글](http://ds.sumeun.org/?p=930)을 참조하자.

# %%
import numpy as np
import pandas as pd
from mypack.utils import pdDataFrame, c

# %%
NA = np.nan

# %%
datWide = pdDataFrame(name = c('ChangSik Park', 'EunJung Lee', 'HaeHee Song', 'HoJun Park', 'InHo Kim', 'JiSup Kim', 'Nari Yoo', 'YeoJin Lee'),
                  gender = list('MFFMMMFF'),
                  height_y2011 = c(74.69, NA, NA, NA, 88.24, 70.6, 64.78, 88.77),
                  height_y2012 = c(84.99, NA, NA, NA, 96.91, 83.78, 80.76, 96.45),
                  height_y2013 = c(91.73, NA, 75.74, NA, 101.85, 94.17, 87.3, 104.72),
                  height_y2014 = c(105.11, NA, 86.5, 71.89, 108.13, 100.03, 97.13, 112.84),
                  height_y2015 = c(111.04, 75.89, 91.5, 81.42, 112.45, 106.35, 103.8, NA))

# %%
datWide

# %% [markdown]
# 파이썬에 가로형을 세로형으로, 세로형을 가로형으로 변환할 때 쓸 수 있는 방법은 다음과 같다.

# %% [markdown]
# |   함수  |   세로형으로        | 가로형으로     |
# |:--------|:--------------------|:---------------|
# |         |                     | `dfL.pivot()`   |
# |         | `dfW.stack()`        | `dfL.unstack()` |
# |         | `dfW.melt()`         |                |
# |         | `pd.wide_to_long(dfW, )` |                |
#
#

# %% [markdown]
# ### 세로형으로

# %% [markdown]
# 주어진 가로형 `datWide`를 세로형으로 변환해보자. 가장 먼저 생각할 점은 변하지 않는 열을 지정하는 것이다. 고정된 열은 변환된 데이터 프레임에서 각 열의 `id`를 나타내게 된다.

# %% [markdown]
# |   세로형으로         | id 설정              |
# |:---------------------|:---------------------|
# |                      | `.pivot(index = )`   |
# | `dfW.stack()`        |  인덱스               | 
# | `dfW.melt()`         | `.melt(id_vars = )`  |
# | `pd.wide_to_long(dfW)` | `pd.wide_to_long(dfW, i = )`|

# %%
from mypack.utils import seq

# %% [markdown]
# `.stack()`의 경우 인덱스가 `id`열이 되므로 미리 `.set_index()`로 `id` 열을 인덱스로 바꿔 줘야 한다.

# %%
datW2 = datWide.set_index(['name', 'gender'])

# %%
datW2

# %%
datW2.stack() 

# %% [markdown]
# 만약 컬럼 인덱스가 멀티 인덱스가 아니라면 결과는 위와 같이 시리즈가 된다.

# %% [markdown]
# `.melt()` 메쏘드는 `id`가 열에 있어도 바로 세로형으로 변환할 수 있다. `id_vars=`만 지정해 주면 나머지 열은 모두 세로형으로 변환된다.

# %%
datLong = datWide.melt(id_vars=['name', 'gender']) 
datLong.head(2)

# %% [markdown]
# 위의 결과를 보면 `variable`의 `height_y2011`은 `value`가 2011년의 키(`height`)임을 나타낸다. 컬럼 이름을 좀 더 정확하게 정리하면 다음과 같이 될 것이다.

# %%
pdDataFrame(name = ('ChangSik Park','EunJung Lee'),
            gender = list('MF'),
            year = c(2011, 2011),
            height = c(74.69, NA))

# %% [markdown]
# 먼저 `datWide.melt(id_vars=['name', 'gender'])`의 결과와 위의 데이터프레임의 다른 점을 살펴보자. 우선 컬럼 이름이 바뀌었다. 그런데 컬럼 이름이 바뀌는 논리를 생각해보자.

# %% [markdown]
# 먼저 `variable` 열의 `height_`를 제거하고 `value`를 `height`로 바꾼다.

# %%
datLong.rename(columns = {'value':'height'})
datLong['variable'] = datLong['variable'].str.replace('height_', '')
datLong2 = datLong.rename(columns = {'value':'height'})
datLong2.head(2)

# %% [markdown]
# 이제 `variable` 열의 `y`를 제거하고 `variable` 대신 컬럼이름을 지정한다.

# %%
datLong2['variable'] = datLong2['variable'].str.replace('y', '').astype('int')
datLong3 = datLong2.rename(columns = {'variable':'year'})
datLong3.head(n=2)

# %% [markdown]
# 우리는 이렇게 원래 데이터프레임(`datWide`)의 컬럼 이름에서 컬럼 이름과 변환 방법을 모두 유추할 수 있었지만, 컬럼 이름이 항상 이렇게 편리하게 지정되어 있지는 않다는 점을 유의할 필요가 있다. 어쨋든 컬럼 이름을 지정하는 것까지는 `.melt()` 메쏘드에서 가능하다. `datWide.melt(id_vars=['name', 'gender'])`에 덧붙여 열 이름을 `var_name=`과 `variable_name=`으로 지정할 수 있다. 

# %%
datLong3 = datWide.melt(id_vars=['name', 'gender'], var_name = 'year', value_name = 'height')
datLong3.head(n=2)

# %% [markdown]
# 한 가지 남은 과정은 `year` 열의 값을 수정하는 것이다.

# %%
datLong3['year'] = datLong3['year'].str.replace('height_y', '').astype('int')
datLong3.head(n=2)

# %% [markdown]
# `datLong3`의 `year` 열에서 `height_y`를 제거하고 정수형으로 바꾸었다.

# %% [markdown]
# 위에서 `datWide`를 `datLong3`로 한 번에 바꿀 순 없을까? `.wide_to_long()` 메쏘드를 활용하면 된다.

# %%
datLong3 = pd.wide_to_long(datWide, "height", i=["name", "gender"], sep = '_y', j="year")
datLong3.head(n=2)

# %% [markdown]
# 이제 위의 `pd.wide_to_long()`을 자세히 살펴보자.

# %% [raw]
# pd.wide_to_long(datWide, stubnames = "height", i=["name", "gender"], sep = '_y', j="year")

# %%

# %% [markdown]
# 먼저 `datWide`는 세로형을 변환할 데이터 프레임이다. `id`열은 `i=`으로 지정한다. 이제 남은 것은 위의 `.melt()`에서 `var_name`과 `value_name`을 지정하는 것, 그리고 열이름을 적절히 수정하는 것이다.

# %% [markdown]
# 이때 `variable_name`은 원래 열이름에 포함되어 있어야 한다. `datLong`의 `height_y2011`, `height_y2012` 등의 열이름이 그 열이 서로 다른 연도에 측정한 키라는 것을 알려준다. 따라서 `variable_name`은 `height`가 되는 것이 타당하다. 이렇게 열이름의 가장 앞에 측정된 값이 나타난다면, `stubnames=`에 `height`를 써줌으로써 세로형에서 열이름이 `height`가 된다. 그리고 `sep=`은 `height_y2011`, `height_y2012` 등에서 `height`와 연도를 의미하는 `2011`, `2012`를 구분하는 문자열을 의미한다. 마지막 `j=`는 `.melt()` 메쏘드의 `var_name`에 해당하는 것으로, 가로형의 여러 열(`height_y2011`, `height_y2012`)이 어떤 변수를 기준으로 나눠진 것인지를 의미한다. 

# %% [markdown]
# 이렇게 `pd.wide_to_long(datWide, stubnames = , i=, sep=, j=)`의 각 매개변수를 적절하게 정해주면 위에서 여러 과정을 통해 얻었던 `datLong3`를 한번에 얻을 수 있다는 장점이 있다. 하지만 그 활용법이 쉬운 건 아니라서 독자가 편한 방법을 사용하면 될 것이다.

# %% [markdown]
# 세로형의 가장 기본적인 골격은 `id`, `variable`(조건변수), `value`(측정된 변수)라는 점을 이해한다면, `pd.wide_to_long()`의 매개변수를 이해하는 데 도움이 될 것이다. `i=`는 `id`를 나타내고, `stubnames=`는 측정된 값, `j=`는 조건을 나타내는 변수이다. `pdWide`에서 `id`는 `name`과 `gender`이고, **열이름의 첫 부분에 포함된** 측정된 변수(`stubnames=`)은 `height`이고, `j=`는 각 열의 조건 변수 `year`이고, `datLong`의 열이름에서 측정된 변수를 나타내는 부분과 조건을 나타내는 부분을 구분하는 문자열을 `sep=`으로 지정한다. 

# %% [markdown]
# ### 가로형으로

# %% [markdown]
# |   함수  | 가로형으로     | id 설정       |
# |:--------|:---------------|-------------|
# |         |  `dfL.pivot()`   | `.pivot(index=)`   |
# |         |  `dfL.unstack()` | 인덱스             |
#

# %% [markdown]
# `.unstack()` 메쏘드는 `.stack()` 메소드의 역함수라고 생각할 수 있다.

# %%
datLong3.unstack()

# %% [raw]
# 위의 결과에서 `year`는 datWide2의 0-번째 수준 열(`2011`, `2012`, ...)의 이름이다. 1-번째 수준의 열은 모두 `name`, `gender`,`height`이다.

# %%
datWide2.columns

# %% [markdown]
# `id`가 인덱스가 아니라 열에 존재한다면 `.pivot()`을 사용하고 `id`열을 `index=`로 지정한다.

# %%
datLong4 = datLong3.reset_index()
datLong4.head(2)

# %%
datLong4.pivot(index=['name', 'gender'], columns = 'year', values='height')

# %% [markdown]
# `.pivot()`을 사용하는 방법은 세로형의 기본 골격을 안다면 쉽게 이해할 수 있다. 세로형의 기본 골격은 id, 조건, 측정된 값이다. 이를 `.pivot(index=, columns= values=)`에 `id`는 `index=`로, 조건 변수는 `columns=`로 측정된 값은 `values=`로 입력하면 된다.

# %% [markdown]
# 측정된 값이 여럿이 있어도 상관없다. 

# %%
datB = pdDataFrame(name = c('ChangSik Park', 'ChangSik Park', 'EunJung Lee', 'EunJung Lee'),
                   gender = list('MMFF'),
                   year = c(2014, 2015, 2014, 2015),
                   height = c(105.11, 111.04, NA, 75.89),
                   weight = c(18, 19, NA, 9))
datB


# %% [markdown]
# 위의 데이터를 보면 앞선 세로형과 비슷하지만 측정된 변수가 `height`와 `weight`로 둘이다. 이런 경우에도 `.pivot()`을 같은 방식으로 활용하여 가로형으로 변환할 수 있다.

# %%
datBWide = datB.pivot(index = ['name', 'gender'], columns = 'year', values=['height', 'weight'])
datBWide

# %% [markdown]
# ### 세로형으로 2: 여러 측정 변수
#
#

# %% [markdown]
# 위의 결과 `datBWide`는 측정된 변수가 둘이다. 앞에서 배웠던 세로형으로 변환하는 함수, 메소드로 `datBWide`를 세로형으로 변환해보자.

# %% [markdown]
# #### `id`가 인덱스에 있는 경우

# %% [markdown]
# `datBWide`는 `id`가 인덱스로 존재한다.

# %%
datBWide

# %% [markdown]
# 그리고 열이름에 수준이 존재한다. 그래서 어떤 열을 세로형으로 만들 것인지 선택할 수 있다. 기본은 가장 하위 수준이다.

# %%
datBWide.stack() # datBWide.stack(-1)

# %%
datBWide.stack(0) # 0-번째 수준

# %%
datBWide.stack([0,1]) # 0-번째, 1-번째 수준을 세로형으로

# %% [markdown]
# #### `id`가 열에 있는 경우

# %%
datBWide2 = datBWide.reset_index()
datBWide2

# %% [markdown]
# * 문제 : `datBWide2`의 `id`는 열에 존재한다. 이를 `.melt()` 또는 `pd.wide_to_long()`을 활용하여 세로형으로 바꿔보자. 참고로 각 메소드, 함수는 다음과 같은 매개변수가 있다.

# %% [raw]
# df.melt(id_vars=)
# pd.wide_to_long(df, subnames= , i=, j=, sep=)

# %%
datBLong1 = datBWide2.melt(id_vars=['name', 'gender'])
datBLong1

# %% [markdown]
# ### 열이름에 측정변수와 조건이 함께 있는 경우

# %% [markdown]
# multi-index 열이름은 다음과 같이 하나의 수준으로 만들 수 있다.

# %%
datBWide3 = datBWide2.copy()
datBWide3.columns = [str(x) + str(y) for x, y in datBWide2.columns]
datBWide3

# %%
datBLong2 = pd.wide_to_long(datBWide3, i=['name', 'gender'], j = 'year', stubnames=['height', 'weight'])
datBLong2

# %% [markdown]
# 위의 경우은 `sep=`를 설정할 필요가 없었다.

# %% [markdown]
# ### 가로형으로 2: 여러 측정 변수

# %% [markdown]
# 이제 측정 변수가 여럿일 때 가로형을 바꾸는 연습을 해보자. 위에서 얻은 세로형 `datBLong1`과 `datBLong2`를 비교해고, 둘 다 가로형을 변환해보자. 가로형으로 변환하는 방법은 `.pivot(index=)`와 `.unstack()`을 쓸 수 있었다.

# %%
datBLong1

# %%
datBLong2

# %% [markdown]
# #### 정답

# %%
datBLong2.unstack()

# %%
datBLong1.pivot(index=['name','gender'], columns = [None, 'year'], values='value')

# %% [markdown]
# None의 역할이 궁금하다면 `datBLong1.columns`을 확인해보자.

# %%
datBLong1.columns

# %% [markdown]
# 열이름을 모두 의미있는 문자열로 바꾸자.

# %%
datBLong1.columns = ['name', 'gender', 'variable', 'year', 'value']

# %% [markdown]
# 그리고 다시 `.pivot()`으로 가로형으로 변환하면 다음과 같다.

# %%
datBLong1.pivot(index=['name','gender'], columns = ['variable', 'year'], values='value')

# %% [markdown]
# ???위의 FutureWarning 의미???

# %% [markdown]
# ## === END OF DOCUMENT

# %%

# %%

# %%

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
