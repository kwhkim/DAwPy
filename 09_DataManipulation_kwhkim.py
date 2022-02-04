# -*- coding: utf-8 -*-
# %% [markdown]
# # 데이터 가공
#
# * 집단별로 함수 적용하기
# * 두 개 이상의 데이터프레임 합치기
# * 가로형/세로형 변환하기

# %% [markdown]
# 자료가 분석에 가장 적합한 상태로 제공되는 경우는 거의 없다.[^crowdflower] 이 장에서는 주어진 데이터를 가공하는 방법을 살펴본다. 구체적으로 다음의 세 작업에 대해 알아본다.
#
# 1. **주어진 데이터에서 집단별 요약치를 구하거나 집단별로 함수를 적용하기** : 예를 들어 학년별 평균 체중을 구하거나, 학급별 평균 체중을 구하는 경우를 생각해보자. 또는 우리나라 광역도시별로 개인의 소득분위수를 구하고 싶다면 어떻게 해야 하는가? 데이터를 특정한 변수를 기준으로 분리한 후 요약통계치를 구하거나(`.aggregate()`), 어떤 변환 작업(`.transform()`)을 한 후, 결과를 모아 합치는 작업을 파이썬에서 어떻게 할 수 있을까?
#
# 2. **분리된 데이터를 합치기** : 자료는 여기저기 흩어져 있는 경우가 많다. GDP 자료는
# 통계청에서, 무역자료는 관세청에서 구했다. 이 둘을 적절하게 합쳐서 새로운 자료를 만들거나, 분석을 해야 경제와 무역에 관한 새로운 통찰을 얻을 수 있을 것이다. 어쨋든 우선 두 자료를 하나로 합쳐야 한다.
#
# 3. **가로형 데이터를 변환하여 세로형으로 만들거나 반대 방향으로 변환하기** : 가로형은
# 가로로 긴 형태의 자료이고, 세로형은 세로로 긴 형태의 자료이다. 영어로는 Wide-form, Long-form이라고 칭한다. 기본적으로 가로형은 한 행에 여러 관측값이 나열되어 있고, 세로형은 한 행에 하나의 관측값이 적혀 있다. 시각화, 자료 제출, 분석 등 목적과 요구에 따라 자료를 두 가지 형태로 변환할 수 있어야 한다.
#
# [^crowdflower]: CrowdFlower의 설문 조사 결과에 따르면 데이터 분석가는 업무 시간의 무려 80%(!) 를 데이터 수집과
# 전처리에 사용한다고 한다.

# %% [markdown]
#
# ## 집단별로 함수 적용하기
#
# 5장에서 판다스 데이터 프레임을 사용하여 데이터를 가공하는 기본적인 방법에 대해 알아보았다. 여기에서는 이를 좀더 확장하고, 데이터프레임이 아닌 경우에도 집단별로 함수를 적용하는 방법에 대해 알아본다. 
#
# 여기에서 소개하는 함수 또는 메쏘드는 기본적으로 `for` 문을 추상화하여 하나의 함수(또는 메쏘드)로 구현한다고 생각할 수 있다.

# %%
# #!pip install rpy2 

# %%
import rpy2.rinterface

# %%
# %load_ext rpy2.ipython

# %%

# %% language="R"
# v <- c(172, 172, 170, 170, rnorm(96, 170, 3))
# g <- rep(c("Male", "Female"), 50)
# c(mean(v[g=="Male"]), mean(v[g=="Female"]))


# %% [markdown]
# pandas.Series class는 R의 벡터 대용으로 쓸 수 있다. 
# pandas.Series는 리스트의 원소로 pandas.Series를 생성한다. 
# pandas.Series는 R의 벡터처럼 vectorized 연산이 가능하다.

# %%
import numpy as np
import pandas as pd

a = pd.Series([1,3,2])
b = pd.Series([-1,-3,-5])
a+b

# %% [markdown]
# 판다스 시리즈에서 `+`는 각 원소를 더하고, 리스트에서 `+`는 두 리스트를 연결한다. 혼동하지 않도록 주의할 필요가 있다.

# %%
[1,3,2]+[-1,-3,-5]

# %% [markdown]
# 집단별로 평균을 구하는 방법은 다음과 같이 R의 방법을 흉내낼 수 있다.
# `v[g=="Male"]`은 v의 원소 중에서 `g`의 원소가 `Male`인 원소에 대응하는 원소를 선별한다.
# 따라서 `v[g=="Male"].mean()`은 `v`의 원소를 `g`의 원소에 대응해서,
# `g`의 원소가 `Male`인 경우의 평균을 구한다.

# %%
import numpy as np
import pandas as pd

# %%
v = pd.Series([172, 172, 170, 170] + np.random.normal(170, 3, 96).tolist())
g = pd.Series(['Male', 'Female']*50)
v[g=="Male"].mean(), v[g=="Female"].mean()


# %%
v.groupby(g).mean()

# %%
type(v[g=='Male'])

# %%
v[g=='Male']

# %%

# %%
v.agg(np.mean)

# %%
v.agg('mean') # v.mean()을 하게 됨. getattr(v, func, None)

# %%
type(v)

# %%
# ? v.agg

# %%
v = pd.Series([172, 172, 170.0, 170., 168.])

# %%
dat = pd.DataFrame({'v1':v, 'v2':v, 'g':['a', 'b', 'b', 'a', 'a']})

# %%
dat.groupby('g').agg(np.mean)

# %%
dat.groupby('g').agg(lambda x: np.mean(x))

# %%
dat.agg(np.mean, axis=0)

# %%
dat.groupby(g).agg("mean")

# %%
dat.agg(lambda x: np.mean(x), axis=1)

# %%
dat.apply(lambda x: np.mean(x), axis=0)

# %%
dat.apply(lambda x: np.mean(x), axis=1)

# %%

# %%
v.agg("mean")

# %%
np.mean(v)

# %%
v2 =np.asarray(v) # view if possible!

# %%
v2[0] = 100

# %%
v, v2

# %%
# ?np.asarray

# %%
type(v), v.dtype

# %%
v._get_axis_number(axis=0)

# %%
v.apply(lambda x: np.mean(x))

# %%
v.agg(lambda x: np.mean(x))

# %%
# apply가 작동하지 않도록 해야 함.
v.agg(lambda x: np.mean(x[:]))

# %%
# ?cast
# cast(typ, val) # cast a value to a type

# %%
from typing import cast

# %%
cast(int, 32.4)

# %%
res = cast(str, lambda x: np.mean(x))
res, type(res)

# %%

# %%
# ?cast

# %%
v.agg(lambda x: [print(x), np.mean(x)], axis=0)

# %%

# %%
v.agg(lambda x: [print(x), np.mean(x.values)])

# %%
v.agg(lambda x: np.mean(x))

# %% [markdown]
# `v.agg(lambda x: np.mean(x))`와 `v.agg(np.mean)`의 결과가 다른 이유는?

# %%

# %%

# %%

# %%

# %%
np.mean(v)

# %%
(lambda x: np.mean(x))(v)

# %%
np.mean(v, axis=0)

# %%
np.mean(v, axis=None)

# %%
`v.agg(labmda x: np.mean(x))`

# %%
# ?np.mean

# %%
v.agg(np.mean), v.agg("mean")

# %%
# !!!
v.agg(lambda x: np.mean(x.values)), v.agg(lambda x: x.mean())

# %%
np.mean(v), np.mean(v.values)

# %%

# %%
v.agg("mean"), v.agg(np.mean)

# %%
v.agg(func=lambda x: np.mean(x))

# %%
getattr(v, "mean")()

# %%
v.agg(lambda x: np.mean(x))

# %%
v.agg([lambda x: np.mean(x), lambda x: np.median(x)])

