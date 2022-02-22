# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: rtopython3-pip
#     language: python
#     name: rtopython3-pip
# ---

# %% [markdown]
# ## 기술 통계량

# %% [markdown]
# ### 1변수 기술 통계량

# %% [markdown]
# 통계는 크게 **기술**(descriptive) 통계와 **추론**(inferential) 통계로 나뉜다. **기술**통계는 주어진 자료의 특성을 몇 개의 수로 요약할 때 사용되며, **추론**통계는 주어진 자료에서 더 큰 집단의 특성을 추정할 때 사용된다.

# %% [markdown]
# **기술**통계량으로 많이 쓰이는 평균, 표준편차 등의 통계량은 흔히 요약(summary) 통계량으로 불리기도 한다. 많은 자료를 몇 개의 수로 요약하기 때문이다. 1 변수 기술 통계량은 한 변수의 특성을 요약한다. 여기서 어떤 특성을 요약하느냐에 따라 다음과 같이 분류할 수 있다.

# %% [markdown]
# 1. 분포의 중심를 나타내는 통계량
# 2. 분포의 퍼짐 정도를 나타내는 통계량
# 3. 분포의 모양을 나타내는 통계량

# %% [markdown]
# 먼저 연속형 자료에 대해 위의 기술통계량을 구하는 방법을 설명하고, 그 다음으로 범주형 자료에서 기술통계량을 구하는 자료를 설명한다.

# %% [markdown]
# #### 연속형 자료에서 기술 통계량

# %% [markdown]
# **분포의 중심**을 요약하는 통계량으로는 **평균**(mean), **중앙값**(median), **최빈값**(mode), **절사평균**(trimmed mean) 등이 많이 쓰인다. 

# %% [markdown]
# 1. **평균**(mean): 평균은 모든 값을 더한 후, 값의 갯수로 나눈 값이다. 만약 값을 수평저울 위의 위치라고 생각하면 중심의 위치라고 생각할 수 있다. 
# 2. **중앙값**(median): 관찰된 값을 정렬했을 때 가운데 값. 자료에서 중앙값보다 큰 값의 갯수와 중앙값보다 작은 값의 갯수가 같다. 만약 값의 갯수가 짝수라면 보통 중간의 두 수를 평균한다.
# 3. **최빈값**(mode) : 가장 빈번하게 관찰된 값. 관측값이 실수라면 동일한 값이 두 번 관찰되는 경우가 거의 없지만, 실제 관찰값은 정밀도에 한계가 있기 때문에 경우에 따라 최빈값이 분포의 중심에 대한 유용한 정보를 전달하기도 한다. 
# 4. **절사평균**(trimmed mean) : 절사평균은 평균과 중앙값의 유용한 특성을 절충하기 위한 시도이다. 절사평균은 절사되는 비율 $p$를 표시하여 $p$-절사평균이라고 하기도 한다. 0.1-절사 평균은 전체 자료에서 가장 큰 값 10%와 가장 작은 값 10%를 제외한 평균이다. 이런 방식으로 평균과 중앙값을 표기하면 평균은 0.0-절사평균이며, 중앙값은 0.5-절사평균이다. 평균은 이산 분포에서도 연속적이라는 특성을 지닌다. 예를 들어 관찰값이 정수 1,2,3 중의 하나라고 해도 평균은 1,2,3의 비율에 따라 조금씩 달라진다. 반면 중앙값은 이런 이산 분포에서는 분포의 미세한 차이를 나타내기 힘들다. 앞의 이산 분포에서 중앙값은 1,2,3 중의 하나이며 분포가 치우치지 않았다면 대부분 2가 될 것이다. 하지만 평균은 극단값에 의해 크게 영향을 받는다는 단점도 가지고 있다. 이에 반해 중앙값은 극단값에 의해 크게 영향을 받지 않는다는 장점이 있다. 이런 이유로 강건한 통계량을 원하는 사람들은 절사 평균을 사용하여 극단값의 영향을 줄이면서 분포의 특성 자세하게 나타내고자 한다. 사분위간 평균(interquantile mean)은 절사 평균의 하나로 최소 또는 최대 25%를 제외한 중앙 50%의 평균이다. 

# %% [markdown]
# 위의 기술 통계량을 파이썬에 구해보자.

# %% [markdown]
# 먼저 임의의 자료를 **넘파이 배열**로 생성하여 변수 `x`에 할당한다.

