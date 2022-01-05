# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: rtopython2-pip
#     language: python
#     name: rtopython2-pip
# ---

# %% [markdown]
# ## 파이썬의 기본적인 데이터 구조에서 CREAD

# %% [markdown]
# 클래스, 인스턴스, 객체에 대한 설명을 앞에서 해야 할 듯!!!

# %% [markdown]
# 파이썬은 범용 프로그램으로 builtins 모듈에 범용적으로 사용할 수 있는 클래스가 여럿 존재한다.
# 특히 여러 값을 여러 값을 저장하기 위해 사용하는 클래스는 `list`, `tuple`, `dict`, `set`이 있다.
# 사실 데이터 분석을 할 때에는 `list`, `tuple` 등의 파이썬 builtins 모듈의 클래스를 사용하지는 않는다.
# 좀더 빠르고 효율적인 제3자 패키지인 `numpy` 또는 `pandas`라는 패키지의 클래스를 주로 사용한다.
# 그럼에도 `list`, `tuple`, `dict` 등의 파이썬 builtins 모듈의 데이터 구조는
# 파이썬 전반에 두루 사용되기 때문에 반드시 배워야한다.

# %% [markdown]
# > **R과 비교** : R에서 주로 사용하는 데이터 구조는 벡터이다. 반면 파이썬에서는 리스트를 광범위하게 사용한다. 파이썬의 리스트는 R의 리스트와 마찬가지로 어떤 종류의 객체로 원소로 저장할 수 있다는 점에서 비슷하지만, R의 리스트가 원소를 모두 저장하는 반면 파이썬의 리스트는 원소가 어떤 객체를 가리키는 **포인터**만을 저장하고 있다는 차이가 있다. 그리고 R에서는 벡터를 다양한 방식(예. `v[1]`, `v[c(1,5)]`, `v[c(-2,-3)]`, `v[c("John", "Mary")]`, `v[c(TRUE, FALSE)]`)으로 활용할 수 있지만, 파이썬의 리스트 활용법은 다소 제한적이다. 여기서는 파이썬을 리스트로 CREAD하는 방법을 소개하고, R 사용자의 편의를 위해 파이썬을 리스트를 R의 벡터처럼 편리하게 조작하는 방법을 제시한다.  

# %% [markdown]
# 먼저 이들 클래스에서 CREAD 작업을 어떻게 하는지를 알아보자. 주요 내용은 다음과 같다.

# %% [markdown]
# #### 파이썬 `list`, `tuple`, `dict`, `set`에서 CREAD
# * 생성(**C**reate)
# * 읽기(**R**ead)
#     - 원소 하나
#     - 임의 위치의 여러 원소
#     - 연속적인 여러 원소(Slicing)
#         - 연속적인 여러 원소
#         - 거꾸로 연속적인 여러 원소
#         - 규칙적인 위치의 여러 원소
#         - 음수 위치
# * 수정(Edit)
#     - 제자리 수정
#     - 수정된 리스트 생성
#     
#     - 위치 기반의 수정
#         - 역순으로 만들기
#     - 내용 기반의 수정
#         - 정렬하기
# * 추가(Add)
#     - 제자리 수정
#     - 수정된 리스트 생성
# * 삭제(Delete)
#
# * 기타
#     - 왜 파이썬 **순번은 0부터 시작**하는가?
#     - 왜 슬라이싱 a:b는 a번째 부터 **b번째 직전**까지를 의미하는가?
#     - 리스트는 무엇을 저장하는가? 내용인가? **주소**인가?
#     

# %% [markdown]
# ## `list`, `tuple`, `dict`, `set` 구분
#
# 리스트, 튜플, 딕, 셋은 모두 여러 값을 저장할 수 있다는 점에서 같다(엄밀히 말해 어떤 객체를 가리키는 포인터를 저장하지만 편의상 값을 저장한다고 표현하였다). 이때 값 하나를 **원소**라고 부르자. 
#
# 리스트, 딕, 셋은 여러 원소를 가질 수 있다는 점에서 같다. 하지만 **하나의 원소를 가리키는 방법**이 다르다.
#
# 리스트는 **순번**을 사용한다. 예를 들어, 세 번째 원소는 뭐냐? 마지막 원소는 뭐냐?라는 질문에 즉각 대답할 수 있다.
# 딕는 **이름**을 사용한다. 예를 들어, 이름이 Mary인 원소는 뭐냐? 이름이 5인 원소는 뭐냐?라는 질문에 즉각 대답할 수 있다.
# 셋은 우리가 흔히 말하는 **집합**이다. 집합은 순서가 없고 있냐 없느냐만 구분 가능하다. 이를 **원소 자신**이 이름인 경우로 생각해 볼 수 있다. 그래서 `"Mary"`가 있느냐? `5`가 있느냐?라고 질문할 수 있다.
#
# 마지막으로 튜플은 리스트와 거의 같다. 한 가지 다른 점은 튜플은 수정이 불가능하다는 점이다.
#
# 다음은 리스트, 튜플, 딕, 셋에서 원소 하나를 만들고(Create), 읽고(Read), 수정하고(Edit), 추가하고, 제거하는 방법을 소개한다.

