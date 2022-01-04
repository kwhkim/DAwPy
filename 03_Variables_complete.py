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
# ### TO-DOs
# * 타입 어노테이션?
# * global(), vars(), locals(), dir() 차이?
# * 

# %% [markdown]
# # 3. 파이썬의 변수, 자료형, 연산/함수
#

# %% [markdown]
# ## 3.1 파이썬의 변수
#
# 파이썬의 변수는 동적 타입이다: 변수의 타입이 코드가 실행되는 도중에 바뀔 수 있다.
# 숫자, 문자, 분석 결과 등은 모두 파이썬의 객체(Object)에 담을 수 있다. 
# 사실 우리가 파이썬에서 다루는 거의 모든 것은 객체이다. 숫자 `3` 역시 객체이다.
# 다음을 보자. `type(3)`은 `int`이고, `int`에 대한 설명을 보면 `class int in module builtins`라고 나온다.
# 숫자 `3`은 모듈 `builtins`에서 정의한 클래스의 인스턴스이다(이 설명을 잘 이해 못하겠다면 파이썬의 클래스/인스턴스을 참조하라).
# 보통 클래스 이름은 첫 글자를 대문자로 하는데 이 경우는 매우 자주 쓰이기 때문에 소문자로 시작하는 듯 하다.

# %%
type(3)

# %%
help("int")
# Help on class int in module builtins:
# 
# class int(object)
# |  int([x]) -> integer
# |  int(x, base=10) -> integer

# %% [markdown]
# 변수는 그 내용이 변할 수 있기 때문에 변수이다. 파이썬에서 변수란 어떤 객체를 가리키는 지시자이다. 예를 들어 변수 `x=3`으로 변수 `x`에 `3`을 담았다고 말할 수 있겠지만, 좀더 정확하게 설명하면 변수 `x`는 객체 `3`을 가리킨다. 하지만 `x=3`의 경우에는 변수 `x`에 `3`이 담겨 있다고 말해도 개념적으로 크게 다르지 않다. 이에 대한 자세한 내용은 이 장의 내용을 끝까지 읽어나가면 이해할 수 있을 것이다. 

# %% [markdown]
# ## 3.1.1 변수의 이름
#
# 파이썬에서는 변수 이름에 알파벳, 숫자, _을 활용할 수 있다. 
# R과 달리 .(점)은 사용할 수 없다.
# Python에서 .(점)은 Class의 attribute을 가리키거나 module의 변수, 함수를 지칭하기
# 위해 사용된다.
# 첫 글자는 숫자가 될 수 없다.
#
# 간명한 변수 이름을 짓는 것은 언제나 쉽지 않다.
# 파이썬에는 PEP(Python Enhancement Proposal)이라는 것이 있다.
# PEP에는 파이썬에 추가되면 좋을 기능, 파이썬를 사용하여 코드를 작성할 때 활용할 수 있는 표준 등이 제안된다.
# PEP에는 모듈 이름, 패키지 이름, 클래스 이름, 메쏘드 이름, 예외 이름, 함수 이름, 전역 상수 이름
# 전역 변수이름, 지역변수 이름, 인스턴스 이름, 인스턴스 변수 이름, 함수 매개변수 이름에 대한
# 표준 방식이 제안되기도 한다. 
#
# * 참고 자료: [https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names]
#
# 몇 가지 규칙은 다음과 같다.
#
# * `_`로 시작하는 이름은 내부용 변수 이름으로 쓴다.
# * 클래스 이름은 대문자로 시작한다.
# * 상수 이름은 모두 대문자로 한다.
# * 파이썬의 변수 이름은 snake 이름(단어를 밑줄로 연결한 형식)이 주로 사용된다.

# %%
myAge = 22
year = 2018
day_of_Month = 3 #Alphabets, numbers, '.', '_'
#stock.high = 13322
whatIGotForMy23thBirthday = "flowers"
print(myAge)
print(year)
print(day_of_Month)
print(whatIGotForMy23thBirthday)

# %% [markdown]
# ## 3.1.2 변수 할당

# %% [markdown]
# 변수 할당을 위해서는 =를 사용한다.
# 여러 변수를 한꺼번에 할당할 수도 있다.
# 이때 만약 **mutable**인 대상을 할당할 경우에는
# 모든 변수가 모두 같은 내용을 항상 공유하므로 유의할 필요가 있다.
# (**mutable**(가변 객체)에 대해서는 후에 설명된다.)
#
# R과 다르게 `<-` 또는 `->`를 사용할 수 없다.
# R과 다르게 별칭(alias)이 자주 쓰인다. (별칭이란 변수가 가리키는 대상이 동일한 경우에 또다른 이름이란 뜻이다)

