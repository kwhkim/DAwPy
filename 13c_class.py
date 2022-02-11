# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: rtopython3-pip
#     language: python
#     name: rtopython3-pip
# ---

# %% [markdown]
# ## 객체
#
# * 참고 자료 
#   - https://docs.python.org/3.8/tutorial/classes.html
#   - https://docs.python.org/3.8/reference/datamodel.html

# %% [markdown]
# 파이썬 공식문서의 "데이터 모델(data model)"을 보면 다음과 같은 문장이 나온다.

# %% [markdown]
# > Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects.
#
# > 객체(object)는 파이썬에서 데이터를 추상화한다. 파이썬 프로그램의 모든 데이터는 객체 또는 객체 사이의 관계로 표현된다.

# %% [markdown]
# 그렇다면 객체(object)란 무엇인가? 

# %% [markdown]
# > Every object has an identity, a type and a value.

# %% [markdown]
# 객체란 **id**, **타입**, 그리고 **값**을 가진 무엇이다. 앞에서 우리는 타입이 어떤 역할을 하는 지 배웠다. 타입은 컴퓨터 메모리에 저장된 이진수가 무엇을 의미하는지, 그리고 어떤 연산이 가능한지를 결정한다. 마지막으로 `id`란 이진수가 저장된 메모리의 주소라고 생각할 수 있다. 실례를 통해 그 의미를 다시 알아보자.

# %% [markdown]
# 우선 메모리의 2바이트로 저장 가능한 이진수 `0b0100000101000010`를 생각해보자. 메모리에 저장된 값은 그 값만 가지고는 무엇을 의미하는지 알 수 없다. 값이 무엇을 의미하는지는 **타입**에 의해 결정된다. 만약 앞의 이진수가 정수타입이라면 16706을 의미한다. 만약 문자열 타입이라면 `AB`를 의미한다.

# %%
0b0100000101000010

# %%
chr(0b01000001), chr(0b01000010)

# %%

chr(0b0100001001000001)


# %% [markdown]
# 파이썬에서 `x=16706`라고 쓰면 파이썬은 `16706`을 적절히 이진수로 변환하여 메모리에 저장하고, 이 **값**이 나중에 읽을 때 정수형으로 읽어야 한다는 것을 표시하고 그 주소를 알려줄 것이다. 이때 정수형으로 해석되어야 한다는 것이 **타입**의 역할이며, 메모리 주소는 **id**라고 생각할 수 있다.  
#
# 이렇게 파이썬에서 정수 16706을 나타내기위해 여러가지 간단하지 않은 과정을 거치지만 우리는 그냥 "정수 16706"이라고 생각하고 코딩을 해도 무방하다. 그리고 객체가 id, 타입, 값을 가진다고 할 때 값은 컴퓨터에 저장되는 이진수가 아니라 이진수가 타입을 통해 해석되는 **값**을 의미하는 경우가 많다. 앞에서 봤듯이 같은 값도 타입이 다를 수 있음을 유의하자(예. 정수형 `2`와 실수형 `2`).

# %%

# %% [markdown]
# ## 클래스

# %% [markdown]
# 다음은 `Patient`(환자) 클래스를 정의한다.

# %%
class Patient0():
    pass
        


# %% [markdown]
# 위의 코드에서 `pass`는 어떤 일도 하지 않는다. 그래서 위에서 정의한 `Patient` 클래스는 일종의 깡통 클래스이다. 아무것도 없다.

# %% [markdown]
# 이제 `Patient` 클래스에 속하는 객체를 만들어보자.

# %%
x = Patient0()

# %% [markdown]
# 위의 코드는 Patient 클래스의 객체를 하나 만들고 변수 `x`는 그 객체를 가리키게 한다.

# %% [markdown]
# 여기서 id, 타입, 값을 확인해보자.

# %%
id(x), type(x)


# %% [markdown]
# `id(x)`는 실제 메모리 주소를 반환하기도 하고, 큰 의미없는 정수값이 반환되기도 하지만 다른 객체의 `id()`와는 다르다. 그래서 굳이 `id()`를 구하기 보다는 두 객체의 `id()` 값이 같지만 `is`를 통해 확인하기도 한다. 아래 코드에서 확인하자.

# %% [markdown]
# `type(x)`를 통해 객체 `x`가 우리가 위에서 정의한 `Patient` 클래스임을 확인할 수 있다. 그런데 값은?
#