# %% [markdown]
# ## 원소 하나
#
#
#

# %% [markdown]
# |   |list   |tuple   |dict   |set   |
# |---|---|---|---|---|
# |Create   |`[1]`   |`(1,)`   |`{'a':1}`   |`{1}`   |
# |         |`[1,2,3]`   |`(1,2,3)`   |`{'a':1, 'b':2, 'c':3}`   |`{1,2,3}`   |
# |Read   |`x[0]`   |`x[0]`   |`x['a']`   | `1 in x`  |
# |Edit   |`x[0]=-5`   | -   |`x['a']=-5`   |`x.remove(1); x.add(-5)` or *edit-set |
# |Add (at the last)   |`x.append(4)`   | -  |`x['d']=4`   |`x.add(4)`   |
# |Add at the random position   |`x.insert(-4, 1)`   | -   |`x['d'] = 4`   |`x.add(4)`   |
# |Remove |`del x[1]`   | -   |`del x['b']` or `x.pop('b')` |`x.remove(2)` |
#
# * edit-set
#
# ```
# try:
#     x.remove(1)
# except KeyError as e:
#     pass
# x.add(5)
# ```

# %%
x = [1,2,3]
print(x)

# %% [markdown]
# ### list
#
# 리스트는 원소를 모아 `[`, `]` 안에 나열하여 생성한다. `[1, 'b', 5]`은 첫 번째 원소가 `1`, 두 번째 원소가 `'b'`, 세 번째 원소가 `5`인 리스트를 생성한다. 그리고 `x=[1,'b',5]`을 하면 리스트를 생성한 후, 변수 `x`가 생성한 리스트를 가리키도록 만든다.
#
# 그리고 리스트 `x`의 각 원소는 `x[0]`, `x[1]`, `x[2]`로 쓴다(파이썬의 순번은 0부터 시작한다). `x[0]`은 리스트 `x`의 0-번째 원소, `x[1]`은 리스트 `x`의 1-번째 원소를 가리킨다. 이제 각 원소를 가리키는 방법을 배웠다. 각 원소를 참조하거나, 수정하는 방법은 자명하다(`x[1]`, `x[1]='c'`). 
#
# 리스트에 가장 마지막에 원소를 추가하거나, 중간에 원소를 추가하는 방법은 `.append()` 또는 `.insert()` 메쏘드를 쓴다. 리스트 `x`의 가장 마지막에 원소 `'eee'`를 추가하고자 한다면, `x.insert('eee')`라고 쓴다. 0-번째 원소 앞에서 `'0th'`라는 원소를 추가하고 싶다면, `x.insert(0, '0th')`라고 쓴다. 리스트 `x`의 1-번째 원소를 제거하고자 한다면 `del x[1]`이라고 쓴다.

# %%
x = [1,2,3]; print(x)
x[0]; print(x[0])
#1 in x; print(1 in x)
x[0]=-5; print(x)
x.append(4); print(x)

x.insert(1, -4); # 1번째 원소 바로 앞에서 -4, 1번째 원소부터 순번이 +1된다.
print(x)
del x[0]; print(x)

# %% [markdown]
# ### tuple
#
# 튜플은 리스트와 모든 게 동일하지만 원소를 수정할 수 없다. 그래서 CREAD의 EAD(**E**dit, **A**dd, **D**elete)는 불가능하다.

# %%
x = (1,2,3); print(x)
#1 in x; print(1 in x)
x[0];        print(x[0])

# EDIT IMPOSSIBLE
# APPEND IMPOSSIBLE
# DELETE IMPOSSIBLE

# %% [markdown]
# ### dict
#
# 딕와 리스트의 차이는 원소를 가리키는 방법이다. 리스트는 순번으로 원소를 지정하고, 딕는 이름으로 원소를 지정한다.
#
# 리스트는 생성할 때 순번이 저절로 정해진다. 가장 처음 원소는 0-번째이고, 1-번째, 2-번째 등으로 지정된다. 딕는 생성 시 이름을 지정해 주어야 한다. 예를 들어, 원소가 `'a'`, `2`, `5`이 딕를 생성하고, `'a'`의 이름을 `'primary'`, `2`의 이름을 `'core'`, `5`의 이름을 `'height'`라고 지정하고자 한다면, 다음과 같이 한다.
#
# `{'primary':'a', 'core':2, 'height':5}`
#
# 이를 변수 `x`에 할당한다면 `x = {'primary':'a', 'core':2, 'height':5}`라고 쓴다. (좀더 엄밀히 말하자면, 이 코드의 결과로 변수 `x`는 딕 `{'primary':'a', 'core':2, 'height':5}`를 가리키게 된다.)
#
# 이제 각 원소를 지칭하기, 또는 수정하기 위해서는 이름을 사용한다.
#
# ```{python}
# x['primary']             # 참조
# x['primary'] = 'A'       # 수정
# ```
#
# 원소를 제거할 때에도 리스트와 동일하게 `del`을 사용한다. 이름이 `'primary'`인 원소를 제거하고자 한다면, `del x['primary']`라고 쓴다.
#
#

