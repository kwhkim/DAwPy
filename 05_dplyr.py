# -*- coding: utf-8 -*-
# %% [raw]
# install.packages("ggplot2")
# install.packages("dplyr")

# %% [markdown]
# # 5.1

# %% [markdown]
# # 5.1.1

# %%
#data(diamonds , package='ggplot2')
from codecs import xmlcharrefreplace_errors # !!!???
# https://www.cmi.ac.in/~madhavan/courses/prog2-2015/docs/python-3.4.2-docs-html/library/codecs.html
# python 3.4.2까지만 지원하는...
#from pydataset import data
#diamonds = data('diamonds')

# %%
#import pandas as pd
#diamonds.to_csv('pydataset_diamonds.csv')

# %%
import numpy as np
import pandas as pd
diamonds = pd.read_csv('pydataset_diamonds.csv', index_col=0)

# %% [markdown]
# `.head(n=)`과 `.tail(n=)`는 데이터 프레임의 처음 `n` 행 또는 마지막 `n` 행을 반환한다. `.shape`은 행과 열의 갯수를 튜플로 반환한다.

# %%
#dim(head(diamonds , n=4)) 
diamonds.head(n=4)
diamonds.tail(n=4)
diamonds.head(n=4).shape

# %% [raw]
# library(magrittr) 
# diamonds %>% head(., n=4) %>% dim(.) 
# diamonds %>% head(n=4) %>% dim() 

# %% [raw]
# diamonds %>% head(n=4) %>% dim 

# %% [markdown]
# 데이터프레임 `diamonds`의 `price` 열은 `['price']`(또는 `.loc[:, 'price']`) 또는 `.price`로도 참조 가능하다. `.price`와 같이 속성으로 참조할 때에는 `.shape` 처럼 데이터프레임에 이미 존재하는 속성은 열을 참조하기 위해 사용할 수 없으므로 유의하자. (만약 `diamonds`에 `shape` 열이 존재한다면 `diamonds.shape`으로 쓸 수 없고, `diamonds['shape']`으로 써야 한다.)

# %%
from mypack.utils import lsf

# %%
diamonds.shape

# %%
diamonds['shape'] = 3

# %%
diamonds.shape # 위에서 새롭게 생성한 shape 열이 아니다!

# %%
del diamonds['shape']  # shape 열을 삭제한다.

# %%
diamonds.head()

# %%
#diamonds %>% .$price %>% .[1:10]
diamonds.price[1:10]

# %%
#diamonds %>% .[["price"]] %>% .[1:10]
diamonds['price'][1:10]

# %% [raw]
# options(tibble.print_max = 5, tibble.print_min = 5)
# ???

# %%
#class(diamonds) 
type(diamonds)

# %% [raw]
# library(dplyr) 
# diamonds 

# %%
#diaTB <- as_tibble(diamonds[1:10, ]) 
#diaDF <- as.data.frame(diamonds[1:10, ])
diaDF = diamonds.iloc[:10, :]

# %% [raw]
# #diaDF$pri      # partial matching
# diaDF.pri      #AttributeError: 'DataFrame' object has no attribute 'pri'
# #diaDF[, 'pri'] # ERROR
# diaDF.loc[:, 'pri'] # KeyError: 'pri'
# #diaTB$pri      # NULL
# #diaTB[, 'pri'] # ERROR


# %% [raw]
# ## 책과 다른 부분 1: data.frame() 의 stringAsFactors 옵션이 원래는 TRUE였는데 4.0+에서 FALSE로 바뀜.
# df <- data.frame(a = c('Kim','Lee','Park'))
# tb <- tibble(a = c('Kim','Lee','Park'))
# ## 그래서 여기서 df의 클래스가 factor 가 아닌 character 로 뜬다.
# class(df$a)
# class(tb$a)

# %%
df = pd.DataFrame({'a':['Kim', 'Lee', 'Park']})
type(df)

# %% [markdown]
# # 5.2

# %% [markdown]
# # 5.2.1

