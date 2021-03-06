# -*- coding: utf-8 -*-
# %% [markdown]
# ## TO-Dos
#
# * !!! TO-DO : 변수 scope에 대한 얘기 추가 필요
#     - !!! global, local이 필요한 예시가 필요할 듯 
# 비교. local assignment
#      nonlocal assignment
#      global assignment
# * !!! TO-DO : doc-string에 대한 내용 추가 필요
# * !!! TO-DO : decorators
# * !!! TO-DO : Datacamp python function
# * !!! TO-DO : Datacamp unit testing

# %% [markdown]
# ## 들어가기

# %% [markdown]
# #### R의 함수
#
# R에서 함수 호출할 때, 인자는 매개변수 이름을 지정해 줄 수도 있다.
# R에서는 매개변수에 인자가 배정되는 방식은 다음과 같다.
# 먼저 **매개변수를 지정한 인수**를 배정한다.
# 그리고 매개변수가 지정되는 않은 인수는 순서대로 함수의 남아 있는 매개 변수에 배정한다.
#

# %% [raw] language="R"
# f = function(a,b,c,d) {
#   print(a,b,c,d)}

# %% [markdown]
# 예를 들어 위의 함수 `f`를 호출할 때
# `f(3,4,a=1,b=2)`, `f(a=1,b=2,3,4)`, `f(3,b=2,a=1,4)`
# 는 모두 `f(a=1,b=2,c=3,d=4)`와 동일하다.
# 왜냐하면 먼저 매개변수를 지정한 인수가 모두 같고(a=1,b=2),
# 매개변수를 지정하지 않은 인수의 경우,
# 3,4의 순서가 모두 일치하기 때문이다. 
#
# 이런 매개변수 배정 방식은 기본값의 유무는 관계가 없다.

# %% [markdown]
# 다음의 함수 `f`는 기본값 설정이 다르지만, 위에서 사용한 호출에 의해 인수에 배정되는 매개변수는 모두 동일하다.

# %% [raw] language="R"
# f = function(a=1,b,c,d)
# f = function(a,b=2,c=3,d)
# f = function(a, b, c, d=4)

# %% [markdown]
# ### R 사용자의 입장에서 Python의 매개변수 배정 방식은 이해하기 어렵다.

# %% [markdown]
# 예를 들어 다음을 보자

# %%
def f(a,b):
    print(a,b)

# %%
f(1,2)
f(2,a=1)

# %% [markdown]
# `f(2,a=1)`는 `TypeError: f() got multiple values for argument 'a'`를 발생시킨다. 
# R 사용자는 두 개의 매개변수 `a`,`b`에서
# `a=1`로 정해줬으므로, 나머지 매개변수 `b`에 `2`가 배정되는 것이 당연하다고 생각하겠지만,
# 오류가 발생하는 것이다.

# %% [markdown]
# ## 파이썬의 인수 배정 방식을 이해해보자.

# %% [markdown]
# 여기서는 파이썬의 매개변수 배정 방식을 이해하려고 노력해보자. 역지사지가 필요하다.
#
# 먼저 R에서의 인수 배정 방식을 이해하려고 해보자.
# R에서 함수 호출시 모든 인자는 매개변수 이름을 정해 줄 수 있다.
# 하지만 순서가 명확하다면 생략해 줄 수도 있다.

# %% [markdown]
# 무슨 말이냐면 함수 정의에서 함수을 실행할 때 반드시 필요한 매개변수는
# 함수의 앞쪽에 위치하게 된다. 
#
# 그리고 그 매개변수의 역할은 함수을 호출하는 사람이라면,
# 정확하게 알고 있는 경우가 대부분이다. 따라서 매개변수이름쯤은 생략해도 괜찮다고 생각할 수 있다.
# 왜냐하면 그 순서가 명확하고, 그 의미도 명확하니까.
#
# 이런 의미에서 R의 함수는 모든 인자에 매개변수를 지정해 줄 수 있지만,
# 그 중 순서에 따른 역할이 분명한 인자는 생략할 수 있게 했다.