# %%
a = 3
b = 2
# d <- -1
d = -1
# e1 <- e2 <- 7
e1 = e2 = 7
print(a, b, d, e1, e2)

# %%
e1 = e2 = e3 = 10
e2 = 3
print(e1, e2, e3)

# %% [markdown]
# 다음의 코르를 보자. 
# e3는 리스트 [1,2,3,4]를 가리키고, e1=e2=e3를 통해 e1, e2는 e3와 동일한 객체를 가리키는 별칭이다.
# e1[0]=-1로 리스트의 첫 번째 원소를 바꾸지만, 동일한 객체를 가리키는 e2, e3의 첫 번째 원소도 바뀐다. 

# %%
e1 = e2 = e3 = [1,2,3,4]
e1[0] = -1
print(e3) 

# %% [markdown]
# 이를 방지하기 위해서 **mutable**은 복사를 한다. 이때 얕은 복사(shallow copy)와 깊은 복사(deep dopy)의 구분을 유의하자. 얕은 복사는 가장 높은 수준에서만 복사를 한다. 깊은 복사는 가장 낮은 수준까지 복사한다.

# %% [markdown]
# #### 깊은 복사
#
# `copy.deepcopy()`를 사용하여 리스트를 깊게 복사할 경우, 그 결과로 새로운 리스트가 생성된다. 다음의 코드에서 `e1`를 깊게 복사하여 `e2`를 만들면(`e2=copy.deepcopy(e1)`) `e2`와 `e1`는 내용이 같지만 서로 다른 객체이며, 메모리의 다른 곳에 저장된다. `e1`이 가리키는 객체의 메모리 주소는 `id(e1)`으로 확인할 수 있다. 

# %%
import copy

a = [1,2,3]
b = ['a', 'b', 'c']
e1 = [1,2,3, a,b]
e2 = copy.deepcopy(e1)
e1[0] = 100
a[0] = 100
print(e1)
print(e2) 
print(id(e1), id(e2))

# %%
copy.__file__ # 모듈 copy는 파이썬 표준 모듈의 일원이다.

# %% [markdown]
# #### 얕은 복사
#
# `.copy()` 또는 `copy.copy()`로 복사한 경우는 얕은 복사이다. 가장 높은 수준에서는 복사가 이루어지지만, 그 다음 단계에서는 동일한 객체를 가리킨다.
#
# 다음 코드에서 `e2=e1.copy()`를 하면 `e1`의 원소인 `[1,2,3,a,b]`가 복사되어 `e2`가 된다. 이때 `1`,`2`,`3`은 복사가 되고, `a`, `b`는 내용이 아니라 주소만 복사가 된다. `e2=e1`를 하면 `e1`의 주소가 `e2`의 주소가 된다는 것과 비교해보자. (조금 더 정확한 설명은 `[1,2,3,a,b]`를 얕은 복사를 하면 각 원소의 주소가 복사된다. 이때 `1`,`2`,`3`는 immutable(불변객체)이기 때문에 주소를 복사하는 것과 대상을 복사하는 것이 차이가 없다. 좀더 자세한 내용은 후에 설명된다.)
#
# 그래서 `e1`과 `e2`가 가리키는 내용의 메모리 주소는 다르지만, `e1[3]`과 `e2[3]`는 동일한 주소에 저장되어 있고, 하나를 바꾸면 다른 것도 바뀐다. (`e1[3]`은 `e1`의 4번째 원소를 가리킨다. 파이썬에서는 `e1[0]`이 `e1`의 첫 번째 원소이다. 하지만 `e1[0]`에서 `0`이기 때문에 0-번째 원소라고도 부른다. 이런 명명법을 사용할 경우(0번째부터 시작할 경우) `e1[3]`은 `e1`의 3-번째 원소이다. 다시 말해, `e1[3]`은 "**파이썬 방식으로**" 또는 "**0-번째부터 시작하면**" 3-번째 원소이다.)

# %%
a = [1,2,3]
b = ['a', 'b', 'c']
e1 = [1,2,3, a,b]
e2 = e1.copy()
e1[0] = 100
a[0] = 100
print(e1)
print(e2) 
print(id(e1), id(e2))
print(id(e1[3]), id(e2[3]))

