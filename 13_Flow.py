# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: p38r2py
#     language: python
#     name: p38r2py
# ---

# # 재연 가능성을 위한 조치들
#
# * 환경 저장 및 설치
#
#     - `pip freeze > requirements.txt`
#
#     - `pip install -r requirements.txt`

# * 변수 모두 제거하기
#     - `%reset -f`

# # 13. 흐름 제어와 함수

# ### 13.1 제어문: 조건과 반복

s = 'here'
if s == 'here':
    print('Seoul')
else:
    print('Somewhere else than Seoul')


import pandas as pd
s_ser = pd.Series(s)

s_ser[s_ser == "here"] = "Moon"

s_ser[s_ser != "here"] = "Somewhere else Moon"

s_ser



s_out = pd.Series(['Moon', 'Somewhere else Moon'])

s_ser = pd.Series(['here', 'LA', 'here', 'SF', 'here', 'here', 'Paris', 'Chiangmai'])

s_out[(s_ser == "here").astype('int')]



# Python에는 딱히 R의 `switch`와 대응되는 함수가 없다.
# 그에 대한 논의는 [PEP 3103](https://www.python.org/dev/peps/pep-3103/)에서 확인할 수 있다.
# 굳이 번역을 하고 싶다면 다음의 예를 보자.

dict_switch = {'one' : 1, 
               'two' : 2}

x = 'two'
dict_switch.get(x, 3) # default = 3


# +
def f_two():
    y = x + ' is entered.'
    return (z+1)

def f_three():
    return z**2


# -

x = 'two'
z = 3
dict_switch = {'one':1, 
               'two':f_two,
               'three':f_three}

dict_switch.get(x)

# +
# 만약 함수를 사용하려면,

x = 'two'
def f_one(a):
    print(a[:1])

def f_two(a):
    print(a[:2])

def f_three(a):
    print(a[:3])

def f_default(a):
    print(a[0])

dict_switchf = {'one':f_one, 
                'two':f_two,
                'three':f_three}

dict_switchf.get(x, f_default)(x)

# -



# ### 13.1.2 반복문
#

s = 0
for i in range(1,11):
    s = s + i
print(s)

s = 0; i = 1
while i <= 10:
    s = s + i
    i = i + 1
print(s)

# python에는 R의 `repeat`(또는 흔히 말하는 `do`~`while`구문)에 해당하는 구문이 없다.
# 하지만 다음과 같이 고쳐 쓰는 것이 가능하다. 꼭 필요하다면 말이다.

s = 0; i = 1
while True:
    s = s + i
    i = i + 1
    if i <= 10:
        continue
    break
print(s)

s = 0; i = 1
while True:
    s = s + i
    i = i + 1
    if i > 10:
        break
print(s)

# ### 13.1.3 다중반복문

for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            if (i+j+k == 15): break
        if (i+j+k == 15): break
    if (i +j+k == 15): break
print(i,j,k)


def f():
    for i in range(1,11):
        for j in range(1,11):
            for k in range(1,11):
                if (i+j+k == 15): return(i,j,z)
i,j,k = f()
print(i,j,k)

# ### 13.1.4 반복문 다시 보기

s = 0
for i in range(1,11):
    s = s + i
print(s)

# +
xs = pd.Series([1,3,5,9,15])
s = list()

for x in xs:
    s.append(x**2)    
print(s)
# -

xs = pd.Series([1,3,5,9,15])
#s = list()
s = pd.Series([]*5)
for i, x in enumerate(xs):
    #s.append(i**2)
    s[i] = x**2
print(s)

s = xs**2
s



# +
#xs = pd.Series([1,3,5,9,15])
#s = pd.Series([]*5)
xs = pd.Series([])
s = pd.Series([]*len(xs))

for i,x in enumerate(xs): # R에서와 같은 문제가 없음!
    s[i] = x**2
# -

s



# ### 13.1.4.2 반복문의 대체