# %%
dic = {'a':1, 'b':2, 'c':3}; print(dic)
# 'a' in x
dic['a'];      print(dic['a'])
dic['a'] = -5; print(dic)
dic['d'] =  4; print(dic)
del dic['b'];  print(dic)

# %% [markdown]
# ### set

# %% [markdown]
# 셋(집합)의 경우, 생성은 `{`, `}` 안에 원소를 나열하여 생성한다. 원소는 셋 안에 존재하거나 존재하지 않는다. 이를 확인하는 방법은 `in`을 쓴다. 예를 들어 `{1,2,3}`(원소가 `1`,`2`,`3`인 셋)에 `1`이 존재하는지 여부는 `1 in {1,2,3}`으로 쓴다.
#
# 원소가 `1`, `"B"`, `-5`인 새로운 셋 `x`를 만들자(**C**reate).
#
# ```
# s = {1,"B", -5}
# ```
#
# 원소 `3`이 셋 `s`에 존재하는가(**R**ead)? `3 in s`
# 원소 `"B"`이 셋 `s`에 존재하는가? `"B" in s`
#
# 원소 `3`을 셋 `s`에 추가(**A**dd)하고자 한다면, `s.add(3)`.
# 원소 `3`을 셋 `s`에서 제거(**D**elete)하고자 한다면, `s.remove(3)`.
#
# 원소 '1'을 '2'로 바꾸고(**E**dit) 싶다면, `s.remove(1); s.add(2)`로 하면 된다.
#
#

# %%
x = {1,2,3}; print(x)
1 in x; print(1 in x)
x.difference_update({1}); print(x)  # x.difference_update() : x와 공통된 원소를 제거
x.add(-5); print(x)
x.add(4); print(x)
x.remove(3); print(x)

# %% [markdown]
# ### 연산 `in`
#
# 셋에서 원소를 참조하는 방법은 `a in s`(`a`: 원소, `s`:셋)이다. 셋은 원소와 이름이 같다고 생각할 수도 있다. 
#
# 리스트와 튜플, 딕에서도 `in`을 쓸 수 있다. 리스트와 튜플에서 `in`은 특정 원소가 리스트 또는 튜플에 존재하는지 확인하고, 딕에서 `in`은 특정 이름이 딕의 원소 이름으로 존재하는지 확인한다. 
#
#

# %%
x = {1,2,3}; print(x)

1 in x; print(1 in x)
# 1 in x에서 in의 경우 list, tuple, dict에서도 모두 사용 가능하고 의미도 비슷하다.
# 차이점은, list, tuple의 경우 1이 존재하는지 확인하기 위해서는 모든 원소를 확인해야 한다
# dict의 경우는 key:value에서 key의 존재를 확인한다.
x.remove(1); x.add(-5); print(x)
x.add(4); print(x)
x.remove(2); print(x)

# %% [markdown]
# ### 생각해볼 거리: 이름으로 쓸 수 있는 값
#
# > 딕는 원소를 이름으로 특정하고, 셋은 이름과 값이 동일한 경우로 역시 이름으로 원소를 특정한다고 생각할 수 있다. 이때 모든 값이 이름이 될 수 있을까? 

# %% [markdown]
# #### 연습문제
#
# 다음을 리스트로 구현해보세요.
#
# ```
# 이 그룹은 0번, ‘하현철’, 1번, ‘김상우’, 2번, ‘이만희’로 구성되어 있다.
# 이 그룹의 0번이 ‘김종철’로 변경되었다.
# 이 그룹의 마지막에 ‘우상호’가 추가되었다.
# 2번과 3번 사이에 ‘추자현’이 추가되었다.
# 3번이 제거되었다. 
# 이 그룹이 현재 상태는 무엇인가?
# ```

# %%
x = ['하현철', '김상우', '이만희']
x[0] = '김종철'; print(x)
x.append('우상호'); print(x)
x.insert(3, '추자현'); print(x)
del x[3]; print(x)