# %% [markdown]
# 만약 변수 이름이 문자열 변수에 저장되어 있다면 어떻게 할당해야 하나? 예를 들어 `varname`에 `"myVar"`이라는 값이 저장되어 있다면 `myVar=10`을, `varname`에 `"amount"`가 저장되어 있다면 `amount=10`를 해야 한다면? R에서는 쉽게 `assign(varname, 10)`을 하면 되지만 파이썬에서는 쉽지 않다. 변수 이름이 변수로 저장되어 있을 때 변수를 할당하는 방법은 이 장의 마지막에서 소개하겠다. 

# %% [markdown]
# ## 3.1.3. 변수관리

# %%
# rm(list = ls())
# del 사용해서 모든 변수 제거가능??

a = 2
# b = function(x) x^2
def b(x):
    return x**2
cc = "Now"


# ls()
globals()  # 글로벌 변수 # jupyter notebook에서와 python script에서 결과가 다르다.

# %%
locals() 

# %%
vars() # 인자 없이 사용하는 vars()는 locals()랑 같다


# %%
# str(a); str(b); str(c)
# ls.str()
def types_list(var):
    res = []
    for i,x in enumerate(var):
        #print(x)
        if isinstance(x, list):        
            res.append(types_list(x))
        else:
            res.append((type(x), x))
            # or res.append(type(x))
    return res
x = ['a', 3, ['b', 4, ['c', 5], [3,2]]]
types_list(x)

# %%
# exists("a"); exists("d")
'a' in globals(), 'b' in globals()

# %%
print(type(a), type(b), type(cc))
#
#

# %%
# ls()
# rm("a")
del a

# %%
_i10

# %%
len(In), len(_)

# %%
[In[x] == _[x] for x in range(len(In))]

# %%
# ?dir

# %%
# ls()
set(dir()) - set(dir(__builtins__)) # jupyter notebook
# !!! __annotations__, __builtins__???

# %%
# rm(list=ls())
for x in set(dir()) - set(dir(__builtins__)):
    if not x.startswith('_') and x not in ['In', 'Out', 'quit', 'exit']:  # jupyter notebook
        print('VARIABLE NAME = '+x)
        print(eval(x))
        print('-'*60)

# %%
b

# %%
# rm(list=ls())
# https://stackoverflow.com/questions/51982189/equivalent-of-rs-ls-function-in-python-to-remove-all-created-objects
for x in set(dir()) - set(dir(__builtins__)):
    if not x.startswith('_') and x not in ['In', 'Out', 'quit', 'exit']:
        print('deleting '+x)
        exec('del '+x)
del x

# %%
dir()
# !!! 위의 vars(), globals(), locals()와는 어떻게 다른가?

# %%
# ls()
for x in set(dir()) - set(dir(__builtins__)+[x for x in dir() if x.startswith('_')]):
    # In, Out, exit, quit
    print(x)
# rm(list=ls())

# %%
# exit : notebook 바로 종료

# %%
# rm(list = setdiff(ls(), lsf.str()))
# save.image()
# load(".RData")

# %%
# R

# 함수                           기능
# ls()                           모든 객체 나열(.로 시작하는 객체 제외)
# rm(list=ls())                  모든 객체 제거(.로 시작하느 객체 제외)
# rm(setdiff(ls(), lsf.str()))   함수를 제외한 모든 객체 제거
# str(x)                         객체 x의 데이터 구조
# ls.str()                       ls()와 str() 동시 실행
# exists('x')                    객체 x의 존재 여부 확인
# rm(x) 또는 rm('x')              객체 x 제거
# save.image()                   모든 객체 저장
# load('.RData')                 .RData 에 저장된 객체 불러오기

# %%
# 파이썬

# 함수                            기능
# globals()/vars()                모든 객체 나열(.로 시작하는 객체 제외)
#                                 모든 객체 제거(.로 시작하는 객체 제외)
#                                 함수를 제외한 모든 객체 제거
# type(x)                         객체 x의 데이터 구조
#                                 ls()와 str() 동시 실행
# 'x' in locals(),
# 'x' in globals()                객체 x의 존재 여부 확인
# del(x)                          객체 x 제거
#                                 모든 객체 저장
#                                 .RData 에 저장된 객체 불러오기

# %%
# #%conda install dill

# %%
def expand_grid(x):
    print(x)
    


# %%
# 파이썬에서 함수 확인하기
# 함수 정의 확인하기
def ifelse(cond, x, y):
    return np.where(cond, x, y)
import numpy as np

# %%
expand_grid

# %%
from dill.source import getsource
print(getsource(expand_grid)) # 현재 모듈에서 정의된 함수 : .py를 바로 실행하면 실행되는데, jupyter notebook에서는 안됨?

