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
# ## 데이터프레임에서 집단별 함수 적용하기 : 요약 통계치 계산 함수

# %% [markdown]
# 먼저 `data/student_height.csv`의 데이터를 읽어오자.

# %%
dat = pd.read_csv('data/student_height.csv')

# %% [markdown]
# `dat`의 `g`열은 학생의 성별(`Male`/`Female`)을, `v`는 학생의 키를 담고 있다. 간단하게 시각화를 해보자.

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
# ### 데이터프레임에서 집단별 요약 통계치 구하기(예)

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
# ### 데이터프레임에서 집단별 함수 적용하기

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

# %% [markdown]
# ### 행렬에서 차원 축소

# %% [markdown]
# R에서 `apply()`함수는 배열의 차원을 축소할 때 사용할 수 있다. 예를 들어 3차원 배열 `a`에 대해 `apply(a, mean, c(1,2))`를 하면 `a`의 1,2차원을 제외한 나머지 차원은 제거된다. 이때 제거하는 방법은 1,2차원을 제외한 차원이 다른 원소를 모두 모아 `mean`을 구하게 된다. 파이썬에서도 이런 **종류**의 기능을 하는 함수 `np.apply_along_axis()`와 `np.apply_over_axes()`가 마련되어 있지만, R의 `apply()`와 완전히 같지 않다.

# %% [markdown]
# `np.apply_along_axis()`는 `axis`가 단수형인 것에서 짐작할 수 있듯이 한 차원에 대해 함수를 적용한다. 

# %%
import numpy as np

# %%
a = np.array([[170, 175, 173],
              [164, 166, 165]])

# %% [markdown]
# 예를 들어 배열 `a`에서 `a[0,:]`은 남자의 키, `a[1,:]`은 여자의 키라면 `np.apply_along_axis(np.mean, a, 1)`을 한다면 `a`의 1-번째 차원의 원소에 `np.mean()`을 하게 된다.

# %%
np.apply_along_axis(np.mean, 1, a) 
# np.apply_along_axis(func1d, axis, arr)

# %%
b = np.array([[[170, 175, 173],
               [164, 166, 165]],
              [[180, 182, 181],
               [175, 173, 166]],
              [[185, 178, 179],
               [165, 163, 160]]])

# %% [markdown]
# 배열 `b`에서 `b[:,0,:]`은 남자의 키, `b[:,1,:]`은 여자의 키다. 배열 `a`와 비교했을 때 한 차원이 증가했는데, `b`의 0-번째 차원은 학교를 나타낸다. `b[0,:,:]`은 학교 A, `b[1,:,:]`은 학교 B, `b[2,:,:]`은 학교 C의 자료라고 생각하자.

# %%
b.shape

# %% [markdown]
# 학교에 따른 (남자와 여자를 모두 합친) 키 평균을 구하고자 한다면 다음과 같이 할 수 있다.

# %%
np.apply_over_axes(np.mean, b, (1,2))

# %% [markdown]
# `np.apply_over_axes(np.mean, b, (1,2))`가 어떻게 계산되는지 확인해보자. 먼저 `b2 = np.mean(b, axis=1, keepdims=True)`을 계산한다. 그 결과 `b2`에 대해 `np.mean(b2, axis=2, keepdims=True)`를 하여 결과를 산출한다.

# %% [markdown]
# 이는 R의 `apply()`와 다른데 왜냐하면 `apply()`에서는 계산이 각 차원마다 순차적으로 이루어지는 것이 아니라 모든 차원을 합쳐서 계산하기 때문이다.

# %% [markdown]
# 만약 `np.median()`을 사용한다면 차원마다 순차적으로 계산되기 때문에 달라지는 상황을 확인할 수 있다.

# %%
np.apply_over_axes(np.median, b, (1,2))

# %%
np.apply_over_axes(np.median, b, (2,1))

# %% [markdown]
# 첫 번째 계산 결과는 `np.median(b, axis=1, keepdims=True)`를 한 후에 그 결과에 `np.median( , axis=2, keepdims=True)`를 하고, 두 번째 결과는  `np.median(b, axis=2, keepdims=True)`를 한 후에 그 결과에 `np.median( , axis=1, keepdims=True)`를 하게 된다.

# %% [markdown]
# 만약 R의 `apply()`처럼 1-번째 차원과 2-번째 차원을 전부 통틀어서 `np.meidan()`을 하고자 한다면? 다시 말해 `np.median(b[0,:,:])`, `np.median(b[1,:,:])`, `np.median(b[2,:,:])`를 구하고자 한다면?

# %%
np.median(b[0,:,:]), np.median(b[1,:,:]), np.median(b[2,:,:])

# %%
b.reshape(b.shape[0], -1)

# %%
b

# %%
np.apply_along_axis(np.median, 1, b.reshape(b.shape[0], -1))

# %% [markdown]
# 하지만 합쳐야 할 차원이 연속하지 않을 경우에는 이렇게 간단하지 않다. 저자는 `mypack/utils.py`에 `np_apply()` 함수를 만들어 놓았다.

# %%
from mypack.utils import np_apply

# %%
np_apply(b, (0,), np.median) # R과 마찬가지로 np_apply(arr, axis, func)에서 axis는 남겨지는 차원이다.

# %% [markdown]
# `np_apply()`를 사용하면 원하는 차원에 대해 함수를 적용할 수 있다. 예를 들어 `np.median(b[:,0,:])`과 `np.median(b[:,1,:])`를 구해보자. 1-번째 차원을 제외하고 다른 차원을 모두 `np.median()`을 적용한다.

# %%
np.median(b[:,0,:]), np.median(b[:,1,:])

# %%
np_apply(b, 1, np.median)

# %% [markdown]
# 만약 학교와 성별 차원을 남기고 싶다면 다음과 같이 할 수 있다.

# %%
np_apply(b, (0,1), np.median)

# %% [markdown]
# ### 리스트에 함수 적용하기

# %% [markdown]
# R의 `rapply()` 함수는 리스트의 각 원소에 함수를 적용한다. 리스트는 계층적 구조가 가능하기 때문에 리스트의 원소가 다시 리스트라면 그 리스트의 원소에 함수를 적용한다.

# %%
from mypack.utils import c

# %%
data = [c(1,4,2), [c(1,1,1), c(2,5,2,5)]]


# %%
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