# %%
import numpy as np
np.random.seed(0)
x = np.random.normal(0,1,7)
x = np.concatenate([x, [0.3, 0.3, 0.3]])

# %%
np.mean(x)                   # 평균, x.mean() : 결측값이 있다면 np.nanmean(x)을 쓴다.

# %%
np.median(x)                 # 중앙값, x.median() : 결측값이 있다면 np.nanmedian(x)

# %%
# numpy에는 mode를 구하는 함수가 없기 때문에
# 패키지 scipy의 최빈값 함수 mode를 사용했다.
from scipy.stats import mode
mode(x)       # 최빈값

# %%
# 절사평균을 구하기 위해 scipy 패키지를 활용한다
from scipy.stats import trim_mean
trim_mean(x, 0.2)

# %%
# 0.2-절사평균을 구하는 다른 방법
x.sort()
x[int(x.shape[0]*0.2):int(x.shape[0]*0.8)].mean()
# 하지만 x.shape[0]*0.2 또는 x.shape[0]*0.8이 정수로 떨어지지 않을 때
# 위의 scipy 결과와 다를 수 있다.

# %%
trim_mean(x, 0.2)

# %% [markdown]
# 만약 데이터가 **판다스 시리즈**라면 다음과 같이 한다.

# %%
import pandas as pd
s = pd.Series(x)

# %%
s.mean()

# %%
s.median()

# %%
s.mode()

# %%
from scipy.stats import trim_mean
trim_mean(s, 0.2)

# %% [markdown]
# 분포의 퍼짐 정도를 구하는 요약 통계량은 다음과 같다.

# %% [markdown]
# 1. **범위**(range) : 최댓값과 최솟값의 차이
# 2. **사분점간 범위**(interquantile range) :  3사분위수와 1사분위수의 차이
# 3. **분산**(variance) : 값과 평균과의 차이 제곱 평균.
#    1. **표준편차**(standard deviation) : 분산의 양의 제곱근
# 4. **평균절대편차**(MAD; **m**ean **a**bsolute **d**eviation) : 값과 중앙값의 절대 차이의 평균
#

# %% [markdown]
# 위에서 생성한 넘파이 배열 `x`에 대한 범위, 사분점간 범위, 분산, 표준편차를 구하는 방법은 다음과 같다.

# %%
x.max()-x.min()  # 범위

# %%
np.quantile(x, q=0.75) - np.quantile(x, q=0.25) # 사분점간 범위


# %%
def IQR(x):
    if len(x.shape) > 1:
        print('x should be 1-dimensional')
    return np.quantile(x, q=0.75) - np.quantile(x, q=0.25)


# %%
IQR(x)

# %%
np.var(x)  # x.var()

# %%
np.std(x)  # x.std()


# %%
def MAD(x):
    return np.mean(np.abs(x-x.mean()))


# %%
MAD(x)

# %% [markdown]
# 만약 판다스 시리즈 `s`에 자료가 저장되어 있다면 다음과 같이 한다.

# %%
s.max()-s.min() # 범위

# %%
IQR(s) # 사분점간 범위

# %%
s.var() # 분산(variance)

# %%
s.std() # 표준편차(standard deviation)

# %%
s.mad() # MAD : Mean Absolute Deviation


# %% [markdown]
# 참고로 백분위수는 중앙값, 최댓값, 최솟값 등을 모두 나타낼 수 있는 개념이다. 파이썬에서 판다스 시리즈에 대해 `.quantile()`로 구할 수 있다.

# %%
s.quantile(q=0.5) # 중앙값

# %% [markdown]
# 만약 넘파이 배열이라면 `pd.Series()`로 판다스 시리즈로 변환한 후 `.qunatile()`을 활용하자.

# %%
pd.Series(x).quantile(q=0.5)

# %%
s.quantile(q=0) # 최솟값 

# %%
s.quantile(q=1) # 최댓값

# %% [markdown]
# 분포의 모양은 보통 **왜도**(skewness)와 **첨도**(kurtosis)로 나타낸다. 


# %%
s.kurtosis()

# %%
s.skew()


# %% [markdown]
# **왜도**와 **첨도**에 대해서는 몇 가지 부연 설명이 필요할 듯 하다. 모분산을 구하는 공식과 비편향(unbiased) 표준분산을 구하는 공식이 다르듯이 왜도와 첨도도 모수를 구하는 방법과 표본 통계량을 구하는 방법이 다르다.