# %% [raw]
# #library(dplyr)
# #data(mtcars) 
# mtcars = data('mtcars')
# df = mtcars

# %% [raw]
# tb = as_tibble(mtcars) 

# %% [raw]
# #from pydataset import data
# #mtcars = data('mtcars')
# #mtcars.to_csv('pydataset_mtcars.csv')

# %%
mtcars = pd.read_csv('pydataset_mtcars.csv', index_col=0)
df = mtcars

# %% [markdown]
# # 5.2.2 `slice`

# %%
# df[2] # 수 하나를 입력할 경우 인덱스로
df[2:5] # slice를 하면 행번호롤
# df[[2,3,4,5]] # 리스트로 여러 값을 입력하면 다시 인덱스로 인식한다!

# %%
df[5:2:-1] # 리스트의 슬라이스와 비슷하게 작동한다.
df[27:50:3]

# %%
df[3:4]

# %%
df[3:3]

# %%
# df[3:3] = df[:10] # 리스트와 다르게 끼어넣기는 안됨
# %%


# %% [markdown]
# 하지만 `.iloc[]`을 사용하는 게 읽기 편하다. 리스트의 슬라이스와 마찬가지로 마자막 순번은 제외된다. 순번 하나 또는 임의의 리스트도 리스트 안에 묶어 쓸 수 있다는 장점이 있다. 만약 `df.iloc[2]`으로 하면 결과는 판다스 데이터프레임이 아니라 판다스 시리즈이다. 만약 데이터프레임을 원한다면 `df.iloc[[2]]`으로 한다.  

# %%
df.iloc[2]

# %%
#tb[2:5, ]
#slice(tb, 2:5)
df.iloc[1:5]  # 2-1 = 1, 5 = 5

# %%
df.iloc[[2,3,5]]

# %% [raw]
# tb %>% .[2:5, ]
# tb %>% slice(., 2:5)


# %% [markdown]
# R의 `c()`, `seq()`와 비슷한 역할을 함수 `lc()`, `lseq()`(결과 리스트)와 `ac()`, `aseq()`(결과 넘파이 배열)을 정의하면 순번을 편하게 지정할 수 있다.

# %%
#tb %>% slice(2:5)
#tb %>% slice(c(2:3, 4, 5))
#from Ax_rutils import ac, aseq, lc, lseq
from mypack.utils import ac, aseq, lc, lseq

# %% [raw]
# import Ax_rutils
# from Ax_rutils import ac as c
# from Ax_rutils import aseq as seq

# %%
# 결과를 lseq, aseq로 구분하는게 나을 듯?(list or array)
df.iloc[lc(lseq(1,2),3,4), :]

# %%
df.iloc[ac(aseq(1,2),3,4), :] # 넘파이 1차 배열을 써도 마찬가지

# %% [markdown]
# ## 5.2.3 `filter`

# %% [markdown]
# 데이터프레임의 행을 선택하는 방법을 소개한다. 예를 들어 `mpg` 값이 30 이상인 행만을 골라내고 싶다면 다음과 같이 할 수 있다. `df['mpg']>30`는 참거짓의 데이터 시리즈이며 인덱스는 `df`가 같다. 

# %%
df['mpg'] > 30

# %%
#tb[tb$mpg>30, ]
df[df.mpg > 30]
df[df['mpg'] > 30] # 위의 방법은 실수할 가능성이 있다.

# %% [markdown]
# 만약 `mpg` 값이 30 이상**이고**, `carb` 값이 1인 행을 골라내고자 한다면, 다음과 같이 `( > ) & ( == )`형태로 쓴다. 이때 `&`는 원래 비트수준(bitwise) AND인데, 판다스 시리즈나 넘파이 배열에 사용하는 경우 벡터화된 AND로 쓰인다. 이때 의미는 벡터화된 AND이지만, 우선 순위는 원래 그대로라서 `>` 나 `==`와 같은 비교 연산자보다 높기 때문에 괄호로 비교연산자의 우선순위를 높여 주었다.

