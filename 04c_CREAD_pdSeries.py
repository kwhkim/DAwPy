# -*- coding: utf-8 -*-
# %% [markdown]
# # pd.Series
# ## Create

# %% [markdown]
# 내용 직접 입력하기

# %%
import pandas as pd
s = pd.Series(['a', 'b', 'c', 'd'])
s = pd.Series([0,1,2,3,4])
s = pd.Series([-0.4, 2.5, 1.41, 2.69],
              index = ['a', 'b', 'c', 'd'])

# %% [markdown]
# 판다스 시리즈의 출력 결과

# %%
s

# %% [markdown]
# 판다스 시리즈의 두 속성(index와 values)
# - index : 값의 위치를 순번이 아니라 이름으로 결정할 수 있다.
# - values : 저장된 값

# %%
print(s.index)
print(s.values)

# %% [markdown]
# 판다스 시리즈를 만드는 다른 방법들

# %%
## 다른 판다스 시리즈의 내용
s2 = s.copy()
s3 = s.view()
s4 = s

## 다른 판다스 시리즈의 일부
s2p = s[2:4]  # copy
s3p = s[2:4].view()  # view

## copy는 동일한 복사본을 만들고, view는 동일한 대상을 가리키는 다른 이름을 만든다.
## copy의 경우 수정을 해도 원본이 그대로이지만, view는 수정을 하면, 원본에도 반영된다(어짜피 같은 거라 원본이라는 말도 어폐가 있지만)
s3p.iloc[0] = -14000 # s도 바뀐다
s3p[0] = -999 
s3p.iloc[0] = -99999 # s는 변하지 않는다. 

## 둘 또는 그 이상의 시리즈를 합쳐서 새로운 시리즈를 만들 수도 있다.
pd.concat([s,s2])
#pd.concat([s,s2], axis=1)

# %% [markdown]
# ## Read

# %% [markdown]
# 판다스 시리즈의 내용을 읽는 방법은 크게 3가지로 나눌 수 있다.
# * 위치(순번)
# * 인덱스(이름)
# * 참/거짓

# %% [markdown]
# 혼동의 여지가 없을 경우(혼동되는 경우는 뒤에서 확인할 수 있다),
# 판다스 시리즈, **브라켓 열고, 위치(순번) 또는 인덱스(이름) 또는 참/거짓 리스트를 쓰고, 브라켓을 닫을 수 있다.** 

# %%
# 위치(순번), 인덱스(이름), 참/거짓
s[1]
s['b']
s[[False, True, False, False]].squeeze()

# %% [markdown]
# ### 위치(순번) 사용하기
#
# `.iloc[]`는 명시적으로 순서를 사용한다. 순서는 list의 순서와 마찬가지로 0부터 시작하고, 마지막은 -1로 쓸 수 있다.

# %%
s.iloc[0] # 0-번째 값 
s.iloc[[2]] # 2-번째를 포함한 시리즈(시리즈의 일부)
s.iloc[1:4] # 리스트의 슬라이스와 비슷하다. 1번째부터 4번째 직전까지의 시리즈
s.iloc[[1,2]] # 1번째와 2번째를 포함한 시리즈

# %% [markdown]
# `.take()`란 메쏘드를 사용할 수도 있다

# %%
s.take([1]) # ! s.take(1) does NOT work

# %% [markdown]
# 만약 `s.iloc[x]`라고 쓰면 그 결과는 변수 `x`에 따라 달라진다.

# %%
x = 3; print(s.iloc[x]); print('-'*10)
x = [1,3]; print(s.iloc[x])

# %% [markdown]
# `s.iat[]`의 결과는 항상 하나의 값이다. 결과로 시리즈가 나타날 수 없다.

# %%
s.iat[1] # for single item

# %%
x = 3; print(s.iat[x])

# %%
x = [1,3]; print(s.iat[x])

