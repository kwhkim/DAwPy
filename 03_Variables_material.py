
# %% [markdown]
# # === END OF DOCUMENT

# %% [markdown] tags=[]
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

# %%

# %% [markdown]
#

# %% [markdown]
# # ===== EDITING

# %%

# %% [markdown]
# ### TO-DOs
# * 타입 어노테이션?
# * global(), vars(), locals(), dir() 차이?
# * https://docs.python.org/3.8/tutorial/classes.html#class-objects

# %%
globals() is locals() # context 안이 아니라서
# globals()
# Return the dictionary containing the **current scope's global variables**.   
#    NOTE: Updates to this dictionary *will* affect name lookups in the current
#    global scope and vice-versa.

# locals()
#    Return a dictionary containing the current scope's local variables.    
#    NOTE: Whether or not updates to this dictionary will affect name lookups in
#    the local scope and vice-versa is *implementation dependent* and not
#    covered by any backwards compatibility guarantees.


# %%
## Local namespace, Global namespace
## 
## REPL's global namespace
## 
## Python code has always these namespaces!!!
## eval("   ", locals=, globals=) # DOESNOT WORK

# %%

# %%
def f():
    print(globals() is locals())
    
f()

# %%
help("locals")

# %%
eval("pow(2,4)", {}) # works fine because pow is builtins 
eval("pow(2,4)", {"__builtins__":{}}) # error!!!
eval("x+50", {}, {"x":x}) # locals() defined

# %% [markdown]
# # =====

# %% [markdown]
#

# %% [markdown]
# 파이썬의 변수는 동적 타입이다: 변수의 타입이 코드가 실행되는 도중에 바뀔 수 있다.
#
# 파이썬은 **객체** 지향(Object-Oriented) 언어이다. 숫자, 문자, 분석 결과 등은 모두 파이썬의 객체(Object)에 담을 수 있다. 
# 사실 우리가 파이썬에서 다루는 거의 모든 것은 객체이다. 숫자 `3` 역시 객체이다.
#
# 다음의 코드를 보자. `type(3)`은 `int`이고, `int`에 대한 설명을 보면 `class int in module builtins`라고 나온다.
# 숫자 `3`은 모듈 `builtins`에서 정의한 클래스 `int`의 인스턴스이다.[^intclass]
#
# [^intclass]: 내장 모듈이 있고 이름이 `builtins`라는 모듈이 따로 있다. 내장 모듈은 Python과 결합되어 따로 파일로 존재하지 않는 모듈을 의미하고 `builtins`라는 모듈은 그 중에서 파이썬을 실행할 때 자동으로 `import` 되는 모듈이다. 파이썬을 실행한 후 아무것도 하지 않고 `imported()`를 해보자. 그리고 `import sys`후 `sys.builtin_module_names`를 해보자.

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
# 보통 클래스는 대문자로 시작하는데 너무 자주 쓰이기 때문에 (또는 너무 기본적이기 때문에) 소문자로 쓰는 듯하다.
#
# 그런데 수 `3`과 같은 **불변(immutable) 객체**은 그냥 어떤 값으로 생각하고, 변수에 그 값이 저장된다고 생각해도 큰 문제가 없기 때문에 이 장에서는 변수가 어떤 값을 저장한다고 설명하겠다(불변 객체가 뭐냐고? 아직 모른다면 추후 설명되니 잠시 그런게 있다는 정도만 알아두자. 간단하게 여러 값과 함수가 모인 덩어리로 생각하자).
#
# 여기서는 수, 문자, 범주, 논리, 날짜 값에 대해서만 생각하겠다. 이들은 모두 변수에 담을 수 있다. 그리고 연산을 하거나, 수정/삭제할 수 있다.

# %%