# %% [markdown]
# `not`, `and`, `or`은 논리값(True/False)에 사용하는 연산
# `~`, `&`, `|`은 비트(bitwise) 연산
#
# 우선순위 : `~` > `&`> `|` > 비교연산자(`==`, `<`, `>` 등) > `not` > `and` > `or`
#
# 비트 연산이 더 높다!
# 비트 연산 `~`, `&`, `|`를 넘파이 배열이나 데이터프레임 시리즈에 적용하면
# **벡터화**된 논리연산으로 작동한다.
#

# %%
# 일반적인 비트 연산의 예
x = 0b011010 # 이진수 011010
y = 0b110011 # 이진수 110011
print(f"{x:08b}") # 형식 08b : 8자리 2진수(앞쪽에 0으로 공란 채움)
print(f"{y:08b}")
print(f"{x & y:08b}")

# %%
# numpy의 벡터화된 연산 예 : +, *, /, ...
np.array([1,2,3]) + np.array([2,4,3])

# %%
np.array([True,False,False]) & np.array([True,True,False]) # 벡터화된 AND
# &, |, ~ # 벡터화된 논리 연산

# %%
df[df['mpg'] > 30 & df['carb'] == 1] 

# %% [markdown]
# 위의 식은 `&`가 비교연산자 `==`, `>`, `<` 등보다 우선순위가 높기 때문에 다음과 같이 해석된다. 
#
# ```
# df[df['mpg'] > (30 & df['carb']) == 1]
# ```
#
# 파이썬 비교 연산자는 `a > b == 1`과 같은 표현이 가능하지만(`a > b and b == 1`로 해석),
# 넘파이 배열은 불가능하다. 다음을 보자.

# %%
a = np.array([1,2,3])
b = np.array([3,2,1])
c = np.array([3,1,1])
a > b

# %%
b == c

# %%
a > b == c

# %%
df[(df['mpg'] > 30) & (df['carb'] == 1)] # &, |, ~ 

# %% [markdown]
# 데이터 프레임은 `.query()`라는 메쏘드를 지원한다. 행이 만족해야하는 조건을 문자열로 적는데, 열이름을 바로 적을 수 있다는 장점이 있다. 예를 들어 `df[df["mpg"] >30]`는 데이터프레임 `df`에서 `mpg` 변수 값이 30보다 큰 행을 선택한다. 이를 `.query()`를 사용하여 적으면 다음과 같다.

# %%
#filter(tb, mpg>30)
#tb %>% filter(., mpg>30)
#tb %>% filter(mpg>30)
df.query("mpg > 30")

# %% [markdown]
# 이때 `query("")` 안의 변수는 모두 데이터프레임의 열을 의미하게 된다는 점을 주의하자. 다른 외부 변수를 가리키려면 다음과 같이 활용할 수 있다.

# %%
x = 30

# %%
df.query("mpg >" + str(x))

# %%
df.query(f"mpg > {x}")

# %% [markdown]
# `.query()` 안에서 NOT, AND, OR 등은 `~`, `&`, `|`이며, 

# %%
# 만약 &가 필요하다면,
df[(df.mpg > 30) & (df.cyl == 4)] # &의 연산 순서가 <,>,==보다 낮기 때문에!
df.query("mpg>30 & cyl==4") # .query()의 경우는 괜찮음
# 연산 순서에 주의할 필요가 있다.

# %%
# query의 경우 column 이름에 공백이나 기호가 들어갈 경우 다음과 같이 backtik을 사용한다
df['horse power'] = df.hp
df[df['horse power'] > 250]
df.query('`horse power` > 250')

# %%

# %% [markdown]
# # 5.2.4 `select`

# %% [markdown]
# 열을 선택할 때에는 앞에서 봤듯이 `.iloc[:, ...]`을 통해 순번으로, `.loc[:,...]`을 통해 열이름으로 할 수 있다.

# %%
#tb <- tb %>% slice(3:5)
df = df.iloc[2:5]

