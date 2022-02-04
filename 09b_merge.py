# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: rtopython3-pip
#     language: python
#     name: rtopython3-pip
# ---

# %% [markdown]
# ## 여러데이터프레임 합치기

# %% [raw] magic_args="language=\"R\""
# #install.packagesc("dplyr")
# library(dplyr)
# options(stringsAsFactors=F)
# dfCustomer <- data.frame(
#   id = c(1,2,3,4,5),
#   name = c("김희선","박보검","설현","김수현","전지현"),
#  addr = c("서울시","부산시","인천시","강릉시","목포시")
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

# %% [markdown]
# 먼저 데이터는 다음과 같다.

# %%
from mypack.utils import c, pdDataFrame


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

# %%
dfCustomer

# %%
dfPurchase

# %%
dfProduct

# %% [raw] magic_args="language=\"R\""
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

# %% [markdown]
# 데이터 프레임을 합칠 때에는 `pd.concat()`을 쓴다.

# %%
df1 = dfCustomer.iloc[[0,1+1],:] # 0-번째부터 1-번째
df2 = dfCustomer.iloc[[2,3+1],:] # 2-번째부터 3-번째
df3 = dfCustomer.iloc[[4],:]     # 4-번째 .iloc[4,:]과 결과를 비교해보자.

import pandas as pd
pd.concat([df1,df2,df3], axis=0) # 세로 방향(axis=0)으로 데이터프레임을 합친다.

# %% [markdown]
# 이때 데이터 프레임의 인덱스나 열이름이 중요하다. 다음을 보자.

# %%
pd.concat([df1,dfProduct], axis=0)

# %%
pd.concat([df1,dfProduct], axis=1)

# %% [markdown]
# 보통 데이터프레임을 합칠 때에는 어떤 변수를 기준으로 한다. 위의 `pd.concat()` 결과를 보자. `pd.concat( , axis=1)`에서 데이터프레임을 데이터 프레임의 인덱스를 기준으로 데이터프레임을 합친다.

# %% [markdown]
# `pd.merge()` 함수는 기준을 명확하게 정한다. 만약 아무 설정을 하지 않는다면 `pd.merge()`는 공통의 열을 기준으로 합친다.

# %%
pd.merge(df1, dfProduct)

# %% [markdown]
# 두 데이터 프레임의 공통열이 없다. 다시 `df1`과 `dfPurchase`를 합쳐보자.

# %%
pd.merge(df1, dfPurchase) 

# %% [markdown]
# 공통된 열이름 `name`을 기준으로 두 데이터 프레임을 합친다.

# %% [markdown]
# 위의 `pd.concat()` 결과와 비교해보자. 데이터 프레임의 한 행이 하나의 사례를 나타낸다고 하자. 
# 두 데이터 프레임 A와 B를 합칠 때, 프레임 A의 한 행(사례)와 프레임 B의 한 행(사례)를 합치게 된다. 그 결과 프레임 A의 한 행에 프레임 B의 열이 추가된다. 그리고 이렇게 두 행을 합치는 기준은 어떤 열이다. 프레임 A의 열과 프레임 B의 열이 같은 경우 합치게 되는 것이다.
#
# 그런데 프레임 A의 열과 합칠 수 있는 프레임 B의 열이 존재하지 않는 경우도 생길 수 있다. 예를 들어 위의 예에서 `df1`에는 `name`이 `설현`인 행이 있지만, `dfPurchase`에는 `name`이 `설현`인 행이 존재하지 않는 경우이다. 이런 경우에 어떻게 할 것인가는 `how=` 인자가 결정한다. 
#
# * `how = 'inner'` : 두 데이터프레임에 모두 존재하는 사례만 결과에 포함시킨다.
# * `how = 'outer'` : 두 데이터프레임에서 한쪽에만 존재하는 사례도 모두 포함시킨다.
# * `how = 'left'`: 왼쪽 데이터프레임의 모든 사례를 남긴다. 왼쪽 데이터프레임에 존재하지 않는 사례는 포함시키지 않는다.
# * `how = 'right'`: 오른쪽 데이터프레임의 모든 사례를 남긴다. 왼쪽 데이터프레임에 존재하지 않는 사례는 포함시키지 않는다.

