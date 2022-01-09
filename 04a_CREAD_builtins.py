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
# - 아직 클래스, 인스턴스는 필요없고.
# - 가변, 불변 객체에 대해서 

# %% [markdown]
# 파이썬은 범용 프로그램으로 builtins 모듈에 범용적으로 사용할 수 있는 **타입**(클래스)가 여럿 존재한다.
# 특히 여러 개의 값을 저장하기 위해 사용하는 클래스는 `list`, `tuple`, `dict`, `set`등이 있다.
# 솔직히 얘기하면 데이터 분석을 할 때 데이터를 저장하기 위한 용도로 `list`, `tuple`, `dict`, `set` 등을 사용하는 경우는 극히 드물다.
# 왜냐하면 좀더 빠르고 효율적인 제3자 패키지인 `numpy` 또는 `pandas`가 개발되었기 때문이다.
#
# 하지만 `list`, `tuple`, `dict`, `set` 등은 파이썬 전반에 두루 사용되기 때문에 파이썬으로 무엇을 하든 반드시 배워야한다.

# %% [markdown]
# > **R과 비교** : R에서 주로 사용하는 데이터 구조는 벡터이다. 반면 파이썬에서는 리스트를 광범위하게 사용한다. 파이썬의 리스트는 R의 리스트와 마찬가지로 어떤 종류의 객체로 원소로 저장할 수 있다는 점에서 비슷하지만, R의 리스트가 원소를 모두 저장하는 반면 파이썬의 리스트는 어떤 객체를 가리키는 **포인터**의 모음이라는 점에서 차이가 있다. 그리고 이런 차이가 R 사용자가 파이썬에서 헤매는 원인을 제공한다. 따라서 R의 벡터 또는 리스트와 파이썬의 리스트의 차이점을 반드시 숙지할 필요가 있다. 

# %% [markdown]
# ### 먼저 객체

# %% [markdown]
# 앞에서 파이썬의 거의 모든 것은 객체라고 했다. 예를 들어 정수 `3`도, 실수 `3.14`도 객체이다. 함수도 객체이고, 모듈도 객체이고, 아무튼 뭐라고 부를 수 있는 것은 객체라고 생각해도 좋다. 구체적으로 어떤 변수에 할당할 수 있는 무엇은 **객체**이다.

# %% [markdown]
# 객체가 메모리에 저장되려면 메모리에 이진수로 표현되어야 한다. 그런데 객체가 필요로 하는 메모리의 크기는 객체마다 다르다. 정수 `3`, 실수 `3.14`, `builtins` 모듈, 내장 모듈의 `abs` 함수는 모두 객체이지만, 저장하기 필요한 메모리 공간은 천차만별이다. 
#
# 파이썬은 무한대의 정수를 저장할 수 있기 때문에 정수의 크기에 따라 필요한 메모리 공간이 달라진다. 실수형 수 하나를 저장하는 데에는 64비트 컴퓨터에서 보통 8 바이트(64 비트) 또는 16 바이트(128 비트)를 사용한다. 모듈을 저장하기 위해서는 모듈에서 저장하는 함수, 변수의 종류, 갯수에 따라 필요한 메모리가 달라질 것이다.

# %% [markdown]
# 만약 파이썬과 같은 동적 타입에서 변수에 객체를 바로 저장한다면 몇 가지 문제가 생긴다. `a=3`을 한 후, `import numpy as a`를 해보자. 변수 `a`는 정수 `3`을 저장하기 위해 필요한 메모리를 확보하고 `3`을 저장한다. 그리고 `numpy` 모듈을 불러들이면서 모듈의 모든 내용을 저장하기 위해 훨씬 큰 메모리가 필요로 하게 된다. 기존의 메모리로는 어림도 없으므로 새로운 메모리를 찾아야 한다.

# %% [markdown]
# 크기가 천차만별인 객체를 한 변수에 저장하는 다른 방법은 변수가 아니라 객체에 메모리를 배정하는 것이다. 자세히 풀어보자. 우리가 실행하는 프로그램에서 정수 `3`이 필요하다면 메모리의 한 장소에 정수 `3`을 저장한다. 그리고 변수 `a`는 정수 `3`을 가리키게 한다. 그리고 `import numpy`를 하면서 메모리에 충분히 큰(`numpy` 모듈이 들어갈 수 있을 만큼 큰) 장소를 배정하여 `numpy` 모듈의 내용을 저장한다. 그리고 변수 `a`가 가리키는 것을 살짝 바꿔서 `numpy` 모듈을 가리키게 한다.