# %% [raw]
# tb[, c(1,3)]
# select(tb, c(1,3))
# tb %>% select(c(1,3))

# %%
#tb <- tb %>% slice(3:5)
#tb[, c(1,3)]
df.iloc[:, [1,3]] # df의 1,3-번째 열

# %% [markdown]
# `.filter()`의 경우 R과 다르게 행이름이나 열이름을 기준으로 데이터를 선택한다. `.filter()`를 사용하는 몇 가지 방법은 다음과 같다.
#
# 1. `df.filter(items=lst_colname, axis=1)` : `df.loc[:, lst_colname]`과 같다(`lst_colname`은 열이름을 담고 있는 리스트). 만약 `df.filter(items= , axis=0)`과 같이 쓴다면 행을 선택하는데 사용할 수도 있다. 
#
# 2. `df.filter(like=substr, axis=1)` : `substr`이 열이름 속에 포함되는 열 선택
#
# 3. `df.filter(regex=regex, axis=1)` : 정규표현식 `regex`에 해당하는 패턴을 열이름 속에서 찾을 수 있는 열 선택
#
#
#
#

# %%
df.filter(items = df.columns[[0,2]]) # df의 0,2-번째 열
#df.loc[:, df.columns[[0,2]]]

# %% [raw]
# tb[, c("cyl", "hp")]
# select(tb, c("cyl", "hp"))
# select(tb, c(cyl, hp))

# %% [raw]
# tb %>% select(c("cyl", "hp"))
# tb %>% select(c(cyl, hp))

# %%
#tb %>% select("cyl", "hp")
#tb %>% select(cyl, hp)
df.loc[:, ['cyl', 'hp']] # 열이름 cyl, hp 열 선택
df.filter(items = ['cyl', 'hp']) # 열이름 cyl, hp 열 선택


# %%
import numpy as np

# %%
#which(colnames(tb)=='hp')
np.where(df.columns == 'hp')[0]  # 열이름이 'hp'인 열의 순번 확인. 여기서 [0]는 np.where()의 결과가 tuple이기 때문에 0-번째 원소를 선택하기 위해 쓰였다. 0-번째 원소의 type은 np.ndarray이다.

# %%
#which(colnames(tb)=='qsec') 
np.where(df.columns == 'qsec')[0] # 열이름이 'qsec'인 열의 순번 확인

# %%
#tb[, which(colnames(tb)=='hp'):which(colnames(tb)=='qsec')] 
df.iloc[:, lseq(np.where(df.columns == 'hp')[0],
                np.where(df.columns == 'qsec')[0])]

# %%
df.iloc[:, np.where(df.columns == 'hp')[0].item():np.where(df.columns == 'qsec')[0].item()]

# %%
#tb %>% select(hp:qsec)
df.loc[:, 'hp':'qsec'] # Slice는 가능하지만
#df.loc[:, lseq('hp', 'qsec')]

# %% [raw]
# slice(tb, c(1, 2))
# #책과 다른 부분 2 : slice 가 벡터를 받지 않아도 실행이 된다.
# slice(tb, 1, 2)

# %%
df.columns

# %% [markdown]
# 연속된 열의 경우에는 `df.loc[:, 'hp':'qsec']`로 쓸 수 있지만, `mpg`에서 `hp`까지 모든 열 **그리고** `vs`에서 `gear`까지의 모든 열을 선택해야 하는 경우에는 Slice를 사용할 수 없게 되므로 모든 열이름 또는 열순번을 알아내야 한다. 

# %%
np.where(df.columns.isin(['mpg', 'hp', 'vs', 'gear']))

# %%
from mypack.utils import lc, lseq

# %%
lseq(7,0) # !!! 문제 case

# %%
df.iloc[:, lc(lseq(0,3), lseq(7,9))]

# %% [markdown]
# # 5.2.4.1 특정한 조건을 만족하는 열이름

# %% [raw]
# #  구문                  의미
# # starts_with('ab')   ab로 시작하는
# # ends_with('yz')     yz로 끝나는
# # contains_with('ef)  ef를 포함하는
# # one_of(coln)        문자열 벡터 coln의 각 원소와 일치하는
# # matches('..[cd]')   정규표현식 ..[cd]와 대응하는