# %%
import inspect
print(inspect.getsourcelines(expand_grid))  # python에서는 안 되는데 jupyter notebook에서 됨

# %%
print(inspect.getsource(np.sum)) # 다른 모듈에서 정의된 함수

# %%

# %% [markdown]
# # 3.2 파이썬의 데이터타입(자료형)

# %% [markdown]
# # 3.2.1 데이터타입(Data types)

# %% [markdown]
# 파이썬의 기본적인(내장 모듈에서 정의된) 데이터 타입은 https://docs.python.org/ko/3.8/library/index.html 에서 확인할 수 있습니다. `dir(__builtins__)`을 통해서도 모듈 빌트인(`builtins`)에 정의된 클래스나 함수를 확인할 수 있습니다. 앞에서 설명했듯이 내장 모듈에 정의된 클래스, 객체, 함수 들은 파이썬 실행 후 바로 사용할 수 있습니다. 아마도 파이썬에서 `from builtins import *`를 하는 듯 합니다. 

# %% [markdown]
# 파이썬 사이트에는 숫자형(`int`, `float`, `complex`), 문자열(`str`), 시퀀스형(`list`, `tuple`), 매핑형(`dict`), 집합형(`dict`, `frozenset`) 등이 소개 되어 있는데, 이 중에 데이터 타입은 논리형(`bool`), 숫자형과 문자열(파이썬 사이트에는 텍스트 시퀀스형이라고 표기됨)입니다.

# %% [markdown]
# # 3.2.2 변수의 데이터 타입 확인하기

# %%
# R

# 데이터타입              확인하는 함수           문자에서 변환하는 함수
# 숫자(numeric)           is.numeric()             as.numeric()
# 정수(integer)           is.integer()             as.integer()
# 문자(character)         is.character()   
# 범주(factor)            is.factor()              as.factoer()
# 순위범주(ordered)       is.ordered()             as.ordered()
# 논리(logical)           is.logical()             as.logical()
# 날짜(Date)              inherits( , "Date")      as.Date()
# 날짜시간벡터(POSIXct)   inherits( , "POSIXct")   as.POSIXct()
# 날짜시간리스트(POSIXlt) is.integer( , "POSIXlt)  as.POSIXlt()

# %%
# 파이썬

# 데이터타입              확인하는 함수                  변환하는 함수
# 실수(float)            isinstance( ,float)             float()
# 정수(int)              isinstance( ,int)               int()
# 문자(str)              isinstance( ,str)               str()
# 범주(factor)           -            
# 순위범주(ordered)      -
# 논리(bool)             isinstance( , bool)         
# 날짜(Date)             isinstance( ,datetime.date)     datetime.date(년,월,일)     
# 날짜시간벡터(POSIXct)  isinstance( ,datetime.datetime) datetime.datetime(년,월,일,시,분,초) 
# 날짜시간리스트(POSIXlt) -

# isinstance는 데이터타입 뿐 아니라 클래스 판별에서도 쓰인다.

# %% [markdown]
# R과 비교했을 때, R에서 기본적으로 제공하는 범주, 순위범주, 날짜, 날짜시간 데이터에 대해 파이썬은 파이썬 표준 모듈 또는 제3자 패키지를 활용해야 합니다. **날짜**, **날짜시간**, **시간**은 파이썬 표준 모듈 `datetime`을 사용해야 하며, **범주**, **순위범주**는 파이썬의 내장 모듈 또는 표준 라이브러리로 구현할 수 없습니다. 보통 `pandas`라는 제3자 패키지를 사용해야 합니다. 

# %%
import pandas as pd
x = pd.Categorical(['a', 'b', 'b', 'a'])
isinstance(x,pd.Categorical)

# %%
# x1 = 23L; class(x1)
# x2 = 22.3; class(x2)
# x3 = "strings";class(x3)
# x4 = factor(c("Hi", "Lo", "Lo")); class(x4)
# x5 = as.Date("2020-01-01"); class(x5)
# x6 = as.POSIXct("2020-01-01 12:11:11"); class(x6)
## "POSIXct" %in% class(x6)
# inherits(x6, "POSIXct")

import datetime
import pandas as pd
x1 = 23; print(type(x1))
x2 = 22.3; print(type(x2))
x3 = "strings"; print(type(x3))
x4 = pd.Categorical(['Hi', 'Lo', 'Lo']); print(type(x4))
x5 = datetime.date(2020, 1, 1); print(type(x5))
x6 = datetime.datetime(2020, 1, 1, 12, 11, 11); print(type(x6))