# %% [markdown]
# 이런 방식에서 변수는 어떤 값을 저장하지 않는다. 단지 메모리에 존재하는 **객체를 가리킬 뿐이다.** 메모리의 한 주소를 가리킨다는 점에서 컴퓨터 공학에서는 흔히 포인터(pointer)라는 용어를 사용하기도 한다. 하지만 포인터는 값은 주소이지만, 파이썬 **변수의 값**은 해당 객체이다.

# %% [markdown]
# ### 불변 객체와 가변 객체

# %% [markdown]
# 객체는 불변(immutable) 객체와 가변(mutable) 객체로 나뉜다. 이전 장에서 소개했던 `int`(정수형), `float`(실수형), `complex`(복소수형), `str`(문자열형), `datetime.datetime`(날짜시간형)는 모두 **불변형**이다.
#
# 근데 뭔가 이상하지 않은가? `a=3`를 한 후, `a=a+1`, `a=4` 등도 아무런 어려움 없이 작동하지 않는가? 여기서 **불변**의 대상은 변수가 아니다(**변**수는 **변**한다). 불변 객체에서 변하지 않는 것은 객체이다. 파이썬에서 정수 `3`이 메모리에 저장된다면, 정수 `3`은 변하지 않는다. 
#
# `a=3`을 하면 메모리에 정수 `3`을 저장하고, 변수 `a`는 정수 `3`을 가리킨다. 그런 후 `a=a+1`을 하면 정수 `4`가 생성되어 메모리에 저장되고, 변수 `a`는 방향을 바꿔 정수 `4`를 가리키게 된다. `a=a+1`은 `a+1`에서 먼저 객체 `4` 생성하고, 변수 `a`가 객체 `4`를 가리키게 한다 .
#
# 이 과정에서 메모리에 이미 저장되어 있는 정수 `3`은 변하지 않는다. 단지 필요가 없어질 때 사라질 뿐이다. 앞에서 불변 객체의 예로 들었던 `int`(정수형), `float`(실수형), `complex`(복소수형), `str`(문자열형), `datetime.datetime`(날짜시간형)의 값은 모두 불변형이다.

# %% [markdown]
# #### 리스트(list)
#
# 리스트는 여러 값을 모아 하나의 값(객체)을 구성한다. 리스트는 가변 객체이다. 여기서 리스트가 무엇이며 무엇이 **가변**인지 자세히 알아보자. 

# %%
lst = [3, 2, 5]

# %% [markdown]
# 리스트는 `[`,`]`안에 원소를 나열하여 생성한다. `[3,2,5]`를 하면 원소가 `3`,`2`,`5`인 리스트가 만들어지고 변수 `lst`는 이 객체(리스트)를 가리키게 된다. 이 리스트의 첫 번째 원소는 `lst[0]`, 두 번째 원소는 `lst[1]`으로 표기한다. 그렇다. 파이썬은 0번째부터 시작한다. 그래서 `lst[0]`을 0번째 원소라고도 말한다. 헷갈리지 않는가? 당연히 `lst[0]`을 첫 번째 원소라고 부르다가 0번째 원소라고 부르다가 다시 1번째 원소라고 부르면 헷릴 것이다. 이 책에서는 파이썬을 얘기할 때에는 항상 0번째부터 시작한다.

# %% [markdown]
# 이제 가변이므로 변화를 줘보자. `lst[0] = 5`를 해보자. 큰 무리없이 작동한다.

# %%
lst[0] = 5
lst[0]

# %% [markdown]
# `3`이 `5`로 바뀌었나? 아니다. `int`타입 `3`은 불변객체이다. 따라서 메모리에 저장된 `3`이 `5`로 바뀌거나 덮어씌어지는(overwrite) 일은 일어나지 않는다. 그렇다면 어떻게 `lst[0]`은 `5`를 **가리키나?** 그렇다! `lst[0]`도 변수와 마찬가지로 어떤 값을 저장하는 게 아니라 어떤 값(객체)를 가리킨다. 그리고 무엇을 가리키느냐는 바뀔 수 있다.