# %% [markdown]
# 다시 실제 쓸만한 클래스를 만들어 보자.

# %%
class Patient():
    def __init__(self, name):
        self.name = name


# %%
y = Patient('한석봉')

# %% [markdown]
# 클래스 정의가 약간 복잡해지만, `x`를 다시 확인해보자.

# %%
id(y), type(y)

# %%
x is y

# %% [markdown]
# 일단 `id()`를 통해 `id(x)`와 `id(y)`가 다름을 확인할 수 있고, `x is y`를 통해 두 객체가 다른 객체임을 확인할 수 있다. 그리고 `type()`으로 객체가 어떤 클래스에 속하지는도 확인했다. 값은?

# %%
y.name

# %% [markdown]
# 드디어 `y.name`을 통해 객체 `y`에 담긴 정보를 확인해볼 수 있다. 이는 우리가 객체를 `Patient('한석봉')`으로 만들 때 넘겨준 정보이다.

# %% [markdown]
# 여기서 `.name`를 객체 `y`의 **속성(attribute)**이라고 부른다. 보통 객체의 정보는 속성에 저장된다.

# %% [markdown]
# 그런데 다음과 같이 `y`만 치면 알 수 없는 정보만 나열된다. 클래스 이름과 메모리 주소라고 생각하면 된다.

# %%
y


# %% [markdown]
# 위에서 배웠듯이 메모리 주소의 이진수를 클래스에 맞게 해석하면 객체 `y`에 저장된 값을 알 수 있다. 하지만 우리가 직접 그런 작업을 하기엔 우리는 너무 인간이다. 

# %% [markdown]
# 그래서 다음과 같이 클래스를 새롭게 정의할 수 있다.

# %%
class Patient():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return(f'Name is {self.name}')


# %%
z = Patient('한석봉')

# %%
z

# %% [markdown]
# 위에서 `def __repr__():`를 통해 `z`라고 쳤을 때 출력되는 값을 변경하였다.

# %% [markdown]
# 이처럼 클래스는 객체에 저장되는 내용, 객체가 어떻게 작동하는지 등을 모두 결정한다. 그런데 `def __repr__():`은 함수를 정의하는 꼴이다. 실제로 이는 `__repr__()` 함수를 정의하고, 이 함수는 `Patient`라는 클래스의 이름공간(namespace)에서 찾을 수 있다.

# %%
Patient.__repr__

# %% [markdown]
# 객체의 이름공간에서도 찾을 수 있다.

# %%
z.__repr__


# %% [markdown]
# 그런데 동일한 함수 `__repr__`에 대한 출력에서 약간 다른 점을 확인할 수 있다. `Pateint.__repr__`은 function으로 나왔고, `z.__repr__`은 bound method라고 나온다. bound method?

# %% [markdown]
# ### 메소드(method)

# %% [markdown]
# 메소드란 객체에 딸려 있는 함수라고 생각할 수 있다. 

# %%
class Patient():
    def __init__(self, name):
        self.name = name
        
    def upname(self):
        return self.name.upper()
        


# %%
w = Patient('han seok-bong')

# %%
w.upname()

# %% [markdown]
# 클래스 `Patient` 아래 `upname()`이라는 함수를 정의하였다. `upname()`의 정의를 살펴보면 `self`라는 인자를 받는다. 글데 `w.upname()`을 보면 인자가 주어지지 않는 것처럼 보인다. 이것이 함수(function)과 메소드(method)의 차이이다. 메소드는 `w.upname()`처럼 객체의 속성으로 함수를 호출한다. 그리고 첫 번째 인자는 항상 현재 객체(`w.upname()`에서 `w`)가 입력된다. 

# %% [markdown]
# 그래서 메소드(클래스 안의 함수)를 정의할 때에는 항상 첫 번째 매개변수의 이름을 `self`로 하는 관례가 있다.

# %% [markdown]
# `Patient.upname()`은 일반적인 함수이므로 다음과 같이 두 가지 방법으로 클래스 `Pateint`에서 정의된 함수를 사용할 수 있다.

# %%
Patient.upname(w)

# %%
w.upname()

# %% [markdown]
# ## 객체

# %% [markdown]
# 이렇게 클래스란 어떤 정보를 저장하기 위한 템플릿으로 생각할 수도 있다. 
#
# 정보는 객체의 속성에 저장된다. 그런데 클래스는 객체에 어떤 속성이 있는지를 알려준다.

