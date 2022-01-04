# -*- coding: utf-8 -*-
# %% [markdown]
# R에서 배열은 1차원 벡터의 다차원 확장 쯤으로 생각했다. 
# R에서 모든 배열은 벡터와 동일한 형태로 저장되어 있고, 차원마다 차원의 크기가 설정되어 있다는 점만 다르다.

# %% [markdown]
# 파이썬에 R의 1차원 벡터를 대신할 수 있는 데이터 구조는
# **넘파이 배열(numpy array)**과 **판다스 시리즈(pandas series)**를 생각할 수 있다.
#
# 여기서는 numpy의 배열에 대해 알아본다. 
# 특히 R의 1차원 벡터와 동일하게 생각할 수 있는 python의 1차원 넘파이 배열에 대해 알아본다.
# 1차원 넘파이 배열은 동일한 type의 값이 순번에 따라 저장되었다고 생각할 수 있다.

# %%
import numpy as np

# %% [markdown]
# ## CREAD(원소의 위치) 
#
# ### Create
# #### Empty array

# %%

a = np.empty(0)
a = np.empty((5,2))
a = np.empty((5,2), dtype='>U3')
# numpy array의 대표적인 dtype
# integer, float, complex?, string, object
# number, character, bool, object

# np.number라면,
# 이 클래스가 속한 모듈 이름 : np.number.__module__
# 그 모듈 : sys.modules[np.number.__module__]
# 

# %% [markdown]
# #### 내용이 있는 배열

# %%
a = np.array([1,4,2,8,7,9], dtype=float)

# %% [markdown]
# #### 다른 배열에서
#
# * copy
# * view

# %%
# # copy
b = a[:]
a is b

# %%
b = a.copy()
a is b

# %%
# view
b = a
a is b

# %% [markdown]
# #### 다른배열의 일부

# %%
# view
a = np.array([0,1,2,3,4,5,6,7,8])
b = a[2:5]
print(a)
print(b)

# %%
b[0] = 0
print(a)
print(b)

# %%
# copy1
b = a[2:5].copy()
print(a)
print(b)

# %%
b[0] = 10
print(a)
print(b)

# %%
# copy2
b = a[[0,1,4]]
b

# %%
b[0] = -1
print(a)
print(b)

# %% [markdown]
# ### Read
#
# 1차원 넘파이 배열의 원소는 순번(위치)을 정해서 읽는다.

# %%
a[3]        # 원소 하나 : a의 3-번째 원소
a[:5:2]     # 연속된 원소 slice 
a[[3,4,-1]] # 임의의 원소 Fancy-index : a의 3,4-번째와 마지막 원소

# %% [markdown]
# ### Edit
#
# 원소를 수정하는 방법은 원소를 읽는 방법과 비슷하다.
# 원소를 읽은 후 그 원소들을 등호의 오른쪽 값으로 바꾼다고 생각할 수 있다.
# 여러 원소가 모두 같은 값이라면, 값을 하나만 써도 된다.

# %%
a = np.array([0,1,2,3,4,5,6])

a[1] = 99
a[:5:2] = [0,0,0]  # 0,2,4-번째
a[[3,4,-1]] = [-10,-10,-10] # 3,4,마지막-번째
print(a)

# %%
a[1] = -1
a[:5:2] = -1  # 0,2,4-번째
a[[3,4,-1]] = -1 # 3,4,마지막-번째
print(a)

# %% [markdown]
# ### Add
#
# 배열에 여러 원소를 추가하려면 `np.append()`를 사용할 수 있다. 이때 `np.append(a,b)`는 배열 `a`에 배열 `b`가 추가된 결과가 반환되고, 배열 `a`와 배열 `b`는 변하지 않음을 유의하자.

# %%
np.append(a, [0,0,0])

# %%
np.append(a, np.array([0,0,0]))

# %% [markdown]
# 여러 배열을 합치려면 `np.concatenate([a1,a2,a3,...])`를 사용할 수 있다.

