# -*- coding: utf-8 -*-
# %% [markdown]
# # 1차원 넘파이 배열

# %% [markdown]
# > R에서 배열은 1차원 벡터의 다차원 확장 쯤으로 생각했다. R에서 모든 배열은 벡터와 동일한 형태로 저장되어 있고, 각 차원의 크기가 설정되어 있다는 점만 다르다. 사용 용도 및 범위에서 R의 벡터에 해당하는 것은 파이썬의 리스트일 것이다. 가장 기본적으로 사용되고, 또 어디서나 사용되기 때문이다. 하지만 파이썬의 리스트는 속도가 느리다는 치명적인 단점이 있다. 이를 해결한 것이 제3자 패키지인 `numpy`이고, `numpy`를 데이터 분석용으로 확장, 발전시킨 것이 또다른 제3자 패키지인 `pandas`이다. `numpy`의 배열(`ndarray`), 그리고 `pandas`의 `Series`는 모두 R의 벡터와 같이 **동일한 타입**의 데이터를 저장한다는 특징을 지녔다. `numpy`는 수치계산에 특화되어 있고, `pandas`는 범용 데이터 분석이라고 생각할 수도 있다. 또 다른 차이는 `numpy`의 배열은 다차원으로 확장할 수 있고, `pandas`의 `Series`는 여러 타입의 데이터를 모아 데이터 프레임을 구성할 수 있다.

# %% [markdown]
# 파이썬에 R의 1차원 벡터를 대신할 수 있는 데이터 구조는 앞에서 소개한 리스트와 
# **넘파이 배열**(numpy array)과 **판다스 시리즈**(pandas series)가 있다.
#
# 여기서는 numpy의 배열에 대해 알아본다. 여기서는 배열의 차원을 1로 제한하여 알아본다.
# 1차원 넘파이 배열은 동일한 type의 값이 메모리에 순차적으로 순번에 따라 저장되어 있는 **가변 객체**이다.

# %% [markdown]
# ### 일차원 넘파이 배열

# %% [markdown]
# 넘파이 배열을 사용하기 위해서는 먼저 넘파이(`numpy`) 패키지를 불러와야 한다. `numpy`는 보통 `np`를 별칭으로 한다. 

# %%
import numpy as np

# %% [markdown]
# 넘파이 배열을 생성하기 위해서는 원소을 나열하고, 모든 원소의 공통적인 타입을 설정한다. 예를 들어 정수 `1`,`2`,`3`을 가지는 넘파이 배열을 만들고자 한다면 다음과 같이 한다.

# %%
np.array([1,2,3])

# %% [markdown]
# 다시 동일한 내용을 하나 더 만들어서 변수 `arr`에 할당한다. 이 과정은 앞에서 소개한 것과 같이 `np.array([1,2,3])`이 메모리에 생성되고, 변수 `arr`은 이 객체을 가리키게 된다.

# %%
arr = np.array([1,2,3])

# %% [markdown]
# 이제 원소의 타입을 살펴보자. 변수에 `.dtype`을 한다.

# %%
arr.dtype

# %% [markdown]
# `dtype('int32')`이다.[^int32] 여기서 중요한 것은 이 데이터 타입(**d**ata **type**; `dtype`)의 표현력이다. 정수형이라면 파이썬의 정수형(`int`)와 비슷하게 정확한 값을 저장하지만 저장한 가능한 수에 범위(최솟값, 최댓값)가 있다. 이 정보는 다음과 같이 확인할 수 있다.
#
# [^int32]: 만약 결과가 `dtype('int64')`로 나온다면 논의의 진행 상 `arr=np.array([1,2,3], dtype='int32')`을 다시 하고 진행하자.

# %%
np.iinfo(np.int32) # integer info

# %% [markdown]
# 최솟값은 `-2147483648`이고 최댓값은 `2147483647`이다. 이 범위를 넘어간 값을 저장하려면 어떤 일이 일어날까?

# %%
np.iinfo(np.int32).max

# %%
np.iinfo(np.int32).max + 1

# %%
arr[0] = np.iinfo(np.int32).max + 1

# %%
arr[0]

# %% [markdown]
# 이게 조금 애매한 데 다음을 보자.[^int32overflow]
#
# [^inte32overflow]: `numpy` 버전에 따라 OverflowError가 발생하기도 한다.