# %%
v = pd.Series(['a', 'b'], dtype=str)

# %%

# %%
v.agg(str), v.apply(str)

# %%
v[:5].apply(np.mean) # !!! vectorised function
# !!! function을 무엇에 적용할 것인가? 

v[:5].mean()

v[:5].agg(np.mean)

# %%

# %%
v[:5].apply(np.mean)

# %%
v.groupby(by = [0]*len(v)).agg(np.mean)

# %%
v.groupby(by = [0]*len(v)).agg(lambda x: np.mean(x))

# %%
pd.DataFrame(v).agg(np.mean)

# %%
pd.DataFrame(v).agg(lambda x: np.mean(x))

# %%

# %%
v[:5].apply(lambda x: np.mean(x))

# %%
(lambda x: np.mean(x))(v[:5])

# %%
isinstance(np.mean, np.ufunc)
# np.ufunc의 의미?
# !!! https://numpy.org/doc/stable/reference/ufuncs.html
# universal functions are instances of the numpy.ufunc class.
#   frompyfunc factory function
# universal functions are for element-wise operations? 
# 

# %%
isinstance((lambda x: np.mean(x)), np.ufunc)
isinstance(np.add, np.ufunc)
# True!!!

## what are groupby functions available?
## pipe, all, any, bfill, backfill, count, cumcount, cummax, 
## cummin, cumprod, cumsum, ffill, first, head, last, 
## max, mean, median, min, ngroup, nth, ohlc, pad, prod, 
## rank, pct_change, size, sem, std, sum, var, tail

## summary(agg)
##   max, mean, median, min, nth, size, sem, std, sum, var, count

# %%
v.groupby(g).max(), v.groupby(g).mean(), v.groupby(g).median(), v.groupby(g).min()

# %%
v, g

# %%
v.groupby(g).nth(n=2), v.groupby(g).size(), v.groupby(g).sem(), v.groupby(g).std()

# %%
v[:5].agg(lambda x: np.mean(x))

# %%
v[:5].agg(lambda x: np.mean(x.tolist())) 
# !!!
# https://stackoverflow.com/questions/14246817/python-pandas-custom-agg-function

# %%
np.mean(v[:5])

# %%
df = pd.DataFrame({'one':[1,1,2,2,3], 'two':list('xyyzz'), 'three':list('eecba')}, 
                  index=list('abcde'), columns=['one','two','three'])

# %%
df.groupby('one').agg(lambda x: "|".join(x.sort_values().unique().tolist()))


# %%

# %%
v[:5]

# %%
type(v[:5])

# %%
type(v[g=="Male"])

# %%
v[g=='Male'].agg(np.mean)


# %%
def f(x):
    return np.mean(x)
v[g=='Male'].agg(f) # !!! 애매하네? 왜???
v[g=='Male'].agg('sum')
v[g=='Male'].mean() # 정답
v[g=='Male'].agg('mean')

# %%
from functools import reduce 
v[g=='Male'].agg(lambda series: reduce(lambda x,y: x+y, series))

# %%
from functools import reduce
  
# define a Custom aggregation 
# function for finding total
def reduce_add(series):
      return reduce(lambda x, y: x + y, series)


# %%
v[g=='Male'].agg(lambda x: sum(x), axis=0)


# %%
def reduce_all(series, func):
    return reduce(lambda x, y: func(x,y), series)


# %%
v[g=='Male'].agg(reduce_add)

# reduce_all의 강점
v2 = pd.Series(np.random.choice(['a', 'b', 'c'], 100))
#v2[g=='Male'].agg(reduce_all, np.sum)
# ??? 어떻게 구현?
# !!! character을 모두 더하려면?
v2.str.cat() # concat

# %%
v[g=='Male'].agg(lambda x: np.sum(x), axis=0) # ???

# %%
v[g=='Male'].agg(lambda x: np.mean(x), axis=0)  
# 내가 custom function을 쓰는 것을 뭔가 잘못 생각하고 있나???

# %%
pd.DataFrame(v[g=='Male']).agg(lambda x: np.mean(x)) 
# 그냥 pd.DataFrame을 쓰라고해???

# %%
v[g=='Male'].groupby([1]*len(v[g=='Male'])).agg('mean')

# %%
v.groupby(g).agg('mean')

# %%
v[g=='Male'].groupby(level=0).agg('mean')

# %%
v[g=='Male'].agg('mean')

# %%
v[g=='Male'].agg(np.mean)

# %%
v[g=='Male'].agg(lambda x: np.mean(x)) 
# !!! 참고 사항으로 남겨야!
# ???? # aggregate도 Series -> scalar가 아니어도 된다?

# %%
v[g=='Male'].agg(lambda x: print(type(x), x)) 
# 왜 입력이 이렇게 나오지?
# 여기서는 ???
pd.DataFrame(v[g=='Male']).agg(lambda x: print(type(x), x))
#>>> pd.DataFrame(v[g=='Male'])
#       0
#0  172.0
#2  170.0
#4  168.0

# !!! .agg()이 작동하는 방식이 pd.Series와 pd.DataFrame에서 다르다!!!

# %%
pd.DataFrame({'a':[1,2,3], 'b':[10,11,12]}).agg(lambda x: print(x)) 
# 여기는 입력이 series인 듯...
# 그래서 최초는 series로 해보고, 그 다음 element로????
pd.DataFrame({'a':[1,2,3], 'b':[10,11,12]}).agg(lambda x: print(type(x), x)) 


# %%
pd.DataFrame(v[g=='Male']).apply(lambda x: np.mean(x))  

# %%
pd.DataFrame(v[g=='Male']).agg(lambda x: np.mean(x)) # apply or agg

# %% [markdown]
# 앞의 경우와 결과가 다른 것은 `np.random.normal()`을 사용하여 무작위 값을 생성했기 때문이다.
# 만약 python의 값을 R에 그대로 옮기려면 다음과 같이 쓸 수 있다. 
#
# python의 변수 `v`를 R에서 사용하고자 한다. 
# `-i`는 **i**nput의 의미이다. 

# %% magic_args="-i v" language="R"
# g <- rep(c("Male", "Female"), 50)
#
# c(mean(v[g=="Male"]), mean(v[g=="Female"]))

# %% [markdown]
# 결과가 동일함을 알 수 있다. 

# %% magic_args="-i v" language="R"
# print(v[1:10])
# print(class(v))
# print(dim(v))

# %% [markdown]
# 참고로 python의 pandas.Series `v`는 R의 벡터(1차원 배열)로 바뀌었다. 
# pandas.Series의 index는 벡터 각 원소의 이름(names)가 된다.
# 1차원 np.array의 경우도 벡터가 되지만, 이 경우에는 이름이 없다.

# %%
v1 = pd.Series([1,5,3])
v2 = np.array([1,3,2])

# %% magic_args="-i v1,v2" language="R"
# print('v1')
# print(v1)
# print('v2')
# print(v2)

# %% [markdown]
# 만약 R의 변수를 python에서 사용하려면 `-o`(**o**uput)을 사용한다.

# %% magic_args="-o py_v -o py_g" language="R"
# set.seed(0)
# py_v <- rnorm(1000, 170, 3) # size크기,loc정규분포 평균, scale표준편차
# py_g <- rep(1:100, 10)
# c(mean(py_v[py_g==1]), mean(py_v[py_g==2]), mean(py_v[py_g==3]), mean(py_v[py_g==4]))

# %%
np.tile(np.arange(100), 10)

# %%
np.repeat(np.arange(100).reshape(1,100), 10, axis=0).reshape(100*10)

# %%
import numpy as np
import pandas as pd


# %%
def rep(x, n_rep, each=1):
    return np.tile(np.repeat(x, each), n_rep)
    
