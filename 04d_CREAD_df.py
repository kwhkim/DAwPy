# -*- coding: utf-8 -*-
# ## 판다스 데이터 프레임

# from rtopython2/04_e_CREAD_df.py

import numpy as np
import pandas as pd

x = pd.Series([1,2,3], index = [0,1,2])
y = pd.Series([2,3,4], index = [1,2,3])

# ### 생성

df = pd.DataFrame({'x':[1,2,3,np.nan], 
                   'y':[np.nan,1,2,3], 
                   'z':[0,np.nan,1,2],
                   'w':[0,1,1,0]})
df

pd.DataFrame({'x':x, 'y':y})


pd.concat([x,y], axis=1) # 비교 pd.concat([x,y], axis=0)


df2 = df

df2 = df.copy()

# ### 조회

# #### 시리즈
#
# 위에서 봤듯이 데이터 프레임은 여러 판다스 시리즈가 합쳐진 것으로 생각할 수 있다. 
# 데이터 프레임에서 시리즈 하나를 조회하려면 `df['colname']` 또는 `df.colname`으로 쓸 수 있다. 
# 이 둘은 완전히 같지 않다. 특히 `df.colname`의 경우 컬럼 이름이 데이터 프레임의 속성과 일치하는 경우에는 사용할 수 없다.

df = pd.DataFrame({'x0':x,
                   'y0':y,
                   'x1':x**2,
                   'iloc':4-y})

df

df['x0'] # 2,2,3
df.x0    # 2,2,3
df['iloc']  # 1,2,1 
df.iloc     # pandas method

# 앞에서 살펴본 데이터 구조와 동일하게 순번, 인덱스, 참/거짓을 사용할 수 있다. 데이터 프레임이 2차원 구조이기 때문에 하나의 값은 2차원의 위치로 결정된다.
#
# `df.iloc[x,y]` 또는 `df.loc[x,y]`
#
# 만약 `,y`를 생략하면 `df.iloc[x,:]`, `df.loc[x,:]`와 같은 의미이다.

# #### 인덱스

df

# +
# df.loc[1,'y']
# > KeyError
# -

# `:`는 전체를 의미한다. 리스트에서 슬라이스를 사용한 `x[:]`의 의미와 동일하다.

df.loc[1,:]

df.loc[1:3, 'x0':'x1']

df.loc[[2,0], ['x0', 'iloc']]


# #### 순번

df.iloc[1,2]
df.iloc[0:2, 1:2]
df.iloc[[0,3],[0,2]]

# #### 참/거짓

df.loc[df.x0 > 2, df.loc[2,:]>1]

df.loc[df.x0 > 2]

# #### 브라켓 없이 사용할 경우에는 2차원 구조를 참조할 수 없다

df

# +
# df[[0,2], ['y0', 'iloc']] # MultiIndex을 의미한다.
# > TypeError
# -

# `.iloc[]` 또는 `.loc[]` 없이 바로 `df[]`로 사용하면 컬럼 이름을 쓰거나, 참/거짓을 사용한다.

df[['y0', 'iloc']]  # column

df[df['iloc'] == 1] # 참/거짓

# +
# df[[1,2]] # 숫자로 넣어도 column에서 찾는다.
# > KeyError
# -

# ### 수정
#
# 수정 방법은 참조할 대상과 대체할 값을 등호의 좌,우에 배치한다.

df = pd.DataFrame({'x0':x,
                   'y0':y,
                   'x1':x**2,
                   'iloc':4-y})
df

df['x0'] = [1,2,3,4]
df

df[df['x0'] == 3] = [0,0,1,2]
df

df.iloc[1,[0,3]] = [-1,-1]
df

# 문제가 되는 경우는 `.loc`, `.iloc`을 섞어 써야 하는 경우이다