# %%
arr[0] = np.int32(np.iinfo(np.int32).max) + 1

# %%
arr[0]

# %% [markdown]
# OverflowError가 발생하든, 하지 않든 dtype `np.int32`으로는 계산 결과를 정확하게 저장할 수 없다.

# %% [markdown]
# 여기서 dtype과 객체의 타입을 구분하자. `arr`의 타입(클래스)는 `np.ndarray`이고, `arr`의 dtype은 `np.int32`이다. `arr`은 기본적으로 numpy 배열이고, 배열의 각 원소의 값을 저장하는 방식을 dtype이 결정한다.`np.int32`은 -2147483648에서 2147483648까지의 정수를 저장할 수 있는 dtype이다.

# %%
type(arr)

# %%
isinstance(arr, np.ndarray)

# %%

# %% [markdown]
# 다음 넘파이 배열에 사용 가능한 dtype과 특징을 보여준다. `np.int8`, `np.int16`, `np.int32`, `np.int64`은 8비트, 16비트, 32비트, 64비트로 저장되는 정수형이다. 

# %% [markdown]
# !!! Table (insert here)
#
#
# ### list of numpy array dtype
#
# * [types](https://numpy.org/doc/stable/user/basics.types.html)
# * [sized-aliases](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases)

# %%
arr = np.array([1,2,3], dtype=np.int64)
arr[0] = np.iinfo(np.int32).max + 1

# %%
arr

# %% [markdown]
# 위에서 저장할 수 없거나 논리적인 오류를 발생시켰던 값도 64비트 정수형으로는 정확하게 저장된다.

# %% [markdown]
# 앞에서 배웠던 각 데이터 타입이 넘파이 배열에 어떻게 저장되는지도 확인해보자. (넘파이 배열은 범주형 dtype을 지원하지 않는다.)

# %%
from datetime import datetime
arr_bool  = np.array([True, False, False, True, True])
arr_int   = np.array([1, 3, 2, 5, 4])
arr_float = np.array([3.14, 2.14, -4.5, 100, 0.5])
arr_str   = np.array(["This is a sentence", 
                      "Hey",
                      "I don't like this",
                      "Surely!",
                      "Am I capable of this?"])

# %%
arr_datetime = np.array([datetime(2022,1,1),
                         datetime(2022,4,1),
                         datetime(2025,3,14,11,14),
                         datetime(1999,12,31),
                         datetime(2000,1,4,9,0)])

# %% [markdown]
# `arr_bool`, `arr_int`, `arr_float`, `arr_str` 그리고 `arr_datetime`을 콘솔에서 출력해보자. 그리고 dtype을 확인해보자.

# %%
arr_bool.dtype, arr_int.dtype, arr_float.dtype, \
arr_str.dtype, arr_datetime.dtype

# %% [markdown]
# `dtype('bool')`, `dtype('int64')`, `dtype('float64')`의 의미는 쉽게 유추 가능할 것이다. 논리형, 64비트 정수형, 64비트 실수형이다. `dtype('<U21')`의 `U`는 유니코드를, `<21`은 최대 글자 갯수를 나타낸다. `arr_str[0][:21]`을 하면 0-번째 원소의 모든 글자를 포함하게 된다.[^strlen] `dtype('O')`는 객체(Object)를 가리킨다. 사실 파이썬의 모든 것은 객체이므로 이건 뭘 특별히 저장하고 있다는 의미가 없다. 뒤에서 설명하겠지만 `dtype('O')`의 경우 값을 저장하지 않고 포인터(객체 레퍼런스)를 저장한다.
#
# [^strlen]: `np.char.str_len()` 함수는 `numpy` 문자열형 배열 각 원소의 글자 갯수를 반환한다. `np.char.str_len(arr_str)`을 해보자.

# %% [markdown]
# `dtype('O')`는 어떤 자료형인지 알려주지 않는다. 예를 들어 다음과 날짜시간형이 아닌 값도 저장할 수 있다.

# %%
arr_datetime[1] = 'This is not datetime.'
arr_datetime

# %% [markdown]
# 날짜시간형의 `dtype`은 다음과 같이 정해줄 수 있다.

# %%
arr_datetime = np.array(['2022-01-01',
                         '2022-04-01',
                         '2025-03-14 11:14',
                         '1999-12-31',
                         '2000-01-04 09:00'], dtype='datetime64')