# %% [markdown]
# 정리를 해보자. 불변객체 `3`은 바뀌지 않는다. 가변 객체 리스트는 변할 수 있다. 그런데 리스트가 무엇인가? 리스트란 단지 일정한 갯수의 포인트이다. 

# %% [markdown]
# 다시 한번 `lst=[1,3,2]`가 내부적으로 어떻게 작동하느지 도식적으로 상상해보자. `[1,3,2]`를 하면 포인터 3개짜리 리스트가 만들어진다. (그리고 **가변 객체** 리스트는 이 3개의 포인트가 가리키는 대상이 변할 수 있다.) 그리고 불변 객체 `1`,`3`,`2`는 메모리 상의 어딘가에 생성된다. (그리고 결코 변하지 않을 것이다.) 리스트의 3 포인트는 차례로 `1`, `3`, `2`를 가리킨다. 그리고 변수 `lst`는 (포인트가 차례로 `1`,`3`,`2`를 가리키는) 방금 생성한 리스트를 가리킨다.

# %% [markdown]
# 그래서 가변 객체가 불변 객체와 어떻게 다르게 행동하는가? 다음을 보자.

# %%
val1 = val2 = val3 = 5

# %%
lst1 = lst2 = lst3 = [1,3,2]

# %% [markdown]
# 변수 `val1`, `val2`, `val3`은 모두 정수 `5`를 가리킨다. `val1`이라고 쓰면 정수 `5`가 나온다.

# %%
val1, val2, val3

# %% [markdown]
# 변수 `lst1`, `lst2`, `lst3`는 모두 원소가 `1`,`3`,`2`인 리스트를 가리킨다. `lst1`이라고 쓰면 `[1,3,2]`가 출력된다.

# %%
lst1, lst2, lst3

# %% [markdown]
# 여기서 `val2 = 6`을 해보자. `val2`는 `5`를 버리고 `6`을 가리킨다.

# %%
val2 = 6
val1, val2, val3

# %% [markdown]
# 반면 `lst2[1] = 30`을 해보자. `lst1`, `lst3`에 어떤 변화가 생기는가?

# %%
lst2[1] = 30
lst1, lst2, lst3

# %% [markdown]
# 모두 `[1, 30, 2]`로 바뀌었다! 왜 그럴까?

# %% [markdown]
# 우선 `val1=val2=val3=5; val2=6`부터 설명해보자. `val1=val2=val3=5`로 메모리에 `5`가 생성되고, `val1`, `val2`, `val3`는 모두 `5`를 가리킨다. `val2=6`를 하면 정수 `6`이 생성된 후 `val2`는 `5`를 버리고 `6`을 가리킨다. 그래서 결과적으로 `val1`은 `5`를 가리키고, `val2`는 `6`을 가리키고, `val3`는 `5`가리킨다.

# %% [markdown]
# 그렇다면 `lst1 = lst2 = lst3 = [1,3,2]; lst2[1] = 30`은 어떤 식으로 작동할까? 먼저 `lst1 = lst2 = lst3 = [1,3,2]`를 보자. 리스트 `[1,3,2]`를 만든다. 메모리에 `1`, `3`,`2`를 만들고 원소 3개짜리 리스트를 만들어서 각 원소가 `1`, `3`, `2`를 가리키게 한다. 그리고 `lst1`, `lst2`, `lst3`는 모두 이 리스트를 가리킨다.
#
# 이제 `lst2[1] = 30`을 하면 리스트의 1번째는 `3`을 버리고 `30`을 가리킨다. 이제 `lst1`, `lst2`, `lst3`을 다시 보자. 리스트의 1-번째 원소가 가리키는 값이 바뀌었지만, 리스트는 메모리의 동일한 위치 존재한다. `lst1`, `lst2`, `lst3`가 모두 그 리스트를 가리키고 있다는 점도 동일하다. 따라서 `lst1`, `lst2`, `lst3`을 출력하면 모두 `[1,30,2]`가 되는 것이다.
#
#

# %% [markdown]
# 마치 `lst1`, `lst2`, `lst3`가 연결된 듯, 또는 한 몸처럼 행동한다. 만약 `lst1`, `lst2`, `lst3`가 각자 따로 값을 유지할 수 있도록 하려면 세 개의 리스트를 만들어야 한다. 다음을 보자.