# %% [markdown]
# 변수는 그 내용이 변할 수 있기 때문에 변수이다. 파이썬에서 변수란 어떤 객체를 가리키는 지시자이다. 예를 들어 변수 `x=3`으로 변수 `x`에 `3`을 담았다고 말할 수 있겠지만, 좀더 엄밀하게 얘기하면 변수 `x`는 객체 `3`을 가리킨다. 하지만 `x=3`의 경우에는 변수 `x`에 `3`이 담겨 있다고 말해도 개념적으로 크게 다르지 않다. 이에 대한 자세한 내용은 **불변객체**와 **가변객체**에 대한 설명이 필요하다. 
#
# 일단 객체는 메모리 상의 한 주소에 저장된다. 문제는 (메모리 상의 어떤 위치에 저장되어 있는) 객체가 변할 수 있느냐이다. `x=3`을 하면 변수 `x`에 `3`을 넣는 것처럼 보이지만(이를 구현하는 컴퓨터의 자세한 메커니즘은 메모리의 특정한 장소를 `x`라고 부르고, 그 곳에 `3`을 넣는 것이다), 사실은 객체 `3`을 만들어 메모리에 저장한 후, 변수 `x`가 `3`을 가리키도록 한다. 그리고 이 `3`은 불변 객체이기 때문에 절대로 변하지 않는다. 만약 `x=4` 또는 `x=x+1`을 하면 메모리에 객체 `4`를 만들고, 변수 `x`가 `4`를 가리키도록 한다. 음... 뭐가 차이냐고? 리스트를 설명할 때 다시 불변 객체와 가변 객체에 대한 얘기를 해보겠다. 
#

# %%

# %% [markdown]
# 다음의 코드를 보자. 
# e3는 리스트 `[1,2,3,4]`를 가리키고, `e1=e2=e3`를 통해 `e1`, `e2`는 `e3`와 동일한 객체를 가리키는 별칭이다.
# `e1[0]=-1`로 리스트의 첫 번째 원소를 바꾸지만, 동일한 객체를 가리키는 `e2`, `e3`의 첫 번째 원소도 바뀐다. 

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

# %%

# %% [markdown]
# 파이썬의 변수는 동적 타입이다: 변수의 타입이 코드가 실행되는 도중에 바뀔 수 있다.
#
# 파이썬은 **객체** 지향(Object-Oriented) 언어이다. 숫자, 문자, 분석 결과 등은 모두 파이썬의 객체(Object)에 담을 수 있다. 
# 사실 우리가 파이썬에서 다루는 거의 모든 것은 객체이다. 숫자 `3` 역시 객체이다.
#
# 다음의 코드를 보자. `type(3)`은 `int`이고, `int`에 대한 설명을 보면 `class int in module builtins`라고 나온다.
# 숫자 `3`은 모듈 `builtins`에서 정의한 클래스 `int`의 인스턴스이다.[^intclass]
#
# [^intclass]: 내장 모듈이 있고 이름이 `builtins`라는 모듈이 따로 있다. 내장 모듈은 Python과 결합되어 따로 파일로 존재하지 않는 모듈을 의미하고 `builtins`라는 모듈은 그 중에서 파이썬을 실행할 때 자동으로 `import` 되는 모듈이다. 파이썬을 실행한 후 아무것도 하지 않고 `imported()`를 해보자. 그리고 `import sys`후 `sys.builtin_module_names`를 해보자.

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
# 보통 클래스는 대문자로 시작하는데 너무 자주 쓰이기 때문에 (또는 너무 기본적이기 때문에) 소문자로 쓰는 듯하다.
#
# 그런데 수 `3`과 같은 **불변(immutable) 객체**은 그냥 어떤 값으로 생각하고, 변수에 그 값이 저장된다고 생각해도 큰 문제가 없기 때문에 이 장에서는 변수가 어떤 값을 저장한다고 설명하겠다(불변 객체가 뭐냐고? 아직 모른다면 추후 설명되니 잠시 그런게 있다는 정도만 알아두자. 간단하게 여러 값과 함수가 모인 덩어리로 생각하자).
#
# 여기서는 수, 문자, 범주, 논리, 날짜 값에 대해서만 생각하겠다. 이들은 모두 변수에 담을 수 있다. 그리고 연산을 하거나, 수정/삭제할 수 있다.