# %% [markdown]
# * 모분산 :  $\mathbb{E}\left[\left(X-\mu\right)^2\right]$
# * 표본분산 : $\sum_{i}^n \frac{x_i - \bar{x}}{n-1}$

# %% [markdown]
# !!! TO-DOs : 왜도 첨도 관련 이론 추가

# %% [markdown]
# #### 범주형 자료에서 기술 통계량

# %% [markdown]
# 만약 범주형 또는 순위형 변수에 대해 요약 통계치를 구하고자 한다면 앞에서 얘기한 많은 통계량이 쓸모 없다. 범주형을 예를 들어보자. 만약 서울, 부산, 대구를 `1`, `2`, `3`으로 코딩을 하고, 빈수가 2, 1, 3일 때 평균을 구하면 2.167이다. 하지만 이게 무슨 의미가 있는가?

# %% [markdown]
# 서울, 부산, 대구를 `1`, `2`, `3`으로 코딩한 것은 단순히 편의를 위해서이다. 서울, 부산, 대구를 `3`, `2`, 1`로 코딩하거나, `2`, `1`, `3`으로 코딩해도 무방하다. 하지만 코딩 방법에 따라 평균은 달라진다!

# %% [markdown]
# 분산이나 표준편차의 경우도 평균과 마찬가지로 코딩 방법에 따라 달라진다. 범주형 변수에서 사용할 수 있는 변산성 측정치는 엔트로피(entropy)와 지니불순도(gini impurity index)가 있다.[^cat01]
#
# [^cat01]: 엔트로피와 지니불순도는 범주형 데이터의 산포도를 나타낼 수 있는 통계량이지만 자주 쓰이지는 않는다. 범주의 갯수가 작다면 빈도표로도 충분하기 때문이다.

# %% [markdown]
# 다음에는 `np.nan`이 없을 때 손쉽게 사용할 수 있는 `gini()` 함수와 `entropy()` 함수를 정의한다.

# %%
from mypack.utils import ordered, unordered

# %%
s = pd.Series(['a', 'a', 'b', 'b', 'a', 'c'])


# %%
def gini(prob):
    return 1-np.sum(np.square(prob))


# %%
s.value_counts()

# %%
s.value_counts()/len(s)

# %%
gini(s.value_counts()/len(s))


# %%
def entropy(prob):
    return -1 * np.sum(np.log2(prob)*prob)


# %%
entropy(s.value_counts()/len(s))

# %% [markdown]
# 만약 범주의 갯수가 많지 않다면 그냥 표를 제시하는 것도 한 방법이다. 파이썬에서 범주형 또는 문자형 시리즈에 대해 빈도표를 작성하기 위해 `.value_counts()` 메소드를 사용한다.

# %%
s.value_counts()

# %% [markdown]
# 비율을 확인하고자 한다면 `s.value_counts()/len(s)`를 사용할 수 있다.

# %%
s.value_counts()/len(s)

# %% [markdown]
# ### 데이터 프레임의 모든 변수(컬럼)에 대해 요약통계치 구하기

# %%
import pandas as pd

# %%
dat = pd.read_csv('dataset/pydataset/mtcars.csv')

# %%
dat = dat.rename(columns = {'Unnamed: 0':'name'})

# %% [markdown]
# R의 `mtcars` 데이터를 활용하겠다. 먼저 범주형 데이터를 범주형으로 변환한다.

# %%
dat['am'] = dat['am'].astype(unordered([0,1])).cat.rename_categories(['automatic', 'manual'])

# %%
dat['vs'] = dat['vs'].astype(unordered([0,1])).cat.rename_categories(['V-shaped', 'straight'])

# %%
dat['gear'] = dat['gear'].astype(unordered([3,4,5]))

# %% [markdown]
# 데이터 프레임의 모든 열에 대해 요약 통계치를 구하기 위해서는 `.describe()` 메소드를 사용한다.

# %%
dat.describe()
# dat.select_dtypes([int, float]).describe()

# %% [markdown]
# `.describe()`는 기본적으로 수치형 변수만을 골라서 갯수(`count`), 평균(`mean`), 표준편차(`std`), 최솟값(`min`) 등의 요약통계치를 구한다. 만약 범주형 또는 문자열에 대해서 요약통계치를 구하고자 한다면 `.select_dtypes(["O", "cateogry"])`로 먼저 해당 데이터타입의 열을 선택한 후 `.describe()`를 한다. 