# %% [markdown]
# ## 임의의 여러 원소 
#
# |   |list   |tuple   |dict   |set   |
# |---|---|---|---|---|
# |Create     |`[1,2,3,4]`   |`(1,2,3,4)`   |`{'a':1, 'b':2, 'c':3, 'd':4}`   |`{1,2,3,4}`   |
# |Read   |`[x[i] for i in [1,-1]]`   |`tuple(x[i] for i in [1,-1])`   |`{k:x[k] for k in ['a', 'd']}`   | `elems.intersection(x)`  |
# |Edit   |*edit-list   | -   |*edit-dict   |`x.difference_update(elems_remove); x.update(elems_add)` |
# |Add (at the last)   |`x.extend([100,200])`   | -  |*edit-dict   |`x.update(elems_add)`   |
# |Add at the random position   |*add-list  | -   | -    | -    |
# |Remove |*remove-list   | -   |*remove-dict   | `x.difference_update(elems_remove)` |
# |Remove(모두)   |         `x.clear()`       |   -  |`x.clear()`         |    `x.clear()`    |
#
# * edit-list
#
# ```
# indices = [1, -1]
# values = [10,20]
#
# for i,v in zip(indices, values):
#     x[i] = v
# ```
#
# * edit-dict
#
# ```
# keys = ['a', 'd']
# values = [10, 20]
#
# for k,v in zip(keys, values):
#     x[k] = v
# ```
#
# * edit-set
#
# ```
# elems_remove = {1,4}
# elems_add = {10,20}
#
# x.difference_update(elems_remove)
# x.update(elems_add)
# ```
#
# * add-list
#
# ```
# elems_add = ['a', 'b', 'c']
# for e in reversed(elems_add):
#     x.insert(1, e)
# ```
#
# * remove-list
#
# ```
# indices = [-1, 1, -2] 
# # 순서에 따라 그 의미가 달라지므로...
# indices2 = [i if i>=0 else len(x)+i for i in indices]
# for i in sorted(indices2, reverse=True):
#     del x[i]
# ```
#
# * remove-dict
#
# ```
# keys_remove = ['a', 'd']
#
# for k in keys_remove:
#     del x[k]
# ```

# %%
elems_add = ['a', 'b', 'c']
print([i for i in elems_add])
print([i for i in reversed(elems_add)])
# 여기서 reversed()의 결과는 단순히 list가 아니라,
# iterator라고 하는 특별한 object이다. 
# 이에 대해서는 나중에 다룬다.

# %%
reversed(elems_add)


# %% [markdown]
# #### 참고

# %%
def reversed2(x):
    i = len(x)-1
    while i > -1:
        yield x[i]
        i=i-1


# %%
reversed2(elems_add)

# %%
x = [1,2,3]

# %%
[x[i] for i in range(len(x)-1,-1,-1)]

# %%
for i in reversed2(x):
    if i < 3: 
        break
    print(i)

# %%

# %%
print([i for i in reversed2(elems_add)])

# %% [markdown]
# ### list

# %%
x = [1,2,3,4,5,6]; print(x)

# Read
indices = [0,2,-1]
[x[i] for i in indices]; print([x[i] for i in indices])

# Edit
indices = [0,2,-1]
values = ['a', 'b', 'c']
for i,v in zip(indices, values):
    x[i] = v
print(x)

# Add
values = [-10,-20,-30]
x.extend(values)
print(x)

# Delete
indices = [-1, 1, -2] 
# 순서에 따라 그 의미가 달라지므로...
indices2 = [i if i>=0 else len(x)+i for i in indices]
for i in sorted(indices2, reverse=True):
    del x[i]
print(x)

x.clear()
print(x)

# %% [markdown]
# ### tuple

# %%
x = (1,2,3,4,5,6,7)

# Read
tuple(x[i] for i in [0,4,-1])

# %% [markdown]
# ### dict

# %%
x = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
print(x)

# Read
keys = ['a', 'b', 'e']
{k:x[k] for k in keys}; print({k:x[k] for k in keys})

# Edit
keys = ['a', 'b', 'e']
values = [-10, -20, -30]
for k, v in zip(keys, values):
    x[k] = v
print(x)

# Add = same as Edit
keys = ['g', 'h', 'i']
values = ['a', 'b', 'c']
for k, v in zip(keys, values):
    x[k] = v
print(x)

# Delete
keys = ['a', 'f', 'g']
for k in keys:
    del x[k]
print(x)

x.clear()
print(x)

# %% [markdown]
# ### set

# %%
x = {1,2,3,4,5,6,7}
print(x)

# Read
elems = {2,5,8}
# elems에서 x에 존재하는 원소는?
elems.intersection(x)
print(elems.intersection(x))

# Edit
elems_remove = {1,4,6}
elems_add = {10,40,60}
# 1,4,6을 10,40,60으로 바꿔라
x.difference_update(elems_remove)
x.update(elems_add)
print(x)

# Add
elems_add = {100,200}
x.update(elems_add)
print(x)

# Delete
elems_remove = {1,10,100}
x.difference_update(elems_remove)
print(x)

x.clear()
print(x)

# %%
x = {1,2,3}; print(x)

1 in x; print(1 in x)
# 1 in x에서 in의 경우 list, tuple, dict에서도 모두 사용 가능하고 의미도 비슷하다.
# 차이점은, list, tuple의 경우 1이 존재하는지 확인하기 위해서는 모든 원소를 확인해야 한다
# dict의 경우는 key:value에서 key의 존재를 확인한다.
x.remove(1); x.add(-5); print(x)
x.add(4); print(x)
x.remove(2); print(x)