# %%
lst3 = [1,3,2]
lst2 = lst3.copy()
lst1 = lst2.copy()
lst2[1] = 30
lst1, lst2, lst3

# %% [markdown]
# 이제 차근차근 위의 코드를 읽어보자.
#
# 1. `lst3 = [1,3,2]` : `lst3`은 리스트 `[1,3,2]`를 가리킨다(이렇게 간단하게 썼지만 포인트 3개짜리 리스트와 불변객체 `1`,`3`,`2`가 따로 저장된 메모리를 상상해야 한다).
# 2. `lst2 = lst3.copy()` : 리스트 `lst3`를 복사하여 동일한 내용의 리스트를 생성한다. 그리고 `lst2`는 이 리스트를 가리킨다. `lst2`는 `[1,3,2]`를 가리킨다. 하지만 `lst3`가 가리키는 리스트 `[1,3,2]`와 다른 객체이다(메모리에서 개별적으로 저장된다).
# 3 `lst1 = lst2.copy()` : 리스트 `lst2`를 복사하여 동일한 내용의 리스트를 생성한 후, `lst1`이 그 리스트를 가리키게 한다. 결론적으로 메모리에는 `[1,3,2]`가 세 개 존재하게 된다. `lst2[1]=30`을 하면 `lst2`가 가리키는 리스트의 두 번째 원소가 `30`을 가리키게 한다. 
# 4. 이제 `lst1`을 출력하면 `[1,3,2]`이고 `lst2`를 출력하면 `[1,30,2]`가 된다.

# %% [markdown]
# 여기서 명심하자. 리스트는 포인터의 집합이다. **리스트를 복사**하는 것은 **포인터 모임을 복사**하는 것이다. 

# %% [markdown]
# 동일한 리스트를 여러 변수에 할당하는 것과 복사하는 것의 차이는 파이썬에서 객체의 ID(식별자)를 반환하는 `id()`함수로 확인할 수 있다.

# %%
lst1 = lst2 = lst3 = [1,3,2]
id(lst1), id(lst2), id(lst3)

# %% [markdown]
# 여기서 눈여겨 봐야하는 것은 `id()`의 값이 모두 같다는 것이다. `lst1`, `lst2`, `lst3`가 모두 하나의 객체를 가리킨다는 것을 보여준다. 반면 복사를 하는 경우를 보자.

# %%
lst2cp = lst1.copy()
lst3cp = lst2.copy()
id(lst1), id(lst2cp), id(lst3cp)

# %% [markdown]
# `id()` 결과를 보면 알 수 있듯이 `lst1`, `lst2`, `lst3`는 서로 다른 객체이다. 이를 쉽게 알 수 있는 방법은 `is` 연산자를 사용하는 것이다. 만약 두 객체 `a`, `b`가 동일한 경우 `a is b`는 `True`가 나오고, 그렇지 않으면 `False`이다.

# %%
lst1 is lst2, lst1 is lst3, lst1 is lst2cp, lst1 is lst3cp

# %% [markdown]
# #### 얕은 복사와 깊은 복사

# %% [markdown]
# 리스트의 값이 연결되지 않고 각자의 값을 나타내려면 리스트를 **복사**해야 했다. 복사를 해야하는 근본적인 원인은 리스트가 아니라 리스트의 원소를 변경하려고 하기 때문이고, 리스트의 원소는 그 자리에서 변경이 가능하기 때문이다. 예를 들어 `lst1=lst2=lst3=[1,3,2]`에서 `lst2=[1,30,2]`를 하면 `lst1`과 `lst2`가 연결되지 않는다.

# %%
lst1 = lst2 = lst3 = [1,3,2]
lst2 = [1,30,2]
lst1, lst2, lst3

# %% [markdown]
# 만약 리스트의 수준이 깊어지면 얕은 복사만으로는 리스트를 각자 유지하는 게 힘들 수 있다. 예를 들어 다음을 보자. 

# %%
lst1 = [1,[3,4],2]
lst2 = lst1.copy()
lst3 = lst2.copy()
lst1, lst2, lst3

# %% [markdown]
# 이제 `lst1[1][0] = 30`을 해보자. 그리고 `lst2`, `lst3`을 확인해보자.

