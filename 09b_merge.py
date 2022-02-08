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
import numpy as np
import pandas as pd

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

# %% [markdown]
# 둘 이상의 데이터프레임을 합치는 것을 보통 join 또는 merge(병합?)이라고 한다. 파이썬의 함수는 크게 `pd.concat()`, `pd.merge()` 그리고 `.join()` 메소드로 나눠볼 수 있다.

# %% [markdown]
# ### `pd.concat()`

# %% [markdown]
# 먼저 어떤 조건없이 둘 이상의 데이터 프레임을 합치고 싶을 때가 있다. 예를 들어 `dfCustomer.iloc[:3]`과 `dfPurchase.iloc[:3]`, 그리고 `dfProduct.iloc[:3]`을 가로로 합치고자 한다면 `pd.concat([ ], axis=1, ignore_index=True)`를 한다. 여기서 `axis=1`은 가로로 합친다는 의미이고, `ignore_index = True`는 인덱스 또는 컬럼은 무시한다는 의미이다. concat은 **concat**enate의 약자이다.

# %%
dfA = dfCustomer.iloc[:3]
dfB = dfPurchase.iloc[:3]
dfC = dfProduct.iloc[:3]

# %%
pd.concat([dfA, dfB, dfC], axis=1, ignore_index = True)

# %% [markdown]
# 세로로 합친다면 다소 번거로운데 다음과 같이 할 수 있다.

# %%
dfA = dfCustomer.iloc[:, :2]
dfB = dfPurchase.iloc[:, :2]
dfC = dfProduct.iloc[:, :2]

# %%
pd.DataFrame(np.concatenate([dfA.values, dfB.values, dfC.values], axis=0))

# %% [markdown]
# 왜 이렇게 번거로운가? 우선 `pd.concat()`의 경우 데이터 프레임을 합칠 때 데이터 프레임의 인덱스와 컬럼을 맞춘다.[^pdconcat] 다음을 보자.
#
# [^pdconcat]: 사실 대부분의 데이터프레임 함수는 별다른 얘기가 없다면 인덱스와 컬럼을 맞춘다.

# %%
pd.concat([dfA, dfB], axis=0)

# %% [markdown]
# `dfA`와 `dfB`의 열이름을 고려하여 데이터프레임이 합쳐졌다. `axis=0`의 경우도 마찬가지이다. 그래서 위에서 `ignore_index=True`를 한 것이다. 하지만 `axis=0`일 때 필요한 `ignore_columns=`는 없기 때문에 다른 방법을 강구해야 한다.

# %% [markdown]
# `dfA.values`와 `dfB.values`는 데이터프레임의 모든 값을 넘파이 배열로 담고 있다. 넘파이 배열에는 인덱스와 열이름이 없다.

# %%
dfA.values

# %% [markdown]
# 따라서 `np.concatenate()`(넘파이 배열을 합치는 함수)를 활용하여 넘파이 배열을 합친 후, 데이터프레임을 만들어 준 것이다. 

# %% [markdown]
# * 문제 : `dfCustomer`와 `dfPurchase`를 합쳐서 각 행에서 `id`, `name`, `addr`, `product` 정보를 얻을 수 있게 해보자(각 행을 통해 이름이 `name`이고 아이디가 `id`이며 주소가 `addr`인 사람이 상품 `product` 구매했음을 알 수 있다). 이때 한 사람은 `name`으로 유일하게 결정된다.

# %% [markdown]
# * 첫 번째 시도

# %%
pd.concat([dfCustomer.set_index('name'), dfPurchase.set_index('name')],axis=1)

# %% [markdown]
# `dfPurchase.set_index('name')`에서 `InvalidIndexError`가 발생했다. `dtype`이 `object`인 열을 인덱스로 만들 경우 값이 중복될 수 없다. 그렇다고 방법이 없는 것은 아니다.

# %%
dfPurchase.assign(name = dfPurchase['name'].astype('category')).set_index('name')

# %% [markdown]
# * 두 번째 시도

# %%
dfCustomer

# %%
dfA = dfCustomer.set_index('name')
dfA