# %% [markdown]
# #### 연습문제
#
# 다음을 딕셔너리(Dictionary)로 구현해보세요. 
#
# ```
# x 카페는 '아메리카노' 3500원, '카페라떼' 4500원, '레몬에이드' 5000원으로 메뉴를 구성하였다. 
# 여름 할인으로 '아메리카노'의 가격을 3200원으로 변경하였고, 신 메뉴를 출시하여 '수박쥬스'를 5500원에 판매하기로 하였다. 
# '레몬에이드'는 레몬 수급 불안정으로 판매를 하지 않기로 하였다.
# 현재 이 카페의 메뉴는 어떻게 구성되어 있는가?
# ```

# %%
x = {'아메리카노' : 3500, '카페라떼' : 4500, '레몬에이드' : 5000}; print(x)

menu = ['아메리카노', '수박쥬스']
count = [3200, 5500]
for k, v in zip(menu, count):
    x[k] = v
print(x)
del x['레몬에이드']; print(x)


# %% [markdown]
# ## 임의의 여러 원소 2
#
# 이번에는 list, tuple, dict, set를 조금 변형시켜 좀 더 편리하게 여러 원소를 다루는 방법을 소개한다.

# %%
class list2(__builtins__.list):

    def __getitem__(self, index):
        if isinstance(index, (slice, int)):
            return super().__getitem__(index)

        return list2([super(list2, self).__getitem__(x) for x in index])
        # np.array, np.series also possible
        #return [super().__getitem__(x) for x in index] # NOT WORKING
        
    def __setitem__(self, index, elem):
        if isinstance(index, (slice, int)):
            return super().__setitem__(index, elem)

        if len(index) != len(elem):
            raise ValueError("Number of elements in index does not match element.")

        for i, e in zip(index, elem):
            self[i] = e

    def __delitem__(self, index):
        if isinstance(index, (slice, int)):
            return super().__delitem__(index)

        for i in sorted(set(index), reverse=True):
            super().__delitem__(i)

    def __repr__(self):
        return f"list2({super().__repr__()})"
    
    
class tuple2(__builtins__.tuple):

    def __getitem__(self, index):
        if isinstance(index, (slice, int)):
            return super().__getitem__(index)

        return tuple2(super(tuple2, self).__getitem__(x) for x in index)
    
    def __repr__(self):
        return f"tuple2({super().__repr__()})"
        
class dict2(__builtins__.dict):
    
    def __getitem__(self, index):
        if isinstance(index, (tuple, list, set)):
            return dict2({i:super(dict2, self).__getitem__(i) for i in index})
            
        return super().__getitem__(index)

    def __setitem__(self, index, elem):
        if len(index) != len(elem):
            raise ValueError("Number of elements in index does not match element.")

        if isinstance(index, (tuple, list, set)):
            for i, e in zip(index, elem):
                super().__setitem__(i,e)
        else:
            return super().__setitem__(index, elem)

    def __delitem__(self, index):
        if isinstance(index, (tuple, list, set)):
            for i in index:
                super().__delitem__(i)
        else:
            return super().__delitem__(index)
        
    def __repr__(self):
        return f"dict2({super().__repr__()})"
    
class set2(__builtins__.set):
    
    def __getitem__(self, index):
        if isinstance(index, (tuple, list, set)):
            return [i in self for i in index]
            
        return index in self

    def __setitem__(self, index, elem):
        if isinstance(index, (tuple, list)):
            if len(index) != len(elem):
                raise ValueError("Number of elements in index does not match element.")
            for i in index:
                if not self[i]:
                    raise IndexError('Index list with nonexistent element')
            self.difference_update(index)
            self.update(elem)
        else:
            self.remove(index)
            self.add(elem)
            
    def __delitem__(self, index):
        if isinstance(index, (tuple, list)):
            self.difference_update(index)
        else:
            self.remove(index)
        
    def __add__(self, value, /):
        if isinstance(value, set):
            return self.union(value)
        elif isinstance(value, (tuple, list)):
            return self.union(set(value))
        else:
            raise ValueError("Only set can be added to a set")

    def __radd__(self, value, /):
        if isinstance(value, set):
            return self.union(value)
        elif isinstance(value, (tuple, list)):
            return self.union(set(value))
        else:
            raise ValueError("Only set can be added to a set")

    def __mul__(self, value, /):
        if isinstance(value, set):
            return set2(self.intersection(value))
        elif isinstance(value, (tuple, list)):
            return set2(self.intersection(set(value)))
        else:
            raise ValueError("Only set can be added to a set")

    def __rmul__(self, value, /):
        if isinstance(value, set):
            return set2(self.intersection(value))
        elif isinstance(value, (tuple, list)):
            return set2(self.intersection(set(value)))
        else:
            raise ValueError("Only set can be added to a set")
    def __repr__(self):
        #return f"set2({super(set2, self).__repr__()})"
        return f"{super(set2, self).__repr__()}"
        #return f"{__builtins__.set.__repr__(self)}"