# %%
a1 = np.array([0,1,2,3,4])
a2 = np.array([10,9,8,7,6])
a3 = np.array([-1,-2,-3,-4,-5])
np.concatenate([a1, a2, a3])

# %%
np.insert(a2, 1, [0,0]) # 1번째 원소 앞에


# %% [markdown]
# ### Delete
#
# 특정한 위치의 원소가 삭제된 새로운 배열을 얻고자 한다면, `np.delete(a, position_list)`를 사용한다.

# %%
a = np.array([0,1,2,3,4,5,6])
a; print(a)
a; print(np.delete(a, [0,-1])) # 가장 처음 원소와 마지막 원소를 제거한 결과

# %% [markdown]
# #### 연습문제
#
# 다음을 numpy array로 구현해보세요. 
#
# ```
# 원소가 1부터 100까지인 numpy array 'x'를 생성해보세요. 
# 'x' 의 20번째에서 30번째까지의 원소를 변수 'y'에 할당해보세요.(여기서 20번째는 0번째부터 시작한다.)
# 'y' 의 짝수번째 원소를 모두 0으로 변경하고, 5번째 원소와 7번째 원소를 50으로 변경해보세요.
# 'y' 에서 0인 원소를 모두 제거하고, 나머지 원소를 'x'와 결합해보세요.
# 이때 결과는 예상했던 것과 같은가? 
# 그렇지 않다면 그 이유는 무엇인가?(x를 생성한 듯, x의 원소를 직접 변경한 적은 없다. 하지만 x의 내용을 살펴보자.) 
# ```

# %%
x = np.arange(1, 101) # 1부터 101 직전까지
y = x[20:31]          # 20번째 원소부터 31번째 직전 원소까지
y[::2] = 0            # 처음부터 끝까지, +2에 해당하는 원소(하나 걸러 하나)
y[[5, 7]] = 50        
np.concatenate([x, np.delete(y, [0, 2, 4, 6, 8, 10])]) # x와 y의 0,2,4,6,8,10번째 원소를 제거한 결과를 합친다. 
np.concatenate([x, y[1::2]])  # x와 y의 1,3,5,...번째 원소를 합친다.

# %% [markdown]
# 위의 연습문제의 마지막 과제에서 우리는 배열 `y`의 원소 중 `0`의 위치(짝수번째)를 미리 알고 있었다. 그리고 이 점을 활용하여 `y`의 원소 중 0를 제거할 수 있었다. 하지만 `y`의 원소를 미리 알지 못하는 경우에는 어떻게 해야 할까?


# %%
import numpy as np
x = np.arange(1, 101)
y = x[20:31].copy()
y[::2] = 0
y[[5, 7]] = 50
np.concatenate([x, np.delete(y, [0, 2, 4, 6, 8, 10])])
np.concatenate([x, y[1::2]])

# %% [markdown]
# ## _READ(원소의 내용)
#
# 넘파이 배열은 원소가 일렬로 배열되어 있다고 생각하면 쉽다. 따라서 원소의 위치(순번)을 알고 있다면, 그 원소를 쉽게 읽고, 수정하고, 추가하고, 삭제할 수 있다. 반면 특정한 내용을 읽고, 수정하고, 추가하고, 삭제하려면 모든 원소를 읽어서 원하는 원소가 맞는지 확인을 해야 한다. 다음은 내용을 기반으로 READ를 하는 방법을 보여 준다. 

# %%

# %% [markdown]
# ### Read

# %%
a = np.array([1,2,3,4])
b = np.array([2,3,5,7,9,11])

# %%
a[a==b[1]] # a에 b[3]가 존재하는지 확인. 몇 개 존재하는가?
print(a[a==b[1]])
np.where(a==b[1]) # a에 b[3]가 존재하는 위치 확인
print(np.where(a==b[1]))

a[np.isin(a, b)] # a 중에서 b에 존재하는 원소
print(a[np.isin(a,b)])
np.where(np.isin(a,b))
print(np.where(np.isin(a,b)))

# %% [markdown]
# ### Edit