# %% [markdown]
# 파이썬에서 문자열을 **텍스트 시퀀스**라고 부르는 이유는 문자열을 배열처럼 취급하기 때문입니다.

# %%
len(x3), x3[0], x3[1]

# %% [markdown]
# ### 타입 어노테이션
#
# 타입 어노테이션(Type Annotation)은 처리하는 데이터와 메서드에서 사용하는 데이터에 대한 타입 힌트를 주는 것이다(강제하는 것이 아니므로 주의를 요한다. 타입이 타입 어노테이션과 다르더라도 오류가 발생하진 않는다).
#
# 파이썬에서는 3.5버전 이후에 타입 어노테이션을 제공하고 있다. 

# %%
# 변수 선언 타입힌팅
n: int = 1
s: str = "문자선언"

# 함수내 인풋 아웃풋에 대한 타입힌팅
def function1(data: list) -> int:
    # function1은 list를 받아 int를 반환
    return data[0]

# 내장 typing 모듈 사용시, list와 dictionary 등의 자료구조 내 데이터 타입도 힌트를 제공할 수 있다.
import typing
_dict: typing.Dict[str, int] = {'a': 1, 'b': 10}

# %% [markdown]
# 하지만, 단순하게 타입에 대한 힌트를 제공하는 것으로 타입힌트에 어긋나더라도 에러를 발생시키지는 않는다.

# %%
_dict['c'] = 'abc'
_dict

# %% [markdown]
# 엄격하게 타입 어노테이션을 규제하고 싶다면, `mypy` 라이브러리를 통해 검사할 수 있다.

# %% [markdown]
# # 3.3 연산과 함수
# # 3.3.1 수치형
# ## 3.3.1.1. 산술연산

# %% [markdown]
# 산술연산으로 별다른 라이브러리 활용없이 기본적인 사칙연산을 제공한다. 
#
# 거듭제곱, 제곱근 등의 계산에는 `math` 내장 라이브러리에서 제공한다.

# %%
import math

3 + 2
5 - 4
3 * 2
72 / 2
3 ** 4 # 3 ^ 4 제곱에는 **가 쓰인다.
math.pow(3,4)
# 3 ^ (1/2); sqrt(3)
math.sqrt(3)
# 3 - 2 + 2 * 4 / 2 ^ ( 1 + 1)
3 - 2 + 2 * 4 / 2 ** ( 1 + 1)

7 / 3 # 나눗셈(Float division)
# 7 %/% 3 # 정수나누기, 몫(Integer division)
7//3 
# 7 %% 3 # 나머지(Remainder)
7%3


# %% [markdown]
# ## 3.3.1.2 함수

# %% [markdown]
# 로그나, 지수, 삼각함수 등도 제공한다.

# %%
# exp(1)
math.exp(1)

# log(180, base=2); log2(180)
math.log(180, 2)

#log10(180)
math.log(180, 10)
math.log10(180)

# sin(2)
math.sin(2)

# %% [markdown]
# ## 3.3.1.3 연산

# %%
3 + 2
3 * 2
# "%p%" =  function(x,y) {2^x + y^2}
def p(x,y):
    return 2**x + 2**y

# 3 %p% 2   ## 책에는 두번 프린트 되어 있습니다.\
p(3,2)

# %%
# "+" = function(x, y) x*y
# 3+2; 3+3
# "+"
# 원상회복하려면 rm("+")

# %% [markdown]
# ## 3.3.1.4 비교연산

# %%
7 < 3
7 > 3
7 == 3
7 != 3

# %%
#sqrt(2)^2 == 2
math.sqrt(2)**2 == 2
#print(sqrt(2)^2)
print(math.sqrt(2)**2)
#print(sqrt(2)^2, digits = 21)
num = math.sqrt(2)**2
print('%.21f' % num)
print('{:.21f}'.format(num))
print(f'{num:.21f}')

# digits = 21의 의미??

# %% [markdown]
# 0.1, 0.2와 같은 소수는 2진법의 부동소수점으로 저장되기 때문에
# 약간의 오차가 발생할 수 있다.
# 약간의 오차를 무시하고 두 수의 크기를 비교하고자 한다면,
# `math.isclose()`를 사용할 수 있다.

# %%
a = 0.1 + 0.2
print(a, a == 0.3, math.isclose(a, 0.3))