# %%


파이썬에서는 변수 이름에 알파벳, 숫자, _을 활용할 수 있다. 
R과 달리 .(점)은 사용할 수 없다.
Python에서 .(점)은 클래스(Class)의 속성(attribute)을 가리키거나 module의 변수, 함수를 지칭하기
위해 사용된다(클래스, 속성은 후에 설명된다).
변수 이름의 첫 글자는 숫자가 될 수 없다.

간명한 변수 이름을 짓는 것은 언제나 쉽지 않다.
파이썬에는 PEP(Python Enhancement Proposal)이라는 것이 있다.
PEP에는 파이썬에 추가되면 좋을 기능, 파이썬를 사용하여 코드를 작성할 때 활용할 수 있는 표준 등이 제안된다.
PEP에는 모듈 이름, 패키지 이름, 클래스 이름, 메쏘드 이름, 예외 이름, 함수 이름, 전역 상수 이름
전역 변수이름, 지역변수 이름, 인스턴스 이름, 인스턴스 변수 이름, 함수 매개변수 이름에 대한
표준 방식이 제안되기도 한다(예. PEP8의 Naming Convention). 

미국의 메가 인터넷 회사인 구글은 독자적인 스타일 가이드(Google Python Style Guide)가 존재한다. 구체적으로 다음과 같다.

```
module_name, package_name, ClassName, method_name, ExceptionName,
function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name,
function_parameter_name, local_var_name, CLASS_CONSTANT_NAME
```
복잡해 보이지만 크게 3종류가 있다. 

1. 단어는 소문자로 시작하고 단어 사이는 밑줄로 연결하는 snake naming. 
2. 단어의 첫 글자는 대문자로 시작하고 단어 사이는 그대로 붙여쓰는 Camel case.
3. 모든 글자를 대문자로 쓰고 단어 사이는 밑줄로 연결하는 방법.

3번은 상수에 쓰이고, 2번은 클래스 또는 예외 이름에 쓰인다. 그리고 1번은 그 밖의 거의 모든 객체(변수, 함수, 함수 매개변수, 모듈 등)에 쓰인다. 

여기에 덧붙여 내부용 변수는 `_`로 시작한다.

# %%
이때 만약 **mutable**인 대상을 할당할 경우에는
모든 변수가 모두 같은 내용을 항상 공유하므로 유의할 필요가 있다.
(**mutable**(가변 객체)에 대해서는 후에 설명된다.)

# %% [markdown]
# 파이썬의 변수는 동적 타입이다: 변수의 타입이 코드가 실행되는 도중에 바뀔 수 있다.
#
# 파이썬은 **객체** 지향(Object-Oriented) 언어이다. 숫자, 문자, 분석 결과 등은 모두 파이썬의 객체(Object)에 담을 수 있다. 
# 사실 우리가 파이썬에서 다루는 거의 모든 것은 객체이다. 숫자 `3` 역시 객체이다.
#
# 다음의 코드를 보자. `type(3)`은 `int`이고, `int`에 대한 설명을 보면 `class int in module builtins`라고 나온다.
# 숫자 `3`은 모듈 `builtins`에서 정의한 클래스 `int`의 인스턴스이다.[^intclass]
#
# [^intclass]: 내장 모듈이 있고 이름이 `builtins`라는 모듈이 따로 있다. 내장 모듈은 Python과 결합되어 따로 파일로 존재하지 않는 모듈을 의미하고 `builtins`라는 모듈은 그 중에서 파이썬을 실행할 때 자동으로 `import` 되는 모듈이다. 파이썬을 실행한 후 아무것도 하지 않고 `imported()`를 해보자. 그리고 `import sys`후 `sys.builtin_module_names`를 해보자.

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
# 보통 클래스는 대문자로 시작하는데 너무 자주 쓰이기 때문에 (또는 너무 기본적이기 때문에) 소문자로 쓰는 듯하다.
#
# 그런데 수 `3`과 같은 **불변(immutable) 객체**은 그냥 어떤 값으로 생각하고, 변수에 그 값이 저장된다고 생각해도 큰 문제가 없기 때문에 이 장에서는 변수가 어떤 값을 저장한다고 설명하겠다(불변 객체가 뭐냐고? 아직 모른다면 추후 설명되니 잠시 그런게 있다는 정도만 알아두자. 간단하게 여러 값과 함수가 모인 덩어리로 생각하자).
#
# 여기서는 수, 문자, 범주, 논리, 날짜 값에 대해서만 생각하겠다. 이들은 모두 변수에 담을 수 있다. 그리고 연산을 하거나, 수정/삭제할 수 있다.