def rep(x, times = 1, length_out = None, each = 1):
    if length_out is None:
        return np.tile(np.repeat(x, each), times)
    elif times != 1:
        if length_out <= len(x)*times:
            return np.tile(x, times)[:length_out]
        else:
            each = length_out / (len(x)*times)
            return np.repeat(np.tile(x,times), each)[:length_out]
    elif each != 1:
        if length_out <= len(x)*each:
            return np.repeat(x, each)[:length_out]
        else:
            times = length_out / (len(x)*each)
            return np.repeat(np.tile(x,times), each)[:length_out]
## !!! doc_string을 포함하여 help()가 가능하도록
## -> Ax_rutils.py
## R의 rep와 비교해봐야 할 듯...


# %%
rep(np.arange(10), 10, 50)

# %%
rep(np.arange(100),10)

# %%
from Ax_rutils import seq, c

# %%
py_v = np.random.normal(170, 3, 1000)
py_g = rep(seq(1,100),10)

# %%
np.random.seed(0)
#v = np.random.normal(170, 3, 1000) #loc정규분포 평균, scale표준편차, size크기
#g = np.array(list(range(1,100+1,1))*10)
(py_v[py_g==1].mean(), py_v[py_g==2].mean(), py_v[py_g==3].mean(), py_v[py_g==4].mean())

# %% [markdown]
# ### 참고
#
# R에는 1차원 벡터를 만들기 위해 손쉽게 사용할 수 있는 `c()` 함수(concatenate)가 있다. 아래에는 python의 `c()`함수를 새로 정의하여 손쉽게 

# %%
import pandas as pd


# %%
# 그래서 c 결과를 pd.Series로 할 것인가? 아니면 np.ndarray로 할 것인가???
def c(*args, axis=0):
    return pd.concat([pd.Series(x) for x in args], axis=axis).reset_index(drop=True) 
    # drop=True ->  인덱스를 컬럼으로 보존하지 않는다
c(pd.Series([1,3,2]), pd.Series([1,4,4,5]))


# %%
c(c(1,2,3),c(1,2),3)

# %% language="R"
# c(c(1,2,3),c(1,2),3)

# %% [markdown]
# R의 `c()`함수는 각 원소의 이름을 정해줄 수도 있다. 이 기능은 위에서 정의한 python `c()`함수가 구현하지 않는다.

# %% language="R"
# c(a=1, b=3, a=2)
# c(a=1, b=c(1,3,2))

# %% [markdown]
# ## 9.1.1 주어진 벡터에 집단을 구분하여 함수 적용하기

# %% language="R"
# v = c(2, 2, 6, 8, 9, 1, 2, 7, 5) 
# g = c(1, 3, 1, 2, 3, 2, 2, 1, 2) 
# tapply(v, g, FUN = mean) 


# %% [markdown]
# python에는 `tapply()`에 1:1 대응하는 함수는 존재하지 않는 듯 하다.
# 먼저 pandas.DataFrame을 만든 후 `.groupby()`, `.mean()` 메쏘드를 사용한다.

# %%
v = pd.Series([2, 2, 6, 8, 9, 1, 2, 7, 5])
g = pd.Series([1, 3, 1, 2, 3, 2, 2, 1, 2])
pd.DataFrame({'v':v, 'g':g}).groupby('g').mean()

# %%
pd.DataFrame({'v':v, 'g':g}).groupby('g').agg(np.mean)

# %%
pd.DataFrame({'v':v, 'g':g}).groupby('g').agg(lambda x: np.mean(x))

# %%
df = pd.DataFrame({'v':[2, 2, 6, 8, 9, 1, 2, 7, 5],
                   'g':[1, 3, 1, 2, 3, 2, 2, 1, 2]}).set_index('g')

# %%
# index를 기준으로 groupby
df.groupby(level=0).mean()
df.groupby(df.index).mean() # 아래 방법이 낫지 않을까? timeit???

# %%

# %% [markdown]
# ## 9.1.2 집단별로 함수 적용하기

# %% [markdown]
# ### 빈도표

# %% magic_args="-o dat" language="R"
# dat <- data.frame(gender=c('M','M','M','M','M','F','F','F','F','F'),
#                   num=c(1,2,3,1,2,3,1,2,3,1),
#                   h=c(170,180,190,180,170,150,160,170,160,150),
#                   w=c(80,70,100,80,60,50,50,60,60,50))
# dat$BMI <- dat$w/(dat$h/100)^2
# head(dat)


# %%
## 8장에서 정의한,
## 그리고 아래에도 있는

import numpy as np
import pandas as pd

def pdDataFrame(**kwargs):
    ar_opt = {}
    ar_data = {}    
    for k in kwargs:
        #print(k)
        if k.startswith('_'):
            ar_opt[k[1:]] = kwargs[k]
        else:
            ar_data[k] = kwargs[k]
    
    #print(ar_opt)
    #print(ar_data)
    
    return pd.DataFrame(ar_data, **ar_opt)

def c(*args):
    return pd.Series(args)


# %%
dat = pdDataFrame(gender=c('M','M','M','M','M','F','F','F','F','F'),
                  num=c(1,2,3,1,2,3,1,2,3,1),
                  h=c(170,180,190,180,170,150,160,170,160,150),
                  w=c(80,70,100,80,60,50,50,60,60,50))

# %%
dat.head()

# %% language="R"
# print(table(dat$gender))
# print(table(dat$gender, dat$num))
# print(table(dat$gender, dat$num, dat$h>170))

# %% [markdown]
# R에서 `table()`은 각 조건에 해당하는 데이터 포인트의 수를 파악하는데 요긴하게 사용된다.
# Python에서 동일한 기능을 하려면 결과 테이블의 차원에 따라 다른 방법을 사용해야 하는 듯 보인다.
#
# * 1차원 : `.value_counts()`
# * 2+차원 : `pd.crosstab(index = , columns = )`, `.groupby().size().unstack()`

# %% [markdown]
# ### 1차원 빈도표 : `pandas.Series.value_counts()`

# %%
dat['gender'].value_counts() # value_counts
# dat.value_counts()가 아님을 유의하자!

# or you can do 
def table(self):
    #print(self.name)
    #print(f'* you can also use \n{self.name}.value_counts()\n or \nDF[\'{self.name}\'].value_counts()')
    print('* TRY .value_counts() NEXT TIME')
    return self.value_counts()

pd.Series.table = table

dat['gender'].table()

# %%

# %%
dat =  pdDataFrame(gender=c('M','M','M','M','M','F','F','F','F','F'),
                   num=c(1,2,3,1,2,3,1,2,3,1),
                   h=c(170,180,190,180,170,150,160,170,160,150),
                   w=c(80,70,100,80,60,50,50,60,60,50))
dat['BMI'] = dat.w/(dat.h/100)**2
dat.head()

# %% [markdown]
# ### 2+차원 빈도표
# * `pandas.crosstab(index = , columns = )`
# * `pandas.DataFrame.groupby().size().unstack()`

# %%
#dat[['gender', 'num']].value_counts(['gender', 'num']) # 오류
pd.crosstab(index = dat.gender, columns = dat.num)
# 다차원 cross table도 가능!!!
pd.crosstab(index = [dat.gender, dat.num], columns = dat.num)

# %%
pd.crosstab(index = [dat.gender, dat.num], columns = dat.h)

# %%
pd.crosstab(index = [dat.gender, dat.num], columns = [dat.h, dat.w])

# %%
dat.groupby('gender').size()

# %%
dat.groupby(['gender', 'num']).size()
# groupby().size()의 문제... NaN이 존재할 때
# 만약 M(gender)-3(num)이 존재하지 않는다면 생략된다?