# %%
#tb3 <- tb %>% slice(1:3) 
#tb3 
#tb3 %>% select(starts_with('c')) 
#tb3 %>% select(starts_with('ca')) 
#tb3 %>% select(ends_with('p')) 
#tb3 %>% select(contains('c'))
df.columns.str.startswith('c')
df.filter(regex = '^c', axis=1) 
df.filter(regex = '^c')
df.filter(regex = '^ca')
df.filter(regex = 'p$')
df.filter(like = 'c') # c를 포함하는
#df.filter(regex = '.*c.*') # c를 포함하는 
df.filter(regex = 'c') # c를 포함하는 

# %%
df.filter(regex='c', axis=0).filter(regex='c', axis=1)

# %%
# %timeit df.filter(like='c')
# %timeit df.filter(regex = 'c')
# 위의 like='c'가 좀 더 빠르지만 큰 차이는 없었다.
# 125 µs ± 2.95 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# 129 µs ± 2.92 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# %%
#coln <- c('drat', 'qsec') 
#tb3 %>% select(one_of(coln)) 
colmn = ['drat', 'qsec']
df.filter(items = colmn)


# %%
#tb3 %>% select(matches('^(.s|.{4})')) 
df.filter(regex = '^(.s|.{4})')

# %% [markdown]
# # 위아래 한쌍으로 dplyr 함수와 동일한 정규 표현식

# %% [raw]
# tb %>% select(starts_with('c'))
# tb[, grep('^c', colnames(tb))]

# %%
df.loc[:, df.columns.str.contains('^c')]

# %%
df.filter(regex = '^c', axis=1)

# %% [raw]
# tb %>% select(ends_with('p'))
# tb[, grep('p$', colnames(tb))]

# %%
df.loc[:, df.columns.str.contains('p$')]

# %%
df.filter(regex = 'p$', axis=1)

# %% [raw]
# tb %>% select(contains('c'))
# tb[, grep('c', colnames(tb))]

# %%
df.loc[:, df.columns.str.contains('c')]

# %%
df.filter(like='c')
# df.filter(like='c', axis=1)
# df.filter(like='c', axis='columns')

# %% [markdown]
# # 5.2.5 특정한 열이름 제외

# %%
#tb %>% select(-cyl, -qsec)
#tb %>% select(-c(cyl, qsec))
#https://stackoverflow.com/questions/406230/regular-expression-to-match-a-line-that-doesnt-contain-a-word
# does NOT contain
df = df.iloc[:5, :]
df.filter(regex = '^((?!m).)*$') # m을 포함하지 않는
df.filter(regex = '^((?!cyl|qsec).)*$') # cyl 또는 qsec을 포함하지 않는
df.filter(regex = '^((?!(cyl|qsec|m)).)*$')

# %%
# NOT one of
df.filter(regex = '^(?!m$)')
# look ahead or look behind
# positive/negative look ahead q(?=u), q(?!u)
# positive/negative look behind (?<=u)q, (?<!u)q 
df.filter(regex = '^(?!(m$|cyl$|qse$))')  # m, cyl, qse를 제외
df.filter(items = df.columns.difference(['m', 'cyl', 'qse']))
# 컴럼 내용은 같지만 순서가 다르다?
# df.filter(regex = '^(?!(m$|cyl$|qse$))').sort_values() #
# TypeError: sort_values() missing 1 required positional argument: 'by'
df.filter(items = df.columns.difference(['m', 'cyl', 'qse'])).sort_values('qsec')


# %%
#df.filter(regex = '^(?<!(m|cyl|qsec))$')  
df.filter(regex = '^(?<!m)(?<!cyl)(?<!qsec)$')  
# when regex = '^(?<!(m|cyl|qsec))$'
# re.error: look-behind requires fixed-width pattern
df.filter(regex = '^.{3}(?<!(cyl|qse))') # seems impossible
# cyl, qse로 시작하지 않는...