# %%
pd.merge(df1, dfPurchase, how='left') # how의 기본값은 'inner'이다.

# %%
pd.merge(df1, dfPurchase, how='outer')

# %% [markdown]
# 위의 결과는 다소 명확하다. 그런데 `df1`의 `name`에 중복되는 값이 있다면 어떻게 될까?

# %%
df1

# %%
df2 = pd.concat([df1, df1.iloc[[0]]], axis=0).reset_index(drop=True)
df2

# %%
pd.merge(df2, dfPurchase, how='inner')

# %% [markdown]
# 마지막으로 `how='cross'`의 경우 왼쪽 데이터프레임의 `name`과 오른쪽 데이터 프레임의 `name`을 별개로 취급하여 결과가 다음과 같다.

# %%
pd.merge(df1, dfPurchase, how='cross')

# %% [markdown]
# 두 데이터프레임을 합칠 때 기준을 데이터 프레임의 인덱스로 할 수도 있다. 왼쪽 데이터프레임의 인덱스를 사용하려면 `left_index=True`, 오른쪽 데이터프레임의 인덱스를 사용하려면 `right_index = True`로 설정한다.

# %%
df1b = df1.set_index('name')

# %% [markdown]
# 만약 `left_index=True`로 설정하면 `right_on='name'`으로 설정해야 한다. 왜냐하면 기준열이 `'name'`인 것은 오른쪽 데이터프레임에만 해당하기 때문이다.

# %%
pd.merge(df1b, dfPurchase, left_index = True, right_on='name') 

# %% [markdown]
# ### `pd.merge()` 또는 `df.join()`
#
# 두 데이터프레임을 합치는 다른 방법으로는 데이터프레임의 `.join()` 메쏘드를 활용하는 것이다. 결과는 `pd.merge()`와 동일하다. 두 데이터프레임 `df1`, `df2`에 대해 `df1.join(df2)`는 기본적으로 두 데이터프레임를 인덱스를 기준으로 합친다. 

# %%
df1.join(dfProduct, how='outer')

# %% [markdown]
# `dfCustomer`, `dfPurchase`, `dfProduct`의 경우 인덱스는 순번 이외에 큰 의미가 없다. `name`을 기준으로 합치려면 일단 합치려는 데이터프레임의 `name` 열을 인덱스로 바꿔줘야 한다.

# %%
df1

# %%

# %% [markdown]
# `df1`과 `dfPurchase`를 합칠 때, `dfPurchase`는 기본적으로 인덱스를 기준으로 하고, `df1`의 기준을 특정열로 지정한다고자 `on='name'`으로 `df1`의 기준열을 지정한다.

# %%
df1.join(dfPurchase.set_index('name'), on='name',how='outer')

# %% [markdown]
# 왼쪽 데이터프레임(`df1`)과 오른쪽 데이터프레임(`dfPurchase`)를 합칠 때, 오른쪽 데이터프레임(`dfPurchase`)는 항상 인덱스를 기준으로 하는 것이다. 

# %%

# %%
df1.join(dfPurchase[[]])

# %%
df1b

# %%
# ?df1b.join

# %%
dfProduct

# %%
dfCustomer

# %%
df1.join(dfProduct.reset_index('name'), on='name')

# %%
df1b.join(dfProduct, on='name')

# %%
df

# %% [markdown]
# 사실 `df1`과 `dfProduct`의 인덱스는 큰 의미가 없다. `dfPurchase`와 `df1`의 공통열은 `name`이다. 이를 기준으로 데이터프레임을 합쳐보자.

# %%
df1.join(dfProduct, how='outer', on='name')

# %% [markdown]
# 문제는 `df1.join()`의 경우 기본적으로 `df1`의 인덱스를 활용한다.

# %%
df1.set_index('name').join(dfCustomer, on='name')

# %%
dfCustomer

# %%
df1.join(dfCustomer.set_index('name'), on='name', how='outer', lsuffix='_')

# %%
# ?pd.merge

# %%
df1.set_index('name').join(dfCustomer, on='name', how='outer', lsuffix='_')

# %%
# ?pd.join

# %%
# ?pd.concat

# %%

# %%
# ?df1.join

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
# pd.concat([DF1, DF2, DF3]) # 인덱스를 기준으로 


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
#
# ## 세로형/가로형 변환

# %%


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