# %% [markdown]
# 하지만 파이썬에서 함수 호출시에는 매개변수 이름이 없는 것이 기본인 듯하다.
# (그리고 R과 다르게 매개변수 이름이 **반드시** 없어야 하는 함수들이 있다.)
#
# 필자의 개인적 경험에 의하면 예전의 컴퓨터 언어들은 함수를 호출할 때 매개변수명을 붙이지 않았다.
# 예를 들면, `print("Hi!")`라고 했지, `print(x="Hi!")`라고 쓰지 않았고,
# `sub(4,1)`이지, `sub(x=4, y=1)`라고 쓰지 않았다.
# 왜냐하면 함수의 기능에 의해 인자의 의미가 분명하고, 또 순서에 의한 의미가 분명하기 때문이라고 추측할 수 있다.
#
# 그리고 인자를 단 하나 받는 함수의 경우에는 매개변수 이름을 명시하는 것이 별 의미가 없기도 하다.
# 예를 들어 파이썬의 `list()`란 함수는 인자를 단 하나 받을 수 있다. 
#
# `help(list)`를 해보면, `list()` 함수의 인자를 확인할 수 있다. 

# %% [markdown]
# `list(iterable=(), /)`
#

# %% [markdown]
# 함수 정의에서 `/` 앞에 나오는 매개변수는 반드시 매개변수이름이 없어야 한다. 따라서 `list([])`은 맞지만, `list(iterable=[])`은 틀리다.

# %% [markdown]
# 파이썬에서 함수는 아마도 이런 전통을 이어받아,
# 기본적으로 매개 변수 이름 없이 호출하며,
# 선택적인 매개변수인 경우는 이름없이 호출할 수 없기 때문에,
# 매개변수이름을 지정한다는 느낌이 강한 듯 하다. 다음의 함수를 보자.

# %%
def f(a,b,c,d=1,e=2,f=3):
    print(a,b,c,d,e,f)

# %% [markdown]
# 위의 함수 `f`에서 처음 3개의 매개변수는 기본값이 없기 때문에,
# 함수를 호출할 때 반드시 지정해 줘야 한다.
# 하지만 `d`,`e`,`f`는 함수 호출 시 지정해 줄 수도 있고, 생략할 수도 있는 **선택적인 매개변수**이다.
# 이때 `d`는 그대로 두고 `e=5`를 하고 싶다면, 매개변수 명을 지정해주지 않고는 불가능하다.
# 왜냐하면 `d`는 그대로 두고 `e=5`로 바꾸고 싶을 때 `f(1,2,3,5)`를 한다고 가정해보자.
# 컴퓨터가 `d=5`를 하라는 것인지, `f=5`를 하라는 것인지 구분할 수 없기 때문이다.
# (이런 경우 컴퓨터는 순서대로 `d=5`를 하게 된다.)
# 따라서 파이썬의 키워드 인수(이름있는 인수 eg. 위에서 d,e,f)는 기본값이 설정되어 있기 때문에
# 선택 가능한 인자 중에서 하나를 설정한다는 느낌이 강한 듯 하다.

# %% [markdown]
# ### 파이썬의 함수 호출 규칙 : 순서 인자 우선, 이름 인자 나중

# %% [markdown]
# 우선 파이썬의 규칙을 알아두자.
# 함수 호출 시 이름있는 인자는 이름없는 인자 뒤에 와야 한다.
# 만약 이름있는 인자가 이름없는 인자 앞에 있다면, 다음의 오류가 발생한다.
# `SyntaxError: positional argument follows keyword argument`

# %% [markdown]
# 파이썬은 이름없는 인자를 우선시 한다.
# 앞에서 설명한 것처럼,
# 파이썬의 이름있는 인자는 선택적인 인자라는 개념이 강하기 때문인 듯하다.
# 이런 의미에서 위의 오류도 이해할 수 있다. 
# 함수를 호출할 때, 반드시 필요한 인자를 우선 입력하고, 그 다음에 선택적인 인자를 입력하라는 얘기이다.

# %%
def f(a,b):
    print(a,b)

# %%
f(2,a=1)

# %% [markdown]
# 위의 오류 역시 함수 호출에서 순서 인자(이름없는 인자)가 우선이라는 맥락에서 이해할 수 있다. 
# 순서에 따라 `a=2`를 했는데, 다시 `a=1`를 하라고?
# 근데 이름없는 인자(순서인자)와 이름있는 인자의 중요성(키워드 인자)을 비교하자면,
# 이름없는 인자가 더 중요하다고 생각하니,
# `a=2`를 버리고, `b=2`로 갈 수 없는 것이다.

# %% [markdown]
# ### 파이썬의 함수 정의 규칙

# %% [markdown]
# 이제 파이썬에서 함수를 정의하는 방법을 보자.

# %% [markdown]
# 함수를 정의할 때, 매개변수는 인자를 입력하는 방식에 따라
# 이름없는 인자만 받는 경우,
# 이름이 없을 수도 있고, 있을 수도 있는 경우,
# 그리고 반드시 이름이 있어야 하는 경우로 나눌 수 있다. 