# %%
dat.select_dtypes(["O", "category"]).describe()

# %% [markdown]
# 하지만 확인할 수 있는 통계량을 많지 않다. 총 갯수(`count`), 유일한 값의 갯수(`unique`), 최빈값(`top`)과 그 빈도(`freq`) 정도이다.
#
# 모든 컬럼에 대해 데이터타입에 따른 요약통계치를 구하고자 한다면, `.describe(include='all')`를 활용한다.

# %%
dat.describe(include='all')

# %% [markdown]
# `pandas_profiling` 패키지는 데이터 프레임의 자료에 대해 자동적으로 분석 문서를 생성한다.

# %%
import pandas_profiling

pr = dat.profile_report()

pr.to_file('./pd_profile_dat.html')

pr

# https://dandyrilla.github.io/2017-08-12/pandas-10min/
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

# %% [markdown]
# ## === END OF DOCUMENT

# %%
## !! TO-DO : 결측치 관련?

# %%

# %%

# %%
import rpy2.rinterface


# %%
# %load_ext rpy2.ipython

# %% language="R"
# sessionInfo()

# %% language="R"
# .libPaths()

# %% language="R"
# .libPaths('usr/bin/R')
# .libPaths('/home/publishingkwon/R/x86_64-pc-linux-gnu-library/3.6')

# %% language="R"
# .libPaths()

# %% language="R"
# Mode <- function(x) {
#   ux <- unique(x)
#   ux[which.max(tabulate(match(x, ux)))]
# }
#
# set.seed(0); x <- rnorm(10); x


# %% language="R"
# mean(x)
# median(x)
# Mode(x) # table을 통해 빈도수를 확인할 수 있다. 
# mean(x, trim = 0.2)


# %%
import numpy as np
np.random.seed(0)
x = np.random.normal(0,1,10)
x

# %%

# %%
np.mean(x)

# %%
np.median(x)

# %%
# numpy에는 mode 없음.
from scipy.stats import mode
mode(x) # count까지 알 수 있다

# %%
xmode = mode(x)

# %%
xmode.mode, xmode.count

# %%
### mean(x, trim = 0.2) 절사평균
from scipy.stats import trim_mean
m = trim_mean(x, 0.2)
m

# %% magic_args="-o x" language="R"
# max(x)-min(x)


# %%
# %R IQR(x)


# %%
# %R var(x)


# %%
# %R sd(x)


# %%
max(x)-min(x)

# %%
np.max(x) - np.min(x)
# max와 np.max의 차이??


# %%
np.quantile(x, q=0.75) - np.quantile(x, q=0.25)

# %%
np.var(x, ddof=1)  # sample variance
# for population variance(or MLE), ddof = 0
# The average squared deviation is normally calculated as x.sum() / N, where N = len(x). If, however, ddof is specified, the divisor N - ddof is used instead.

# %%
np.std(x, ddof=1)

# %%
import pandas as pd
x = pd.Series(data=x)

x.describe()

# %% language="R"
# gini = function(x, ...) { #useNA = 'always', 'no', 'ifany'
#     1-sum(prop.table(table(x, ...))^2)
# }
# print(x); gini(x)
# %%
xSer = pd.Series(x)


# %%
def gini(x, **kwargs):
    xSer = pd.Series(x)
    return 1-(xSer.value_counts(normalize=True, **kwargs) ** 2).sum()


# %%
gini(x)

# %% language="R"
# x = c(1,3,2,2,4,NA,5,NA)
# gini(x)

# %%
x = [1,3,2,2,4,np.nan, 5, np.nan]
gini(x)

# %% language="R"
# gini(x, useNA = 'no')

# %%
gini(x, dropna = True)

# %% language="R"
# gini(x, useNA = 'ifany')

# %%
gini(x, dropna = False)

# %% language="R"
# gini(x, useNA = 'always')

# %%
gini(x, dropna = False)

# %% language="R"
# data(mpg, package='ggplot2'); require(dplyr)


# %% language="R"
# table(x)

# %% language="R"
# prop.table(table(x))

# %%
pd.Series(x).value_counts()

# %%
pd.Series(x).value_counts(normalize=True)

# %%
pd.Series(x).value_counts(normalize=True, dropna=False)

# %%
# 파이썬 ggplot 사용할 수 있는 라이브러리 plotnine
from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
#from plotnine.data import mpg
import plotnine as p9

