# -*- coding: utf-8 -*-
# %% [markdown]
# ## READINGLIST
#
# ### type vs class
# * https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

# %% [markdown]
# > R에서 배열은 1차원 벡터의 다차원 확장 쯤으로 생각했다. R에서 모든 배열은 벡터와 동일한 형태로 저장되어 있고, 각 차원의 크기가 설정되어 있다는 점만 다르다. 사용 용도 및 범위에서 R의 벡터에 해당하는 것은 파이썬의 리스트일 것이다. 가장 기본적으로 사용되고, 또 어디서나 사용되기 때문이다. 하지만 파이썬의 리스트는 속도가 느리다는 치명적인 단점이 있다. 이를 해결한 것이 제3자 패키지인 `numpy`이고, `numpy`를 데이터 분석용으로 확장, 발전시킨 것이 또다른 제3자 패키지인 `pandas`이다. `numpy`의 배열(`ndarray`), 그리고 `pandas`의 `Series`는 모두 R의 벡터와 같이 **동일한 타입**의 데이터를 저장한다는 특징을 지녔다. `numpy`는 수치계산에 특화되어 있고, `pandas`는 범용 데이터 분석이라고 생각할 수도 있다. 또 다른 차이는 `numpy`의 배열은 다차원으로 확장할 수 있고, `pandas`의 `Series`는 여러 타입의 데이터를 모아 데이터 프레임을 구성할 수 있다.

# %% [markdown]
# 파이썬에 R의 1차원 벡터를 대신할 수 있는 데이터 구조는 앞에서 소개한 리스트와 
# **넘파이 배열(numpy array)**과 **판다스 시리즈(pandas series)**가 있다.
#
# 여기서는 numpy의 배열에 대해 알아본다. 특히 여기서는 배열의 차원을 1로 제한하여 알아본다.
# 1차원 넘파이 배열은 동일한 type의 값이 메모리에 순차적으로 순번에 따라 저장되어 있는 **가변 객체**이다.

# %%
from mypack import utils

# %%
import numpy as np

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
# `dtype('bool')`, `dtype('int64')`, `dtype('float64')`의 의미는 쉽게 유추 가능할 것이다. 논리형, 64비트 정수형, 64비트 실수형이다. `dtype('<U21')`의 `U`는 유니코드를, `<21`은 최대 글자 갯수를 나타낸다. `arr_str[0][:21]`을 하면 0-번째 원소의 모든 글자를 포함하게 된다.[^strlen] `dtype('O')`는 객체(Object)를 가리킨다. 사실 파이썬의 모든 것은 객체이므로 이건 뭘 특별히 저장하고 있다는 의미가 없다. 뒤에서 설명하겠지만 `dtype('O')`의 경우 값을 저장하지 않고 포인터를 저장한다.
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

# %%
<그림 ??? 삽입>

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
# 마지막으로 dtype이 `dtype('O')`인 경우는 리스트와 동일하게 배열은 포인터(객체가 저장된 주소)를 저장하게 된다.

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

# %%
# Indexing : https://www.labri.fr/perso/nrougier/from-python-to-numpy/#id58

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

# %%

# %%
어디가 nonzero인가?


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