# %%
#tb %>% select(-starts_with('c'))
#tb %>% select(-contains('c'))
df.filter(regex = '^(?!c)')
df.filter(regex = '^((?!c).)*$')

# %% [markdown]
# # 5.3

# %% [markdown]
# # 5.3.1

# %%
#library(dplyr)
#data(mtcars) 
#tb = as_tibble(mtcars) 
#tb2 <- tb %>% select(hp, cyl, qsec) %>% slice(1:3)
#df = data('mtcars')
df = pd.read_csv('pydataset_mtcars.csv', index_col=0)
df2 = df.loc[:, ['hp', 'cyl', 'qsec']].iloc[:3, :]
df2['shape'] = True
# 넘파이 배열에는 기본적 정보를 담고 있는 속성이 있다. 
# 예를 들어 .shape(각 차원의 크기), .size(원소의 갯수) 등이 대표적이다.
# 이렇게 자동적으로 존재하는 속성과 열이름이 겹치게 되면 
# df2['shape']을 df2.shape으로 확인할 수 없다.
# df2.shape은 df2의 각 차원의 크기를 나타낸다. 

# %%
df2

# %%
#df2['hp']
df2.hp

# %%
#df2.shape
df2['shape']

# %%
#tb2 %>% mutate(hp/cyl)
#tb2 %>% mutate(hpPerCyl = hp/cyl)
#tb2 %>% mutate(hpPerCyl = hp/cyl, V2 = hp*qsec)
df2.assign(hpPerCyl = df2.hp/df2.cyl)

# %%

# %%
df3 = df2.assign(hpPerCyl = df2.hp/df2.cyl, V2=df2.hp*df2.qsec)

# %% [raw]
# tb2$`hp/cyl` 
# tb3 <- tb2 %>% mutate(hp/cyl) 
# tb3$`hp/cyl` 

# %% [raw]
# tb$V2 = with(tb, hp*qsec)
# tb[c('V1', 'V2')] = data.frame(tb$hp/tb$cyl, tb$hp*tb$qsec)

# %% [markdown]
# # 5.3.2

# %% [markdown]
# # dplyr 함수와 기존의 방법 비교

# %%
#tb %>% arrange(cyl)
#tb[order(tb$cyl), ]
df.sort_values("cyl")

# %%
#tb %>% arrange(desc(cyl))
#tb[order(tb$cyl, decreasing = T), ]
df.sort_values('cyl', ascending = False)

# %%
#tb3 %>% arrange(cyl, desc(qsec))
df.sort_values(['cyl', 'qsec'], ascending = [True, False])

# %% [markdown]
# # 5.3.3

# %%
#tb %>% summarise(mean(hp)) 
#tb %>% summarize(V1 = mean(hp))
#tb %>% summarise(hpMean = mean(hp), qsecMedian =median(qsec))
df[['hp']].agg('mean') # aggregate
df[['hp','qsec']].agg(np.mean)

# %%
df.agg(V1 = ('hp', np.mean)) # V1은 'hp' 컬럼에 np.mean을 적용하라
df.agg(hpMean = ('hp', np.mean), qsecMedian = ('qsec', 'median'))
# df.agg(hpMean = ('hp', 'mean'), qsecMedian = ('qsec', np.median)) 와 동일한 결과

# %%
# df.agg(hpMean = np.mean, qsecMedian = np.median) # TypeError

# %%
df.groupby([0]*len(df)).\
    apply(lambda x: 
      pd.Series([np.mean(x.hp), np.median(x.qsec)],
                index = ['hpMean', 'qsecMedian']))

# %%
df.groupby([0]*len(df)).\
    apply(lambda x: 
      pd.Series(
          {'hpMean':np.mean(x.hp), 
           'qsecMedian':np.median(x.qsec)}))

# %%
df.pipe(lambda x: 
      pd.Series([np.mean(x.hp), np.median(x.qsec)],
                index = ['hpMean', 'qsecMedian']))