# %%
dfB = dfPurchase.assign(name = dfPurchase['name'].astype('category')).set_index('name')
dfB

# %%
pd.concat([dfA, dfB], axis=1)

# %%
pd.concat([dfCustomer.set_index('name'), dfPurchase.assign(name = dfPurchase['name'].astype('category')).set_index('name')],axis=1)

# %% [markdown]
# 하지만! `pd.concat([,,,], axis=1)`은 인덱스를 기준으로 둘 이상의 데이터프레임을 합치지만 인덱스는 중복이 있을 수 없다!

# %% [markdown]
# 그 밖에도 `pd.concat()`은 인덱스 또는 컬럼이 다수준일 때 각 수준을 이름을 고려하지 않는다.

# %% [markdown]
# ### `pd.merge()`

# %% [markdown]
# `pd.concat()`의 한계는 분명하다. 인덱스는 항상 중복이 없어야 한다. 하지만 위에서 봤듯이 `dfPurchase`에는 같은 사람이 여러 번 구매할 수도 있다. 만약 `dfCustomer`와 `dfPurchase`를 합치려고 한다면 어떻게 해야 하는가?

# %% [markdown]
# 이렇게 첫 번째 데이터프레임의 한 행이 두 번째 데이터프레임의 여러 행과 대응하여 합치는 방법을 강구해야 한다(이런 관계에서 데이터 프레임을 합치는 것을 "1-n 병합"이라고도 한다).

# %% [markdown]
# `pd.merge()`는 `pd.concat([,], axis=1)`의 "1:1 병합" 뿐 아니라 "1:n 병합", "n:1 병합", 그리고 "n:n 병합"까지도 할 수 있는 함수이다. 단지 `pd.concat()`은 여러 데이터프레임을 한꺼번에 합칠 수 있지만, `pd.merge()`는 두 데이터 프레임을 합친다.

# %% [markdown]
# 먼저 `pd.concat([dfA, dfB], axis=1)`은 `pd.merge(dfA, dfB, left_index = True, right_index = True)`로 쓸 수 있다.

# %%
dfA = dfCustomer.iloc[:3].set_index('name')
dfB = dfPurchase.iloc[:2].set_index('name')

# %%
dfA

# %%
dfB

# %%
pd.concat([dfA, dfB], axis=1)

# %%
pd.merge(dfA, dfB, left_index = True, right_index = True)

# %% [markdown]
# `pd.merge()`는 기본적으로 공통된 열을 기준으로 합친다. 보통 인덱스는 아이디처럼 유일성이 보장되는 경우가 많지 않은가? 하지만 열은 꼭 그렇지 않다. `dfPurchase`와 같이 구매이력에서 한 행은 구매이며, 어떤 사람이 여러 번 구매를 할 수 있다. 이런 경우 보통은 구매 번호를 인덱스로 삼기 마련이다(구매 번호는 구매를 유일하게 나타낸다).

# %% [markdown]
# `dfCustomer`와 `dfPurchase`를 보면 공통열로 `name`이 있다. `pd.merge()`는 `name`을 기준으로 n:n 병합을 실시한다.

# %%
pd.merge(dfCustomer, dfPurchase)

# %% [markdown]
# 하지만 자료는 여러 가지 다양한 방식으로 존재하기 마련이고, 처음부터 이렇게 `pd.merge()`만 써서 성공적으로 병합을 할 수 있는 경우가 많지 않다.

# %% [markdown]
# 몇 가지 경우를 생각해보자.
#
# 1. 공통열이 인덱스에 존재할 때
# 2. 공통열의 열이름이 다를 때

# %% [markdown]
# #### 공통열이 인덱스에 존재할 때

# %% [markdown]
# 만약 첫 번째 데이터프레임의 공통열이 인덱스에 존재한다면 `left_index = True`를 한다. 만약 두 번째 데이터프레임의 공통열이 인덱스에 존재한다면 `right_index = True`를 한다.

# %% [markdown]
# #### 공통열의 일부만을 고려할 때

