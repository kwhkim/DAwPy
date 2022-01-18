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

# %% [markdown]
# ### 벡터화 연산

# %%
a1 ** 2  # dtype=int8  # cf. [x**2 for x in lst]
a1 * a4  # dtype=int64

# %% [markdown]
# ## 판다스 시리즈

# %% [markdown]
# ### 넘파이 배열 기반

# %%
import numpy as np
import pandas as pd
s1 = pd.Series([1,2,3,4], index = ['b', 'c', 'd', 'e'], dtype='int8')
s2 = pd.Series([1,2,3,4], index = ['b', 'c', 'd', 'e'], dtype='int16')
s3 = pd.Series([1,2,3,4], index = ['b', 'c', 'd', 'e'], dtype='int32')
s4 = pd.Series([1,2,3,4], index = ['b', 'c', 'd', 'e'], dtype='int64')

s1.index, s1.values

# %% [markdown]
# ### 인덱스 사용 가능

# %%
s1['b':'d'] # last point inclusive
s1[['b', 'c', 'e']]

# %% [markdown]
# #### 모호성 해소

# %%
s1.iloc[0]
s1.iloc[0:2] # last point exclusive
s1.iloc[[0,1,3]]

# %%
s1.loc['b']
s1.loc['b':'d'] # last point inclusive
s1.loc[['b', 'c', 'e']]

# %% [markdown]
# ### 시간대 포함 날짜시간형, 범주형 지원

# %%
from mypack.utils import ordered

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

# %% [markdown]
# ### 기타 : `.loc[]` 또는 `.iloc[]`이 없는 경우

# %%
df1[['s3', 's5']]

# %%
df1['s3':'s5']

# %%
df1['b':'e']

# %% [markdown]
# ### 행/열 동시에 참조하기

# %%
df1.loc['b', df1.columns[1]] # df1.loc['b'].iloc[:,1]
df1.loc['b', df1.columns.str.endswith('5')]

# %%
df1.loc['b':'d', df1.columns[1:3]] # df1.loc['b'].iloc[:,1]
df1.loc['b':'d', df1.columns.str.contains('[35]')]

# %%
df1.loc[['b', 'e', 'f'], df1.columns[[0,1,3]]] # df1.loc['b'].iloc[:,1]
df1.loc[['b', 'e', 'f'], df1.columns.str.contains('[35]')]

# %%

# %% [markdown]
# ## Add & Delete

# %% [markdown]
# ### 넘파이 행렬

# %%
import numpy as np
import pandas as pd

# %%
a = np.array([1,2,3,4,5], dtype='int8')

# %%
dir

# %%
a.append(np.array([6,7,8]))

# %%
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
s2.drop(['b', 'c'])

# %%
# np.delete -> pd.drop
# np.concatenate -> pd.concat


# %%

# %% [markdown]
# ## Slice 비교

# %%
lst = list(range(10))
lst[2], lst[:], lst[7:len(lst)+3], lst[6:6]

# %%
import numpy as np
A = np.arange(10, dtype='int32')
A[2], A[:], A[7:len(A)+3], A[6:6], A[[2,3,7]] # A[[2,3,7,len(A)+3]] -> IndexError

# %%
import numpy as np
import pandas as pd
s = pd.Series(list(range(10)), index = list('abcdefghij'))
s[2], s[:], s[7:len(s)+3], s[6:6], s[[2,3,7]]

# %%
s['b'], s[:], s['g':], s['g':'g'], s[['b', 'c', 'h']]

# %%