# %%
arr_datetime

# %%
arr_datetime

# %% [markdown]
# 날짜시간 데이터는 다루기 까다롭고 사전지식이 필요하므로 여기서는 다루지 않고 뒤에 관련 장에서 다룬다.
#

# %% [markdown]
# ### 1차원 넘파이 배열의 크기(원소의 갯수)

# %% [markdown]
# 1차원 넘파이 배열에서 가장 중요한 속성은 dtype과 원소의 갯수이다. 원소의 총 갯수는 `.size` 속성으로 확인할 수 있다. `.shape`은 다차원 배열에서 각 차원의 크기를 알려준다. 1차원 배열은 원소의 갯수가 하나인 튜플로 0-번째 차원의 크기를 알 수 있다(1차원의 0-번째 차원이 헷갈릴 수 있지만, 파이썬에서 순번은 0부터 시작하는 게 보통이다. 1차원 배열에서 차원의 갯수는 1, 차원의 순번은 0이다.)

# %%
arr = np.array([1,3,2], dtype=np.int64)

# %%
arr.ndim, arr.shape, arr.size  # 차원의 갯수, 각 차원의 크기, 원소의 총갯수

# %% [markdown]
# 이제 1차원 배열에서 기본적인 데이터 처리인 CREAD을 구현하는 방법에 대해 알아볼 것이다. 그 전에 배열은 **가변객체**라는 것을 유의하자.

# %%
arr1 = np.array([1,3,2], dtype = "int64")
arr2 = arr1
arr1[0] = 0
arr1, arr2

# %% [markdown]
# 위의 결과는 앞에서 리스트를 설명한 것과 동일한 논리에 의해 설명될 수 있다. 하지만 약간 다른 점도 있으니 위의 결과가 어떻게 나왔는지 설명해보자.
#
# `np.array([1,3,2], dtype='int64')`를 통해 메모리의 어딘가에 원소가 1,2,3인 정수형 배열이 생성된다. 이때 배열은 리스트와 달리 단지 정수형 객체 1, 2, 3을 가리키는 것이 아니라 1,2,3을 저장하고 있다. 그러니까 리스트와 정수형 배열의 차이는 다음의 그림과 같다.

# %% [markdown]
# ![내장 리스트 vs numpy 배열](04b_CREAD_1dArray_01.png)

# %% [markdown]
# 이제 변수 `arr1`은 방금 생성한 정수형 배열을 가리키게 되고, `arr2=arr1`을 통해 `arr2`도 동일한 배열을 가리키게 된다. 그리고 `arr1[0]=0`하게 되면 `arr1`이 가리키는 배열의 0-번째 원소를 `0`으로 덮어쓰게 된다. 이때 `arr2`도 `arr1`과 같은 배열을 가리키고 있으므로 `arr2`를 출력하면 원소의 내용이 `0`, `3`, `2`로 나타나게 되는 것이다. 

# %% [markdown]
# 넘파이 배열에 dtype이 그렇게나 많은 이유는 dtype에 따라 저장할 수 있는 수의 범위와 성격도 달라지고, 넘파이 배열이 메모리에서 차지하는 공간의 크기도 달라지기 때문이다. 만약 0부터 10까지의 수 십만개를 저장한다고 생각해보자. 뒤에서 배우겠지만 `Z = np.random.randint(1,10,100000)`으로 `0`부터 `10`까지의 무작위 정수 십만개의 배열을 생성할 수 있다. 이 배열의 dtype이 `dtype('int64')`라면 이 배열은 800000 바이트(800 KByte)의 메모리 공간을 필요로 한다. 

# %%
arr1 = np.random.randint(1,10,100000)
arr1.dtype

# %%
arr1.itemsize * arr1.size
# arr1.itemsize는 배열 arr1의 원소 하나를 저장하는 데 필요한 메모리 크기(byte),
# arr1.size는 배열 arr1의 총 원소 갯수를 나타낸다. 

# %% [markdown]
# 만약 이 배열의 dtype을 `dtype('int8')`로 정해준다면, 필요한 메모리 크기는 100000바이트로 크게 줄어든다.

# %%
arr2 = np.random.randint(1,10,100000, dtype='int8')

# %%
arr2.dtype

# %%
arr2.itemsize * arr2.size