# %%

# %% [markdown]
# 파이썬의 변수는 동적 타입이다: 변수의 타입이 코드가 실행되는 도중에 바뀔 수 있다.
#
# 파이썬은 **객체** 지향(Object-Oriented) 언어이다. 숫자, 문자, 분석 결과 등은 모두 파이썬의 객체(Object)에 담을 수 있다. 
# 사실 우리가 파이썬에서 다루는 거의 모든 것은 객체이다. 숫자 `3` 역시 객체이다.
#
# 다음의 코드를 보자. `type(3)`은 `int`이고, `int`에 대한 설명을 보면 `class int in module builtins`라고 나온다.
# 숫자 `3`은 모듈 `builtins`에서 정의한 클래스 `int`의 인스턴스이다.[^intclass]
#
# [^intclass]: 내장 모듈이 있고 이름이 `builtins`라는 모듈이 따로 있다. 내장 모듈은 Python과 결합되어 따로 파일로 존재하지 않는 모듈을 의미하고 `builtins`라는 모듈은 그 중에서 파이썬을 실행할 때 자동으로 `import` 되는 모듈이다. 파이썬을 실행한 후 아무것도 하지 않고 `imported()`를 해보자. 그리고 `import sys`후 `sys.builtin_module_names`를 해보자.

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
# 보통 클래스는 대문자로 시작하는데 너무 자주 쓰이기 때문에 (또는 너무 기본적이기 때문에) 소문자로 쓰는 듯하다.
#
# 그런데 수 `3`과 같은 **불변(immutable) 객체**은 그냥 어떤 값으로 생각하고, 변수에 그 값이 저장된다고 생각해도 큰 문제가 없기 때문에 이 장에서는 변수가 어떤 값을 저장한다고 설명하겠다(불변 객체가 뭐냐고? 아직 모른다면 추후 설명되니 잠시 그런게 있다는 정도만 알아두자. 간단하게 여러 값과 함수가 모인 덩어리로 생각하자).
#
# 여기서는 수, 문자, 범주, 논리, 날짜 값에 대해서만 생각하겠다. 이들은 모두 변수에 담을 수 있다. 그리고 연산을 하거나, 수정/삭제할 수 있다.

# %%
# str(a); str(b); str(c)
# ls.str()
def types_list(var):
    res = []
    for i,x in enumerate(var):
        #print(x)
        if isinstance(x, list) or isinstance(x, tuple):        
            res.append(types_list(x))
        else:
            res.append((type(x), x))
            # or res.append(type(x))
    return res
x = ['a', 3, ['b', 4, ['c', 5], [3,2]]]
types_list(x)

# %%

# %%
# rm(list=ls())
for x in set(dir()) - set(dir(__builtins__)):
    if not x.startswith('_') and x not in ['In', 'Out', 'quit', 'exit']:  # jupyter notebook
        print('VARIABLE NAME = '+x)
        print(eval(x))
        print('-'*60)
        
# rm(list=ls())
# https://stackoverflow.com/questions/51982189/equivalent-of-rs-ls-function-in-python-to-remove-all-created-objects
for x in set(dir()) - set(dir(__builtins__)):
    if not x.startswith('_') and x not in ['In', 'Out', 'quit', 'exit']:
        print('deleting '+x)
        exec('del '+x)