# %% [markdown]
# 만약 `.groupby().size()`를 사용해서 R의 `table()`처럼 2차원의 표를 원한다면, 
# `.unstack()`을 사용할 수 있다.

# %%
dat.groupby(['gender', 'num']).size().unstack('num')

# %%
dat['h_if'] = dat['h'] > 170
dat.groupby(['h_if', 'gender', 'num']).size().unstack(['gender'])

# %%
dat.groupby(['h_if', 'gender', 'num']).size()

# %%
dat.groupby(['h_if', 'gender', 'num']).size().unstack().unstack().stack(dropna=False).stack(dropna=False)

# %% [markdown]
# 다음의 R의 스타일과 동일하게 출력되도록 한 결과이다.

# %%
for dfgrouped in dat.groupby(['h_if','gender', 'num']).size().unstack('num').reset_index('h_if').groupby('h_if'):
    print('h_if='+str(dfgrouped[0]))
    #cols = dfgrouped[1].columns.values
    cols = dfgrouped[1].columns
    print(dfgrouped[1][cols[cols !='h_if']])
    # ??? 여기서 생략된 gender F(h_if = True)도 표시하려면?
    print()
    # print(type(dfgrouped[1])) # <class 'pandas.core.frame.DataFrame'>

# %% [markdown]
# ### 집단별로 함수 적용하기

# %% language="R"
# tapply(dat$h, list(dat$gender, dat$num), mean)
# #dat$h에 대해서 list(dat$gender, dat$num)기준으로 mean 적용하기
#
# #https://stackoverflow.com/questions/53781634/aggregation-in-pandas
# #https://stackoverflow.com/questions/17621325/equivalent-pandas-function-to-this-r-aggregation

# %%
dat[['gender', 'num', 'h']].groupby(['gender', 'num']).mean()

# %%
dat[['gender', 'num', 'h']].groupby(['gender', 'num']).mean().unstack('num')

# %% language="R"
# aggregate(h~gender+num, sum, data=dat)
# # h에 대해서 gender와 num 기준으로 sum


# %% [markdown]
# `.groupby()`를 하기 전에 먼저 컬럼을 선택하는 데 낫다??

# %%
dat.groupby(['gender', 'num'])[['h']].sum()
dat[['gender', 'num', 'h']].groupby(['gender', 'num'])[['h']].sum()
# 위의 두 가지가 속도 차이가 많이 나는가?

# %%
dat.groupby(['gender', 'num'])[['h']].sum() 
# 그냥 .groupby() 한 후에 columns을 선택해도 괜찮을 듯???

# %%
dat[['gender', 'num', 'h']].groupby(['gender', 'num']).sum()

# %% language="R"
# aggregate(cbind(h,w)~gender+num, sum, data=dat)


# %%
dat.groupby(['gender', 'num'])[['h', 'w']].sum()

# %% language="R"
# aggregate(.~gender+num, sum, data=dat)


# %%
dat.groupby(['gender', 'num']).sum()

# %%
#tapply(dat$h, list(dat$gender, dat$num), mean)
dat[['h', 'gender', 'num']].groupby(['num', 'gender']).mean().unstack('num')

# %%
#aggregate(h~gender+num, sum, data=dat)
dat[['h', 'gender', 'num']].groupby(['gender', 'num']).sum()

# %%
#aggregate(h+w~gender+num, sum, data=dat)
dat['h_plus_w'] = dat['h']+dat['w']
dat[['h_plus_w', 'gender', 'num']].groupby(['gender', 'num']).sum()

# %%
#aggregate(cbind(h,w)~gender+num, sum, data=dat)
dat[['h', 'w', 'gender', 'num']].groupby(['gender', 'num']).sum()

# %%
#aggregate(.~gender+num, sum, data=dat)
dat.groupby(['gender', 'num']).sum()

# %% [markdown]
# `.sum()`, `.mean()` 등의 메쏘드가 아니라 임의 함수를 적용하고 한다면,
# `.apply()`를 활용한다. `apply()`는 데이터 프레임의 각 열마다 함수를 적용한다.

# %%
dat[['num', 'h', 'w', 'BMI']].apply(lambda x: np.mean(x)/np.std(x))

# %%
dat[['num', 'h', 'w', 'BMI']].agg(lambda x: np.mean(x)/np.std(x))

# %% [markdown]
# 위에서는 `.apply()`와 `.agg()`의 결과가 동일했다. 하지만 항상 그렇지는 않다. `.apply(lambda x: f(x))`의 경우, `lambda` 함수의 입력은 데이터 프레임이다. 따라서 `.apply(lambda x: x.describe())`와 같이 데이터 프레임을 가정하고 메쏘드를 쓸 수 있다. 하지만 `.agg(lambda x: f(x))`의 경우, 입력 `x`에는 데이터 프레임의 한 컬럼(`pandas.Series`)이 들어가므로, `.apply(lambda x: x.describe())`는 불가능하다. 

# %%
dat.apply(lambda x: x.describe())

# %%
dat.num.head()

# %%

# %%
dat.num.describe()

# %%
dat.agg(lambda x: x.describe())

# %% [markdown]
# 함수를 적용하기 전에 함수를 적용하기에 적절한 컬럼을 선별해야 함을 유의하자.

# %% [markdown]
# `.groupby()`와 함께 사용하여 집단별 함수를 적용할 수 있다.

# %%
#aggregate(dat, list(dat$gender, dat$num), length)
dat.groupby(['gender', 'num']).apply(lambda x: len(x))
# apply의 경우, 입력은 DataFrame, 출력은 DataFrame, Series, scalar 모두 가능하다. 하지만 group마다 그 결과 다를 경우엔?

# %%
dat.groupby(['gender', 'num']).agg(lambda x: len(x))

# %% language="R"
# by(dat, list(dat$gender, dat$num), summary)[c(1,2)]

# %% [markdown]
# `apply()`에 사용하는 함수는 스컬라(scalar)를 반환할 수도 있고, 다음과 같이 pandas.Series를 반환할 수도 있다.

# %%
datDescribe = dat.groupby(['gender', 'num']).apply(lambda x: x.describe())
datDescribe.head(n =10)

# %% [markdown]
# # 9.1.3 `sweep`, `mapply`, `rapply`

# %%
# 근데 중요한 것은 이런 함수가 아니라, 어떤 작업을 하려는 것이며,
# 그것이 어떤 논리에 의해 이런 함수로 나타나게 되었는가가 중요?

# %% [markdown]
# ### `apply`

# %% magic_args="-o mat" language="R"
# mat=matrix(c(1,3,6,2,4,5), 3, 2)
# mat


# %%
mat = np.array([1,3,6,2,4,5]).reshape(2,3).T

# %%
mat

# %% language="R"
# apply(mat, MARGIN=1, FUN=function(x) x-1)


# %%
mat - 1

# %%
np.apply_over_axes(np.sum, mat, 1) # R에서는 남길 차원, Python에서는 aggregate할 차원

# %%
np.apply_over_axes(sum, mat, 1)

# %%
sum(np.array([[1,3,2], [2,2,2]]))
# 기본값 axis=0

# %%
help(np.apply_over_axes)

# %%
np.apply_over_axes(lambda x, y: print(x,y), mat, 1)
mat
np.apply_over_axes(sum, mat, 1)

# !!!
#>>> np.sum(mat, axis=0)
#array([10, 11])
#>>> np.sum(mat, axis=1)
#array([ 3,  7, 11])
#>>> sum(mat, 0)
#array([10, 11])
#>>> sum(mat, 1)
#array([11, 12])
### mat[0] + mat[1] + 1 의 결과인 듯...


# %%
np.apply_along_axis(lambda x: print(x), mat, 1)
# !!! apply_along_axis와 apply_over_axes의 차이는???

# Custom function을 쓰기가 어렵네...??!!!