# %%
a = np.array([0,1,2,3,4,5,6,7])
# 원소 3을 -1로 수정
a[np.where(a==3)[0]] = -1; print(a)

# %%
# 0을 -10으로, 5를 2로 수정
replace = {0:-10, 5:-20}
for k in replace:
    a[np.where(a==k)[0]] = replace[k]
print(a)

# %% [markdown]
# ### Add

# %%
a = np.array([0,1,2,3,4,5,4,3,2,1,0])

a2 = a.tolist()
# 원소 3 앞에 -1, -2, -3을 추가
# a에는 원소 3이 두 번 나타나고 있음을 유의하자.
elems = [-1, -2, -3]

whs = np.where(a==3)[0].tolist()
whs = [None] + whs + [None]

sliced = [a2[slice(x,y)] for x,y in zip(whs[:-1], whs[1:])] # x[slice(n, m)] : x[n:m] 동일

res = sliced[0]
for x in sliced[1:]:
    res = res + elems + x
np.array(res)

# %% [markdown]
# !!!) 만약 리스트에서도 원소 내용을 통해 Add한 경우가 있다면, 그걸 활용하는 게?
#
# 위의 방법을 좀 더 상술해보자. 
# 우선 배열 `a`를 리스트로 변환한다. (리스트에서 리스트 `a`와 리스트 `b`를 합치는 것은 간단하게 `a+b`로 나타낼 수 있다.)
# 그리고 `3`의 위치를 확인하여, 리스트를 `3`이 가장 앞에 나오는 부분 리스트로 나눈다.
# `a2 = [0,1,2,3,4,5,4,3,2,1,0]`
# `a2 = [0,1,2] + [3,4,5,4] + [3,2,1,0]`
# 그리고 중간에 키워넣을 리스트 넣어 새로운 리스트를 만든다.
# `[0,1,2] + [-1,-2,-3] + [3,4,5] + [-1,-2,-3] + [3,2,1,0]`
# 그리고 다시 배열로 만든다.

# %%
a = np.array([0,1,2,3,4,5,4,3,2,1,0])

a2 = a.tolist()
# 원소 3 뒤에 -1, -2, -3을 추가
elems = [-1, -2, -3]

whs = (np.where(a==3)[0]+1).tolist(); print(whs)
whs = [None] + whs + [None]; print(whs)

sliced = [a2[slice(x,y)] for x,y in zip(whs[:-1], whs[1:])]

res = sliced[0]

for x in sliced[1:]:
    res = res + elems + x
np.array(res)


# %% [markdown]
# 위의 예처럼, 
# 배열 `a`의 특정한 원소 앞(type='pre') 또는 뒤(type='post')에 원소를 삽입하고 싶을 때 쓸 수 있는 함수를 만들었다.

# %%
def np_add_where(a, where, elems, type='pre'):
    a2 = a.tolist()
    
    if type=='pre':
        whs = (np.where(a==where)[0]).tolist()
    elif type=='post':
        whs = (np.where(a==where)[0]+1).tolist()
    else:
        raise ValueError('type should be pre or post')
        
    whs = [None] + whs + [None]
    
    sliced = [a2[slice(x,y)] for x,y in zip(whs[:-1], whs[1:])]
    
    res = sliced[0]
    for x in sliced[1:]:
        res = res + elems + x
    return np.array(res)
    


# %%
np_add_where(np.array([3,4,5,4,5]), 4, [1], type='pre')

# %%
np_add_where(np.array([3,4,5,4,5]), 4, [1], type='post')

# %%
np_add_where(np.array([3,4,5,4,5]), 0, [1,2], type='pre')

# %% [markdown]
# ### Delete

# %%
a = np.array([1,3,2,4,3,2,2,1,3])
# 3인 원소 지우기
np.delete(a, np.where(a==3))
# 3 또는 4인 원소 지우기
np.delete(a, np.where((a==3) | (a==4)))
# 3 또는 4인 원소 지우기
np.delete(a, np.isin(a, [3,4]))