import numpy as np

x = pd.Series([1,3,5,9,15])
s = np.sqrt(x)
s

x = pd.Series([1,3,5,9,15])
s = x.apply(lambda x: np.sqrt(x))
s

x = pd.Series([1,3,5,9,15])
s = x.apply(np.sqrt)
s



dict_switch = {'one':1, 'two':2}
def tonum(x):
    return dict_switch.get(x, 3)



xs = ['one', 'three', 'two', 'four', 'two']
[tonum(x) for x in xs]

xs = ['one', 'three', 'two', 'four', 'two']
tonums = np.vectorize(tonum)

tonums(xs)

xs = pd.Series(['one', 'three', 'two', 'four', 'two'])
xs.apply(tonum)

# (p207)
#
# ### 13.1.4.3 `for`의 몇 가지 변형

# * `for x in xs:`
# * `for i,x in enumerate(xs):`
# * `for x,y in zip(xs,ys):`

pd.Series([])



np.nan

# +
# Initializing a list
# https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size
# -

l = [None] * 10
l

l = [ [] for _ in range(10)]
l

xs = pd.Series([1,3,2,4])
result = [np.nan] * len(xs)
for i,x in enumerate(xs):
    result[i] = pd.Series([x]*x)


result

# +
### ??? 어떻게 list를 다 합치나???

# +
# 참고
## https://stackoverflow.com/questions/13653030/how-do-i-pass-a-list-of-series-to-a-pandas-dataframe
# -

#https://stackoverflow.com/questions/30885005/pandas-series-of-lists-to-one-series
pd.Series(result).apply(pd.Series).stack().reset_index(drop=True)

pd.Series(result).sum()

pd.Series(result).explode()

pd.DataFrame({'a':[[1,2],['a', 'b']],
              'b':[1,2]}).explode('a')
              # 리스트를 row로

xs = pd.Series([1,3,2,4])
result = [np.nan] * len(xs)
for i,x in enumerate(xs):
    result[i] = [x]*x

result

pd.Series(result)

pd.__version__


res2 = [np.array(x) for x in result]

np.array(res2).flatten()

# outer level에서 pd.Series를 list로, list를 pd.Series로???


pd.Series([[1,2,3],3])

pd.Series([[1,2,3],3]).tolist()

np.array(pd.Series([[1,2,3],3]).tolist())

# +
import itertools

[x for x in itertools.chain(*[[1,2,3],4])]
# -
for x in itertools.chain(*[[1,2,3],[2,3]]):
    print(x)

# 리스트를 chain처럼 연결해줌
for x in itertools.chain(*[[1,2,3],[2,3], [['a', 'b'], [['c'], 'd']]]):
    print(x)


import functools
import operator
functools.reduce(operator.iconcat, [[1,2,3],4], [])

l = [[1,2,[4,3],3], 4, [4,3,2]]
l = ['a', ['ab', 'bc'], 'c', [['a']]]

# [https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists](https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists)

from pandas.core.common import flatten
list(flatten(l))

# (p.207)
# ### 13.1.4.4 반복문의 속도 비교

mat1 = np.arange(1000).reshape(1,-1)
mat2 = np.ones((1000,1000))

mat = mat1 * mat2

mat[:5, :5]

mat[995:1000, 995:1000]


result0 = np.sum(mat, axis=0)  # result <- colSums(mat)

result1 = np.apply_over_axes(np.sum, mat, 0)

np.sum(result0 != result1)

result2 = [None] * 1000
for i in range(mat.shape[0]):
    result2[i] = np.sum(mat[:,i])

np.sum(result1 != result2)

# %timeit result0 = np.sum(mat, axis=0) 

# %timeit result1 = np.apply_over_axes(np.sum, mat, 0)

# %%timeit 
result2 = [None] * 1000
for i in range(mat.shape[0]): 
    result2[i] = np.sum(mat[:,i])    

# +
# 참고 