# %% [markdown]
# ### `sweep`
#

# %% language="R"
# sweep(mat, MARGIN=1, STATS=c(1,3,5), FUN="-") 
# # sweep(mat, MARGIN=1, STATS=1, "-") 도 동일하다.


# %% language="R"
# apply(mat, MARGIN=1, FUN=sum)

# %%
np.apply_over_axes(np.sum, mat, 1)  
# R의 MARGIN은 남겨질 차원을 의미하고,
# Python np.apply_over_axes의 axes는 합쳐질 차원을 의미한다.
# 따라서 R apply의 MARGIN과 Python np.apply_over_axes의 axes를 모두 모으면,
# 전체 차원이 된다.

# %%
# 하지만 np.sum이 아니라 sum을 쓰면 이상해진다.
np.apply_over_axes(sum, mat, 1)  

# 이런 실수를 방지하려면,
# #!!!???
np.apply_over_axes(np.sum, mat, 1)
np.apply_over_axes(np.sum, mat, axes=1)

np.apply_over_axes(sum, mat, axes = 1)
np.apply_over_axes(sum, mat, axes = 0)  # 비교

np.apply_over_axes(sum, mat, [0,1]) # !!! ???

# %%
# 하지만 R처럼 1차원으로 반환받고 싶다면,
np.apply_over_axes(np.sum, mat, 1).squeeze() # 크기가 1인 차원은 생략한다

# 이건 그냥 func(a, axis)... axis는 another argument
np.apply_over_axes(lambda x, y: np.array([print(x, y) is None]), mat, axes = 0)  
# %% magic_args="-o arr" language="R"
# arr = array(rnorm(5^4), c(5,5,5,5))

# %%
arr = np.random.normal(0,1, (3,3,3,3))

# %% language="R"
# apply(arr, MARGIN=c(1,4), FUN=sum)

# %%
np.apply_over_axes(np.sum, arr, [1,2]).squeeze() 
# 위 행렬의 (0,0)-번째 원소는 
arr[0, :, :, 0].sum()
# 0,1,2,3에서 첫번째와 4번째를 제외하면, 1,2

# %% [markdown]
# ## `mapply` 

# %% language="R"
# x <- list(c(1,3,2), c(1,4,4,4), c(1,0))
# lapply(x, sum)
# mapply(sum, x, SIMPLIFY=FALSE)


# %% language="R"
# x <- list(c(1,3,2), c(1,4,4,4), c(1,0))
# sapply(x, sum)
# mapply(sum, x, SIMPLIFY=TRUE)

# %% language="R"
# x <- c(12,14,11)
# y <- c(3,1,5)
# z <- c('a', 'b','c')
#
# mapply("-", x, y)

# %%
x = [12,14,11]
y = [3,1,5]

[a-b for a, b in zip(x,y)]

# %%
x = np.array([12,14,11])
y = np.array([3,1,5])

x-y

# %% language="R"
# mapply(paste, x, y, z, MoreArgs = list(sep='/'))

# %% [markdown]
# R의 `paste(..., sep='/')`는 python에서 `/.join([...])`로 번역될 수 있다.

# %%
x = [12,14,11]
y = [3,1,5]
z = ['a', 'b', 'c']

["/".join([str(a),str(b),c]) for a,b,c in zip(x,y,z)]

# %% language="R"
# rapply(list(c(1,4,2), list(c(1,1,1), c(2,5,2,5))), sum)


# %%
def c(*args):
    return pd.Series(args)


# %%
c(1,4,2)

# %%
data = [c(1,4,2), [c(1,1,1), c(2,5,2,5)]]

def rapply(the_list, func):
    res = []
    for each_item in the_list:
        if isinstance(each_item, list):
            res.append(rapply(each_item, func))
        else:
            res.append(func(each_item))
    return res

rapply(data, np.sum)

# %% [markdown]
# 위의 결과를 다시 `flatten`하는(tree 구조를 1차원으로 펴는) 방법은 다음의 링크를 참조하세요.
# * https://winterj.me/list_of_lists_to_flatten/

# %% language="R"
# rapply(list(c(1,4,2), list(c(1,1,1), c(2,5,2,5))), sum, how='list')


# %% [markdown]
# ## 9.2 여러데이터프레임 합치기

# %% language="R"
# #install.packagesc("dplyr")
# library(dplyr)
# options(stringsAsFactors=F)
# dfCustomer <- data.frame(
#   id = c(1,2,3,4,5),
#   name = c("김희선","박보검","설현","김수현","전지현"),
#   addr = c("서울시","부산시","인천시","강릉시","목포시")
# )
# dfPurchase <- data.frame(
#   name = c("김희선","박보검","김희선","설현","김수현","박보검"),
#   product = c("바지","샴푸","텔레비전","바지","바지","샴푸")
# )
# dfProduct <- data.frame(
#   product = c("샴푸","텔레비전","바지"),
#   price =c(13800, 560000,80000)
# )

# %%
# 8장에서 정의한 `pdDataFrame`을 사용해보자.

def pdDataFrame(**kwargs):
    ar_opt = {}
    ar_data = {}    
    for k in kwargs:
        #print(k)
        if k.startswith('_'):
            ar_opt[k[1:]] = kwargs[k]
        else:
            ar_data[k] = kwargs[k]
    
    #print(ar_opt)
    #print(ar_data)
    
    return pd.DataFrame(ar_data, **ar_opt)

def c(*args):
    return pd.Series(args)


# %%
dfCustomer = pdDataFrame(
  id = c(1,2,3,4,5),
  name = c("김희선","박보검","설현","김수현","전지현"),
  addr = c("서울시","부산시","인천시","강릉시","목포시")
)
dfPurchase = pdDataFrame(
  name = c("김희선","박보검","김희선","설현","김수현","박보검"),
  product = c("바지","샴푸","텔레비전","바지","바지","샴푸")
)
dfProduct = pdDataFrame(
  product = c("샴푸","텔레비전","바지"),
  price =c(13800, 560000,80000)
)

# %% language="R"
# dfCustomer <- data.frame(
#   id = c(1,2,3,4,5),
#   name = c("김희선","박보검","설현","김수현","전지현"),
#   addr = c("서울시","부산시","인천시","강릉시","목포시")
# )
# df1 = dfCustomer %>% slice(1,2)
# df2 = dfCustomer %>% slice(3,4)
# df3 = dfCustomer %>% slice(5)
#
# rbind(df1, df2, df3)
# dplyr::bind_rows(df1, df2, df3)

# %%
df1 = dfCustomer.iloc[[0,1],:]
df2 = dfCustomer.iloc[[2,3],:]
df3 = dfCustomer.iloc[[4],:]

pd.concat([df1,df2,df3], axis=0)

# %% [markdown]
# 다음은 동일한 내용을 일반적인 방법으로 실행한다.

# %%
import pandas as pd
dfCustomer = pd.DataFrame({"id":[1,2,3,4,5], 
                           "name":["김희선","박보검","설현","김수현","전지현"],
                           "addr":["서울시","부산시","인천시","강릉시","목포시"]})
dfPurchase = pd.DataFrame({"name":["김희선","박보검","김희선","설현","김수현","박보검"],
                           "product":["바지","샴푸","텔레비전","바지","바지","샴푸"]})
dfProduct = pd.DataFrame({"product":["샴푸","텔레비전","바지"], 
                          "price":[13800, 560000,80000]})

df1 = dfCustomer.iloc[0:(1+1),:]
df2 = dfCustomer.iloc[2:(3+1),:]
df3 = dfCustomer.iloc[4:(4+1),:]

# %% language="R"
# data.table::rbindlist(list(df1,df2,df3))
# %%
import datatable as dt