# %% [markdown]
# 마지막으로 dtype이 `dtype('O')`인 경우는 리스트와 동일하게 배열은 포인터(객체가 저장된 주소; 객체 레퍼런스)를 저장하게 된다.

# %% [markdown]
# ## CREATE
#
# 앞에서 넘파이 배열을 생성하는 방법을 배웠다. 배열의 원소와 dtype을 파이썬에게 알기 쉽게 제공해주면 된다.

# %%
# 유명한 상수 제공?
arr1 = np.array([3.141592, 1.414, 2.11421, -372], dtype='float')
print(arr1)

# %% [markdown]
# 하지만 원소 1이 10만 개로 구성된 정수형 배열을 만들어 보자. 손목이 부러질 정도 빠르게 1을 눌러보자. 1초에 `1`, `,` 를 5번 반복할 수 있다고 쳐도, 10만개의 원소를 모두 치려면 100000/5 = 20000 초, 즉 333분(5시간 30분)이 필요하다! 만약 `np.ones()`라는 넘파이 배열 생성함수를 사용한다면 `np.ones(100000, dtype='int64')`로 간단하게 끝낼 수 있다.

# %% [raw]
# np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,...

# %%
arr = np.ones(100000, dtype='int64')

# %%
arr.ndim, arr.shape, arr.size, arr.itemsize

# %% [markdown]
# 이제 다음의 배열 생성 함수를 열심히 배워야 할 이유가 충분하지 않은가? 하지만 여기서는 1차원 배열에서 자주 쓰는 몇 개만 소개하겠다. (더 많은 내용은 <배열> 장을 참조하자.)

# %% [markdown]
# ### 하나의 값의 이루어진 배열

# %%
a = np.zeros(10) # 원소가 모두 0(zero), 원소 갯수 10
b = np.ones(10)  # 원소가 모두 1(one), 원소 갯수 10
c  = np.full(10, 3) # 원소가 모두 3, 원소 갯수 10

# %%
print(a); print(b); print(c);

# %% [markdown]
# 만약 dtype을 정해주고 싶다면, `np.zeros(10, dtype='int64')`와 같이 `dtype=`을 설정할 수 있다.

# %% [markdown]
# ### 원소 상관없이 특정한 길이의 배열

# %%
d = np.empty(10) # 원소 상관없이, 원소 갯수 10

# %%
# 다음의 np.printoptions()는 실수형 배열의 출력을 보기 좋게 만든다.
with np.printoptions(precision=3, suppress=True):
    print(d)

# %% [markdown]
# 무작위 내용의 문자열 배열도 한번 만들어보자.

# %%
e = np.empty(10, dtype='<U10')
e

# %% [markdown]
# ### 수열

# %% [markdown]
# #### `np.arange(시작, 정지, 간격)`

# %% [markdown]
# `np.arange()`는 slicing의 `start:stop:step`과 비슷한 방식으로 배열을 생성한다. `start`에서 시작해서 `step`만큼씩 증가하면서 `stop`이 **되기 전**에 끝난다. 

# %%
np.arange(1,10,1) 

# %%
np.arange(10,20,0.5, dtype='float16')
# dtype=으로 dtype 설정이 가능하다.

# %% [markdown]
# #### `np.linspace(시작, 정지(끝), 갯수)`

# %% [markdown]
# `np.linspace()`는 시작하는 값과 끝나는 값을 포함해서 주어진 갯수만큼의 등차수열 배열을 생성한다. 예를 들어 1부터 10까지의 원소 5개의 등차수열을 배열로 만든다면 다음과 같다.

# %%
np.linspace(1,10,5)

# %% [markdown]
# 여기서 끝값을 `np.arange()`와 마찬가지로 포함시키지 않으려면 `endpoint=False`로 한다.

# %%
np.linspace(1,10,5,endpoint=False)

# %% [markdown]
# 1부터 10까지 총 6(5+1)개의 원소로 이루어진 등차수열에서 마지막 수를 제외한 결과를 확인할 수 있다. 만약 등차수열의 등차가 궁금하다면, `retstep=True`(**ret**urn **step**)를 덧붙인다.

# %%
np.linspace(1,10,5,endpoint=False, retstep=True) 


# %% [markdown]
#