# %% [markdown]
# ### 인덱스 사용하기
#
# 인덱스를 사용할 때에도 순번과 마찬가지로 
# * 값 하나
# * 슬라이스(`a`:`b`에서 `b`포함)
# * 여러 값(Fancy Indexing)
# 을 사용할 수 있다.

# %%
s

# %%
s.loc['b'] # 값 하나
s.loc['b':'d'] # 슬라이스(인덱스를 사용할 때에는 start:stop에서 stop을 포함한다)

# %%
s.loc['a':'d':2] # step까지 사용하기

# %%
s.loc[['b', 'd']] # 여러 값(Fancy Indexing)

# %% [markdown]
# `.at[]`은 `.iloc[]`에서 `.iat[]`의 의미와 비슷하다. 결과는 항상 값이어야 한다.

# %%
x = 'b'
s.at[x]

# %%
x = ['b', 'c']
s.at[x]

# %% [markdown]
# ### 참/거짓 사용하기

# %% [markdown]
# 시리즈와 같은 길이의 참/거짓 리스트를 사용하여 원하는 값의 위치를 정해줄 수 있다.

# %%
s[[False, False, False, True]]

# %% [markdown]
# 혼동의 여지가 없을 때에는 `s[]`, `s.iloc[]`, `s.loc[]`이 모두 가능하지만, `s.loc[]`을 쓰는 것을 권고한다.
#
# 그 이유는 뒤에서 소개한다.

# %% [markdown]
# 이 방식의 결과는 항상 시리즈이므로, 값을 원한다면 `.squeeze()` 메쏘드를 사용할 수 있다.

# %%
s.loc[[False, False, False, True]].squeeze()

# %% [markdown]
# 참의 갯수만큼의 값이 시리즈로 반환된다. 

# %%
x = [True, True, False, True]
sum(x) # 참-거짓으로 구성된 리스트에서 참의 갯수는 sum()함수로 구할 수 있다

# %%
s.loc[[True, True, False, True]]

# %% [markdown]
# 참/거짓은 이렇게 직접 사용하기보다는 어떤 조건에서 참/거짓을 구해서 사용한다.

# %%
s > 0  ## s의 원소 중 0부터 큰 원소는?

# %% [markdown]
# s>0의 결과인 (`pd.Series([False, True, False, True])`)는 s의 원소 중에서 0부터 큰 원소의 위치를 나타낸다고 할 수 있다.
#
# 따라서 `s[s>0]` 또는 `s.loc[s>0]`는 `s`의 원소 중에서 0부터 큰 원소를 보여준다.

# %%
s[s>0]

# %%
s.loc[s > 0]  

# %% [markdown]
# 여기서 `s>0`의 결과는 판다스 시리즈이다. 따라서 인덱스와 값(참/거짓)을 동시에 가지고 있다.
# `s.loc[]`은 원래 인덱스를 사용하는 방식이다.
# 만약 `s.loc[]` 안에 판다스 시리즈가 사용될 경우, 인덱스의 유무로를 참/거짓으로 결정한다.

# %%
x = pd.Series([False, True, False, True])

# %%
s.loc[x]

# %% [markdown]
# **왜 `x`의 값은 `s>0`과 동일함에서도 `s[x]`와 `s[s>0]`의 결과가 다른가?**

# %% [markdown]
# #### 참/거짓을 사용하는 예 : 특정 인덱스 제외하기

# %%
s[~s.isin(['a', 'b'])] # 인덱스가 'a', 'b'인 경우를 제외한 나머지

# %% [markdown]
# ### `.loc` 또는 `.iloc` 없이 참조하는 방식은 읽기 어려울 수 있다.

# %%
s = pd.Series(['West', 'East', 'North', \
               'South', 'Center'],
              index = ['a', 'b', 'c', 'd', 'e'])

# %%
s['a':'e'] # 혼동의 여지가 거의 없다.

# %%
s = pd.Series(['West', 'East', 'North', \
               'South', 'Center'],
              index = [3,1,2,4,0])

# %%
s[3] # index가 3을 의미하는가? 아니면 순번 3을 의미하는가?