dt1 = dt.Frame(df1)
dt2 = dt.Frame(df2)
dt3 = dt.Frame(df3)

dt.rbind(dt1,dt2,dt3)

# %% [markdown]
# `.rbind()`를 메쏘드로 사용하여 주어진 데이터테이블 프레임에 바로 연결할 수도 있다. 

# %%
dt1.rbind(dt2)
dt1


# %%


# %%
pd.concat([df1,df2,df3], axis=0)

# %% [markdown]
# pd.DataFrame의 `.join()` 메쏘드를 사용할 수도 있다. 하지만 R과 사용법이 약간 다르다.

# %%
dfPurchase.columns, \
dfProduct.columns

# %%
dfPurchase.join(dfProduct)
# ValueError: columns overlap but no suffix specified: Index(['product'], dtype='object')
# 기본적으로 index를 기준으로 join?

# %%
from mypack.utils import summary_set

# %%
summary_set(set(dfPurchase.columns), set(dfProduct.columns))
dfPurchase.join(dfProduct, on='product')
# !!! df.join()는 왼쪽은 index를 기준으로?

# %%
pd.merge(dfPurchase, dfProduct, left_on = 'product', right_on = 'product')
# !!! or

# %%
dfPurchase.set_index('product').join(dfProduct, on='product')
#ValueError: You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat
# 여기서 on='product'는 B가 아니라 A의 컬럼

# %%
dfPurchase.join(dfProduct.set_index('product'), on='product')

# %%
dfPurchase.set_index('product').join(dfProduct.set_index('product'))

# %%
dfPurchase.columns
dfProduct.columns
set(dfPurchase.columns) - set(dfProduct.columns)
set(dfProduct.columns) - set(dfPurchase.columns)
set(dfPurchase.columns).intersection(dfProduct.columns)

A = set(dfPurchase.columns)
B = set(dfProduct.columns) 
#!!!
#def summary_set(A, B):
#    print(A.__name__)
#    print(B.__name__)


import re
import traceback

# NOT WORKING
# https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-functione 
def func(var):
    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-2]
    vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
    print(vars_name)
    return

def func(var):
    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-2]
    print(filename, lineno, function_name, code)

func(A)


import inspect, ast

def foo(a, f, b):
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.findsource(frame[0])[0]

    nodes = ast.parse(''.join(string))

    i_expr = -1
    for (i, node) in enumerate(nodes.body):
        if hasattr(node, 'value') and isinstance(node.value, ast.Call) \
            and hasattr(node.value.func, 'id') and node.value.func.id == 'foo':  # Here goes name of the function:
            i_expr = i
            break

    i_expr_next = min(i_expr + 1, len(nodes.body)-1)  
    lineno_start = nodes.body[i_expr].lineno
    lineno_end = nodes.body[i_expr_next].lineno if i_expr_next != i_expr else len(string)

    str_func_call = ''.join([i.strip() for i in string[lineno_start - 1: lineno_end]])
    params = str_func_call[str_func_call.find('(') + 1:-1].split(',')

    print(params)

foo(A,A,A)

# !!!function argument의 expression 얻기?
# https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function
# https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string

def name(**variables):
    return [x for x in variables]

def fun(x):
    return name(x=x)

# !!! 그냥 포기하고

def summary_set(A,B):
    if not isinstance(A, set):
        A = set(A)
    if not isinstance(B, set):
        B = set(B)
    print('* elements only in A:')
    print(A-B)
    print('* elements both in A & B:')
    print(A.intersection(B))
    print('* elements only in B:')
    print(B-A)


# %%
dfPurchase.set_index('product')

# %%
dfProduct.set_index('product')

# %%
dfPurchase.set_index('product').join(dfProduct.set_index('product'))

# %% [markdown]
# 기본적으로 `.join()`은 두 데이터 프레임의 index를 기준으로 병합한다.

# %%
dfPurchase.join(dfProduct.set_index('product'), on='product')

# %% [markdown]
# 한 데이터 프레임(`dfA`)의 index와 다른 데이터 프레임(`dfB`)의 컬럼(`colB`)을 기준으로도 가능하다.
#
# `dfB.join(dfA, on='colB')`

# %% [markdown]
# 하지만 다음의 경우를 보면 index에 상관없이 잘 병합되는 듯 보인다.
#
# 하지만, 자세히 보면 문제점을 발견할 수 있을 것이다.

# %%
dfProduct.join(dfCustomer)
summary_set(dfProduct.columns, dfCustomer.columns)
# 그냥 정수 index를 기준으로 병합

# %% [markdown]
# R에서 동일한 형식의 데이터프레임이 DF1, DF2, DF3으로 나눠져 있을 때, 다음의 함수를 쓸 수 있다.


# %% [raw]
# rbind(DF1, DF2, DF3)
# dplyr::bind_rows(DF1,DF2,DF3)
# data.table::rbindlist(list(DF1, DF2, DF3))


# %% [markdown]
# python에서는 `pd.concat()`을 사용한다.


# %% [raw]
# pd.concat([DF1, DF2, DF3])


# %%
# 공유하는 열이 없을 떄는 NaN 값이 뜬다.

#2 DF1.append(DF2)
# DF2가 한행의 데이터프레임일 때


# 두 데이터에 공통으로 존재하는 열을 기준으로 두 데이터 프레임을 합칠 때
# merge(DF1, DF2)
# dyplyr::left_join(DF1, DF2)

#1 pd.merge(DF1, DF2, on='key')
#pd.merge(left, right, # merge할 DataFrame 객체 이름
            #  how='inner', # left, rigth, inner (default), outer
            #  on=None, # merge의 기준이 되는 Key 변수
            #  left_on=None, # 왼쪽 DataFrame의 변수를 Key로 사용
            #  right_on=None, # 오른쪽 DataFrame의 변수를 Key로 사용
            #  left_index=False, # 만약 True 라면, 왼쪽 DataFrame의 index를 merge Key로 사용
            #  right_index=False, # 만약 True 라면, 오른쪽 DataFrame의 index를 merge Key로 사용
            #  sort=True, # merge 된 후의 DataFrame을 join Key 기준으로 정렬
            #  suffixes=('_x', '_y'), # 중복되는 변수 이름에 대해 접두사 부여 (defaults to '_x', '_y'
            #  copy=True, # merge할 DataFrame을 복사
            #  indicator=False) # 병합된 이후의 DataFrame에 left_only, right_only, both 등의 출처를 알 수 있는 부가 정보 변수 추가
#2 DF1.join(DF2)
# DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)[source]


# %% [markdown]
# ## 9.2.1 기준열을 사용하지 않는 경우

# %% language="R"
# knitr::kable(left_join(dfPurchase, dfProduct), booktabs=TRUE, 
#              caption='소비자의 구매목록', longtable=FALSE)


# %% language="R"
# knitr::kable(list(dfPurchase, dfProduct),
#              booktabs=TRUE, longtable=FALSE,
#              caption='소비자의 구매목록과 상품목록')
# #knitr::kable(dfProduct)


# %% language="R"
# dfCustomer <- data.frame(
#   id = c(1,2,3,4,5),
#   name = c("김희선","박보검","설현","김수현","전지현"),
#   addr = c("서울시","부산시","인천시","강릉시","목포시"),
#   phonenumber = c('0104432332', '0106642632', '01059382', '0109958372', '0102929484')
# )
#
# ## 설현 전화번호 두자리 부족


# %%
dfCustomer = pd.DataFrame({"id":[1,2,3,4,5],
                          "name":["김희선","박보검","설현","김수현","전지현"],
                          "addr":["서울시","부산시","인천시","강릉시","목포시"],
                           "phonenumber":['0104432332', '0106642632', '01059382', '0109958372', '0102929484']})
## 설현 전화번호 두자리 부족                