del x

# %%
globals().keys()


# %%

# %%
# https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
def isnotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter


# %%
isnotebook()

# %%

# %%
isinstance(3, (int, float, complex, bool, str))

# %%
a = 3; b = False;
var_float = 4.5; var_complex = 3+4j
s = "This is string"


# %%
def globals_user_type(dict_ = False, type_=(int, float, complex, bool, str)):    
    varnames = globals().keys()
    varnames2 = [varname for varname in varnames if not varname.startswith('_') and isinstance(globals()[varname], type_)]     
    if dict_:
        return {k:globals()[k] for k in varnames2}
    else:
        return varnames2
globals_user_type()

# %%
import pickle
with open('_Data.pkl', 'wb') as f:
    pickle.dump(globals_user_type(dict_=True), f)

# %%
import pickle
with open('_Data.pkl', 'rb') as f:
    variables = pickle.load(f)
    for variable in variables:
        globals()[variable] = variables[variable]


# %%
def globals_user_type(dict_ = False, type_=(int, float, complex, bool, str)):    
    varnames = globals().keys()
    varnames2 = [varname for varname in varnames if not varname.startswith('_') and isinstance(globals()[varname], type_)]     
    if dict_:
        return {k:globals()[k] for k in varnames2}
    else:
        return varnames2
globals_user_type()

# %%
help("dill.dumps")

# %%

# %%
dill.dumps(globals_user(dict_=True), "_data.pkl")

# %%
import dill
with open('_data.pkl', 'wb') as file:
    dill.dumps(globals_user(dict_=True), file)

# %%
import dill

# %%
help(dill)


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

# %%
x = 3

# %%
del(x)


# %%
# #%conda install dill

# %%
def expand_grid(x):
    print(x)
    


# %%
help("dill.dumps")

# %%
globals_user(dict_=True).keys()

# %%
import datetime
x = datetime.datetime.strptime("2021-01-04", "%Y-%m-%d")
type(x)

# %%
import numpy as np
np.array(["2021-01-04", "2022-04-01"], dtype="datetime64")

# %%
isinstance(x, datetime.datetime)

# %%
import pandas as pd
x = pd.Categorical(["Right", "Middle", "Left", "Left", "Middle"])
isinstance(x, pd.Categorical)

# %%

# %%
# int, bool, float
# str
# pd.Categorical
# datetime.datetime, datetime.date, datetime.time

# %%
dir()

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

# %%
a = datetime.datetime.strptime('2022-03-01', "%Y-%m-%d") # 년(4자리)-달(2자리)-일(2자리)
b = datetime.datetime.strptime('22:10:14', "%H:%M:%S")   # 시(2자리):분(2자리):초(2자리)
c = datetime.datetime.strptime('2022-04-01 22:30:00', "%Y-%m-%d %H:%M:%S") 
# 년(4자리)-달(2자리)-일(2자리) 시(2자리):분(2자리):초(2자리)

# %% [markdown]
# 파이썬에서 문자열을 **텍스트 시퀀스**라고 부르는 이유는 문자열을 각 원소가 문자인 배열처럼 취급하기 때문입니다. 

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

# %%

# %%

# %%

# %%
math.isclose(0,1e-300, rel_tol=1e-16)

# %%
math.isclose(1e-23, 1e-24, rel_tol=1e-16)

# %%
math.isclose(1e-23, 1e-24) # rel_tol = 1e-09
# R> all.equal(1e-23, 1e-24)
# R> dplyr::near(1e-23, 1e-24)
# R> near <- dplyr::near; near(1e-23, 1e-24)

# %%

# %%
x1 =  np.array([1,1]); y1 = np.array([1,2])
x2 = np.array([1.4, 1.4]); y2 = np.array([1.4, 2.3])
x3 = np.array([1+3j, 1+3j]); y3 = np.array([1+3j, 2+3j])
x4 = np.array([True, False]); y4 = np.array([True, True])
x5 = np.array(['equals', 'equals']); y5=np.array(['equals', 'equal'])
print(eq(x1,y1))
print(eq(x2, y2))
print(eq(x3, y3))
print(eq(x4, y4))
eq(x5,y5)

