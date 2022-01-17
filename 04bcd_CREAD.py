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
# ## 1차원 데이터 구조 : list vs. numpy array vs. pandas Series

# %% [markdown]
# 리스트는 파이썬의 **내장** 클래스이다(`__builtins__.list`). 거의 모든 파이썬 소스 코드는 리스트를 포함한다. 중요하다! 

# %% [markdown]
# **넘파이 배열**(여기서는 1차원 배열으로 한정한다)은 그 데이터 구조에서 리스트와 동일하다고 볼 수 있다. 여러 자료 값을 저장한다. 몇 가지 차이점은 다음과 같다.
#
# * 수많은 데이터타입(dtype)의 존재 -> 좀더 효율적인 데이터 저장
# * 자료를 실제로 저장
# * 순번 또는 참거짓을 사용한 Fancy-indexing -> 데이터 다루기 편리함 
# * 벡터화된 연산 -> 빠른 연산

# %% [markdown]
# **판다스 시리즈**는 넘파이 배열을 기반으로 데이터 분석에 필요한 기능을 추가했다. 대표적인 추가 사항은 다음과 같다.
#
# * 인덱스 지원 -> 순번, 참거짓 뿐 아니라 인덱스를 통해 원소에 접근할 수 있다.
# * 날짜시간형에 시간대를 저장할 수 있고, 범주형(명목형, 순위형) 데이터를 지원한다.
# * 데이터 분석에 필요한 다양한 함수를 지원한다.

# %% [markdown]
# **판다스 데이터프레임**은 판다스 시리즈를 여럿 모아놓은 데이터 구조이다. 행과 열을 기준으로 데이터를 선별하는 방법을 제공한다.

# %% [markdown]
# ## 넘파이 배열

# %% [markdown]
# ### 지원하는 데이터타입(dtype)

# %%
import numpy as np
a1 = np.array([1,2,3,4], dtype='int8')
a2 = np.array([1,2,3,4], dtype='int16')
a3 = np.array([1,2,3,4], dtype='int32')
a4 = np.array([1,2,3,4], dtype='int64')

# 데이터를 차지하는 메모리 공간 = .size(총 원소 갯수) * .itemsize(한 원소의 저장 공간)
a1.size * a1.itemsize, a2.size * a2.itemsize, a3.size * a3.itemsize, a4.size *a4.itemsize

# %% [markdown]
# ### 데이터를 참조하거나 활용하는 다양한 방법

# %%
b1 = a1
b2 = a1.view()
b3 = a1.copy()
b4 = a1[1:3] # view
b5 = a1.view(dtype='int16')
b6 = a1[[0,1,3]] # fancy-indexing -> copy

# %%
b5 = a1.view(dtype='>i2') # 좀더 구체적으로 Big Endian(>), integer(i), 2 bytes(2)

# %%
b5

# %%
# Endianness를 확인하는 방법

# %%
np.info(b5) # 출력 결과에서 byteorder를 확인한다(big, little)

# %%
b5.dtype.byteorder # >(big), <(little)

# %%
b5 = a1.view(dtype='<i2') # Little Endian, integer, 2 bytes

# %%
b5

# %%
# 513, 1027의 이진수 표기
bin(513), bin(1027)

# %%
# 513, 1027의 이진수 표기를 출력하는 다른 방법(16자리 수)
print(f'{513:016b}')
print(f'{1027:016b}')

# %%

# %%
# 2바이트 수 0b0000001000000001를 저장하는 두 가지 방법
# Big Endian
0b00000010, 0b00000001
# Little Endian
0b00000001, 0b00000010 

# %%

# %%
0b00000010, 0b00000001, 0b00000100, 0b00000011

# %% [markdown]
# ### 벡터화 연산

# %%
a1 ** 2  # dtype=int8  # cf. [x**2 for x in lst]
a1 * a4  # dtype=int64

# %% [markdown]
# ## 판다스 시리즈

# %% [markdown]
# ### 넘파이 배열 기반

# %% [markdown]
# 넘파이 배열을 기반으로 하여 넘파이 배열에서 가능했던 순번을 이용하는 참조 방법(원소 하나, 슬라이스, Fancy-Indexing)이 가능하다. 데이터는 넘파이 배열로 저장되면 `.values`를 통해 확인할 수 있다. 그리고 각 원소를 가리킬 수 있는 (딕의 키에 해당하는) 인덱스를 포함한다(`.index`).