# 참거짓/순서
#df.loc[df['x0']<=0].iloc[[1,2]] = 0
# > A value is trying to be set on a copy of a slice from a DataFrame
# > See the caveats in the documentation: 
# > https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
df.loc[df['x0']<=0, df.columns.isin([1,2])] = 0
df

# 참거짓/인덱스
df.loc[df['x0']<=0, ['x0', 'y0']] = [-10, -11]
df

# 순서/참거짓
df.loc[df.index[[1,2]], df.iloc[1,:] >0] = 100
df


df.loc[df.index[[1,2]], ['x0', 'y0']]

# 순서/인덱스(컬럼)
df.loc[df.index[[1,2]], ['x0', 'y0']] = [[1,2], [3,4]]
df

df.index[[0,-1]]

# * 참고
#     - `df.index[[0,-1]]` : 0-번째와 마지막 인덱스
#     - `df.index.isin(['a', 'b'])` : 인덱스가 'a' 또는 'b'인 위치를 참/거짓으로 나타냄
#     

# ### 추가
#
# 인덱스로는 가능하지만, 순번, 참/거짓으로는 불가능하다.

df = pd.DataFrame({'x0':x,
                   'y0':y,
                   'x1':x**2,
                   'iloc':4-y})
df

df['inf'] = [100,99,98,97]
df

df[['inf2', 'inf3']] = [[1,2],
                        [2,3],
                        [3,4],
                        [4,5]] # 2차원 배열처럼
df

#df.loc[3,:] = [0,0,0,1,2,3,4]
df.loc[3] = [0,0,0,1,2,3,4]
df

# 이건 안 됨?

# +
# df.loc[[4,5]] = [[0,0,0,1,2,3,4],
#                  [1,1,1,4,4,4,4]] 
# > KeyError
# -

df.append([[0,0,0,1,2,3,4],
           [1,1,1,4,4,4,4]] )

df.append(
    pd.DataFrame(
        [[0,0,0,1,2,3,4],
         [1,1,1,4,4,4,4]],
    columns = ['x0', 'y0', 'x1', 'iloc', 'inf', 'inf2', 'inf3']))

df.append(pd.DataFrame(
            {'x0':[10,0], 
             'y0':[11,0], 
             'x1':[12,0], 
             'iloc':[13,0], 
             'inf':[14,0], 
             'inf2':[15,0], 
             'inf3':[16,0]}), ignore_index=True)

# #### 중간에 삽입

# column 삽입 : `df[colname]=`

df = pd.DataFrame({'x0':x,
                   'y0':y,
                   'x1':x**2,
                   'iloc':4-y})
df

df.insert(2,'xx', [0,0,0,0]) # 2번째 컬럼 앞에, 'x'란 컬럼으로 inplace

# 새로운 데이터 프레임 생성
pd.concat([df.iloc[:,:2], pd.DataFrame({'xx':[0,0,0,0]}), df.iloc[:,2:]], axis=1)

# row 삽입

df

pd.concat([df.iloc[:2], df.iloc[2:]], axis=0)

x = pd.DataFrame(
            {'x0':[10,0], 
             'y0':[11,0], 
             'x1':[12,0], 
             'iloc':[13,0], 
             'inf':[14,0], 
             'inf2':[15,0], 
             'inf3':[16,0]})
x

pd.concat([df.iloc[:2], x, df.iloc[2:]], axis=0)

# inplace로 할 수 있는 방법이 없을까?

# ### Delete

x = pd.Series([1,2,3], index = [0,1,2])
y = pd.Series([2,3,4], index = [1,2,3])

df = pd.DataFrame({'x0':x,
                   'y0':y,
                   'x1':x**2,
                   'iloc':4-y})
df

del df['x1']

# +
# del df[['inf', 'inf2']]  
# > TypeError
# -

df.drop(['x0', 'y0'], axis=1)  # `inplace = True` is possible

# +
# del df.loc[3]
# > AttributeError
# -

df.drop([2,3], axis=0)