# %%
import pydataset

# %%
mpg = pydataset.data('mpg')

# %%
# levels 지정 미입력
mpg.sort_values(by=['drv'])

# %% language="R"
# library(ggplot2)
# library(dplyr)
#
# mpg$drv <- ordered(mpg$drv, levels=c("f", "r", "4"))
# mpg
# %% language="R"
# mpg$fl <- factor(mpg$fl)


# %% magic_args="-o mpg2" language="R"
# mpg2 <- mpg %>% select(class, drv, fl, hwy)


# %% language="R"
# summary(mpg2)


# %%
mpg2.describe()

# %%
mpg2.describe(include='all') 
# include ='all'을 쓰면 categorical variable에 대해서도 
# 정보를 확인할 수 있다. 

# %% language="R"
# install.packages('prettyR')

# %% magic_args="-o mpg2" language="R"
# mpg2[c(1,4,5,16),1] = NA
# mpg2[c(1,4,5,16),2] = NA
# prettyR::freq(mpg2)


# %%
mpg2.iloc[[0,3,4,15],[0,1]] = np.nan

# %%
mpg2

# %%
mpg2['class'].value_counts()

# %%
# pd.DataFrame({'class':mpg2['class'].value_counts()}).T
pd.DataFrame({'freq':mpg2['class'].value_counts()}).T

# %%
df = pd.DataFrame({'freq':mpg2['class'].value_counts()}).T
df.columns.name = 'class'
df

# %%
for col in mpg2.columns:
    print('Frequency for '+col)
    print(pd.DataFrame({col:mpg2[col].value_counts()}).T)
    print('')

# %%
col = 'class'

# %%
# #?pd.Series.value_counts

# %%
mpg2[col].value_counts(normalize=True, dropna=True)

# %%
pd.DataFrame({col:mpg2[col].value_counts(normalize=True, dropna=True)})

# %%
for col in mpg2.columns:
    print('Frequency for '+col)    
    row1= pd.DataFrame({col:mpg2[col].value_counts(dropna=False)}).T
    row2 = pd.DataFrame({col:mpg2[col].value_counts(normalize=True, dropna=False)}).T
    row3 = pd.DataFrame({col:mpg2[col].value_counts(normalize=True, dropna=True)}).T
    allrows = pd.concat([row1, row2, row3], axis=0)
    allrows.index = ['freq', '%', '%(!NA)']
    print(allrows)
    print('')

# %% [markdown]
# ## 결측치 관련

# %%
mpg2.isnull().sum() # 각 컬럼의 결측치 갯수

# %%
mpg2.isnull().sum().sum()  # 전체 결측치 갯수

# %%
mpg2.isnull().any()  # 각 컬럼에 결측치가 존재하는가?

# %%
mpg2.isnull().any().any() # 전체에 결측치가 하나라도 존재하는가?

# %% [markdown]
# ### 결측치 존재 여부 시각화

# %% [raw]
# %pip install missingno

# %% [raw]
# Collecting missingno
#   Downloading missingno-0.4.2-py3-none-any.whl (9.7 kB)
# Requirement already satisfied: seaborn in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno) (0.10.1)
# Requirement already satisfied: matplotlib in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno) (3.1.3)
# Requirement already satisfied: numpy in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno) (1.18.1)
# Requirement already satisfied: scipy in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno) (1.5.0)
# Requirement already satisfied: pandas>=0.22.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from seaborn->missingno) (1.0.5)
# Requirement already satisfied: cycler>=0.10 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib->missingno) (0.10.0)
# Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib->missingno) (2.4.6)
# Requirement already satisfied: kiwisolver>=1.0.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib->missingno) (1.1.0)
# Requirement already satisfied: python-dateutil>=2.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib->missingno) (2.8.1)
# Requirement already satisfied: pytz>=2017.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas>=0.22.0->seaborn->missingno) (2020.1)
# Requirement already satisfied: six in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from cycler>=0.10->matplotlib->missingno) (1.14.0)
# Requirement already satisfied: setuptools in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from kiwisolver>=1.0.1->matplotlib->missingno) (45.2.0.post20200210)
# Installing collected packages: missingno
# Successfully installed missingno-0.4.2
# Note: you may need to restart the kernel to use updated packages.

# %%
import missingno as msno
import matplotlib.pyplot as plt

msno.matrix(mpg2)
plt.show()