# 컴퓨터가 계산한 0.1+0.2와 직접 생성한 0.3은 $10^{-18}$보다 작은 오차가 있다.
(0.1+0.2)-0.3
# 5.551115123125783e-17

# `math.isclose()`는 이렇게 작은 차이는 무시한다. 허용 가능한 오차의 크기는
# `math.isclose(a,b, *, rel_to=1e-09,, abs_tol=0.0)`의 `rel_tol=`, `abs_tol=` 매개변수로 조정가능하다.
# `rel_tol`은 relative tolerance, `abs_tol`은 absolute tolerance로
# 두 수의 상대적 차이, 절대적 차이를 얼마나 허용할 것인가를 결정한다

# %%
# all.equal(sqrt(2)^2, 2)
# all.equal(1e-23, 1e-24)
math.isclose(math.sqrt(2)**2, 2)
math.isclose(1e-23, 1e-24) # rel_tol = 1e-09
# dplyr::near(1e-23, 1e-24)
# near <- dplyr::near; near(1e-23, 1e-24)

# %% [markdown]
# ## 3.3.2 문자

# %%
print("Letter")
# cat('Letter')
print("\"Hello\", says he")
# cat("\"Hello\", says he")

# %%
print('Cheer up!\r\nRight Now!')
# cat('Cheer up!\r\nRight Now!')
# nchar('hello?') # 문자 갯수
len('hello?')
# paste('Here is', 'an apple.') # 문자열 연결
list = ['Here is', 'an apple.']
text = ' '.join(list)
print(text)
print('Here is'+ ' '+'an apple.')

# substring('hello?', 2, 3) # 문자열의 일부분
a = "hello?"
a[1:3]

# %% [markdown]
# ## 3.3.3 날짜/시간

# %%
import datetime

# %%
# Sys.Date() # 현재 날짜
print(datetime.date.today())
# Sys.time() # 현재 날짜와 시간(POSIXct 형식)
print(datetime.datetime.now())

# as.Date("2018/12/31") # 문자열 "2018/12/31"을 날짜 형식으로
print(datetime.datetime(2018,12,31))
# as.POSIXct("2018/12/31 23:59:59") # 문자열 "2018/12/31 23:59:59"을 날짜시간 형식으로
print(datetime.datetime(2018,12,31,23,59,59))

# Sys.Date() - as.Date("2019-01-01") # 2018년 1월 1일과 현재 날짜의 차이
a = datetime.date.today()
b = datetime.date(2019,1,1)
print(a-b)  # a-b는 datetime.timedelta 자료형을 가진다.
# as.POSIXct("2019/12/31 23:59:59")-Sys.time() # 현재 날짜 시간과 2019년 12월 31일 23시 59분 59초의 차이
a = datetime.datetime.today()
b = datetime.datetime(2019,12,31,23,59,59)
print(a-b) # a-b는 datetime.timedelta 자료형을 가진다.


# 현재 날짜 시간과 2018년 12월 31일 23시 59분 59초와의 차이
# difftime(as.POSIXct("2018/12/31 23:59:59"), Sys.time()) 
a = datetime.datetime.today()
b = datetime.datetime(2018,12,31,23,59,59)
print((a-b).days, "일") 

# 현재 날짜 시간과 2018년 12월 31일 23시 59분 59초와의 차이(분 단위로)
# difftime(as.POSIXct("2018/12/31 23:59:59"), Sys.time(), units='mins')
print((a-b).seconds/60, "분")
print(f"{(a-b).seconds/60:.2f}분")

# 현재 날짜 시간과 2018년 12월 31일 23시 59분 59초와의 차이(초 단위로)
# difftime(as.POSIXct("2018/12/31 23:59:59"), Sys.time(), units='secs')
# R : units은 다음 중 하나: 'auto', 'secs', 'mins', 'hours', 'days', 'weeks'
# 파이썬 : timedelta 값은 날짜, 초, 밀리초를 days, seconds, miliseconds 속성 이용해 접근할 수 있다.
a = datetime.datetime.today()
b = datetime.datetime(2018,12,31,23,59,59)
print((a-b).seconds, "초")

# as.numeric(as.POSIXct("2018/12/31 23:59:59"))-as.numeric(Sys.time())

#'2020-01-01'-'2019-12-31'
# as.Date('2020-01-01')-as.Date('2019-12-31')

# %% [markdown]
# # @@@@@@@@@@@@@@@@@@@@@@@

# %%
# 날짜 시간 format 변환
# R format(today, '%Y-%m-%d %H:%M')
today = datetime.datetime.today()
str_today = today.strftime('%Y-%m-%d %H:%M')