# %%
lst1[1][0] = 30
lst1, lst2, lst3

# %% [markdown]
# 먼저 `lst1[1][0] = 30`을 살펴보자. `lst[1]`은 `[3,4]`를 가리킨다. 앞에서 얘기했듯이 `lst[1]`은 포인터 두 개짜리 리스트를 가리키고, 0번째 포인터는 `3`, 1번째 포인터는 `4`를 가리킨다. `lst[1][0]`은 원소 3개짜리 리스트의 1-번째 원소(이 역시 리스트이다)의 0번째 원소를 가리킨다. 따라서 원소 3개짜리 리스트가 하나 있고, 원소 2개짜리 리스트가 하나 있다. 그리고 첫 번째 리스트의 1번째 포인터는 두 번째 리스트를 가리킨다. 
#
# 만약 `lst2 = lst1.copy()`를 하면 두 개의 리스트 중 첫 번째만 리스트만 복사된다. 얕은 복사이다. `lst3 = lst2.copy()`도 마찬가지이다. 따라서 3개의 포인터 3개짜리 리스트와 1개의 포인터 2개짜리 리스트가 존재하게 된다.
#
# 이제 `lst1[1][0]=30`을 하면 `lst1[1]`의 0번째 원소는 `3`이 아니라 `30`을 가리킨다. 그런데 `lst1[1]`과 `lst2[1]`, 그리고 `lst3[1]`는 모두 동일한 원소 2개짜리 리스트를 가리킨다. 따라서 `lst1`, `lst2`, `lst3`를 출력하면 동일한 값이 출력되는 것이다.

# %% [markdown]
# 그렇다면 `lst1`, `lst2`, `lst3`를 모두 분리하려면 어떻게 해야 하나? `lst1`가 가리키는 객체 중에서 모든 가변 객체를 복사해야 한다. 이를 위해 `copy` 모듈의 `deepcopy()` 함수를 사용할 수 있다.

# %%
import copy
lst1 = [1,[3,4],2]
lst2 = copy.deepcopy(lst1)
lst3 = copy.deepcopy(lst1)
lst1[1][0] = 30
lst1, lst2, lst3

# %% [markdown]
# 안정적인 리스트 관리를 위해서는 **얕은 복사**(shallow copy)와 **깊은 복사**(deep dopy)를 구분할 줄 알아야 한다. 
# 얕은 복사는 하나의 리스트를 복사한다. 깊은 복사는 리스트의 포인터가 다시 리스트를 비롯한 다른 가변 객체를 가리킬 경우에는 그 가변 객체도 복사한다. 아니 리스트의 모든 포인터가 닿는 가변 객체를 복사한다.
#

# %% [markdown]
# 다음은 가변객체인 딕에 대해서도 위에서 설명한 상황이 펼쳐진다는 점을 분명히 보여준다. `.copy()`를 해도 `lst3[1]['a'][2]`의 변화는 `lst2`, `lst1`의 출력도 변화시킨다. 하지만 `copy.deepcopy()`를 사용할 경우에는 `lst1`, `lst2`, `lst3`는 서로 분리된다.

# %%
lst3 = lst2 = lst1 = [1,{'a':[3,4,5]},2]
lst3[1]['a'][2] = 50
lst1, lst2, lst3

# %%
lst1 = [1,{'a':[3,4,5]},2]
lst2 = lst1.copy()
lst3 = lst1.copy()
lst3[1]['a'][2] = 50
lst1, lst2, lst3

# %%
lst1 = [1,{'a':[3,4,5]},2]
lst2 = copy.deepcopy(lst1)
lst3 = copy.deepcopy(lst1)
lst3[1]['a'][2] = 50
lst1, lst2, lst3

# %% [markdown]
# ### 불변 vs 가변

# %% [markdown]
# 어쩌면 아이러니해 보일 수 있다. 변수 `x`가 가리키는 것이 **불변 객체**라면 변수 `x`에 해당 객체가 저장되었다고 생각해도 큰 무리가 없다. `x`를 변형시키면 `x`는 새로운 객체를 가리키게 되기 때문이다.
#
# 변수 `x`가 가리키는 것이 **불변 객체**라면, `x`를 거치지 않고 `x`를 변화될 일이 없다.