# %%
x1 =  np.array([1,1]*2); y1 = np.array([1,2, np.nan, None])
x2 = np.array([1.4, 1.4]*2); y2 = np.array([1.4, 2.3, np.nan, None])
x3 = np.array([1+3j, 1+3j]*2); y3 = np.array([1+3j, 2+3j, np.nan, None])
x4 = np.array([True, False]*2); y4 = np.array([True, True, np.nan, None])
x5 = np.array(['equals', 'equals']*2); y5=np.array(['equals', 'equal', np.nan, None])
print(eq(x1,y1))
print(eq(x2, y2))
print(eq(x3, y3))
print(eq(x4, y4))
eq(x5,y5)


# %%
def eq(a,b):
    vnan = np.isnan(a) | np.isnan(b) # numpy일 수 있으니 bool이 아닐 수 있다..
    res = a == b
    print(vnan, res)
    print(type(vnan), type(res))
    if isinstance(vnan, np.ndarray):
        print('a')
        res[vnan] = np.nan
        return res
    elif isinstance(vnan, np.bool_):
        print('b')
        if vnan:
            print('c')
            return np.nan
        else:
            return res


# %%
import numpy as np

# %%
import pandas as pd

# %%
dir(pd)

# %%
np.isna(3)

# %%
np.isnan(3)

# %%
np.isnan(np.nan)

# %%
eq("3", "3")

# %%
np.isnan(32)

# %%

# %%
np.isnan("a")

# %%
np.isnan(np.array(['a', np.nan, 'c'], dtype='U10'))

# %%
np.isnan(np.array(['a', np.nan, 'b'], dtype='U10'))

# %%
eq(3, np.nan)

# %%
for dtype in ['object', 'int']:
    print("dtype =", dtype)
    # %timeit np.arange(1E6, dtype=dtype).sum()
    print()


# %%

# %%
## np.nan, None을 구분없이 분석하려면
## pd.Series... pd.Series면 충분한가?

# %%

# %% [markdown] tags=[] jp-MarkdownHeadingCollapsed=true
# ## 3.4 특별한 값

# %% [markdown] tags=[] jp-MarkdownHeadingCollapsed=true
#

# %% [markdown] tags=[]
# ## 3.4.2 몇가지 유의사항

# %%
# x <- c(2, 5, NA, 3)
# vec <- c(3, 7, 0, NA, -3)

import pandas as pd
x = pd.Series([2,5,np.nan,3]) # np.nan은 실수형이다.
print(x)
vec = pd.Series([3, 7, 0, np.nan, -3])
print(vec)

# %%
import numpy as np

def ifelse(cond, x, y):
    return np.where(cond, x, y)
print(ifelse(x > 3, "3+", "below")) 
# 주의! np.nan이 제대로 반영되지 않았다
# 왜냐하면 np.nan > 3의 결과는 False이기 때문이다.


# %%
print(np.nan < 3, np.nan <= 3, np.nan == 3, np.nan <= 3, np.nan < 3) # np.nan을 포함한 모든 대소비교가 False!

# %%
# ifelse(is.na(x), NA, x %in% vec)
ifelse(np.isnan(x), -99, x.isin(vec))  
# 왜냐하면 return 값이 array이고,
# -99가 포함되므로, True/False는 int로 변환

# %%
ifelse(np.isnan(x), np.nan, x.isin(vec))
# np.nan은 dtype = 'bool' or 'int*'에서는 지원하지 않는다  
ifelse(np.isnan(x), 'NA', x.isin(vec))

# %%
xs = [2,5,np.nan,3]
[np.nan if np.isnan(x) else x in vec for x in xs]

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

# %%

# %% [markdown]
# ## assign

# %%

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

# %% [markdown] tags=[]
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