print(today, str_today)
# R as.Date(str_today, format='%Y-%m-%d %H:%M')
datetime.datetime.strptime(str_today, '%Y-%m-%d %H:%M')

# %% [markdown]
# ## 3.3.4 논리형

# %%
#(7 < 3) & (4 > 3)
#(7 < 3) | (4 > 3)
#!(7 < 3)
#xor(T, T) # XOR
#x = NA
#isTRUE(x == 3) # robust to NAs

import numpy as np
(7 < 3) & (4 > 3)
(7 < 3) | (4 > 3)
not(7<3)
x = np.nan
bool(x==3) # !!!is this robust to NAs?
# !!! R과 다르게,
#     np.nan == np.nan -> False
#     3 == np.nan -> False
#     math.isclose(np.nan, np.nan) -> False
#



# R에서 NA은 잘못된 값, Null 은 정해지지 않은 값으로 다른 의미
# 파이썬에서는 NaN(NA)와 Null 을 정해지지 않은 값으로 같이 사용. NaN으로 모두 표현.



# %%
#TRUE <- c(3,2) 불가능
#T <- c(3,2) 
#T 

TRUE = [3,2] # 가능
T = [3,2] 
T 
True = [3,2]
# SyntaxError: cannot assign to True

# %%
# 모든 예약어 확인
import keyword
#keyword.kwlist
", ".join(keyword.kwlist)

# %%
"True" in keyword.kwlist
keyword.iskeyword("True")

# %% [markdown]
# ## 3.3.5 데이터 타입에 따른 연산과 함수

# %%
# 데이터 타입       대표적인 연산과 함수 
# 숫자(numeric)     ^(**), *, /, +, -, <, ==, >, exp(), log()
# 문자(str)         nchar(), paste(), substring()
# 날짜(Date)        Sys.Date(), -, difftime()
# 날짜시간(POSIXct) Sys.time(), -, difftime()
# 논리(logical)     &, |, !, xor(), &&, ||

# %%
# 데이터 타입                 대표적인 연산과 함수 
# 실수(float)                 **, *, /, +, -, <, ==, >, math.exp(), math.log()
# 문자(str)                   len(), count(), find(), index(), join(), upper(), lower(), split()
# 날짜(datetime.date)          -  !!!
# 날짜시간(datetime.datetime)  -  !!!
# 논리(bool)                  &, |, !, &&, ||

# %% [markdown]
# ## 3.4 특별한 값

# %%
1.32e+308  
1.32e+308*10  # 64bit의 경우, inf
import sys
sys.float_info.max 
1.7976931348623157e+308
1.7976931348623158e+308
1.7976931348623159e+308 # inf
sys.float_info.min
2.2250738585072014e-308
2.2250738585072010e-308
2.2250738585072006e-308
2.2250738585072006e-310
2.2250738585072006e-320
2.2250738585072006e-321
2.2250738585072006e-322
2.2250738585072006e-323
2.2250738585072006e-324 # 0.0

# %% [markdown]
# ## 3.4.2 몇가지 유의사항

# %%
# x <- c(2, 5, NA, 3)
# vec <- c(3, 7, 0, NA, -3)


import pandas as pd
x = pd.Series([2,5,np.nan,3])
print(x)
vec = pd.Series([3, 7, 0, np.nan, -3])
print(vec)

# %%
import numpy as np

def ifelse(cond, x, y):
    return np.where(cond, x, y)
print(ifelse(x > 3, "3+", "below")) # !!!주의! np.nan이 제대로 반영되지 않았다)


# %%
# ifelse(is.na(x), NA, x %in% vec)
ifelse(np.isnan(x), -99, x.isin(vec))  
# !!! True가 int로 변환됨!
# 왜냐하면 return 값이 array이고,
# -99가 포함되므로, True/False는 int로 변환

# %%
ifelse(np.isnan(x), np.nan, x.isin(vec))
# np.nan은 dtype = 'bool' or 'int*'에서는 지원하지 않는다  
ifelse(np.isnan(x), 'NA', x.isin(vec))

# %%
#x <- 1e-16
#c(log(1+x), log1p(x), exp(x)-1, expm1(x)) 
# ## log(1+x)의 결과값이 책(0e+00)과 다름
x = 1e-16
math.log(1+x), math.log1p(x), math.exp(x)-1, math.expm1(x)
# math.log(1+x), math.exp(x)-1의 경우 발생하는 UNDERFLOW를 
# math.log1p(x)와 math.expm1(x)는 방지한다.