# %% [markdown]
# ### 무작위 원소
#
# 원소는 무엇이든 상관없이 배열의 크기만 설정한다면, `np.empty(n) # n : 원소의 갯수`로 할 수 있다.
# 하지만 이때 원소가 무엇이 될지는 컴퓨터만 안다. 심술꾸러기 컴퓨터는 처음에는 이상한 값들을 넣고, 다른 경우에는 `0` 또는 `1`처럼 아주 정돈된 값을 넣기도 한다.
#
# 경우에 따라 특정한 범위의 정수나 특정한 범위의 실수, 또는 특정한 분포의 실수가 필요한 경우가 있다. 이때에는 `np.random` 서브패키지의 함수를 사용할 수 있다. 
#
# 특정한 범위의 수를 무작위로 추출하여 배열을 생성하는 함수는 다음과 같다
#
# * 정수형 무작위 배열 생성 : `np.random.randint(low, high, size, dtype)` 
#     - **rand**om **int**eger
#     - `low`에서 `high`-1까지의 정수 중에서 무작위로 `size`개 생성
# * 실수형 무작위 배열 생성 : `np.random.random_sample(size)`
#     - 0에서 1(제외)까지의 실수를 `size`개 생성
#     - 만약 `low` ~ `high`(제외)의 실수를 생성하고자 한다면 `low + (high-low)*np.random.random_sample(size)` 또는 `np.random.uniform(low, high, size)`를 사용할 수 있다.
# * 정수형/실수형 표본 추출 : `np.random.choice([x1,x2,...], size, replace)`
#     - `x1`, `x2`... 에서 크기 `size`의 표본 추출
#     - 비복원추출 : `replace=False`
#     
# 특정한 분포를 따르는 무작위 배열 생성은 <배열> 장을 참조하자.
#     

# %% [markdown]
# ### Python vs R
#
# | 원소                |     Python    |     R      |
# |:-----------------|:-----------------|:-----------------
# |1부터 5까지(간격 2)        |  `np.arange(0,(5-1)//2+1)*2+1`  | `seq(from=1,to=5,by=2)`  |
# |1부터 7까지(갯수 3)        |  `np.linspace(1,7,3,endpoints=True)`  | `seq(from=1,to=7,length.out=3)`  |
# |2을 3번 반복        |  `np.ones(3)*2`  | `rep(2,3)`  |
# |1,2을 3번 반복        |  * rep_times | `rep(1:2,times=3)`  |
# |1,2를 길이 5까지 계속 반복 |  * rep_length_out  | `rep(1:2, length.out=5)` |
# |1,2,3을 각각 2번 반복 |  * rep_each  | `rep(1:3, each=2)` |
#

# %%
def xor(a,b):
    return a and not b or not a or b