# %%
def f(parg1, parg2, /, arg1, arg2, *, kwarg1, kwarg2):
    print(parg1, parg2, arg1, arg2, kwarg1, kwarg2)

# %% [markdown]
# 위의 `def f(...):`는 함수를 정의하는 방법을 보여준다.
# /, * 는 순서 인자, 선택인자, 키워드 인자를 구분하기 위해 사용한다.
# 여기서 parg1, parg2는 반드시 이름이 없어야 하며,
# arg1, arg2는 선택 가능하고,
# kwarg1, kwarg2는 반드시 이름이 있어야 한다. 
#
# 
#
# 일반적으로 함수 정의에서 `/` 앞의 인자는 순서 인자이다. 호출시에 반드시 이름이 없어야 한다.
# `/` 뒤 `*` 앞의 인자는 순서/이름 인자이다. 호출시에 이름이 있어도 되고, 없어도 된다.
# 하지만 앞의 파이썬 함수 호출 규칙을 기억하자. 이름이 없는 인자는 반드시 이름 있는 인자의 앞에 와야 한다.
# 마지막으로 `*` 뒤의 인자는 반드시 이름이 있어야 한다. 

# %%
f(1,2,3,4,kwarg1=5,kwarg2=6)
f(1,2,arg1=3,arg2=4,kwarg1=5,kwarg2=6)
f(1,2,kwarg2=6,kwarg1=5,arg2=4,arg1=3)


# %% [markdown]
# 위의 예에서 확인할 수 있듯이, 순서 인자는 순서를 지켜야 하고, 이름 인자는 순서가 바뀌어도 이름으로 매개변수에 배정된다.

# %% [markdown]
# #### 가변 순서 인자

# %%
def f(*args):
    for i in range(len(args)):
        print(args[i], end=',')


# %%
f(1,2,3,4,5)

# %%
f(1,2,3)


# %% [markdown]
# 위의 함수 `f()`의 정의(`def`)에서 `*args`는 가변 순서 인자를 받는다[^1]. `f(1,2,3,4,5)`는 순서 인자가 5개이고, `f(1,2,3)`는 순서 인자가 3개 뿐이지만, 괜찮다. 왜냐하면 `*args`가 **가변**(갯수가 변할 수 있는) 순서 인자이기 때문이다. 이렇게 함수 호출에서 순서 인자가 쓰였지만, 함수 정의에 대응되는 매개변수가 없는 경우, 해당 인자는 변수 `args`에 리스트의 형태로 들어가게 된다. 
#
# [^1]: 보통은 인자(argument)가 여럿 있다는 의미에서 `args`라고 많이 쓰지만, 반드시 그래야 하는 것은 아니다.

# %% [markdown]
# `*args`에 해당하는 인자는 **반드시** 이름이 없어야 한다.

# %% [markdown]
# #### 가변 이름 인자

# %%
def f(**kwargs):
    for k in kwargs:        
        print(k, "=", kwargs[k], end=',  ')
        # 뒤에서 배울 포맷팅을 사용하면 다음과 같이 쓸 수도 있다. 
        # print(f"{k}={kwargs[k]}", end=',  ') 
        


# %%
f(a=3, b=2, morning=4)

# %%
f(coffee='black', x=3, morning = '10am', z=99, w=32)


# %% [markdown]
# 위의 함수 정의에서 `**kwargs`는 가변의 이름 인자를 받는다[^2]. 함수 호출 시에 이름인자로 쓰였지만, 함수 정의에 대응하는 매개변수가 없는 경우, 이름을 키워드로 하는 딕셔너리의 형태로 `kwargs`에 저장된다. 
#
# [^2]: **k**ey**w**ord **arg**ument**s**란 의미로 kwargs로 많이 쓴다.

# %% [markdown]
# #### 보통 인자와 가변 인자

# %% [markdown]
# (이름이 있어도 되고, 없어도 되는)보통 인자가 가변 인자와 같이 쓰일 경우, 가변 인자를 활용하려면 보통 인자는 이름을 붙이지 않아야 한다.

# %%
def f(a,b,*args):
    print(a,b)
    for x in args:
        print(x, end=',')


# %%
f(1,2,3,4,5)

# %% [markdown]
# 예를 들어 함수 호출 시에 `b=2`를 쓰고 싶다고 해보자.

# %% [markdown]
# 파이썬의 함수 호출 규칙에 의해 다음은 SyntaxError를 발생시킨다.

# %%
f(1,b=2,3,4,5)