# %%
import numpy as np
import pandas as pd
s1 = pd.Series([1,2,3,4], index = ['b', 'c', 'd', 'e'], dtype='int8')
s2 = pd.Series([1,2,3,4], index = ['b', 'c', 'd', 'e'], dtype='int16')
s3 = pd.Series([1,2,3,4], index = ['b', 'c', 'd', 'e'], dtype='int32')
s4 = pd.Series([1,2,3,4], index = ['b', 'c', 'd', 'e'], dtype='int64')

s1.index, s1.values

# %% [markdown]
# 다른 `dtype`에 대해 연습해보기. 

# %% [markdown]
# ### 인덱스 사용 가능

# %%
s1['b':'d'] # last point inclusive
s1[['b', 'c', 'e']]

# %%
s5 = pd.Series([1,2,3,4], 
               index = [1, 2, 'd', 'e'], dtype='int64')

# %% [markdown]
# 판다스 시리즈에서는 `.iloc[]`과 `.loc[]`을 지원한다. `.iloc[]`은 명시적으로 순번을 사용하고, `.loc[]`은 명시적으로 인덱스를 사용한다.

# %% [markdown]
# #### 모호성 해소
#
# 왜 `.iloc[]` 또는 `.loc[]`이 필요한가? 판다스 시리즈의 인덱스는 정수형도 가능하다. 만약 정수형이 포함된 인덱스가 존재하는 시리즈의 경우 `.iloc[]`없이 바로 `[]`을 쓰면 순번을 의미하는지 아니면 인덱스를 의미하는지 헷갈릴 수 있다. `[]`안에 정수형을 쓸 경우 인덱스에 정수형이 하나라도 존재하면 인덱스로 취급하고, 그렇지 않은 경우에만 순번으로 취급한다.

# %%
s1.iloc[0]
s1.iloc[0:2] # last point exclusive
s1.iloc[[0,1,3]]

# %%
s1.loc['b']
s1.loc['b':'d'] # last point inclusive
s1.loc[['b', 'c', 'e']]

# %%
s1[0] # 0번째 원소

# %%
s1.index = ['b', 'c', 'd', 5]  # 인덱스 수정

# %%
s1[0] # 인덱스에 정수형 값이 하나라도 포함되면 -> 인덱스 0을 찾는다

# %%
s1.index = ['b', 'c', 'd', 'e'] 

# %% [markdown]
# ### 시간대 포함 날짜시간형, 범주형 지원

# %%
from mypack.utils import ordered
# 만약 ModuleNotFound가 발생한다면 conda install dateparser 등을 활용하여 
# 존재하지 않는 패키지/모듈을 설치한다

s5 = pd.Series(['2022-03-01', '2022-05-05', '2022-05-08', '2022-06-06'], 
               index = ['b', 'c', 'd', 'e'], dtype='datetime64[ns]')
s6 = pd.Series(['2022-03-01', '2022-05-05', '2022-05-08', '2022-06-06'], 
               index = ['b', 'c', 'd', 'e'], 
               dtype='datetime64[ns]').dt.tz_localize('Asia/Seoul')
s7 = pd.Series(['Left', 'Middle', 'Left', 'Right','Right', 'Right'], 
               index = ['b', 'c', 'd', 'e', 'f', 'g'], dtype='category')
s8 = pd.Series(['Left', 'Middle', 'Left', 'Right','Right', 'Right'], 
               index = ['b', 'c', 'd', 'e', 'f', 'g'], dtype= ordered(['Left', 'Middle', 'Right']))


# %%
s5.dtype, s6.dtype, s7.dtype, s8.dtype

# %%

# %% [markdown]
# ## 2차원 데이터 구조 : pandas DataFrame

# %% [markdown]
# 판다스 데이터프레임은 다양한 데이터타입(dtype)의 판다스 시리즈가 하나로 묶인 것으로 생각할 수 있다. 판다스 데이터프레임은 판다스 시리즈에서 가능한 참조방법을 행과 열 모두에 시행할 수 있다.
#

# %%
df1 = pd.DataFrame({'s1':s1,                     
                    's3':s3, 
                    's5':s5,
                    's7':s7})

# %%
df1

# %% [markdown]
# ### 행 선택하기

# %%
# 인덱스
df1.loc[['b']]  # cf. df1.loc['b']
df1.loc['b':'d']
df1.loc[['b', 'e', 'f']]
# 순번
df1.iloc[0]
df1.iloc[0:3]
df1.iloc[[0, 2, 3]]
# 참거짓
df1[df1['s3'] < 3]

# %%
df1.loc[df1['s3'] < 3]

# %%
df1.loc[['b']] # ['b']는 리스트. ['b', 'c'] 등으로 확장시킬 수 있음.
df1.loc['b']  
df1.iloc[0]
df1.iloc[[0,1,3]] # 마찬가지로 0 대신 여러 행을 담고 있는 리스트를 사용할 수 있음.
# 스칼라(예. 'b', 0)을 사용할 때와 리스트(예. ['b'], [0,1,3])을 사용할 때 결과의 type이 달라진다.