# +
# numpy operations vs. standard library  (random can be predicted)
#https://stackoverflow.com/questions/52603487/speed-comparison-numpy-vs-python-standard

# -> numba https://pythonkim.tistory.com/95

# +
# #%conda install numba
## Package Plan ##

#   environment location: /home/ubuntu/anaconda3/envs/p38r2py

#   added / updated specs:
#     - numba


# The following NEW packages will be INSTALLED:

#   libllvm10          conda-forge/linux-64::libllvm10-10.0.1-he513fc3_3
#   llvmlite           conda-forge/linux-64::llvmlite-0.34.0-py38h4f45e52_2
#   numba              conda-forge/linux-64::numba-0.51.2-py38hc5bc63f_0


# -



s = 0
for i in range(1,6):  # 1 부터 6 바로 전까지
    s = s + i
print(s)

for i in range(1,6):
    print(i, end=' ')

# +
s = 0
for i in range(1,11):  # 1 부터 10 바로 전까지
    s = s + i
print(s)

s = 0
for i in range(1,21):  # 1 부터 20 바로 전까지
    s = s + i
print(s)


# -

# 달라지는 부분을 변수로 나타낸다.

# + active=""
# s = 0
# for i in range(1,n+1):
#     s=s+i
# print(s)
# -

# 전체를 indent한다.

# + active=""
#     s = 0
#     for i in range(1,n+1):
#         s=s+i
#     print(s)
# -

# 반환값을 명시한다.

# + active=""
#     s = 0
#     for i in range(1,n+1):
#         s=s+i
#     print(s)
#     return(s)
# -

# 함수의 이름과 인자를 명시한다.

def sumToN(n):
    s = 0
    for i in range(1,n+1):
        s=s+i
    print(s)
    return(s)


sumToN(5)
sumToN(10)
sumToN(20)


# ### 13.2.3 함수의 인자

# +
# https://www.w3schools.com/python/python_functions.asp
# parameter? argument?
# -

def f(a,b=3):
    print(a)


f(1)


def f(b, a=3, *arg):
    print(a)



# #### 리스트 인자(기본값)

def f(a, b=[]):
    b.append(3)
    print(b)


f(1)

f(2)

f(3)

x = [3]

f(3,x)

f(3,x)


def g(a, b=[]):
    b = b+[3]
    print(b)


g(2), g(2), g(2)

g(2,[33]), g(2,[34])


# +
## list.append와 list+list의 차이?
# -

def g(a, b=[]):
    b.append(3)
    print(b)


g(2), g(2), g(2)

g(2,[33]), g(2,[34])


def g(a,b, *args):
    print(a,b)
    #if 존재여부 확인?
    #print(locals())
    #print(locals().keys())
    if 'args' in locals():
        for i in range(len(args)):
            print(args[i], end=' ')



locals()

g(3,2)

g(b=3,a=2)

g(3,2,5,4)



def g(a,b, *args, **kwargs):
    print(a,b)
    #if 존재여부 확인?
    #print(locals())
    #print(locals().keys())
    if 'args' in locals():
        for i in range(len(args)):
            print(args[i], end=' ')
    print('')
    if 'kwargs' in locals():
        for k in kwargs.keys():
            print(k, '=', kwargs[k], end=' ')


g(1,2,3,4,5,ab=3,bb=3)


def g(a,b=3, *args, **kwargs):
    print(a,b)
    #if 존재여부 확인?
    #print(locals())
    #print(locals().keys())
    if 'args' in locals():
        for i in range(len(args)):
            print(args[i], end=' ')
    print('')
    if 'kwargs' in locals():
        for k in kwargs.keys():
            print(k, '=', kwargs[k], end=' ')


g(1,2,3,4,5,ab=3,bb=3)

g(1,2,3,4,5,b=3,bb=3)

# +
## 여전히 positional arguments와 keyword arguments가 헷갈리네...???!!!
# -