# %% [markdown]
#
# |   |list2   |tuple2   |dict2   |set2   |
# |---|---|---|---|---|
# |Create     |`list2([1,2,3])`   |`tuple2(1,2,3)`   |`dict2({'a':1, 'b':2, 'c':3})`   |`dict({1,2,3})`   |
# |Read   |`x[1,-1]` or `x[[1,-1]]`   |`x[1,-1]`   |`x['a', 'c']`  | `x[1,2]`  |
# |Edit   |`x[1,-1] = ['a', 'b']`   | -   |`x['a', 'c'] = ['A', 'C']`  |`x[1,2] = ['a', 'b']` |
# |Add(마지막에)    |`x.extend([10,100])` | - | - | - |
# |Add(중간에)    |`x[3:3] = [10,100]` | - | `x['AA','AAA'] = [11,111]` | `x.update(['A', 'B'])`|
# |Remove |`del x[1,-1]`   | -   |`del x['a', 'c']`   | `del x[1,2]` |
#
#

# %% [markdown]
# ### list2

# %%
x = list2([1,2,3,4,5,6,7,8]); print(x)
x[1, 4, -1]; print(x[1, 4, -1])
x[0, -2] = [3, 'b']; print(x)
x.extend(['l', 'll']); print(x)
x[1:1] = ['A', 'AA', 'AAA']; print(x) # 1번째 원소 바로 앞에 추가
del x[0,1,2]; print(x)

# %% [markdown]
# ### tuple2

# %%
x = tuple2([1,2,3,4,5,6,7,8]); print(x)
x[1, 4, -1]; print(x[1, 4, -1])

# %% [markdown]
# ### dict2

# %%
x = dict2({'a':0, 'b':1, 'c':2, 0:'a', 1:'b', 2:7}); print(x)
x['a', 'b', 0]; print(x['a', 'b', 0])
x['a', 'b', 0] = [-1, -2, -3]; print(x)
x['A', 'B'] = [-11, -22]; print(x)
del x['a', 'b', 'A', 'B', 0]; print(x)
x.clear(); print(x)

# %% [markdown]
# ### set2

# %%
x = set2({1, 2, 3, 4, 5,'a', 'b', 'c'}); print(x)
x[1,2,'a']; print(x[1,2,'a'])
x[4,'b'] = [44, 'B']; print(x)
# Index가 존재하지 않는 원소라면 IndexError 발생
x.update({'AA', 'BB'}); print(x)
del x[1,2,'a']; print(x)


# %%

# %% [markdown]
# * `list()` 역시 R과 비슷하게 만들 수 있다.

# %%
def list(*args):
    if len(args) > 1:
        return [*args]
    else:
        return __builtins__.list(args[0])


# %%

# %% [markdown]
# ## 연속적인 여러 원소: 슬라이스(`slice`)
#
# 리스트와 튜플의 경우 `start:stop:step`의 꼴로 원소를 읽거나, 수정, 삭제할 수 있다.
#
# 예를 들어, `x = [0,1,2,3,4,5,6,'a','b','c','d','e']`에서,
# `x[1:8:3]`은 1-번째 원소에서 8-번째 **직전** 원소까지 중에서 0,3,6,9번째 원소를 의미한다.
# 여기서 **직전**에 유의하자. 8-번째 원소까지가 아니라, 8-번째 **직전** 원소까지이다.

# %%
x = [0,1,2,3,4,5,6,'a','b','c','d','e']
x[1:8:3]; print(x[1:8:3])
x[1:8:3] = ['A', 'B', 'C']; print(x)
del x[1:8:3]; print(x)

# %% [markdown]
# `x[start:stop:step]`에서 `step`은 0이 아닌 양의 정수와 음의 정수가 가능하며,
# 음의 정수는 리스트 원소를 역순으로 참조한다.

# %% [markdown]
# ### 참조

# %%
x = [0,1,2,3,4,5,6,'a','b','c','d','e']
x[8:1:-3]; print(x[8:1:-3])

# %% [markdown]
# 원소의 위치를 나타내는 `start`, `end`는 0, 양의 정수, 음의 정수가 가능하며,
# 0은 처음에서 0-번째, -1은 뒤에서 0번째 위치를 가리킨다.
# -1이 **뒤에서 0-번째**라는 것이 헷갈린다면,
# -1은 앞에서 `len(x)-1`번째에서 `len(x)`를 생략한 것으로 생각할 수 있다.
#
# 참고로,
# 리스트 `x`의 원소 갯수는 `len(x)`이고, 
# `x[0]`은 `x`의 가장 앞쪽 원소이며,
# `x[len(x)-1]`은 `x`의 가장 뒤쪽 원소이다.
# `x[len(x)]`는 존재하지 않기 때문에 IndexError가 발생하게 된다.

# %%
x = ['a', 'b', 'c', 'd', 'e', 'f']; print(len(x))
x[0]; print(x[0])
x[len(x)-1]; print(x[len(x)-1])
x[len(x)]; print(x[len(x)])