# %%
x = 1e-16
np.array([np.log(1+x), np.log1p(x), np.exp(x)-1, np.expm1(x)])

# %% [markdown]
# ## R의 `assign`

# %% [markdown]
# Python에는 R의 `assign` 함수에 정확히 대응되는 함수가 존재하지 않는다. 
# 다음은 stackoverflow에서 찾은 몇 가지 대용방법이다. 
# 첫 번째 방법은 `exec`를 사용하고, 두 번째 방법은 `globals()`를 사용한다.
# `exec`를 사용하는 경우 외부에서 입력을 받는 경우 몇 가지 보안상 위험 상황이 발생할 수도 있다.
# 예를 들어 `exec('{}={}'.format(varname, d)`에서 `varname='del a; b'; d=3`이라면 변수 `a`를 지워버릴 수 있다.
# 만약 varname을 바로 입력하지 않고 varname에 공란이나 `;`가 포함되어 있는지 확인하는 
# 과정을 거친다면 큰 문제가 없을 것이다.

# %% [markdown]
# ### 첫 번째 방법 : `exec()`
# `exec()` 문자열 fommating으로 변수를 선언할 수 있다.

# %%
varnames = ['a', 'b', 'c']
ds = [1, 5, 2]

# %%
# https://stackoverflow.com/questions/36353774/whats-the-analogous-function-for-aasign-of-r-in-python
varnames = ['a', 'b', 'c']
ds = [1, 5, 2]
for varname,d in zip(varnames,ds):
    exec('{}={}'.format(varname,d))
a,b,c    

# %% [markdown]
# ### 두 번째 방법 : `globals()`
# `globals()`는 전역으로 선언된 변수들에 대한 {'변수명' : 데이터}의 구조로 이루어진 dictionary를 반환하는 함수이다.
#
# 변수명 문자를 dictionary에 key로 선언해준다.

# %%
globals()['데이터'] = 1
print(데이터)

# %%
varnames = ['a', 'b', 'c']
ds = [2, 3, 4]
for varname,d in zip(varnames, ds):
    globals()[varname] = d
a,b,c

def assign(varname, value):
    globals()[varname] = value
assign('a', 3)
a
assign('a2', np.array([3,2,1]))
a2

# %%
# 첫 번째 방법은 `exec()` 함수를 사용한다. 
# `exec()`함수는 파이썬 코드의 동적 실행을 지원한다. "동적 실행"이란 프로그램 코드가 실행하면서 변할 수 있다는 의미이다.
# exec의 인자는 코드를 나타내는 문자열이다.
exec('print(123)')

# 만약 잘못된 구문이 입력되면 에러가 발생한다.
# exec('give me money!')
# # SyntaxError: invalid syntax

# 파이썬 변수규칙상 숫자로 시작하는 변수, 특수문자는 변수명으로 선언할 수 없다.
# 변수 할당에서는 파이썬에서 지원하지 않는 변수명에 대해서는 에러를 발생시킨다.
# exec('@@=3')
# SyntaxError: invalid syntax

# exec()함수는 단순히 변수 할당뿐 아니라, 모든 파이썬 구문과 함수를 실행할 수 있다.
# 만약 exec()로 실행하는 구문의 내용을 외부로부터 입력받는다면 문제가 발생할 수 있다.
# 다음을 보자. 프로그래머의 의도와 상관없이 `xx`라는 변수가 생성되었다.
a='c'
b='3; xx=10'
exec(f'{a}={b}') # exec('{}={}'.format(a,b))와 동일하다

# 다음과 같은 코드는 프로그램을 먹통으로 만들 것이다.
a='c'
b="3; [x for x in range(1000000000000)]"
exec(f'{a}={b}')

# %%

# %% [markdown]
# 두 번째 방법은 파이썬이 지원하지 않는 변수명에 대해서도
# 에러가 발생하지 않는다. 그렇다고 변수가 생성되지도 않지만,
# globals()에서 찾을 수는 있다.
#
# globals()['@@'] = 'symbol at'
# @@
# # SyntaxError: invalid syntax

# %%
globals()['@@']
# 'symbol at'

# %%

# %% [markdown]
# # =====

# %%
from __future__ import print_function
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
try:
    from reprlib import repr
except ImportError:
    pass

def total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                   }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


##### Example call #####

if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, d=[4,5,6,7], e='a string of chars')
    print(total_size(d, verbose=True))

# %%
a = [1]*100
b = [2]*100
c = [a,b]
print(sys.getsizeof(c))
print(total_size(c))