# %%
df.pipe(lambda x: 
      pd.DataFrame(
          {'hpMean': [np.mean(x.hp)], 
           'qsecMedian' : [np.median(x.qsec)]}))

# %%
#tb %>% summarise(newVar1 = mean(hp) + median(qsec))
#tb %>% summarise(newVar1 = mean(hp), newVar2 = median(qsec))
df.pipe(lambda x:
  pd.DataFrame({'newVar1':[np.mean(x.hp) + np.median(x.qsec)]}))
df.pipe(lambda x:
  pd.Series({'newVar1':np.mean(x.hp),
             'newVar2':np.median(x.qsec)}))

# %%
#tb %>% summarise(v1 = mean(hp), v2 = median(qsec), v3 = v1 + v2)
#data.frame(v1 = mean(tb$hp), v2 = median(tb$qsec), v3 = v1 + v2)
df2 = df.agg(v1 = ('hp', np.mean),
             v2 = ('qsec', np.median)).T
df2['v3'] = df2.v1 + df2.v2
df2.agg('mean', axis=0)


# %% [markdown]
# ### 5.3.4

# %%
#tb3 %>% group_by(cyl) 
#tb3_grp <- tb3 %>% group_by(cyl) 
#class(tb3_grp)
df3.groupby('cyl') # pandas.core.groupby.generic.DataFrameGroupBy

# %%
##5.3.5
#tb %>% group_by(am) %>% summarise(mean(qsec))
df.groupby('am').agg({'qsec':'mean', 'drat':'median'})

# %%
df.groupby('am').agg(np.mean)

# %%
df.groupby('am').apply(lambda x: 
  pd.Series({'mQsec':np.mean(x.qsec)}))


# %% [markdown]
# # 5.3.6

# %%
#tb %>% summarise(range(hp))
def peak_to_peak(x):
    return x.max() - x.min()
df.groupby([0]*len(df)).apply(lambda x: peak_to_peak(x.hp))
#tb %>% group_by(am) %>% do(head(., n=2))

# %%
peak_to_peak(df)

# %%
(lambda x: x.head(n=2))(df)
# np.mean(df)

# %%
df.head(n=10)

# %%
df.groupby('am').apply(lambda x: x.head(n=len(x))) # ??? 모르겠음???

# %%
df.groupby('am').apply(lambda x: x.head(n=2))
# df.groupby('am').agg(np.mean)

# %%
np.mean(df)

# %%
df.groupby('am').agg(np.mean)

# %%
df['am'][0]


# %%
def myfunc(x):
    print('am=',x['am'][0])
    #print('mpg=', x['mpg'])
    print(x.head(3))


# %%
df.groupby('am').apply(myfunc)

# %%
#tb %>% group_by(am) %>% do(summary(.))
df.groupby('am').apply(lambda x: x.describe())

# %%
#tb %>% group_by(am) %>% 
#  do(as.data.frame(summary(.))) %>% 
#  slice(1:3)
df.groupby('am').apply(lambda x: pd.DataFrame(x.describe())).iloc[:3, :]

# %% [markdown]
# # 5.3.7

# %% [raw]
# # 선별 및 가공 절차
# #tb %>% select() %>% filter() %>% group_by() %>%
# #summarise(), do(), arrange(, .by_group=T)
# %%


# %% [markdown]
# # 5.4
# # 5.4.1


# %%
#library(dplyr)
#mtcars %>% mutate(exp(qsec)) %>% head(3)
mtcars.assign(q = np.exp(mtcars.qsec)).head(3)

# %%
#mtcars %>% 
#  mutate(expMpg=exp(mpg), expCyl=exp(cyl), expDisp=exp(disp), 
#         expHp=exp(hp), expDrat=exp(drat), expWt=exp(wt), 
#         expQsec=exp(qsec), expVs=exp(vs), expAm=exp(am), 
#         expGear=exp(gear), expCarb=exp(carb)) %>% 
#  head(n=3)
mtcars.assign(expMpg = np.exp(mtcars.mpg),
              expCyl = np.exp(mtcars.cyl)) # 뒷 부분 생략?