# %% [markdown]
# #### 연습문제
#
# 위의 함수 np_add_where()를 활용하여 아래를 구현해보세요.
#
# ```
# 1부터 30으로 이루어진 numpy array 'x'를 생성해보세요.
# 'x' 의 원소 중 10보다 크고, 20보다 작은 원소를 변수 'y'에 할당해보세요.
# 'y' 의 원소 중 짝수로 이루어진 원소 앞에 0을 추가해보세요.
# ```

# %%
x

# %%
x > 10

# %%
x[x>10]

# %%
x = np.arange(1,31); print(x)
y = x[(x>10) & (x<20)]; print(y)


# %%
np.where(y % 2 == 0)[0]

# %%
이 경우에 바로 쓸 수 없으므로, 확장성을 위해 코드를 조금 변경해 보았다.


# %%
def np_add_where(a, whs, elems, type='pre'):
    import numpy as np
    a2 = a.tolist()
    
    if isinstance(whs, list):
        if type == 'post':
            pass
    elif isinstance(whs, np.ndarray):
        whs = whs.tolist()  
    else:
        ValueError('whs should be list or np.ndarray')
    
    if type == 'post':
        whs = [x + 1 for x in whs]

    whs = [None] + whs + [None]
    
    sliced = [a2[slice(x,y)] for x,y in zip(whs[:-1], whs[1:])]
    
    res = sliced[0]
    for x in sliced[1:]:
        res = res + elems + x
    return np.array(res)


# %%
np_add_where(y, np.where(y % 2 == 0)[0], [0], type='pre')

# %%

# %% [markdown]
# ## View와 Copy

# %% [markdown]
# 위의 연습문제에서 우리는 `x`의 원소를 직접 변경하지 않았지만, `y=x[20:31]`를 통해 변수 `y`는 `x`의 원소 20번째부터 31번째를 가리키게 되었기 때문에, `y`의 원소를 변경하면 `x`의 원소도 변경됨을 보았다. 
#
# 이렇게 메모리에 이미 존재하는 배열의 일부 또는 전체를 다른 이름으로 부를 수 있으며, 이를 해당 배열의 뷰(View)라고 한다. 따라서 변수 `y`는 배열 `x` 일부의 뷰이다. 뷰는 원래 행렬의 일부를 가라킬 수도 있고, 원래 행렬을 다른 type으로 볼 수도 있다. 

# %%
x = np.array([1,3,5,2], dtype='f4')

# %%
x

# %%
y = x.view(dtype='f8')

# %%
y

# %% [markdown]
# 위의 예에서 행렬 `x`의 원소는 `f4`(4바이트 부동소수점) 타입이다. 반면 동일한 내용을 `y`는 `f8`(8바이트 부동소수점)으로 본다. 메모리 상의 내용은 단순한 숫자이다. 이 숫자는 필요에 따라 정수, 부동소수점, 또는 문자열로 해석이 가능하다. 

# %%
z = y.view(dtype='<U2')  # |S4

# %%
z

# %% [markdown]
# ### 언제 View이고, 언제 Copy인가?

# %% [markdown]
# 두 행렬 `x`가 있을 때, 
# `y=x` 또는 `y=x[]` 꼴은 언제 view이고, 또 언제 copy인가?

# %%
x = np.array([1,10,2,9,3,7])

# %%
y = x # view

# %%
x is y

# %%
y = x[:] # copy

# %%
x is y

# %%
# view임을 확인하는 방법?

# %%
y = x[1:3] # view

# %%
id(y[0])

# %%
id(x[1])

# %%
y[0] is x[1]

# %%
y[0], x[1]

# %%
y[1], x[2]

# %%


## Why not use np.arange() with float?
# https://forum.quantumatk.com/index.php?topic=110.0
# https://stackoverflow.com/questions/63130895/how-can-i-fix-the-problem-that-numpy-arange-is-not-working-properly
# https://stackoverflow.com/questions/40152997/numpy-arange-floating-point-inconsistency/40153453
# https://github.com/numpy/numpy/issues/17189
# more in README.md