# %% language="R"
# knitr::kable(list(dfCustomer[,(1:2)], dfCustomer[,(3:4)]),
#              booktabs=TRUE,  longtable=FALSE,
#              caption='동일한 행 갯수, 다른 변수를 가진 두 데이터프레임')
# #knitr::kable(dfCustomer[,(3:4)])


# %% language="R"
# x <- dfCustomer[1:3, ]; y <- dfCustomer[4:5,]
# knitr::kable(list(x, y),
#              booktabs=TRUE,  longtable=FALSE,
#              caption='열의 갯수가 동일하고 동일한 변수를 저장하고 있는 두 데이터프레임')
#
# #knitr::kable(dfCustomer[1:3,])
# #knitr::kable(dfCustomer[-(1:3),])


# %% language="R"
# x <- dfCustomer[1:3,c(1,2,3,4)]
# y <- dfCustomer[-(1:3),c(2,3,1)]
# knitr::kable(list(x,
#                   y),
#              booktabs=TRUE,  longtable=FALSE,
#              caption='동일한 열이름, 다른 순서')
# #knitr::kable(dfCustomer[1:3,c(1,2,3,4)])
# #knitr::kable(dfCustomer[-(1:3),c(2,3,1)])


# %%
## 동일한 열이름으로 저장되어 있지만 열의 순서와 갯수가 다르면 다음의 두가지 방법 사용

## data.table::rbindlist(list(DF1,DF2), fill=TRUE)
## dplyr::bind_rows(DF1, DF2)

## 데이터프레임 모양 동일, 변수 순서 동일하고 열이름만 다르다면 열이름 통일
## # colnames(DF2) <- colnames(DF1)
# %%
# python에서 동일한 열이름이지만, 열의 순서와 갯수가 다른 두 데이터프레임을 합치려면, `pd.concat([...], axis=0)`을 사용하면 된다.

# %%
DF1 = dfCustomer.iloc[[0,1,2],:]
DF2 = dfCustomer.iloc[[3,4],:][['name', 'phonenumber', 'addr']]
DF2

# %%
pd.concat([DF1, DF2], axis=0)

# %%
DF3 = dfCustomer.iloc[[3,4],:][['name', 'phonenumber', 'addr']]

# %%
pd.concat([DF1, DF3], axis=0)

# %%
DF3.rename(columns = {'phonenumber':'phone', 'addr':'ad'}, inplace=True)
# rename() 메쏘드를 쓸 때, `columns=`를 잊지 말자.
DF3

# %%
pd.concat([DF1, DF3], axis=0)

# %% [markdown]
# ## 9.2.2 기준열을 사용하는 경우

# %% language="R"
# DF1 <- dfCustomer[c(1,5,4,3,2),c(2,3)]
# DF2 <- dfCustomer[c(2,4,3,5,1),c(2,4)]
#
# full_join(DF1, DF2)

# %% language="R"
# knitr::kable(list(dfCustomer[c(1,5,4,3,2),c(2,3)],
#                   dfCustomer[c(2,4,3,5,1),c(2,4)]),
#              booktabs=TRUE, longtable=FALSE,
#              caption='행의 순서가 다른 두 데이터프레임')


# %% language="R"
# knitr::kable(list(dfCustomer[c(1,4,3,2),c(2,3)],
#                   dfCustomer[c(2,5,1),c(2,4)]),
#              booktabs=TRUE, longtable=FALSE,
#              caption='행을 1대1 대응할 수 없는 두 데이터프레임')


# %% language="R"
# DF1 <- dfCustomer[c(1,5,4,3,2),c(2,3)]
# DF2 <- dfCustomer[c(2,4,3,5,1),c(2,4)]
#
# full_join(DF1, DF2)

# %% language="R"
# DF1 <- dfCustomer[c(1,5,4,3,2),c(2,3)]
# DF2 <- dfCustomer[c(2,5,1), c(1,4)]
# full_join(DF1, DF2)

# %%
DF1 = dfCustomer
DF2 

#pd.merge(DF1, DF2, on=)

# %% [markdown]
# ## 9.2 데이터프레임 합치기

# %% language="R"
# DF1 <- dfCustomer1 <- data.frame(
#   id = c(3,4,1,5,2),
#   name = c("김희선","박보검","설현","김수현","전지현"),
#   phonenumber = c('0104432332', '0106642632', '01059382', '0109958372', '0102929484')
# )
# DF2 <- dfCustomer2 <- data.frame(
#   id = c(2,3,4,5), 
#   name = c("박보검","설현","김수현","전지현"),
#   addr = c("부산시","인천시","강릉시","목포시")
# )

# %%
DF1 = pd.DataFrame({"id":[3,4,1,5,2],
                    "name":["김희선","박보검","설현","김수현","전지현"], 
                    "phonenumber":['0104432332', '0106642632', '01059382', '0109958372', '0102929484']})
DF2 = pd.DataFrame({"id":[2,3,4,5],
                   "name":["박보검","설현","김수현","전지현"],
                   "addr":["부산시","인천시","강릉시","목포시"]})


# %% language="R"
# install.packages('knitr')

# %% language="R"
# install.packages('dplyr')

# %% language="R"
# #knitr::kable(dfCustomer1 %>% arrange(id))
# #knitr::kable(dfCustomer2 %>% arrange(id))
# library(dplyr)
# knitr::kable(list(dfCustomer1 %>% arrange(id),
#                   dfCustomer2 %>% arrange(id)),
#              booktabs=TRUE,  longtable=FALSE,
#              caption='name과 id가 다른 두 데이터프레임')


# %%
DF1

# %%
DF2

# %% language="R"
# full_join(DF1, DF2)  # 동일한 컬럼을 기준으로


# %% language="R"
# full_join(DF1, DF2, by='name') # 컬럼 name을 기준으로


# %%
pd.merge(DF1, DF2, how='outer')  # full_join -> pd.merge(A, B, how='outer')

# %%
DF1.columns, DF2.columns

# %%
## 공통의 컬럼
cols_on = list(set(DF1.columns.values) & set(DF2.columns.values))
## !!! .intersection() or &
cols_on

# %%
pd.merge(DF1, DF2, on='name')

# %% [markdown]
# ## 9.3 세로형/가로형 변환

# %% language="R"
# #install.packages('tidyr')

# %% language="R"
# #데이터준비
# library(dplyr)
# library(tidyr)
# mtcars$name = rownames(mtcars); rownames(mtcars) = NULL
# mtcars %>% select(name, mpg, cyl, disp) -> mtcars01
# head(mtcars01, 4)


# %%
import numpy as np
#from pydataset import data
#mtcars = data('mtcars')
mtcars = pd.read_csv('dataset/pydataset/mtcars.csv')

# %%
mtcars01 = mtcars.copy()
mtcars01.reset_index(inplace=True)
mtcars01.rename(columns = {'index':'name'}, inplace=True)
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

# %% language="R"
# mtcars01 %>% gather(key='key', value='value', mpg, cyl, disp) -> mtcarsLong
# head(mtcarsLong, 4)


# %%
mtcarsLong = pd.melt(mtcars01, id_vars=["name"])
mtcarsLong.head()

# %% language="R"
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

# %% language="R"
# all.equal(mtcars01, mtcars02)


# %%
mtcars01.equals(mtcars02)

# %% language="R"
# all.equal(mtcars01 %>% arrange(name), 
#           mtcars02 %>% select(name, mpg, cyl, disp) %>% arrange(name))


# %%
mtcars01.head(), mtcars02[['name', 'mpg', 'cyl', 'disp']].head()

# %%
mtcars02.columns.name = None

# %%
mtcars01.sort_values('name').head(), mtcars02[['name', 'mpg', 'cyl', 'disp']].sort_values('name').head()