# %%
#mtcars %>% mutate_all(exp) %>% head(n=3) 
mtcars.transform(np.exp) 

# %% [markdown]
# ### 5.4.2


# %% [raw]
# #                  _all         _at      _if
# # select       select_all  select_at   select_if
# # mutate       mutate_all  mutate_at   mutate_if
# # transmute    transmute_all transmute_at  transmute_if
# # group_by     group_by_all  group_by_at group_by_if
# # summarise    summarise_all summarise_at summarise_if 

# %% [raw]
# options(digits=4)

# %% [raw]
# coln = c('cyl', 'disp', 'drat', 'carb') 
# mtcars %>% mutate_at(coln, exp) %>% head(n=3) 

# %%
colmn = ['cyl', 'disp', 'drat', 'carb']
mtcars.loc[:, colmn].transform(np.exp).head(3)
# R의 transmute와 같이 기존의 열에 덮어쓴다.

# %%
#mtcars %>% 
#  select(starts_with('c'), starts_with('d')) %>% 
#  mutate_all(exp) %>% 
#  head(n=3)
mtcars.filter(regex=('(^c|^d)')).transform(np.exp).head(3)

# %% [raw]
# mtcars %>% 
#  mutate_at(vars(starts_with('c'), starts_with('d')), 
#            exp) %>% 
#  head(n=3)

# %%
#mtcars %>% 
#  mutate_if(function(x) { sum(x)<100 }, exp ) %>% 
#  head(n=3)
colmn = mtcars.apply(lambda x: x.sum() < 100, axis=0) # axis=0을 모두 모아...
mtcars.loc[:, colmn].transform(np.exp).head(3)


# %% [raw]
# mtcars %>% 
#  transmute(expCarb = exp(carb)) %>% head(n=3) 

# %%
mtcars.assign(expCarb = np.exp(mtcars.carb)).head(3)
mtcars.pipe(lambda x:
    pd.DataFrame({'expCarb':
        np.exp(mtcars.carb)})).head(3)
pd.DataFrame({'expCarb': np.exp(mtcars.carb)}).head(3)

# %% [raw]
# mtcars %>% transmute_if(function(x) sum(x)<100, exp) %>% head(n=3)
# #`funs()` is deprecated as of dplyr 0.8.0
# mtcars %>% transmute_if(funs(sum(.) <100), exp) %>% head(n=3)


# %% [raw]
# mtcars %>% 
#  mutate_if(funs(sum(.) >= 100), 
#            funs(paste(.,"+",sep=""))) %>% head(n=3)
# mtcars %>% transmute_at(vars(starts_with('d')), exp) %>% head(n=3)

# %%
# Ref : https://towardsdatascience.com/python-pandas-vs-r-dplyr-5b5081945ccb
# To add
#   renaming axis
#   
df2.rename(columns = {'hp':'horse power', 
                      'cyl':'cylinder(2/4/6)',
                      'qsec':3.14159})
df2.rename({'hp':'horse power', 
                      'cyl':'cylinder(2/4/6)',
                      'qsec':3.14159}, axis=1)
df2.rename(lambda x: x.upper(), axis=1)                     
df2.rename(len, axis=1) # 입력은 str?
def renamer(x):
  if len(x) < 4:
    return x.upper()
  else:
    return x
    # return None  # name will be NaN
df2.rename(renamer, axis=1)
df2.rename(columns = renamer)

# %%
# distinct values?
import pandas as pd
df2.apply(lambda x: x.unique(), axis=0)
df2.apply(lambda x: pd.Series(x.unique()), axis=0)

# %%
df.value_counts('cyl')
df.groupby('cyl').size()

# %%
# Delete Column
df.drop("mpg", axis=1, inplace=True)
'mpg' in df.columns
'hp' in df.columns

# %%
# Reordering columns
df.reindex(df.columns.sort_values(), axis=1).head()

# %%

# %%