# %% [markdown]
# ### 열 선택하기

# %%
# 인덱스
df1.loc[:,['s1']]  # cf. df1.loc['b']
df1.loc[:,'s1':'s3']
df1.loc[:,['s1', 's5', 's7']]
# 순번
df1.iloc[:,0]
df1.iloc[:,0:3]
df1.iloc[:,[0, 2, 3]]
# 참거짓
df1.loc[:,df1.columns.str.endswith('5')]

# %%
df1

# %%
df1_index = df1.index.tolist()

# %%
df1_index[4] = 'c'

# %%
df1.index = df1_index 

# %%
df1

# %%
df1.at['c', 's1']

# %% [markdown]
# ### 기타 : `.loc[]` 또는 `.iloc[]`이 없는 경우

# %%
df1['s3'] # 열이름으로 찾는다.

# %%
df1[['s3', 's5']] # 열이름으로 찾는다

# %%
df1[1:4] # slice는 행순번 우선

# %%
df1['s3':'s5'] # slice : 행순번 우선, 그다음 행이름으로 찾는다
# R의 df['colname'] 꼴과
# R의 dplyr의 slice() 함수를 생각하면 쉽게 기억할 수 있을 듯 하다.

# %%
df1['b':'e']

# %%
# df1['b':'e', :], df1['b':'e', 's5'], df1['b':'e', ['s3', 's5']] 모두 불가능

# %% [markdown]
# 특히 판다스 데이터프레임은 `[]`만 썼을 때 헷갈리기 쉬우므로 순번, 인덱스, 참거짓에 따라 `.iloc[]` 또는 `.loc[]`을 사용하길 권장한다. 
#
# * 순번 : `.iloc[]`
# * 인덱스, 참거짓 : `.loc[]`
#
# 참거짓을 사용하면 인덱스와 헷갈릴 가능성이 없진 않다. 하지만 참거짓으로만 구성된 인덱스는 거의 없다. 만약 `df[df['col1']>3]`과 같이 사용할 경우에 결과는 단순히 리스트가 아니라 인덱스를 포함한 판다스 시리즈이기 때문에 혼동의 여지가 거의 없다(인덱스를 포함한 참거짓 판다스 시리즈를 `[]` 또는 `.loc[]`안에 사용할 경우 참거짓의 순서보다 인덱스-참거짓 쌍이 결과를 결정한다). 불가피한 경우를 제외하고 인덱스로 `True` 또는 `False`를 사용하지 말자.

# %%
df2 = df1.copy()

# %%
df2.index = [True,True,False,False,True,True]

# %%
df2

# %% [markdown]
# ### 행/열 동시에 참조하기

# %% [markdown]
# 만약 수정을 염두에 둔다면 `.loc[].iloc[]`과 같은 표현을 사용할 수 없다. 왜 그럴까?

# %%
df1

# %%
df1.loc['b', df1.columns[1]] # df1.loc[['b']].iloc[:,1]
df1.loc['b', df1.columns.str.endswith('5')]

# %%
df1.loc['b':'d', df1.columns[1:3]] # df1.loc['b':'d'].iloc[:,1]
df1.loc['b':'d', df1.columns.str.contains('[35]')]

# %%
df1.loc[['b', 'e', 'f'], df1.columns[[0,1,3]]] # df1.loc['b'].iloc[:,1]
df1.loc[['b', 'e', 'f'], df1.columns.str.contains('[35]')]

# %%
df1

# %%
df1.loc['b'].iloc[3] = 'Right'

# %%
df1

# %%
df1.loc['b', df1.columns == "s7"] = "Right"

# %%
df1

# %% [markdown]
# ## Add & Delete

# %% [markdown]
# ### 넘파이 행렬

# %%
a = np.array([1,2,3,4,5], dtype='int8')

# %%
np.append(a, np.array([6,7,8]))

# %%
# 참고
np.concatenate([a, np.array([6,7,8])])

# %%
np.delete(a,[1,4])

# %% [markdown]
# ### 판다스 시리즈

# %%
s = pd.Series([1,2,3,4,5], 
              index = list('bcdef'),
              dtype='int8',)

# %%
s.append(pd.Series([6,7,8]))

# %%
# 참고
pd.concat([s, pd.Series([6,7,8])])

# %%
s2.drop(['b', 'c'])

# %%
# np.append -> Series.append
# np.delete -> Series.drop
# np.concatenate -> pd.concat


# %%