def seq(from_,to,by=None, length_out = None):
    if by is None and length_out is None:
        by = 1
    if not xor(by is not None,length_out is not None):
        raise ValueError('one of by and length_out is required')
    if by is not None:
        return np.arange(0,(to-from_)//by+1)*by + from_
    if length_out is not None:
        return np.linspace(from_, to, length_out, endpoint=True)


# %%
# testing seq
seq(1,5,2)

# %%
seq(1,7,length_out=3)

# %%
# rep_times
x = np.array([1,2])
times = 3
np.array(x.tolist()*times, dtype=x.dtype)

# %%
# rep_length_out
x = np.array([1,2])
length_out = 5
nrep = length_out // x.shape[0] + 1
np.array(x.tolist()*nrep, dtype=x.dtype)[:length_out]

# %%
# rep_each
x = np.array([1,2,3])
each = 2
np.array(np.broadcast_to(x.reshape(1,-1).T, (x.shape[0], each)).flat, dtype=x.dtype)


# %%
def rep(x, times=None, length_out=None, each=None):
    if not xor(xor(times is not None, length_out is not None), 
                   each is not None):
        raise ValueError('only one of times, length.out, each is required.')
    if times:
        if isinstance(x, (np.ndarray, list)):
            if isinstance(x, np.ndarray):
                lst = x.tolist()
                return np.array(lst*times, dtype=x.dtype)
            else:
                return np.array(x*times)            
        else:
            return np.full(times, x) 
    elif length_out:
        if isinstance(x, (np.ndarray, list)):
            if isinstance(x, np.ndarray):
                lst = x.tolist()
                nrep = length_out // x.shape[0] + 1
                return np.array(x.tolist()*nrep, dtype=x.dtype)[:length_out]
            else:
                nrep = length_out // len(x) + 1
                return np.array(x*nrep)[:length_out]
        else:
            return np.full(length_out, x)
    else:
        if isinstance(x, (np.ndarray, list)):
            if isinstance(x, list):
                x = np.array(x)                              
            return np.array(np.broadcast_to(x.reshape(1,-1).T, 
                                            (x.shape[0], each)).flat, dtype=x.dtype)                
        else:
            return np.full(each, x)
        


# %% [markdown]
# #### Testing rep

# %%
print(rep(2,3))
print(rep(2,length_out=3))
print(rep(2,each=3))

print(rep(seq(1,3), times=3))
print(rep(seq(1,3), length_out=5))
print(rep(seq(1,3), each=2))

# %%
print(rep('a',3))
print(rep('a',length_out=3))
print(rep('a',each=3))

print(rep(['a', 'b', 'c'], times=3))
print(rep(['a', 'b', 'c'], length_out=5))
print(rep(['a', 'b', 'c'], each=2))

# %% [markdown]
# ## 넘파이 배열의 원소 살펴보기

# %% [markdown]
# ### 넘파이 배열의 내용 출력

# %%
vInt = seq(1,35)
vFloat1 = np.random.uniform(-10,10,10)
vFloat2 = np.array([1.2475842, 1.43, 10240333211])
vStr = np.array(['안녕?\n또 보다니!', "Hi,\tWait a moment",
                 "오랜만이야?\t!", "Long time no see!", "..."])
vDatetime = np.array(['2022-01-01',
                      '2023-04-01',
                      '2024-05-04'], dtype='datetime64')

# %% [markdown]
# 넘파이 배열을 출력하는 방법은 `print()`를 쓰거나 `print(repr())`를 쓸 수 있다. (`print(repr(x))`는 콘솔에서 `x`만 입력하고 엔터를 칠 때와 동일한 출력 결과를 얻는다.)
#
# `print(repr(x))`를 하면 코드를 작성할 때 `x=np.` 뒤에 바로 복사해 넣을 수 있는 형태로 출력이 된다. 문자열형과 날짜시간형에서는 `dtype=`을 출력하여 데이터타입의 구분을 용이하게 해주는 장점이 있다.

# %%
print(vInt)

# %%
print(repr(vInt))

# %% [markdown]
# 위의 정수형 넘파이 배열과 아래의 리스트의 출력을 비교해보자.

# %%
print([1,2,3]) 

# %%
print(repr([1,2,3]))

# %% [markdown]
# 실수형 배열은 `with np.printoptions(precision=5, suppress=True):`를 통해 수의 출력 형식을 조정할 수 있음을 기억하자.
#
#

# %%
print(vFloat1)

# %%
print(repr(vFloat1))

# %% [markdown]
# 다음은 문자열형과 날짜시간형 배열의 출력 결과이다. 리스트와 달리 원소 사이에 `,`가 없다. `print(repr())`을 할 경우 `array()`와 `dtype=`을 통해 넘파이 배열이라는 것과 데이터타입을 확인할 수 있다.

# %%
print(vStr)

# %%
print(repr(vStr))

# %%
print(vDatetime)

# %%
print(repr(vDatetime))

# %% [markdown]
# ### 넘파이 배열의 내용 요약하기

# %% [markdown]
# 넘파이 배열의 원소 갯수가 너무 많을 때에는 간단하게 정리해 볼 필요가 있다. 

# %%
v = np.random.randint(1,101,10000)

# %%
v[:5] # 처음 다섯 원소

# %%
v[-5:] # 마지막 다섯 원소

# %%
import pandas as pd
pd.DataFrame({'v':v}).describe()

# %%
import matplotlib.pyplot as plt
plt.hist(v);

# %% [markdown]
# 다음은 무작위 문자열 배열의 경우이다.

# %%
v = np.random.choice(list('abcdef'),10000)
v

# %%
print(v[:5])
print(v[-5:])

# %%
pd.DataFrame({'v':v})

# %%
pd.DataFrame({'v':v}).value_counts()

# %%
pd.DataFrame({'v':v}).value_counts().plot(kind='bar')

# %% [markdown]
# ## CREAD(원소 위치로)

# %% [markdown]
# ### CREATE(다른 변수에서)
#

# %% [markdown]
# 배열을 생성하는 두 번째 방법은 이미 존재하는 배열을 활용하는 것이다. 이때 다음의 두 방법이 존재한다.
#
# 1. 이미 존재하는 **배열을 그대**로 사용하기
# 2. 이미 존재하는 **배열의 일부분**만 사용하기 

# %% [markdown]
# #### 배열 전체
#
# 변수 `arr1`이 넘파이 배열을 가리키고 있을 때,
# `arr2 = arr1`으로 한다면, `arr2`는 `arr1`과 내용이 동일하다.

# %%
arr1 = np.array([3,9,7,14], dtype='int64')
arr2 = arr1

# %%
print(arr1)
print(arr2)

# %% [markdown]
# 이때 `arr2`는 `arr1`을 복사한 것처럼 보이지만, 리스트를 복사할 때와 동일한 상황이 발생한다.
#
# 앞에서 리스트를 복사하는 방법을 살펴보았다. 예를 들어 `lst1`이라는 리스트가 있을 때, 다음의 세 가지 방법의 차이를 구분하였다. 리스트는 리스트의 원소가 가리키는 객체를 복사할 것인지에 따라 별칭(alias)를 만들거나 복사본을 만들었다.
#
# ```
# lst2=lst1
# lst3=lst1.copy()
# lst4=copy.deepcopy(lst1)
# ```

# %% [markdown]
# 배열도 리스트와 동일하게 적용 가능하다.
# ```
# arr2 = arr1
# arr3 = arr1.copy()
# arr4 = copy.deepcopy(arr1)
# ```

# %% [markdown]
# 한 가지 다른 점은 dtype이 `dtype('O')`가 아닌 경우,  넘파이 배열은 실제 내용을 담고 있기 때문에 `copy.deepcopy()`가 필요없다(`copy.deepcopy(arr)`과 `arr.copy()`의 결과가 동일하다). dtype이 `dtype('O')`인 경우에는 배열의 원소가 다른 객체를 가리키는 포인터(객체 레퍼런스)이기 때문에 얕은 카피만으로는 부족하다. 내용이 분리된 배열을 복사하려면 `copy.deepcopy()`가 필요하다.

# %% [markdown]
# 위의 세 가지 방법 외에 배열에서는 `arr1[:]` 또는 `arr1.view()`를 할 수도 있다.
#
# ```
#     arr5 = arr1.view(dtype)
#     arr6 = arr1[:]
# ```
#
# 예를 들어 `arr5 = arr1.view()`를 하면 내용이 그대로인 배열이고, `arr5=arr1.view(dtype='f')`를 하면 `arr1`이 저장되어 있는 메모리의 이진수들을 float(실수형)으로 해석한다. 
#
# `arr6 = arr1[:]`은 `arr6=arr1`과 거의 비슷하다. 둘 다 동일한 원소를 가지고 있으니까.
#    

# %%
arr5 = arr1.view(dtype=bool)
arr5

# %%
arr6 = arr1[:]

# %%
arr1 == arr6 

# %% [markdown]
# 여기서 `==`는 벡터화된 비교 연산으로 각 원소의 같고 다름을 판단한다. 원소가 모두 `True`라는 것은 `arr1`과 `arr6`의 대응하는 원소가 모두 같음을 나타낸다. 그렇지만 완전히 같지는 않은데, 다음에서 `arr2 = arr1`의 `arr2`와 `arr6 = arr1[:]`의 `arr6`을 비교해 보면 다음과 같다.

# %%
arr2 = arr1
arr6 = arr1[:]

# %%
arr2 is arr1, arr6 is arr1

# %%
arr2.base is None, arr6.base is None

# %%
`arr2`는 `arr1`의 별칭(alias)이고, `arr6`는 `arr1`의 뷰(view)이다. `arr7 is arr1.view()

# %%
arr7 = arr1.view()

# %%
arr8 = arr1.view()

# %%

# %%
dir(arr7)

# %%
np.info(arr7)

# %%
np.info(arr8)

# %%
arr7 is arr8

# %%
arr2 is arr1

# %%
arr6.base

# %%
a = arr1[:]
b = arr1

# %%
a.base

# %%
b.base

# %%
np.info(b)


# %%
np.info(a)

# %%
arr2 = arr1

# %%
arr5 = arr1.view()

# %%
id(arr5)

# %%
id(arr1)

# %%
arr1

# %%
arr1.base

# %%
arr5.base

# %%
np.info(arr2)

# %%
np.info(arr5)

# %%
arr2.info()

# %%
help(arr1.view)

# %%

# %% [markdown]
# 이미 존재하는 배열에서 원소의 위치를 지정하여 새로운 배열을 생성하는 방법에 대해 알아본다. 
# 이때 내용을 완전히 복사할 수도 있고, 그냥 내용을 확인할 수 있는 변수를 만들 수도 있다. 
#
#

# %% [markdown]
#

# %% [markdown]
#

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

# %%

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

# %%
만약 원소의 순서를 거꾸로 바꾸고 싶다면, 

# %%
a[::-1]

# %%

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
a = np.array([1.4,2.1,3.3,4.5])
b = np.array([2.1,3.3,5.0,7.9,9.1,11.4])

# %%
print("                      a   = ", a)
print("                      b   = ", b)

np.isin(a, b)          
# 진리값 벡터 : a[0]이 b의 원소인가?, a[1]이 b의 원소인가?, ...
print("           np.isin(a,b)   = ", np.isin(a,b))
print("                            ",
      [a[0] in b, a[1] in b, a[2] in b, a[3] in b])

a[np.isin(a, b)]          # a의 원소 중에서 b에 존재하는 원소
print("         a[np.isin(a,b)]  = ", a[np.isin(a,b)])

np.where(np.isin(a,b))    # a의 원소는 b의 어디에 존재하는가?
print("  np.where(np.isin(a,b))  = ", np.where(np.isin(a,b)))

a[np.where(np.isin(a,b))] # a의 원소 중 b에 존재하는 원소
print("a[np.where(np.isin(a,b))] = ", a[np.where(np.isin(a,b))])


# %%

# %% [markdown]
# #### 비슷한 역할을 하는 함수 
# * `np.nonzero()` : 어디가 nonzero인가

# %%
np.nonzero(np.array([1,0,0,1,1.4,2]))  # index 구하기

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

# %% [markdown]
# ## 왜 넘파이 배열인가?

# %% [markdown]
# 1. 연산 속도가 빠르다.
# 2. 연산이 벡터화되어 `for` 문 없이도 전체 원소에 대한 연산이 가능하다.
#
#

# %% [markdown]
# ### 벡터화된 연산
#
# #### 모든 원소에 대해 연산을 수행하는 방법 비교
#
# 1. `for` 문
# 2. list-comprehension
# 3. 넘파이 배열의 벡터화된 연산

# %%
# for 문
lst = [1,2,3,4,5]
res = []
for x in lst:
    res.append(x**2)
res

# %%
# list-comprehension
lst = [1,2,3,4,5]
[x**2 for x in lst]

# %%
# numpy vectorized operation
arr = np.array([1,2,3,4,5])
arr*2

# %% [markdown]
# #### 여러 가지 벡터화된 연산

# %%
arr > 3

# %% [markdown]
# ### Fancy-Indexing

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

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ## READINGLIST
#
# ### type vs class
# * https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

# %%

# %%

# %% [markdown]
# 패키지 `numpy`의 버전과 기본적인 설정을 확인해보자.

# %%
print(np.__version__)
np.show_config()
# blas_info, blas_opt_info, lapack_info, lapack_opt_info, 
# Supported SIMD extensions in this NumPy install

# %%
utils.lsf(np) # subpackage는 출력되지 않음!!!

# %%
import pkgutil
import numpy
package=numpy
for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
                                                      prefix=package.__name__+'.',
                                                      onerror=lambda x: None):
    print(modname)

# %%
import numpy

# %%
len(utils.lsf(numpy.random)), len(utils.lsf(numpy.core)), len(utils.lsf(numpy.distutils)), len(utils.lsf(numpy.f2py)), \
len(utils.lsf(numpy.fft)), len(utils.lsf(numpy.lib)), len(utils.lsf(numpy.linalg)), len(utils.lsf(numpy.ma)), \
len(utils.lsf(numpy.matrixlib)), len(utils.lsf(numpy.polynomial)), len(utils.lsf(numpy.random)), len(utils.lsf(numpy.testing)), \
len(utils.lsf(numpy.tests)), len(utils.lsf(numpy.typing)) # tests는 유닛 테스팅?

# %%

# %%
from mypack import utils