# %% [markdown]
# 반면 변수 `x`가 가리키는 것이 **가변 객체**이고, 다른 변수 `y`도 동일한 **가변 객체**를 가리킨다면, 변수 `y`를 통해 수정이 가능하다. 이런 경우에는 변수 `x`에 어떤 변화도 없지만, `x`의 내용이 달라진다.

# %% [markdown]
# #### 종합

# %% [markdown]
# 파이썬 리스트와 R 리스트의 가장 큰 차이를 보았다. 파이썬 리스트는 가변 객체이고, R 리스트는 불변 객체이다. R 리스트는 원소 하나만 바뀌어도 새로운 리스트를 생성해야 하지만 파이썬은 그렇지 않기 때문에 서로 다른 두 변수가 같은 같은 리스트를 가리키거나 서로 다른 두 리스트의 어떤 원소가 동일한 객체를 가리킬 수도 있다.
#
# 사실 이렇게 변수 `a`를 명확하게 언급하지도 않으면서 `a`를 수정할 수 있다는 것은 프로래밍을 복잡하게 하고 해결하기 어려운 버그를 생산한다. R은 기본 데이터 타입은 이런 상황이 발생하지 않도록 고안되었다. R이 파이썬보다 쉽게 느껴지는 이유 중의 하나일 것이다.

# %% [markdown]
# 그렇지만 파이썬 리스트에서 위의 상황을 걱정하지 않아도 되는 경우도 많다. 예를 들어 리스트를 `lst1 = [1,3,2]; lst2 = lst1`와 같이 다른 변수에 할당하지 않는다면 위와 같은 경우는 발생하지 않는다. 리스트 안에 리스트를 만드는 경우도 그리 흔치 않으므로 위의 설명을 완전히 이해하지 못했다고 걱정할 필요는 없다. 하지만 그런 경우에는 리스트는 항상 깊은 복사를 하고, 되도록 리스트 안에 리스트를 구성하지 않도록 하자. 

# %% [markdown]
# 이 장에서는 파이썬의 가장 기본적인 데이터 구조인 `list`, `tuple`, `dict`, `set`에 대한 데이터 전처리 방법을 배운다. `list`와 `tuple`은 가변, 불변 쌍둥이라고 할만큼 가변성을 제외하고는 비슷하다. `dict`, `set`은 모두 가변객체이다. `set`은 가변객체이지만, 그 원소가 가변객체가 될 수는 없다.

# %% [markdown]
# # 파이썬 `list`, `tuple`, `dict`, `set`에서 CREAD
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
# 딕는 **이름**을 사용한다. 예를 들어, 이름이 Mary인 원소는 뭐냐? 이름이 5인 원소는 뭐냐?라는 질문에 빠르게 대답할 수 있다.
# 셋은 우리가 흔히 말하는 **집합**이다. 집합은 순서가 없고, 있냐 없느냐(존재 유무)만 구분 가능하다. 이를 **원소 자신**이 이름인 경우로 생각해 볼 수 있다. 그래서 `"Mary"`가 있느냐? `5`가 있느냐?라는 질문에 빠르게 답할 수 있다.
#
# 여기서 빠르게 대답할 수 있는 것이 무엇인가?가 `list`, `dict`, `set`을 구분한다고 볼 수 있다. `list`의 경우도 어떤 이름이 존재하냐라는 질문에 답할 수 있지만, 모든 원소를 확인하여 비교해야 한다. `dict`와 `set`에는 순번이라는 개념 자체가 없다.
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


# %%
### 부록

