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

# %% [raw]
# !pip install rpy2 
# import rpy2.rinterface

# %% [raw]
# %load_ext rpy2.ipython

# %% [raw] language="R"
# v <- c(172, 172, 170, 170, rnorm(96, 170, 3))
# g <- rep(c("Male", "Female"), 50)
# c(mean(v[g=="Male"]), mean(v[g=="Female"]))

# %% [markdown]
# #### 들어가기 전에
#
# 판다스 시리즈의 산술연산 `+`와 두 리스트를 `+` 하는 것은 다음과 같이 다르다.

# %%
import numpy as np
import pandas as pd

a = pd.Series([1,3,2])
b = pd.Series([-1,-3,-5])
a+b

# %%
[1,3,2]+[-1,-3,-5]

# %% [markdown]
# ## 집단별 함수 적용하기 : 요약 통계치 계산 함수

# %% [markdown]
# 먼저 `data/student_height.csv`의 데이터를 읽어오자.

# %%
dat = pd.read_csv('data/student_height.csv', index_col=0)

# %% [markdown]
# `dat`의 `g`열은 학생의 성별(`Male`/`Female`)을, `v`는 학생의 키를 담고 있다. 간단하게 시각화를 해보자.

# %%
dat.head()

# %%
dat.hist(by='g', sharex = True) 
# .hist() : 히스토그램 그리기
# by=''   : 집단을 나타내는 열
# sharex = True : 동일한 x-좌표

# %% [markdown]
# 앞에서 배운 바와 같이 성별로 키 평균을 구하고자 한다면 다음과 같이 한다.

# %%
dat.groupby('g').mean()


# %% [markdown]
# (`mean()`뿐 아니라 사용자 함수도 적용 가능한) 일반적인 과정은 다음과 같다.

# %% [raw]
# dat.gropuby('g').agg('mean')
# dat.gropuby('g').agg(np.mean)

# %% [markdown]
# 만약 문자열 `'mean'`을 입력한다면, `agg()` 함수는 입력된 데이터 프레임에 `dat`에서 `getattr(dat, 'mean')`을 찾아서 실행한다. 다시 말해 `dat.mean()`을 실행하는 것이다. 좀더 자세한 내용은 마지막의 

# %% [markdown]
# 95-백분위수와 05-백분위수의 차이를 구하는 다음과 같은 함수 `perc_diff90()`를 정의해 보자.

# %%
def perc_diff90(x):
    y = np.percentile(x, [95, 5])
    return y[0] - y[1]


# %%
perc_diff90(np.arange(101))

# %% [markdown]
# 이를 집단마다 적용한다면 다음과 같이 한다.

# %%
dat.groupby('g').agg(perc_diff90)

# %% [markdown]
# 이는 사실 다음과 같은 `for`-문을 간단하게 표현한 것이다.

# %%
res = {} # res는 result의 약자
for g in dat['g'].unique():
    res[g] = dat[dat['g'] == g].mean().item() 
    # .mean()의 결과가 판다스 시리즈이기 때문에 .item()으로 스칼라 값으로 변환
res

# %% [markdown]
# `.gropuby().agg()`를 활용하면 "**어떤 값을 기준**으로 **어떤 함수를 적용**해라"와 같이 `for`-문없이 생각할 수 있으므로 사고를 단순화할 수 있다는 장점이 있다.

# %% [markdown]
# 만약 `v`와 `g`라는 시리즈만 있을 때에는 어떨까?

# %%
g = dat['g']
v = dat['v']
del dat

# %% [markdown]
# 이때에도 굳이 데이터 프레임을 만들 필요가 없이 바로 `.gropuby()`를 할 수 있다. 다음을 보자.

# %%
v.groupby(g).mean(), v.groupby(g).agg(np.mean), v.groupby(g).agg('mean')

# %%
v.groupby(g).agg(perc_diff90)

# %% [markdown]
# * 생각해 볼 문제: `v.groupby(g)` 대신 `v.groupby('g')`를 해보자. 무엇이 문제인가?
#     - 힌트: 위에 `dat.groupy('g')`의 경우는 `dat.groupby(dat['g'])`와 동일하다고 한다.