# %% [markdown]
# `x[start:stop:step]`에서 `start`, `end`, `step`은 필요에 따라 생략될 수 있다.
# `step`이 양수일 때, `x[::step]`에서 `x[:]`은 `x`의 모든 원소를 의미한다.
# 따라서 `x[0:len(x)]`와 같다.(여기서 `x[0:len(x)-1]`이 아님을 유의하자.)
#

# %%
x = ['a0', 'b1', 'c2', 'd3', 'e4', 'f5', 'g6', 'h7', 'i8', 'j9']
x[0:-1:3]; print(x[0:-1:3])

# %% [markdown]
# 위의 예에서 `x[0:-1:3]`은 0-번째 원소에서 가장 마지막 원소 **직전**까지 원소 중에서 0,3,6,9,...번째 원소를 의미한다. 
# 따라서 `x[0:-1]`은 `['a0', 'b1', 'c2', 'd3', 'e4', 'f5', 'g6', 'h7', 'i8']`이고, 
# 여기서 0,3,6,9,...번째 원소를 고르면, 결과는 `['a0', 'd3', 'g6']`가 된다.

# %%
x[::3]

# %% [markdown]
# `step`이 음수일 때에도 `x[::step]`에서 `x[:]`은 `x`의 모든 원소를 의미한다.
# 이때에도 `x[:]`를 풀어쓰면 `x[-1:-len(x)-1]`이 된다.
#
# `x[-len(x)]`은 가장 앞쪽의 원소이고, `-len(x)-1`은 그보다 앞선 위치를 가리킨다. 
#
# (`x[-1:0:-1]`은 가장 앞쪽 원소를 제외하게 됨을 유의하자.)

# %%
x[-len(x)]

# %%
x[::-3]

# %%
x[-1:-len(x)-1:-3]

# %%
x[-1:0:-3]

# %% [markdown]
# `x[start:stop:step]`에서 `step`이 양수일 때, `stop`이 가리키는 위치가 `start`의 위치와 같거나, 작다면, 그 결과는 `[]`(빈 리스트)가 된다.

# %%
x[4:3:1]

# %%
x[-1:-2:1]

# %%
x[3:3]

# %% [markdown]
# `step`이 음수인 경우도 쉽게 유추할 수 있을 것이다. 

# %%
x[3:4:-1]

# %% [markdown]
# 이렇게 `x[start:stop:step]`에서 `start:stop:step`에 원소가 존재하지 않을 때에는 빈 리스트가 반환된다. 
# 만약 `start:stop:step` 중 일부에 원소가 존재하지 않을 때에는 어떻게 될까?

# %%
x = ['a0', 'b1', 'c2', 'd3', 'e4', 'f5', 'g6', 'h7', 'i8', 'j9']
x[5:15:3]; print(x[5:15:3])

# %% [markdown]
# `x[5:15:3]`는 `x`의 5-번째 원소에서 14-번째 원소 중에서 0,3,6,... 번째 원소를 골라낸다. 
# 따라서 `x`의 5,8,11,14-번째 원소가 된다. 이때 `x`의 11, 14-번째 원소는 존재하지 않기 때문에 단순히 무시된다.

# %% [markdown]
# 한 가지 유의할 점은 `step`이 음수일 때다.
# `x[14:4:-3]`의 결과는 무엇일까? 
# 방금 전과 같이 계산하면, `x`의 14, 11, 8, 5-번째 원소 중에서 존재하는 원소인 8, 5-번째 원소가 반환될 것 같다. 

# %%
x[14:4:-3]

# %% [markdown]
# 결과는 그렇지 않다. `x[14:4:-3]`이 계산되는 방식은 `x[14:4]`에서 `x`의 14,13,12,11,10-번째 원소는 존재하지 않으므로, 
# `x[14:4]`가 `x[9:4]`로 바뀐 후, `x[9:4:-3]`이 반환되는 형식인 듯 하다.

# %% [markdown]
# ### 수정

# %% [markdown]
# 수정을 할 때에는 참조 결과로 예상되는 원소의 갯수만큼 수정할 원소를 리스트를 묶어 주면 된다.

# %%
x = ['a0', 'b1', 'c2', 'd3', 'e4', 'f5', 'g6', 'h7', 'i8', 'j9']
x[1:9:3] = ['_A', '_B', '_C']; print(x)

# %% [markdown]
# 만약 참조되는 원소의 갯수와 등호로 연결된 리스트 원소의 갯수가 다르다면 오류가 발생한다.

# %%
x[1:9:3] = ['_X', '_Y']; print(x)

# %% [markdown]
# 하지만 슬라이싱의 결과가 빈 리스트라면, 이런 제약이 없어진다. 다음을 보자.


# %%
x[1:1] = ['_X', '_Y']; print(x)

# %%
x[14:13:1] = [10,100]; print(x)