# %% [markdown]
# ## 부록 : 임의의 여러 원소 2
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
# ### 연습문제(리스트 슬라이싱)
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
# `id(y1)`은 변수 `y1`이 가리키는 메모리 주소를 가리킨다고 생각하면 쉽다. `id(y1)==id(y2)`은 변수 `y1`이 가리키는 객체와 `y2`이 가리키는 객체가 동일하다는 것을 알려준다. 따라서  `y1`과 `y2`는 동일한 객체를 가리키는 서로의 별칭(alias)라고 할 수 있다

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
# ### Hashable
#
# 리스트와 같은 가변 객체는 딕의 키나 셋의 원소가 될 수 없다. 
#
# 딕 또는 셋은 어떻게 이름을 빠르게 찾을 수 있을까? 리스트와 같이 메모리 주소를 **계산**할 수 있다면 바로 원소를 찾을 수 있겠지만 딕의 키는 정수형, 문자형 등 다양한 타입이지 않은가? 맞다. 딕의 키로 다양한 타입의 값을 사용할 수 있지만, 모든 값이 가능한 것은 아니다. 왜냐하면 딕은 키를 주소처럼 사용한다. 정확히 말하면 키에 특별한 계산을 하여 값이 존재하는 메모리를 단 순간에 찾아내는 것이다. 
#
# 간단한 예를 들어보자. `d = {'apple':3, 'banana':35, 'melon':45', 'grape':32}`라고 하자. `d['apple']`은 `3`이다. 이때 값의 종류나 크기는 문제가 아니다. 왜냐하면 딕은 포인터를 가지고 있을 뿐 객체를 모두 저장하지 않기 때문이다. 따라서 딕는 여러 개의 포인터를 가지고 있다. 여기서 정확히 4개가 아닌 이유는 딕은 여유분의 메모리가 필요하다. 왜냐하면 딕의 키로 어떤 값이 필요할지 미리 알 수 없기 때문이다. 그리고 키가 몇 개나 필요할지도 미리 알 수 없다(딕은 가변객체이다. 딕에 원소를 추가할 수 있다). 
#
# 만약 딕에 기본적으로 100개의 주소를 마련한다고 해보자. 이제 키에서 주소를 찾는 법을 알아야 한다. 가장 쉬운 방법은 첫 번째 문자의 아스키코드에서 100을 나눈 나머지로 주소를 정하는 것이다. 첫 번째 문자의 아스키 코드값을 구해보자. `a`는 97, `b`는 98, `m`은 109, `g`는 103이다. 이제 100을 나눠보면 `d['apple']`의 값은 메모리 주소 97에, `d['melon']`의 값은 메모리 주소 9에 저장하면 된다. 이런 식으로 저장하면 일렬로 키와 값(을 가리키는 포인터)를 저장한 후 처음부터 키를 확인하는 과정에 비해 훨씬 빠른 속도로 값을 찾을 수 있다. 이렇게 수가 아닌 데이터에 적절한 계산을 하여 주소를 생성하는 방법을 해쉬표(hash table)을 만든다고 한다. 
#
# 그런데 만약 키가 변화된다면 어떻게 될까? 키가 가리키는 주소도 바뀌게 되고 따라서 원래 주소로 가서 원래 객체를 찾을 수 없다. 예를 들어 `d={lst:'three'}`이고, `lst=[3,4]`가 `lst[1]=5`로 해서 `lst`가 `[3,5]`로 바뀌었다고 해보자. 이렇게 키로 쓰인 `lst`가 바뀌면 바뀌기 전에 계산된 주소(해쉬값)를 얻을 수 있는 방법이 없게 되는 문제가 생긴다. 그래서 딕의 키는 불변 객체만 사용할 수 있다. 딕의 키로 쓸 수 있는 값을 Hashable이라고 하기도 한다. 
#
#

# %%

# %% [markdown]
# ## 모든 원소를 한꺼번에 수정하는 방법
#
# 예를 들어 리스트 `lst=[1,2,3]`의 모든 원소를 제곱하고 싶다고 해보자.

# %%
lst = [1,2,3]

# %% [markdown]
# ###`for` 문 : 순번

# %%
res = [] # 결과를 담을 빈 리스트
for i in range(len(lst)):
    res.append(lst[i]**2)
res

# %%

# %% [markdown]
# ###`for` 문 : 원소

# %%
res = []
for x in lst:
    res.append(x**2)
res

# %%

# %% [markdown]
# ### list comprehension : more pythonic!
#
# * Beautiful, Simple, Sparse, Readability
# * One obvious way to do it
# * If the implementation is easy to explain, it may be a good idea.
# * Namespaces are one honking great idea -- let's do more of those!

# %%
res = [x**2 for x in lst]
res

# %%
# Namespace!!!
res = []
res = [res**2 for res in lst]
res

# %%
list(map(lambda x: x**2, lst))

# %%
import this # PEP20

# %% [markdown]
# ### What is Pythonic?
#
# PEP(Python Enhancement Proposals)

# %%
