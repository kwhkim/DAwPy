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
# ## 클래스
#
# * 참고 자료 
#   - https://docs.python.org/3.8/tutorial/classes.html
#   - https://docs.python.org/3.8/reference/datamodel.html

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