# %% [markdown]
# `s[3]`에서 `3`이 무엇을 의미하는지, `s`의 내용을 모르면 알 수 없다.
# `3`은 인덱스일 수도 있고, 순번일 수도 있다.
#
# 위에서 확인할 수 있듯이, **가장 먼저 인덱스인지 확인한다.**

# %%
s = pd.Series(['West', 'East', 'North', \
               'South', 'Center'],
              index = [3,'a', 'b', True,False])

# %% [markdown]
# 위의 `s`의 인덱스를 확인하자. 와! `3`(정수), `'a'`(문자열), `True`(참/거짓)까지 없는 게 없다.

# %%
s[3] # 역시 인덱스

# %%
s[True] # 역시 인덱스

# %%
s[[True,False]] # 참,거짓만 써서 리스트를 만들면

# %%
s[[3,True,False,'a']] # 하지만 다른게 섞이면...

# %% [markdown]
# 결국 참-거짓만으로 이루어진 리스트가 아니라면 **가장 먼저 인덱스를 확인한다.**

# %%
s[[3,3,'a']] # 비교

# %% [markdown]
# 그런데 `[s=="West"]` 같은 경우 `s[]` 안은 `s`와 인덱스가 같은 판다스 시리즈이므로 혼동될 여지는 크지 않다.

# %%
s[s=='West']

# %% [markdown]
# 결론적으로 `s[s == 3]`은 혼동의 여지가 없다.
# `s[정수]`의 경우 인덱스가 정수라면 혼동될 여지가 있으므로, 순번을 의미한다면 `s.iloc[정수]`로 쓰자.
# 인덱스를 사용하고, 인덱스에 True/False가 포함되지 않는다면 `s[]`도 혼동의 여지가 없어보인다.
# 그리고 인덱스에 True/False가 포함되는 경우는 극히 드물다. 
#
# 하지만 어쨋든 `s[]`보다는 `s.iloc[]` 또는 `s.loc[]`을 쓰는 것을 권장한다. 왜냐하면, 다음과 같이 **`s[]`는 일관성이 없어보인다!**

# %%
s1 = pd.Series([1,2,3,5,7,11,13],
              index = [4,5,6,7,1,2,3])
s1[5]; print(s1[5]); print('-'*10)
s1[5:7]; print(s1[5:7]); print('-'*10)
s1[[5,6]]; print(s1[[5,6]]); print('-'*10)

# %% [markdown]
# ## Edit
#
# 수정하는 방법은 참조한 대상을 왼쪽에 덮어쓸 값을 등호 좌우에 적는다. 
# 판다스 시리즈는 넘파이 배열과 마찬가지로 브로드캐스팅(broadcasting)이 가능하다. 
# 다시 말해, 값 하나만 적어도 여러 원소의 내용을 바꿀 수 있다.
#
# 참조는 위에서 소개한 인덱스, 순번, 참/거짓이 모두 가능하다.
# `s[i]=x`와 `s.loc[i]=x`가 모두 가능하지만,
# `s.loc[i]=x`과 같이 명시적으로 인덱싱을 사용한다는 것을 알려주면,
# 프로그램을 읽기 편하다.

# %%
import pandas as pd
s1 = pd.Series([1,2,3,5,7,11])
s2 = pd.Series([1,2,3,5,7,11],
               index = ['a', 'b', 'c', 'd', 'e', 'f'])
# %% [markdown]
# 아래에서 `s2`은 인덱스가 정수가 아니므로 `s2[정수]` 꼴은 `s2.iloc[정수]`와 같다.
# 반면 `s1`은 인덱스가 정수이므로 `s1[정수]`는 `s1.loc[정수]`와 같게 된다. 
# `s1`의 인덱스가 `0`부터 시작해서 `1`씩 증가한다면 `s1.iloc[정수]`, `s1.loc[정수]`의 결과가 같지만,
# 인덱스가 추가되거나 하면 그 결과가 달라질 수 있으니 유의하자.
#
# 따라서 결론적으로 `s[]` 대신 `s.loc[]` 또는 `s.iloc[]`을 쓰자. `s[]`는 `s[s>0]`와 같은 경우만 쓰자.
#