# %% [markdown]
# 하지만 속성이 항상 클래스 정의에 포함되어야 하는 것은 아니다. 원한다면 객체에 새로운 속성을 만들어 줄 수 있다.

# %%
w.name2 = 'sinsa imdang'


# %%
def upname2(self):
    return (self.name2.upper())


# %%
Patient.upname2 = upname2


# %%
w.upname2()

# %% [markdown]
# 여기서 `w.name2 = upname2`로 하지 않도록 유의해야 한다. `w.name2 = upname2`로 하면 `w.name2`가 함수가 된다. `w.name2`가 메소드가 되게 하려면 함수는 클래스에서 정의하고 접근은 객체를 통해 해야 한다.
#
#

# %%
w.upname2 = upname2

# %%
w.upname2()

# %%
w.upname2(w)

# %% [markdown]
# **메소드**란 클래스에서 정의된 함수를 객체를 통해 접근하여 첫 번째 인자가 객체가 되는 것이라고 생각하자.

# %% [markdown]
# 그런데 객체마다 따로 속성이나 함수를 정해주기는 번거롭다. 공통적인 속성과 함수를 모아 템플릿처럼 만든 것을 클래스라고 할 수 있다.

# %% [markdown]
# 객체는 객체만의 특별한 정보를 담고 있으므로 객체를 만들 때에도 이런 정보를 지정해줄 수 있다. 위에서 `__init__()`은 이런 역할을 하는 함수이다.

# %% [markdown]
# 다시 말해 `w=Patient(name='han seokbong')`을 실행하면 `Patient` 클래스에서 정의된 함수 `__init__(self, name)`이 실행되고 첫 번째 인자는 만들어진 객체, 두 번째 인자는 `Patient()`의 첫 번째 인자가 된다. 그리고 `__init__()`는 항상 `self`를 반환하게 된다. 따라서 `w`에 새로 생성된 객체가 저장되는 것이다.

# %%

# %%

# %%

# %%

# %%
dir('Han seok-bong')

# %%
'han seok-bong'.capitalize()

# %%
import numpy as np

# %%

# %%
x = np.array([2022], dtype=np.int16)
x

# %%
print(f'{0x4142:016b}')

# %%
print(f'{x[0]:016x}')

# %%
chr(0x41), chr(0x42)

# %%
0x4142