# %% [markdown]
# * 문제 : 위의 결과를 보며 `Female`이 `Male`에 우선한다. 알파벳 순서에 따른 것이다. 만약 `Male`을 우선 출력하고 싶다면 어떻게 할 수 있을까? 데이터 프레임의 데이터 타입을 타입을 적절하게 변환해보자.

# %% [markdown]
# ### 집단별 요약 통계치 구하기(예)

# %% [markdown]
# #### 빈도표
#
#

# %% [raw] magic_args="-o dat" language="R"
# dat <- data.frame(gender=c('M','M','M','M','M','F','F','F','F','F'),
#                   num=c(1,2,3,1,2,3,1,2,3,1),
#                   h=c(170,180,190,180,170,150,160,170,160,150),
#                   w=c(80,70,100,80,60,50,50,60,60,50))
# dat$BMI <- dat$w/(dat$h/100)^2
# head(dat)


# %%

# %%
from mypack.utils import c, pdDataFrame

# %% [markdown]
# 먼저 데이터를 만들자.

# %%
# 판다스 데이터를 생성하는 좀 더 쉬운(혹은 R과 비슷한) 방법
dat =  pdDataFrame(gender=c('M','M','M','M','M','F','F','F','F','F'),
                   num=c(1,2,3,1,2,3,1,2,3,1),
                   h=c(170,180,190,180,170,150,160,170,160,150),
                   w=c(80,70,100,80,60,50,50,60,60,50))
dat['BMI'] = dat.w/(dat.h/100)**2
dat.head()

# %%
dat.head()

# %% [raw] language="R"
# print(table(dat$gender))
# print(table(dat$gender, dat$num))
# print(table(dat$gender, dat$num, dat$h>170))

# %% [markdown]
# R에서 `table()`은 각 조건에 해당하는 데이터 포인트의 수를 파악하는데 요긴하게 사용된다.
# Python에서 동일한 기능을 하려면 결과 테이블의 차원에 따라 다른 방법을 사용해야 하는 듯 보인다.
#
# * 1차원 : `.value_counts()`
# * 2+차원(a) : `pd.crosstab(index = , columns = )`
# * 2+차원(b) : `.groupby().size().unstack()`

# %% [markdown]
# #### 1차원 빈도표 : `pandas.Series.value_counts()`

# %%
dat['gender'].value_counts() # value_counts
# dat.value_counts()가 아님을 유의하자!

# %%
# or you can do 
def table(self):
    #print(self.name)
    print('* PYTHON WAY: .value_counts()')
    return self.value_counts()

pd.Series.table = table  # monkey-patching

dat['gender'].table()

# %% [markdown]
# 만약 `.groupby()`를 응용한다면 다음과 같이 쓸 수 있다.

# %%
dat.groupby('gender').size(), dat['h'].groupby(dat['gender']).size()

# %% [markdown]
# 위의 두 결과는 어떻게 다른가? `.groupby()` 메쏘드를 데이터 프레임에 적용하는 경우와 시리즈에 적용하는 경우에 어떤 차이가 있는가?

# %% [markdown]
# ### 2+차원 빈도표
#
# 2+차원 빈도표는 2개 이상의 변수를 기준으로 데이터를 나눠서 자료의 갯수를 센다.
#
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

# %% [markdown]
# `pd.crosstab()`은 cross-table을 의미하는 듯 하다. 행을 나누는 변수와 열을 나누는 변수를 `index=`와 `columns=`에 지정한다. 두 개 이상의 변수를 지정할 수도 있다.

# %% [markdown]
# `pd.crosstab()`을 `.groupby()`로 구현한다면 다음과 같이 할 수 있다.

# %%
dat.groupby(['gender', 'num']).size()
# groupby().size()의 문제... NaN이 존재할 때
# 만약 M(gender)-3(num)이 존재하지 않는다면 생략된다?

# %%
pd.crosstab(index = [dat['gender'], dat['num']], columns = 1)