# %% [markdown]
# #### 순번

# %%
s1.iloc[2] = 1; print(s1); print('-'*10)
# slice
s1.iloc[2:4] = [-1,-2]; print(s1); print('-'*10)
# slice, broadcasting
s1.iloc[2:4] = 0; print(s1); print('-'*10)
# fancy indexing
s1.iloc[[2,3]] = -1; print(s1); print('-'*10)

# %% [markdown]
# #### 인덱스

# %%
s2.loc['b'] = 1; print(s2); print('-'*10)
# slice
s2.loc['b':'d'] = [-1,-2,-3]; print(s2); print('-'*10)
# slice, broadcasting
s2.loc['b':'d'] = 0; print(s2); print('-'*10)
# fancy indexing
s2.loc[['b', 'c', 'd']] = -1; print(s2); print('-'*10)

# %% [markdown]
# s2

# %% [markdown]
# #### 참/거짓

# %%
s2 = pd.Series([1,2,3,5,7,11],
               index = ['a', 'b', 'c', 'd', 'e', 'f'])

# %%
s2[s2 > 5] = 8; print(s2); print('-'*10)
s2[s2 == 8] = [1,2]; print(s2); print('-'*10)
s2[s2 == 1] = 0; print(s2); print('-'*10)

# %% [markdown]
# ### Add

# %%
import pandas as pd
s1 = pd.Series([1,2,3,5,7,11])
s2 = pd.Series([1,2,3,5,7,11],
               index = ['a', 'b', 'c', 'd', 'e', 'f'])
s1

# %% [markdown]
# #### 원소 하나
#
# `s[]=` 꼴은 인덱스는 가능하지만, 순번, 참/거짓은 불가능하다

# %%
s1.loc[-1] = -100

# %%
s1[-1] = -100 # 바로 인덱스를 써서 바로 추가가 가능하다
s1

# %%
x = len(s1)
s1.iloc[x] = 12

# %% [markdown]
# #### 여러 원소
#
# `s[x] = y`꼴은 불가능하고,
# `s.append(pd.Series(y, index = x))`로 써야 한다.

# %%
s1.loc[[6, 7]] = [2,4]

# %%
s1.append(pd.Series([2,4], index = ['x', 'y']))

# %% [markdown]
# ### Delete

# %%
s = pd.Series([-0.4, 2.5, 1.41, 2.69],
              index = ['a', 'b', 'c', 'd'])

# %% [markdown]
# #### 원소 하나

# %% [markdown]
# 인덱스 사용하기

# %%
del s['a'] # del s.loc['a']는 사용 불가

# %%
s.drop('b')

# %%
s.drop('b', inplace=True); print(s)

# %% [markdown]
# 순번

# %%
#del s.iloc[0] # 불가능

# %%
# 우회 방법
s.drop(s.index[0])

# %% [markdown]
# 참/거짓

# %%
del s[s>0] # 불가능

# %%
# 우회 방법
s.drop(s.index[s>3])

# %% [markdown]
# #### 원소 여럿

# %% [markdown]
# 인덱스

# %%
s = pd.Series([-0.4, 2.5, 1.41, 2.69],
              index = ['a', 'b', 'c', 'd'])

# %%
del s[['a', 'b']]

# %%
s.drop(['a', 'b'], inplace=False)

# %%
s.drop(['a', 'b'], inplace=True); print(s)

# %% [markdown]
# 순번 : 우회 방법

# %%
s = pd.Series([-0.4, 2.5, 1.41, 2.69],
              index = ['a', 'b', 'c', 'd'])

# %%
s.drop(s.index[[0,2]])

# %% [markdown]
# 참/거짓 : 우회 방법

# %%
s.drop(s.index[s>3])