# %% [markdown]
# `x[start:start] = [a,b,c, ...]`는 `x`의 `start`-번째 위치 앞에 원소 `a`, `b`, `c`, ...를 추가할 때 쓸 수 있다.

# %% [markdown]
# `x[:start] + [a,b,c,...] + x[start:]`으로 새로운 리스트를 생성할 수도 있다. 

# %%
x = [1,10,100]
x[:1] + ['aa', 'bb'] + x[1:]

# %%

# %% [markdown]
# `x[start:stop:end]`는 왜 `start`에서 시작해서 `stop` **직전**인가?
#
# `x` 전체를 다음과 같이 간단하게 slice 가능하다. 
# `x[:2] + x[2:5] + x[5:]`

# %%
x = [0,1,2,3,4,5,6,7,8]
x[:2] + x[2:5] + x[5:]

# %% [markdown]
# 심지어 인덱스가 start < stop을 만족한다면, 길이를 벗어나는 경우에도 항상 성립한다.

# %%
x[:10] + x[10:20] + x[20:]

# %% [markdown]
# 하지만,

# %%
x[:-1] + x[-1:3:1] + x[3:]

# %% [markdown]
# 비교

# %%
x[:7:-1] + x[7:3:-1] + x[3::-1]

# %% [markdown]
# ### 삭제
#
# 슬라이싱을 사용하여 원소를 삭제할 때에는 참조되는 원소가 삭제된다.

# %%
x = ['a0', 'b1', 'c2', 'd3', 'e4', 'f5', 'g6', 'h7', 'i8', 'j9']; print(x)
del x[3::3]; print(x)

# %%

# %%
x = [1,3,2,5,6]

# %%
y = x[4]

# %%
y 

# %%
y = 'a'

# %%
x

# %%
y = x

# %%
y[0] = 'a'

# %%
x

# %%
y = x[2:5] # 이건 copy

# %%
y[0] = 'a'

# %%
x

# %% [markdown]
# #### 연습문제(리스트 슬라이싱)
#
# 다음을 리스트 슬라이싱으로 구현해보세요.
#
# ```
# 1부터 20까지의 리스트를 생성하여 5부터 10까지 원소 출력하세요.
# 리스트의 원소 중 짝수만 출력하세요. 
# 리스트의 원소를 역순으로 홀수만 출력하세요. 
# 리스트의 11부터 15까지의 원소를 제거하여 해당 위치에 원소 'a', 'b', 'c', 'd' ,'e' ,'f'를 추가하세요.
# 원소 중 'e', 'f'를 제거하세요.
# ```

# %%
x = list(range(1, 21)); print(x)
print(x[5:11]) # 5 ~ 10 출력
print(x[::2]) # 짝수만 출력
print(x[19::-2]) # 홀수만 역순으로 출력
print(x[10:-5]) 
x[10:-5] = ['a', 'b', 'c', 'd', 'e', 'f']; print(x)
del x[14:16]
print(x)

# %% [markdown]
# ## 가변(mutable)객체, 불변(immutable)객체
#
# 위의 예에서 리스트는 원소를 수정 또는 삭제할 수 있었으나, 튜플의 경우는 그럴 수 없었다. 이렇게 내용을 수정할 수 있는 객체(object)를 **가변** 객체라고 하고, 수정할 수 없는 객체를 **불변** 객체라고 한다.

# %%
x = [1,3,2,4]
y = (1,3,2,4)

# %%
x[2] = 10

# %%
y[2] = 10

# %%
del x[2]

# %%
del y[2]

# %%
x.append(5)

# %%
y.append(5)

# %%
del x

# %%
del y

# %% [markdown]
# 위의 예를 보면 `del y[2]`는 불가능하지만, `del y`은 가능하다. 이 둘의 차이는 무엇인가?

# %% [markdown]
# ### 변수가 저장하는 것은?
#
# `y=(1,3,2,4)`은 튜플 `(1,3,2,4)`를 만들고, 변수 `y`가 이 튜플을 가리키게 한다. 여기서 중요한 것은 변수 `y`에 튜플이 담겨 있는 것이 아니라, 변수 `y`는 단순히 튜플 `(1,3,2,4)`를 가리킨다는 사실이다.
#
# 이 구분은 중요한 이유는 동일한 튜플을 다른 변수가 가리킬 수도 있기 때문이다. 다음을 보자.

# %%
y1 = (1,3,2,4)
y2 = y1
print(y1)
print(y2)

# %%
print(id(y1))
print(id(y2))
id(y1) == id(y2)

# %% [markdown]
# 같은 대상, 다른 이름(alias). 

# %%
a=[1,3,7]
b=a
a[1] = 5
print(a)
print(b)

# %%
id(a) # id(a) : 변수 a가 가리키는 곳

# %%
id(b)

# %%
id(a) == id(b) # 변수 a와 변수 b는 정확하게 같은 지점을 가리킨다.

# %% [markdown]
# ## Hashable
# * 딕셔너리의 키나 셋의 원소가 될 수 있는 자격)

# %%

# %%

# %%