# %% [markdown]
# 그렇다면 `b=2`를 뒤에 쓸 수도 없다. 왜냐하면 이름이 붙지 않은 인자가 우선 `b`에 배정되기 때문이다. 

# %%
f(1,3,4,5,b=2)


# %% [markdown]
# 따라서 가변인자를 쓰기 위해서는 함수 정의에서 가변인자 이전에 나타나는 보통 인자는 모두 이름없이 함수를 호출해야 한다. 
# 비슷한 이유로 함수 정의에서 가변인자 이후에 나타나는 매개변수는 함수 호출 시 반드시 이름을 붙여야 한다.

# %% [markdown]
# ## 함수 인자 정리
#
# * 파이썬은 **함수를 호출**할 때, 순서 인자를 먼저 쓰고, 이름 인자를 나중에 써야 한다. 
# * **함수를 정의**할 때에도 순서 인자로 써야 하는 매개변수와 이름 인자로 써야 하는 매개변수를 분명히 구분하는 것이 좋다.
#     - `def f(parg1, parg2, /, arg1, arg2, *, kwarg1, kwarg2):`
# * 가변 인자가 존재할 때, 보통 인자(`arg1`, `arg2`)는 이름을 붙이지 않아야 한다. 
#  

# %% [markdown]
# # 파이썬 변수 스코프(Scope)

# %% [markdown]
# 변수의 스코프란 변수가 통용되는 범위를 의미한다. 예를 들어 다음과 같이 함수의 매개변수는 함수 밖에서 사용될 수 없다. 이렇게 변수가 창조된 지역에서 쓸 수 있는 변수를 지역(local) 변수라고 한다.

# %%
def f(a=1, b=1):
    print(a, b)

f(5,5)

# %%
a

# %% [markdown]
# 함수에서 최초로 할당된 변수는 함수 안에서만 사용할 수 있다. 함수 밖에서 정의된 변수를 사용하려면 먼저 `global `로 선언해야 한다. 보통 모든 지역에서 사용할 수 있는 변수를 전역(gloabl) 변수라고 하기 때문이다. 

# %%
a = 10


# %%
def f2():
    print(a)
    a = a + 1
    return a


# %%
f2()


# %%
def f2():
    global a
    print(a)
    a = a + 1
    return a


# %%
f2()


# %% [markdown]
# 정리하자면 함수 내에서 새로운 변수를 만들어 쓸 수 있지만, 그 변수의 스코프는 함수 안으로 제한된다. 만약 모듈에서 정의된 변수를 사용하려면 `gloabl`로 사용하려는 변수를 미리 선언해야 한다.

# %% [markdown]
# 만약 함수 내의 함수를 사용한다면 `nonlocal` 선언문이 필요할 수도 있다. 함수 안의 변수도 아니고, 모듈의 변수도 아닌 중간 함수의 변수를 사용하려면 `nonlocal` 선언을 한다. 왜냐하면 모든 지역에서 사용할 수 있는 것은 아니지만, 한 지역 내에서만 쓰는 것도 아니기 때문이다. `nonlocal`의 예는 다음과 같다.

# %%
def f():
    def g():
        a = a + 1
        print(a)
    a = 3
    g()


# %%
f()

# %% [markdown]
# 오류를 확인하자. `UnboundLocalError: local variable 'a' referenced before assignment` 여기서 확인할 수 있듯이 함수 내의 변수는 별다른 얘기가 없다면 무조건 지역(local) 변수로 취급된다.

# %% [markdown]
# 그런데 아래의 코드에서 `a`는 모듈에도 존재하고, 함수 안에도 존재한다.

# %%
a = 10
def f():
    def g():
        a = a + 1
        print(a)
    a = 3
    g()


# %%
f()

# %% [markdown]
# `def g():` 아래에 `global a`로 하면 `a=10`의 `a`를 의미하고, `nonlocal a`를 하면 `a=3`(함수 `g()` 안의 변수 `a`)를 의미하게 된다.

# %%

# %%

# %% [markdown]
# ### END OF DOCUMENT

# %% [markdown]
# 함수는 기본적으로 프로그램의 다른 부분에 영향을 주지 않으면서 자신의 기능을 하도록 설계된다. 파이썬에서 함수 내에서 사용할 수 있는 변수는 기본적으로 함수의 정의에 포함된 매개변수와 함수 내에서 생성된 변수이다. 만약 함수 밖의 변수를 사용하려면 어떤 방법이 있을까?

# %%
첫 번째 방법은 매개변수로 받는 방법이다. 

# %%

# %%

# %%