# %%
# #mtcars01.sort_values?

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

# %% language="R"
# #install.packages('reshape2')

# %% language="R"
# library(reshape2)
# mtcarsLong <- mtcars %>% select(am, name, mpg, cyl, disp) %>%
#   gather(-name, -am, 
#          mpg, cyl, disp, 
#          key='key', value='value', 
#          factor_key=TRUE) 
# head(mtcarsLong)

# %% language="R"
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
mtcarsLong.set_index(['name', 'am']).pivot(columns='key').head()

# %%
mtcarsLong.\
    pivot_table(values='value', index=['name', 'am'], columns = 'key').head()

# %%
mtcarsLong.groupby(['name', 'am', 'key'])['value'].mean().unstack(level=2).head()

# %%
mtcarsWide = mtcarsLong.groupby(['am', 'name','key'])['value'].mean().unstack(level=2).reset_index()

# %%
mtcarsWide.head()

# %% language="R"
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

# %% language="R"
# all.equal(mtcarsLong, mtcarsLong2)
# all.equal(mtcarsWide, mtcarsWide2)


# %%

# %% language="R"
# dcast(mtcarsLong2, am ~ key, fun.aggregate=mean)


# %%
mtcarsLong.groupby(['am', 'key']).agg('mean').unstack(1)

# %%
mtcarsLong.pivot_table(index=['am'], columns=['key'], aggfunc='mean').fillna(0)

# %% language="R"
# dcast(mtcarsLong2, name + am ~ key, fun.aggregate=mean) %>% head(5)


# %%
mtcarsLong.groupby(['name', 'am', 'key']).agg('mean').unstack(2).head()

# %%
mtcarsLong.pivot_table(index=['name', 'am'], columns=['key'], aggfunc='mean').\
    fillna(0).head()

# %% language="R"
# dcast(mtcarsLong2, key ~ am, fun.aggregate=mean)


# %%
mtcarsLong.groupby(['am', 'key']).agg('mean')

# %%
mtcarsLong.pivot_table(index=['am'], columns=['key'], aggfunc='mean').\
    stack().head()

# %% language="R"
# dcast(mtcarsLong2, . ~ am + key, fun.aggregate=mean)

# %%
#mtcarsLong.groupby(['am', 'key']).agg('mean').unstack().unstack()의 결과가 pd.Series이기 때문에
pd.DataFrame(mtcarsLong.groupby(['am', 'key']).agg('mean').unstack().unstack()).T

# %%
pd.DataFrame(mtcarsLong.pivot_table(columns = ['key', 'am'], aggfunc='mean')).T

# %% language="R"
# dcast(mtcarsLong2, am + key ~ ., fun.aggregate=mean)

# %%
mtcarsLong.groupby(['am', 'key']).agg('mean')

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ####  `s.agg(np.mean)`와 `s.agg(lambda x: np.mean(x))`의 결과가 다른 이유는?

# %% [markdown]
# 판다스를 사용하다보면 가끔 의도했던 결과와 다른 결과에 당황하는 경우가 있다. 판다스 시리즈 `s`에 대해 `s.agg(np.mean)`와 `s.agg(lambda x: np.mean(x))`도 비슷한 경우이다.

# %%
s = pd.Series([2,3,5,7,11], dtype=int)

# %%
s.agg(np.mean)

# %%
s.agg(lambda x: np.mean(x))

# %% [markdown]
# 이게 정말 이상한 것은 `np.mean()`과 `lambda x: np.mean(x)`은 동일한 결과를 산출하기 때문이다.

# %%
np.mean(s), (lambda x: np.mean(x))(s)

# %% [markdown]
# 저자는 판다스 시리즈의 `.aggregate()` 또는 `.agg()` 메쏘드[^aggr]의 소스 코드를 검토하여 다음과 같은 사실을 알아냈다.[^pandas14]
#
# 1. `s.agg("mean")`과 같이 `.agg()` 메쏘드의 인자가 문자열인 경우 `getattr(s, "mean")`과 같이 메쏘드를 찾아내서 적용한다.
# 2. `s.agg(np.mean)`과 같이 특별한 함수의 경우는 `s.agg('mean')`으로 바꿔서 결과를 산출한다. 결국 `s.agg(np.mean)` 이나 `s.agg("mean")`은 `s.mean()`이 실행된다.
# 3. `s.agg(func)`와 같이 함수가 인자로 설정된다면, 먼저 `s.apply(func)`을 해본다.[^sapply] `func`가 넘파이 배열이나 판다스 시리즈처럼 여러 값을 전제하고 있다면 `func(s[0])`은 에러를 발생시킨다. 이렇게 에러가 발생되는 경우에 `func(s)`를 시도한다.
#
# [^aggr]: `.agg()`는 `.aggregate()`의 다른 이름일 뿐이다. 
#
# [^pandas14]: pandas 버전은 1.4이었다.
#
# [^sapply]: `s.apply(func)`은 `func(s[0])`, `func(s[1])`, ...을 모아서 결과를 산출한다.

# %% [markdown]
# 그래서 `s.agg(lambda x: np.mean(x))`의 경우는 `s.apply(lambda x: np.mean(x))`을 먼저 실행하는데 `np.mean(s[0])`, `np.mean(s[1])` 등이 모두 에러없이 실행되기 때문에 위에서 봤던 것과 같이 `np.mean(s[0])`, `np.mean(s[1])` 등을 원소로 가지는 판다스 시리즈가 산출된다.

# %% [markdown]
# 만약 `s.agg("mean")`과 동일한 결과를 얻고 싶다면 어떻게 해야할까? `func(s[0])`은 에러가 나도록 하면 된다. `s.agg(lambda x: np.mean(x))`를 `s.agg(lambda x: np.mean(x[:]))`로 살짝 바꿔보자.

# %%
(lambda x: np.mean(x[:]))(s[0])

# %% [markdown]
# `(lambda x: np.mean(x[:]))(s[0])`는 `x=s[0]`이라고 했을 때 `x`가 정수이기 때문에 `x[:]`를 할 수 없고, 에러가 발생한다.

# %% [markdown]
# 따라서 다음과 같이 우리가 원했던 결과를 얻을 수 있다.

# %%
s.agg(lambda x: np.mean(x[:]))

# %% [markdown]
# 근데 굳이 이렇게 해야 하나? 그냥 어떤 함수 `func()`에 대해 `func(s)`가 가능하다면 그렇게 하는게 편하다.

# %%
(lambda x: np.mean(x))(s)

# %% [markdown]
# 그리고 이런 특성은 판다스 시리즈에만 적용되며, 데이터프레임이나, 집단화된 데이터프레임(`df.groupby()`)에서는 적용되지 않음을 유의하자.

# %% [markdown]
# | 함수 |  문자열 |
# |:-----|:-------|
# |builtins.sum|`"sum"`|
# |builtins.max|`"max"`|
# |builtins.min|`"min"`|
# |np.all|`"all"`|
# |np.any|`"any"`|
# |np.sum|`"sum"`|
# |np.nansum|`"sum"`|
# |np.mean|`"mean"`|
# |np.nanmean|`"mean"`|
# |np.prod|`"prod"`|
# |np.nanprod|`"prod"`|
# |np.std|`"std"`|
# |np.nanstd|`"std"`|
# |np.var|`"var"`|
# |np.nanvar|`"var"`|
# |np.median|`"median"`|
# |np.nanmedian|`"median"`|
# |np.max|`"max"`|
# |np.nanmax|`"max"`|
# |np.min|`"min"`|
# |np.nanmin|`"min"`|
# |np.cumprod|`"cumprod"`|
# |np.nancumprod|`"cumprod"`|
# |np.cumsum|`"cumsum"`|
# |np.nancumsum|`"cumsum"`|