# %% [markdown]
# 공통열의 갯수가 하나 이상일 경우에는 모든 공통열을 고려하여 데이터프레임을 병합한다. 만약 일부만을 고려하고자 한다면 `on=`에 고려하고자 하는 열이름을 나열한다.

# %%
dfPurchase2 = pdDataFrame(id=c(10,11),
                          name = c('김희선', '박보검'),
                          product = c('바지', '샴푸'))

# %% [markdown]
# `dfPurchase2`는 `dfPurchase`와 달리 `dfCustomer`와 공통열이 둘이다. 하지만 `pd.merge()`를 해보면 다음과 같다.

# %%
pd.merge(dfCustomer, dfPurchase2)

# %% [markdown]
# 왜냐하면 공통열이 모두 대응하는 경우가 없기 때문이다. 이렇게 공통열이 존재하지 않는 경우는 어떻게 해야 하나?

# %% [markdown]
# 그 원인을 밝혀야 한다. 그리고 우리가 원하는 결과를 생각해야 한다.

# %% [markdown]
# 첫 번째로 가능한 원인은 `dfPurchase2`의 `id`가 잘못된 경우이다. 아마도 여기서 `id`는 구매번호를 의미할 수도 있다. 그렇다면 `id`는 병합시 고려하지 않아야 한다. 방법은 다음과 같다.

# %%
pd.merge(dfCustomer, dfPurchase2, on=['name'])

# %% [markdown]
# `on=['name']`은 명시적으로 두 데이터프레임을 병합할 때 `name` 열만 고려하라고 알려준다. 결과를 보면 열이름이 같은 `id`를 구분하기 위해 `id_x`(첫 번째 데이터 프레임의 `id`)와 `id_y`(두 번째 데이터 프레임의 `id`)로 열이름이 변형되었다.

# %% [markdown]
# 두 번째 가능한 원인은 `dfPurchase2`의 `id`와 `dfCustomer`의 `id`는 같은 의미를 가지며, 자료 손실 등의 이유 대응되는 자료가 없는 경우이다. 

# %% [markdown]
# 그런데 병합을 하려는 이유가 모든 구매에 대해 주소(`addr`)과 같은 구매자의 정보를 알아보는 것이라고 한다면 `pd.merge()`의 결과로 빈 데이터프레임이 나타나는 것은 바람직하지 않다. 자료 손실 등으로 구매자 정보가 없더라도 구매자 정보가 없다는 것을 나타낼 필요가 있다.

# %%
pd.merge(dfCustomer, dfPurchase2)

# %%
pd.merge(dfCustomer, dfPurchase2, how='right')

# %% [markdown]
# `how='right'`은 대응하는 데이터가 없더라도 두 번째 데이터프레임의 모든 행을 남긴다. 다음은 `how=`의 의미이다.

# %% [markdown]
# | `how=` | 의미    |
# |:-------|:-------|
# |`"outer"`| 두 데이터프레임의 모든 행을 남긴다
# |`"inner"` | 두 데이터프레임의 공통 행을 남긴다
# |`"left"`  | 첫 번째 데이터프레임의 모든 행을 남긴다
# |`"right"` | 두 번째 데이터프레임의 모든 행을 남긴다
# |`"cross"` | (`help(pd.merge)`로 확인하자)

# %% [markdown]
# ### `.join()` 메소드

# %% [markdown]
# 앞에서 `pd.concat([dfCustomer.set_index('name'), dfPurchase.assign(name = dfPurchase['name'].astype('category')).set_index('name')],axis=1)`는 오류를 발생시켰다.

# %% [markdown]
# `pd.concat()`은 중복된 인덱스를 다룰 수 없기 때문이다.
#
#

# %% [markdown]
# `.join()` 메소드는 `pd.merge()`와 동일하다. 한 가지 다른 점은 공통열이 인덱스에 있다는 것을 전제하고 있다.

# %%
dfA = dfCustomer.assign(name = dfPurchase['name'].astype('category')).set_index('name')
dfB = dfPurchase.assign(name = dfPurchase['name'].astype('category')).set_index('name')

# %%
dfA.join(dfB)