# %%
s.index

# %%
s.drop(s.index[[True,False,False, True]])

# %% [markdown]
# ### 추가될 내용

# %% [markdown]
# `np.nan`, `pd.NA` 등 결측치 관련 내용이 추가되어야 할 듯
# `np.nan`은 float에서 NA, `pd.NA`은 dtype='Int64'(여기서 I는 대문자이다. pd.__version__ >= 1.0.0)

# %% [raw]
# >>> float(9007199254740992) == float(9007199254740992+1)
# True
# >>> float(9007199254740992) == float(9007199254740992+2)
# False
# >>> float(9007199254740995) == float(9007199254740995+1) 
# True

# %%
import os

lst = [10**x for x in range(14,18)]

j = 0
with open('test-float.txt', 'wt') as f:
    for e in range(32, 64):
        i= 2**e
        if float(i) == float(i+1) or float(i-1) == float(i):
            print(i)
            f.write("{}, ".format(i))
            f.flush()
        if j < len(lst) and i>lst[j]:
            print('>> {}'.format(lst[j], e))
            j = j + 1
f.close()

# %% [markdown]
# 위의 예에서 보듯이 `int`eger를 `float`로 변환시킬 경우, 
# 서로 다른 값을 같은 값으로 인식하는 논리 오류가 발생하므로 유의해야 하자.
# 파이썬의 native type인 float는 플랫폼에 따라 저장에 필요한 바이트 수 등이 달라지므로 유의하자.

# %%
import sys
sys.float_info

# %% [markdown]
# 위의 내용을 보면, `float` 타입으로 나타낼 수 있는 최대값은 179769313486231570000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000이지만, 그렇게 큰 수에서는 1 작은 수는 구분할 수 없을 만큼 정확도가 낮아진다.

# %%
float(179769313486231570000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

# %%
a = float(179769313486231570000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
b = float(179769313486231569000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
a == b

# %%
이런 현상은 9007199254740992 와 같은 작은 수에서부터 시작한다.

# %%
float(9007199254740992) == float(9007199254740993)

# %% [markdown]
# 만약 넘파이 배열에서 `float16`처럼 더 작은 메모리로 부동소수점을 저장한다면, 이런 현상은 더 작은 정수에서부터 시작된다.

# %%
import numpy as np
np.array([10000], dtype='float16') == np.array([10001], dtype='float16')

# %% [markdown]
# 판다스에서 `pd.NA`와 같이 int 전용의 결측값(missing value)를 만든 이유도 비슷하다(ref?)

# %% [markdown]
# `int`의 경우, 파이썬은 메모리가 허용하는 한 **모든 수를 정확하게 저장한다**. 이런 이유로 파이썬에서 `int`의 연산은 느리고, 넘파이 배열은 저장가능한 크기가 한정되어 있지만 빠르다.

# %%
10**700 == (10**7000 + 1)

# %% [markdown]
# 이런 **예외적인 상황**(?)이 문제가 됐던 경우를 알아보자. 인스타그램의 post id를 다룰 때였다. 인스타그램의 post id는 정수형이었던 것으로 기억한다. 정수형이지만 매우 큰 값이었기 때문에, 그리고 NA가 포함되어 있었기 때문에, 판다스는 `float`로 변환을 하였고, 원래는 서로 다른 post id가 같은 값으로 인식되는 문제가 발생되었다. 그래서 문자형으로 바꿔 보았는데, 문자형은 처리 속도가 매우 느렸다. 그때에는 결국 R의 데이터 테이블(`data.table`)을 사용하여 해결하였다. 만약 파이썬에서 해결을 한다면, post id를 두 개의 정수로 쪼개서 사용하는 방법을 시도해 볼 것 같다. 하나의 문자열을 두 개로 나눈 과정에서 어느 정도 시간이 걸리겠지만, 그 다음부터 정수를 사용하여 post id를 비교하므로 시간이 많이 걸리지 않을 것이다.

# %%