# %% [markdown]
# 사실 열을 구분하는 변수를 지정할 수 없으므로 `.groupby().size()`는 한계가 있다. 하지만 뒤에서 배울 가로형-세로형 변환을 사용하면 그런 한계를 뛰어 넘을 수 있다. 물론 `pd.crosstab()`으로 할 수 있는 일은 `pd.crosstab()`으로 하면 된다. 단순히 자료의 갯수를 세는 일이 아니라면 도움이 될 것이다.

# %% [markdown]
# 여기서는 간단하게 `.groupby().size()`의 세로형 결과를 가로형으로 변환해보자.  
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
# 다음은 R의 `table()`과 비슷한 형식으로 출력한다.

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
# ### 집단별 함수 적용하기

# %% [markdown]
# 집단별로 함수를 적용할 때 함수의 결과에 따라 다음의 분류가 가능하다.
#
# 1. 함수의 결과로 한 값이 산출되는 경우 : `np.mean()`과 같이 여러 값을 하나의 값으로 요약하는 경우이다. 
# 2. 함수의 결과로 여러 값이 동일한 갯수의 여러 값으로 변환되는 경우: 표준화[^standardization]의 결과는 동일한 갯수의 데이터로 변환된다. 
# 3. 그 밖에 : 입력된 자료의 갯수와 같지도 않고, 결과값이 1개도 아닌 경우이다. 모든 집단에 대해 동일한 갯수의 결과가 산출될 수도 있고, 집단마다 결과값의 갯수가 달라질 수도 있다.
#
# [^standardization]: 표준화라 주어진 자료의 평균과 표준편차를 사용해서 평균 0, 표준편차 1의 값으로 변환하는 것이다. 

# %% [markdown]
# 판다스의 `.gropuby()`를 쓴다면 다음의 판다스 메쏘드를 적용 가능하다.

# %% [markdown]
# 1. 함수의 결과로 한 값이 산출되는 경우 : `.aggregate()` 또는 `.agg()`
# 2. 함수의 결과로 여러 값이 동일한 갯수의 여러 값으로 변환되는 경우: `.transform()`
# 3. 그 밖에 : `.apply()` 

# %% [markdown]
# 위에서 집단별 요약 통계치를 구하는 법을 배웠으므로 여기서는 집단별 표준화를 해보자. 집단별 표준화의 가장 큰 특징은 집단별 평균과 표준편차를 사용한다는 점이다.

# %%
def normalize(x):
    return (x-np.mean(x, axis=0))/np.std(x, axis=0)


# %%
normalize(dat['h'])

# %%
dat.groupby('gender')['h'].transform(normalize)

# %% [markdown]
# `normalize()` 함수는 시리즈를 전제로 만들어진 함수이기 때문에 데이터 프레임에 `.groupby()` 이후에 `['h']`로 하나의 열을 선택했다. 만약 데이터 프레임 전체를 다룬다면 다음과 같이 한다. (함수는 각 열에 적용된다.)

# %%
dat.groupby('gender').transform(normalize)

# %% [markdown]
# 문제는 `gender` 열이 사라졌다는 점이다. 새롭게 붙여주거나 애시당초 `gender` 열을 인덱스로 설정할 수도 있다.

# %%
dat.groupby('gender').transform(normalize_df).assign(gender = dat['gender'])

# %%
# 첫 번째 열로 삽입한다면
dat2 = dat.groupby('gender').transform(normalize_df)
dat2.insert(0,"gender",dat['gender'], True) 
dat2

# %% [markdown]
# 만약 `gender` 열을 인덱스로 지정한다면 다음과 같이 `.transform()` 이후의 작업이 필요없다.

# %%
dat.set_index('gender').groupby('gender').transform(normalize_df)

# %% [markdown]
# 기존의 인덱스를 보존하고자 한다면 다음과 같이 한다.

# %%
dat.set_index('gender', append=True).groupby('gender').transform(normalize_df) 

# %%

# %%

# %%

# %%

# %%

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

# %%

# %%

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