# %%
`

# %% [markdown]
# > Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the `id()` function returns an integer representing its identity.

# %%
x=3


# %%

# %% [markdown]
# 클래스는 새로운 타입을 만들 수 있다. 초기에 설명했듯이 타입이란 메모리의 이진수를 해석하는 방식이라고 생각할 수 있다. 

# %%

# %% [markdown]
# Namespace에 관한 내용. 
#
# https://docs.python.org/3.8/library/functions.html#built-in-funcs
#
# 모든 내장 함수에 대한 설명. 분류하기. 예제. 아니면 github에서 자주 사용되는 예 확인
#

# %% [markdown]
# ### 용어
#
# * 클래스 객체 vs. 어떤 클래스의 객체
# * 클래스의 인스턴스
# *
#
# * 클래스 객체
#   - 속성 참조(reference attributes?)
#   - 인스턴스 생성?(instantiation?)
#   
# * 클래스의 여러 속성
#   - 클래스 내부에서 할당된
#   - 기본적으로 생성되는 `.__doc__`
#   - 
#   

# %%
class MyClass():
    pass
    
x = MyClass()

# %% [markdown]
# 클래스의 인스턴스를 생성하고, 이 객체를 변수 `x`에 할당한다.

# %%
빈 클래스? 특정한 상태(state) 또는 속성의 인스턴스를 생성하고 싶을 때

# %% [markdown]
# There are two kinds of valid attribute names: data attributes and methods

# %%
lst = [1,3,2]

# %%
type(lst)

# %% [markdown]
# 가장 쉬운 클래스 예제를 만들어 본다면?
#
# * 필요한 구성 요소
#     - `self.func1` 안에서 `self.func2`를 부른다
#     - class attribute와 instance attribute
#     - 
#
# "Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__"
#
# 그렇다면 `type(x)`와 `x.__class__`는 어떻게 다른가? 

# %%
x = 3

# %%
x.__class__

# %%
type(x)

# %%
# https://stackoverflow.com/questions/33137934/what-types-of-attributes-does-the-dir-function-give-in-python
x = 2; x.conjugate()
(2).conjugate()
2 .conjugate()  # note the whitespace
Since the python parser has special handlings of numeric literals, it doesn't allow this awkward syntax:

 2.conjugate()

# %%
# inheritance -> resolving attribute reference
# inheritance에서 method... base class의 method가 derivedclass의 method를 call하게 될 수도 있다.


# %%
# checking inheritance
isinstance(3, int)
issubclass(float, int)


# %% [markdown]
# ## Naming convention
#
# * with single underbar
# * 

# %% [markdown]
# ### Private variables
#
# 코드가 inheritance에서 깨질 수 있으므로 name mangling을 하면 낫다?

# %%

# %%

# %%

# %% [markdown]
# 파이썬에서 함수는 입력되는 데이터 타입을 가리지 않는다. 이는 약간 의도적인데, 여러 데이터 타입에 적용되는 함수를 만들 수 있기 때문이다. 다음을 보자.

# %%
def add(x,y):
    return(x+y)


# %% [markdown]
# 위에서 정의한 함수 `add`는 두 숫자 입력에 대해 두 수를 합친다.

# %%
add(3,5)

# %% [markdown]
# 그런데 문자열도 입력이 가능하다.

# %%
add('a', 'b')

# %% [markdown]
# 리스트도 입력이 가능하다.

# %%
add([3,2,'five'], ['b', 5])

# %% [markdown]
# 왜냐하면 `+`가 입력되는 변수의 타입에 따라 다르게 작동하기 때문이다. 하지만 다음을 보자.

# %%
add([3,2,5], 5)

# %% [markdown]
# 위에서 리스트 `[3,2,5]`에 마지막 원소로 `5`를 추가하기 위해서 `add([3,2,5], 5)`를 시도해보았다. TypeError가 발생하였지만 어떻게 수정해야할지 감이 오지 않는다. 만약 특정한 변수 타입을 가정하고 함수를 정의할 수 있다면 여러 타입의 입력을 모두 한꺼번에 처리하기 위해 고민할 필요가 없다. 특정한 타입을 전제하고 만들어진 함수를 **메소드**라고 한다. 

# %% [markdown]
# 사실 앞에서 **타입**이라고 했지만 리스트는 보통 **클래스**라고 불린다. 파이썬에서 거의 모든 것이 **객체**라고 한다. **객체**란 인스턴스(instance)라고도 하는데, 객체는 클래스의 구체적인 실현이다. 예를 들어 사람이 클래스라면, 특정인 홍길동은 인스턴스라고 생각할 수 있다.

# %% [markdown]
# 리스트에는 이미 `.append()`라는 메소드가 있어서 우리가 앞에서 하고자 했던 기능을 한다.

# %%
lst = [3,2,5]
lst.append(5)
lst

# %% [markdown]
# 여기서 `append(lst, 5)`는 불가능함을 유의하자.

# %%
append(lst, 5)


# %%

# %%

# %%
class Student():
    def __init__(self, name, scoreA, scoreB):
        self.name = name
        self.scores = [scoreA, scoreB]
        
    
    def mean_score(self):
        return (self.scores[0] + self.scores[1])/2

# %%
a = Student('Kim', 90,80)
b = Student('Park', 85,75)

# %%
a.scores  # Attribute

# %%
a.mean_score() # Method


# %%
## Monkey-patching Class method

def f(self, identity):
    #print("제 이름은 "+self.name + "입니다.\n 저는 "+x+" 입니다.")
    print(f"제 이름은 {self.name}입니다.\n저는 {identity} 입니다.")


# %%
Student.intro = f

# %%
a.intro('2학년')


# %%
class Free():
    pass


# %%

# %%
b = Free()

# %%
b.name = '철수'

# %%
Free.intro = f

# %%
b.intro('전학생')


# %%

# %%

# %%

# %%

# %%
## testing

# %%
class Foo:
    def __init__(self):
        self.__bar = 42
        self.xxx = 32
    def method0(self):
        return self.__bar * 2
    def method1(self):
        return eval('self.__bar * 2')

f = Foo()
f.method0()

# %%
getattr(f, '__bar')

# %%
getattr(f, 'xxx')

# %%
f.__dict__
# double underbar의 의미!
# 

# %%