# %%
msno.bar(mpg2)
plt.show()

# %%
# #%%R
#install.packages('psych', dependencies=TRUE)
#library(psych)
# psych 설치의 고질점 문제점. mnormt 패키지가 항상 최신의 R만 지원!


# %%
mpg2

# %% [raw] language="R"
# install.packages('psych', dependencies=TRUE)

# %% language="R"
# psych::describe(mpg2)
# #describe(mpg2)


# %% language="R"
# install.packages('Hmisc')

# %% [raw] language="R"
# install.packages('cluster')

# %% language="R"
# .libPaths()

# %% language="R"
# Hmisc::describe(mpg2)
# # .libPaths()를 설정하지 않으면 install되는 곳과 library에서 찾는 장소가 달라지는 듯
# %%

# %%

# %% language="R"
# pastecs::stat.desc(mpg2)
#
# %% [raw]
# %pip install -U pandas_profiling

# %% [raw]
# Collecting pandas_profiling
#   Downloading pandas_profiling-2.8.0-py2.py3-none-any.whl (259 kB)
#      |████████████████████████████████| 259 kB 2.6 MB/s eta 0:00:01
# Collecting visions[type_image_path]==0.4.4
#   Downloading visions-0.4.4-py3-none-any.whl (59 kB)
#      |████████████████████████████████| 59 kB 1.8 MB/s  eta 0:00:01
# Collecting confuse>=1.0.0
#   Downloading confuse-1.3.0-py2.py3-none-any.whl (64 kB)
#      |████████████████████████████████| 64 kB 985 kB/s eta 0:00:011
# Collecting matplotlib>=3.2.0
#   Downloading matplotlib-3.3.0-1-cp36-cp36m-manylinux1_x86_64.whl (11.5 MB)
#      |████████████████████████████████| 11.5 MB 7.9 MB/s eta 0:00:01
# Collecting astropy>=4.0
#   Downloading astropy-4.0.1.post1-cp36-cp36m-manylinux1_x86_64.whl (6.5 MB)
#      |████████████████████████████████| 6.5 MB 28.9 MB/s eta 0:00:01
# Collecting htmlmin>=0.1.12
#   Downloading htmlmin-0.1.12.tar.gz (19 kB)
# Collecting tangled-up-in-unicode>=0.0.6
#   Downloading tangled_up_in_unicode-0.0.6-py3-none-any.whl (3.1 MB)
#      |████████████████████████████████| 3.1 MB 25.5 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: joblib in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (0.16.0)
# Collecting requests>=2.23.0
#   Downloading requests-2.24.0-py2.py3-none-any.whl (61 kB)
#      |████████████████████████████████| 61 kB 436 kB/s  eta 0:00:01
# Requirement already satisfied, skipping upgrade: ipywidgets>=7.5.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (7.5.1)
# Requirement already satisfied, skipping upgrade: numpy>=1.16.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (1.18.1)
# Requirement already satisfied, skipping upgrade: missingno>=0.4.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (0.4.2)
# Requirement already satisfied, skipping upgrade: scipy>=1.4.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (1.5.0)
# Requirement already satisfied, skipping upgrade: pandas!=1.0.0,!=1.0.1,!=1.0.2,>=0.25.3 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (1.0.5)
# Collecting phik>=0.9.10
#   Downloading phik-0.10.0-py3-none-any.whl (599 kB)
#      |████████████████████████████████| 599 kB 58.0 MB/s eta 0:00:01
# Collecting tqdm>=4.43.0
#   Downloading tqdm-4.48.2-py2.py3-none-any.whl (68 kB)
#      |████████████████████████████████| 68 kB 7.3 MB/s  eta 0:00:01
# Requirement already satisfied, skipping upgrade: jinja2>=2.11.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (2.11.1)
# Requirement already satisfied, skipping upgrade: attrs>=19.3.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from visions[type_image_path]==0.4.4->pandas_profiling) (19.3.0)
# Collecting networkx>=2.4
#   Downloading networkx-2.4-py3-none-any.whl (1.6 MB)
#      |████████████████████████████████| 1.6 MB 55.9 MB/s eta 0:00:01
# Collecting imagehash; extra == "type_image_path"
#   Downloading ImageHash-4.1.0.tar.gz (291 kB)
#      |████████████████████████████████| 291 kB 52.6 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: Pillow; extra == "type_image_path" in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from visions[type_image_path]==0.4.4->pandas_profiling) (7.0.0)
# Requirement already satisfied, skipping upgrade: pyyaml in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from confuse>=1.0.0->pandas_profiling) (5.3.1)
# Requirement already satisfied, skipping upgrade: cycler>=0.10 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib>=3.2.0->pandas_profiling) (0.10.0)
# Requirement already satisfied, skipping upgrade: kiwisolver>=1.0.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib>=3.2.0->pandas_profiling) (1.1.0)
# Requirement already satisfied, skipping upgrade: python-dateutil>=2.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib>=3.2.0->pandas_profiling) (2.8.1)
# Requirement already satisfied, skipping upgrade: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib>=3.2.0->pandas_profiling) (2.4.6)
# Requirement already satisfied, skipping upgrade: chardet<4,>=3.0.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from requests>=2.23.0->pandas_profiling) (3.0.4)
# Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from requests>=2.23.0->pandas_profiling) (2020.6.20)
# Requirement already satisfied, skipping upgrade: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from requests>=2.23.0->pandas_profiling) (1.25.8)
# Requirement already satisfied, skipping upgrade: idna<3,>=2.5 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from requests>=2.23.0->pandas_profiling) (2.8)
# Requirement already satisfied, skipping upgrade: ipykernel>=4.5.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (5.1.4)
# Requirement already satisfied, skipping upgrade: ipython>=4.0.0; python_version >= "3.3" in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (7.12.0)
# Requirement already satisfied, skipping upgrade: nbformat>=4.2.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (5.0.4)
# Requirement already satisfied, skipping upgrade: widgetsnbextension~=3.5.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (3.5.1)
# Requirement already satisfied, skipping upgrade: traitlets>=4.3.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (4.3.3)
# Requirement already satisfied, skipping upgrade: seaborn in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno>=0.4.2->pandas_profiling) (0.10.1)
# Requirement already satisfied, skipping upgrade: pytz>=2017.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas!=1.0.0,!=1.0.1,!=1.0.2,>=0.25.3->pandas_profiling) (2020.1)
# Collecting numba>=0.38.1
#   Downloading numba-0.50.1-cp36-cp36m-manylinux2014_x86_64.whl (3.6 MB)
#      |████████████████████████████████| 3.6 MB 49.2 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: MarkupSafe>=0.23 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jinja2>=2.11.1->pandas_profiling) (1.1.1)
# Requirement already satisfied, skipping upgrade: decorator>=4.3.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from networkx>=2.4->visions[type_image_path]==0.4.4->pandas_profiling) (4.4.1)
# Requirement already satisfied, skipping upgrade: six in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from imagehash; extra == "type_image_path"->visions[type_image_path]==0.4.4->pandas_profiling) (1.14.0)
# Collecting PyWavelets
#   Downloading PyWavelets-1.1.1-cp36-cp36m-manylinux1_x86_64.whl (4.4 MB)
#      |████████████████████████████████| 4.4 MB 70.3 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: setuptools in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from kiwisolver>=1.0.1->matplotlib>=3.2.0->pandas_profiling) (45.2.0.post20200210)
# Requirement already satisfied, skipping upgrade: jupyter-client in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipykernel>=4.5.1->ipywidgets>=7.5.1->pandas_profiling) (5.3.4)
# Requirement already satisfied, skipping upgrade: tornado>=4.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipykernel>=4.5.1->ipywidgets>=7.5.1->pandas_profiling) (6.0.3)
# Requirement already satisfied, skipping upgrade: jedi>=0.10 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.16.0)
# Requirement already satisfied, skipping upgrade: backcall in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.1.0)
# Requirement already satisfied, skipping upgrade: pickleshare in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.7.5)
# Requirement already satisfied, skipping upgrade: pexpect; sys_platform != "win32" in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (4.8.0)
# Requirement already satisfied, skipping upgrade: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (3.0.3)
# Requirement already satisfied, skipping upgrade: pygments in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (2.5.2)
# Requirement already satisfied, skipping upgrade: jsonschema!=2.5.0,>=2.4 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (3.2.0)
# Requirement already satisfied, skipping upgrade: ipython-genutils in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (0.2.0)
# Requirement already satisfied, skipping upgrade: jupyter-core in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (4.6.1)
# Requirement already satisfied, skipping upgrade: notebook>=4.4.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (6.0.3)
# Collecting llvmlite<0.34,>=0.33.0.dev0
#   Downloading llvmlite-0.33.0-cp36-cp36m-manylinux1_x86_64.whl (18.3 MB)
#      |████████████████████████████████| 18.3 MB 31.4 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: pyzmq>=13 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jupyter-client->ipykernel>=4.5.1->ipywidgets>=7.5.1->pandas_profiling) (18.1.1)
# Requirement already satisfied, skipping upgrade: parso>=0.5.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jedi>=0.10->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.6.1)
# Requirement already satisfied, skipping upgrade: ptyprocess>=0.5 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pexpect; sys_platform != "win32"->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.6.0)
# Requirement already satisfied, skipping upgrade: wcwidth in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.1.8)
# Requirement already satisfied, skipping upgrade: pyrsistent>=0.14.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (0.15.7)
# Requirement already satisfied, skipping upgrade: importlib-metadata; python_version < "3.8" in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (1.5.0)
# Requirement already satisfied, skipping upgrade: nbconvert in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (5.6.1)
# Requirement already satisfied, skipping upgrade: terminado>=0.8.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.8.3)
# Requirement already satisfied, skipping upgrade: prometheus-client in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.7.1)
# Requirement already satisfied, skipping upgrade: Send2Trash in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (1.5.0)
# Requirement already satisfied, skipping upgrade: zipp>=0.5 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from importlib-metadata; python_version < "3.8"->jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (2.2.0)
# Requirement already satisfied, skipping upgrade: bleach in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (3.1.0)
# Requirement already satisfied, skipping upgrade: testpath in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.4.4)
# Requirement already satisfied, skipping upgrade: defusedxml in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.6.0)
# Requirement already satisfied, skipping upgrade: mistune<2,>=0.8.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.8.4)
# Requirement already satisfied, skipping upgrade: entrypoints>=0.2.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.3)
# Requirement already satisfied, skipping upgrade: pandocfilters>=1.4.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (1.4.2)
# Requirement already satisfied, skipping upgrade: webencodings in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.5.1)
# Building wheels for collected packages: htmlmin, imagehash
#   Building wheel for htmlmin (setup.py) ... done
#   Created wheel for htmlmin: filename=htmlmin-0.1.12-py3-none-any.whl size=27084 sha256=8f3bf5cf671e4150123194abaebee1ae12202117e3cfe92b96bcacd310fd98c4
#   Stored in directory: /home/publishingkwon/.cache/pip/wheels/c3/fe/0b/4450b38bceb9ae43dd7d0f16e353566f30f5f4d59a58eca2ed
#   Building wheel for imagehash (setup.py) ... done
#   Created wheel for imagehash: filename=ImageHash-4.1.0-py2.py3-none-any.whl size=291990 sha256=249afeabccb08deb883bac4783e7a6088ecf8fe9676683e40281dd0751b37dcd
#   Stored in directory: /home/publishingkwon/.cache/pip/wheels/43/f6/25/a58e553441acfc5ad7782c545147759c94d0d95ea1c1edd4bf
# Successfully built htmlmin imagehash
# Installing collected packages: networkx, tangled-up-in-unicode, PyWavelets, imagehash, visions, confuse, matplotlib, astropy, htmlmin, requests, llvmlite, numba, phik, tqdm, pandas-profiling
#   Attempting uninstall: matplotlib
#     Found existing installation: matplotlib 3.1.3
#     Uninstalling matplotlib-3.1.3:
#       Successfully uninstalled matplotlib-3.1.3
#   Attempting uninstall: requests
#     Found existing installation: requests 2.22.0
#     Uninstalling requests-2.22.0:
#       Successfully uninstalled requests-2.22.0
# Successfully installed PyWavelets-1.1.1 astropy-4.0.1.post1 confuse-1.3.0 htmlmin-0.1.12 imagehash-4.1.0 llvmlite-0.33.0 matplotlib-3.3.0 networkx-2.4 numba-0.50.1 pandas-profiling-2.8.0 phik-0.10.0 requests-2.24.0 tangled-up-in-unicode-0.0.6 tqdm-4.48.2 visions-0.4.4
# Note: you may need to restart the kernel to use updated packages.

# %%
import pandas_profiling

pr = mpg2.profile_report()

pr.to_file('./14_DescStat_report.html')

pr

# https://dandyrilla.github.io/2017-08-12/pandas-10min/
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html


# %%

# %%
## 참고
* from rtopython2/14_Desc_Stat_juri
