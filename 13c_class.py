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
# * 참고 자료 
#   - Python Language Reference
#       - https://docs.python.org/3.8/reference/index.html
#
#   - https://docs.python.org/3.8/tutorial/classes.html
#   - https://docs.python.org/3.8/reference/datamodel.html
#   
#   - 메소드 관련 : https://journeytosth.tistory.com/73
#       - 인스턴스 메소드
#       - 클래스 메소드
#       - 정적 메소드
#       - 상속에서 차이점
#       
#  - Expression vs Statement 
#     - https://stackoverflow.com/questions/4728073/what-is-the-difference-between-an-expression-and-a-statement-in-python
#     
#  - Datacamp's Python OOP

# %% [markdown]
# ## 객체
#
#

# %% [markdown]
# 파이썬 공식문서의 "데이터 모델(data model)"을 보면 다음과 같은 문장이 나온다.

# %% [markdown]
# > Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects.
#
# > 객체(object)는 파이썬에서 데이터를 추상화한다. 파이썬 프로그램의 모든 데이터는 객체 또는 객체 사이의 관계로 표현된다.

# %% [markdown]
# 데이터 추상화는 잠시 넘어가자. 파이썬은 모든 데이터를 객체 또는 객체 사이의 관계로 표현한다고 한다. 그렇다면 **객체(object)**란 무엇인가? 

# %% [markdown]
# > Every object has an identity, a type and a value.

# %% [markdown]
# 객체란 **id**, **타입**, 그리고 **값**을 가진 무엇이다. 앞에서 우리는 **타입**이 어떤 역할을 하는 지 배웠다. 타입은 컴퓨터 메모리에 저장된 이진수가 무엇을 의미하는지, 그리고 어떤 연산이 가능한지를 결정한다. 마지막으로 `id`란 이진수가 저장된 메모리의 주소라고 생각할 수 있다. 실례를 통해 그 의미를 다시 알아보자.

# %% [markdown]
# 우선 메모리의 2바이트로 저장 가능한 이진수 `0b0100000101000010`를 생각해보자. 메모리에 저장된 값은 그 값만 가지고는 무엇을 의미하는지 알 수 없다. 값이 무엇을 의미하는지는 **타입**에 의해 결정된다. 만약 앞의 이진수가 정수타입이라면 16706을 의미한다. 만약 문자열 타입이라면 `AB`를 의미한다.

# %%
0b0100000101000010

# %%
chr(0b01000001), chr(0b01000010)

# %% [markdown]
# 파이썬에서 `x=16706`라고 쓰면 파이썬은 `16706`을 적절히 이진수로 변환하여 메모리에 저장하고, 나중에 읽을 때 정수형으로 읽어야 한다는 것을 표시한다. 그리고 변수 `x`에 메모리에 저장된 주소를 저장한다. 우리가 `x` 또는 `print(x)`를 하면 `16706`으로 나오기 때문에 변수 `x`에 16706가 저장된 것으로 생각하기 쉽지만, 사실은 `x`에 저장된 주소로 가서 그 내용을 타입에 따라 해석하여 출력하게 된다.   

# %% [markdown]
# **객체**란 메모리에 저장된 어떤 정보를 의미하며, 이 정보는 특정한 타입이 있다. 정수형 `2`와 실수형 `2.`와 같이 동일한 값이라도 **타입**이 다를 수 있음을 이해하자. 

# %%
x1 = [1,2,3]; x2 = [1,2,3]
y1 = y2 = [10,20,30]

# %%
id(x1), id(x2), id(y1), id(y2)

# %%
x1 is x2, y1 is y2


# %% [markdown]
# 객체는 메모리의 한 주소를 차지하고 있다. 만약 두 변수가 가리키는 객체의 주소가 같다면 한 변수를 수정할 때, 다른 변수도 수정된다. 만약 두 변수가 가리키는 객체의 주소가 다르다면 두 변수는 값이 같더라도 서로 별개이다. 위에서 `x1`과 `x2`는 동일한 정보를 담고 있지만, 서로 별개이다. 반면 `y1`과 `y2`는 `id()`가 같고 따라서 `y1 is y2`는 `True`이다. 이는 `y1`과 `y2`가 변수 이름은 같지 않지만 가리키는 객체는 `id`, 타입, 그리고 값이 같은 동일한 객체이다.

# %% [markdown]
# ## 클래스

# %% [markdown]
# 객체의 타입은 클래스라고도 한다. 우리는 새로운 클래스를 정의할 수 있다.

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

# %%
x


# %% [markdown]
# `id(x)`는 실제 메모리 주소를 반환하기도 하고, 큰 의미없는 정수값이 반환되기도 한다. 그러나 중요한 것은 다른 객체는 다른 `id()` 값을 반환한다는 점이다. 그래서 굳이 `id()`를 구하기 보다는 두 객체의 `id()` 값이 같지만 `is`를 통해 확인하기도 한다. 

# %% [markdown]
# `type(x)`를 통해 객체 `x`가 우리가 위에서 정의한 `Patient` 클래스임을 확인할 수 있다. 그런데 위에서 `x`를 출력했을 때 결과를 보자. `<__main__.Patient0 at ...>`. `__main__`은 현재 모듈을 의미한다. 그리고 `Patient0`은 `class Patient0():`에서 정의된 클래스 이름이다. 그리고 `at` 이후에는 클래스가 저장된 주소를 나타낸다(`0x7fdf5801c2b0`은 10진수로 `id(x)`의 출력 결과와 같다). 그래서 `x`의 출력 결과인 `<__main__.Patient0 at ...>`에는 `x`가 속한 클래스(**타입**)과 메모리 주소(**id**)가 포함되어 있지만 `x`의 값은 알 수가 없다. 사실 `x`에는 어떤 정보도 없기 때문에 어떤 값을 출력하길 바라는 건 무리이긴 하다.
#

# %% [markdown]
# 새로운 클래스 `Patient`를 정의하여 값을 저장해보자.

# %%
class Patient():
    def __init__(self, name):
        self.name = name


# %%
y = Patient('한석봉')

# %% [markdown]
# 클래스 `Patient`의 객체를 생성하며 이 객체에 `한석봉`이란 정보를 저장한다. 그리고 변수 `y`가 이 객체를 가리키도록 하였다. 클래스 정의가 약간 복잡해지만, `y`를 확인해보자.

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
# 그런데 다음과 같이 `y`만 치면 여전히 클래스 이름(**타입**)과 메모리 주소(**id**)만 출력된다.

# %%
y


# %% [markdown]
# 위에서 배웠듯이 메모리 주소의 이진수를 클래스에 맞게 해석하면 객체 `y`에 저장된 값을 알 수 있다. 하지만 우리가 직접 그런 작업을 하기엔 우리는 너무 인간이다. 

# %% [markdown]
# 그래서 다음과 같이 클래스를 새롭게 정의할 수 있다.

# %%
class Patient2():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return(f'Name is {self.name}')


# %%
z = Patient2('한석봉')

# %%
z

# %% [markdown]
# 위에서 `def __repr__():`를 통해 `z`라고 쳤을 때 출력되는 값을 변경하였다. 클래스에서 정의하는 `__repr__()` 함수는 특별한 함수로 객체가 출력되는 방식을 결정한다.

# %% [markdown]
# 이처럼 클래스는 객체에 저장되는 내용, 객체가 어떻게 작동하는지 등을 모두 결정한다. 그런데 `def __repr__():`은 함수를 정의하는 꼴이다. 실제로 이는 `__repr__()` 함수를 정의하고, 이 함수는 `Patient`라는 클래스의 이름공간(namespace)에서 찾을 수 있다.

# %%
Patient2.__repr__

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
class Patient3():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return(f'Name is {self.name}')
    def upname(self):
        return self.name.upper()
        


# %%
w = Patient3('han seok-bong')

# %%
w.upname

# %% [markdown]
# 클래스 `Patient` 아래 `upname()`이라는 함수를 정의하였다. `upname()`의 정의를 살펴보면 `self`라는 인자를 받는다. 그런데 `w.upname()`을 보면 인자가 주어지지 않는 것처럼 보인다. 이것이 함수(function)과 메소드(method)의 차이이다. 메소드는 `w.upname()`처럼 객체의 속성으로 함수를 호출한다. 그리고 첫 번째 인자는 항상 현재 객체(`w.upname()`에서 `w`)가 입력된다. 

# %% [markdown]
# 그래서 메소드(클래스 안의 함수)를 정의할 때에는 항상 첫 번째 매개변수의 이름을 `self`로 하는 관례가 있다.

# %% [markdown]
# `Patient.upname()`은 일반적인 함수이므로 다음과 같이 두 가지 방법으로 클래스 `Pateint`에서 정의된 함수를 사용할 수 있다.

# %%
Patient3.upname(w)

# %%
w.upname()

# %% [markdown]
# ## 다시 객체
#
# 객체-클래스-메소드로 이어지는 설명의 흐름이 이해가 잘 되었는데, 다시 객체로 돌아오면서 흐름에 다소 혼동이 발생. 

# %% [markdown]
# 이렇게 클래스란 어떤 정보를 저장하기 위한 **템플릿**으로 생각할 수도 있다. 
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
Patient3.upname2 = upname2


# %% [markdown]
# `w`에 새로운 속성 `name2`를 만들었고, 클래스 `Patient3`에 새로운 속성 `upname2`에 함수 `upname2`를 할당했다. (여기서 `upname2`와 `Patient3.upname2`를 혼동하지 말자. `upname2`는 현재 모듈(`__main__`)의 이름공간에서 `upname2`를 찾고 `Patient3.upname2`는 클래스 `Patient3`의 이름 공간에서 `upname2`를 찾는다)

# %%
w.upname2()

# %% [markdown]
# 여기서 `w.name2 = upname2`로 하지 않도록 유의해야 한다. `w.name2 = upname2`로 하면 `w.name2`가 함수가 된다. `w.name2`가 메소드가 되게 하려면 **함수는 클래스에서 정의하고 접근은 객체를 통해 해야 한다.**
#
#

# %%
w.upname2 = upname2

# %%
w.upname2()

# %%
w.upname2(w)

# %% [markdown]
# 따라서 **메소드**란 클래스에서 정의된 함수를 객체를 통해 접근하여 첫 번째 인자가 객체가 되는 것이라고 생각하자.

# %% [markdown]
# 그런데 객체마다 따로 속성이나 함수를 정해주기는 번거롭다. 공통적인 속성과 함수를 모아 템플릿처럼 만든 것을 클래스라고 할 수 있다.

# %% [markdown]
# 객체는 객체만의 특별한 정보를 담고 있으므로 객체를 만들 때에 이런 정보를 지정해줄 수 있다. 위에서 `__init__()`은 이런 역할을 하는 함수이다.

# %% [markdown]
# 다시 말해 `w=Patient3(name='han seokbong')`을 실행하면 `Patient3` 클래스에서 정의된 함수 `__init__(self, name)`이 실행되고 첫 번째 인자는 `w=Patient3(name='han seokbong')`을 통해 만들어질 객체를 나타낸다. 두 번째 인자는 `Patient()`의 첫 번째 인자이다. 그리고 `__init__()`는 항상 `self`를 반환하게 된다. 이를 위의 `Patient3`의 정의에 대해 구체적으로 풀어보자.

# %% [markdown]
# ### 클래스의 `__init__()` 

# %% [markdown]
# `Patient3`의 정의에서 `__init__()` 부분만 따로 떼어보면 다음과 같다.

# %% [raw]
# class Patient3():
#     def __init__(self, name):
#         self.name = name

# %% [markdown]
# `__init__()` 부분은 클래스에 속하는 새로운 객체를 만들 때 사용된다. `Patient3`에 속하는 새로운 객체을 생성하기 위해서 함수와 비슷하게 `Patient3(...)`로 쓴다.

# %% [markdown]
# 이때 함수와 마찬가지로 `...` 부분에 인자를 적어 줄 수 있다. 이렇게 입력된 인자가 `__init__()`에서 어떻게 활용되는지 알아보자.

# %%
w = Patient3('han seok-bong')

# %% [markdown]
# `Patient3('han seok-bong')`의 `'han seok-bong'`은 `__init__(self, name)`에서 `name`에 대응한다. 그렇다면 `self`는 무엇일까? `self`는 `Patient3('han seok-bong')`으로 생성되는 새로운 객체를 가리키기 위해 사용된다. (#위에서는 w) 이는 다른 메소드에서 사용되는 방식과 비슷하다. 

# %% [markdown]
# `def __init__(self, name):` 아래 `__init__()` 함수의 구체적 내용을 보면 `self.name=name`에서 `Patient3('han seok-bong')`에서 입력된 `'han seok-bong'`을 `self.name`이 가리키게 된다. 그래서 새롭게 생성되는 객체(`self`)의 속성 `name`은 `'han seok-bong'`을 가리키게 된다. 다음을 보자.

# %%
w.name

# %% [markdown]
# ### 다른 속성들

# %% [markdown]
# 클래스 `Patient3`의 객체인 `w`의 다른 속성들은 `dir(w)`로 나열해볼 수 있다.

# %%
dir(w)

# %% [markdown]
# 파이썬의 거의 모든 것은 객체이기 때문에 파이썬에서 다루는 거의 모든 것은 `dir()`로 속성을 나열해 볼 수 있다. `dir(3)`, `dir('text')` 등을 해보자.

# %% [markdown]
# ### 메소드의 속성

# %% [markdown]
# `w`의 메소드 `w.upname` 역시 객체이므로 `dir(w.upname)`을 해볼 수 있다.

# %%
dir(w.upname)

# %%
w.upname.__self__ is w # 그럼 뭐에 쓰는 거지?

# %%
w.upname.__func__

# %%
w.upname.__doc__

# %%
w.upname.__name__


# %% [markdown]
# ## 클래스와 인스턴스의 관계 : 속성

# %% [markdown]
#

# %% [markdown]
# 속성은 크게 인스턴스 속성과 클래스 속성으로 나눠볼 수 있다. 클래스 속성이란 클래스에 딸린 속성이다. 클래스 속성은 인스턴스 속성과 마찬가지로 클래스 속성에서 만들 수도 있고 나중에 만들어 줄 수도 있다. 

# %%
class Patient4():
    name = '환자정보'


# %%
Patient4.name

# %% [markdown]
# 클래스 속성은 클래스를 통해 접근할 수도 있고, 인스턴스를 통해 접근할 수도 있다. 이는 이름 공간으로 이해해야 한다. 클래스의 이름 공간은 객체의 이름 공간과 별도로 존재한다.

# %%
a = Patient4()

# %%
a.name

# %% [markdown]
# 위의 `Patient4` 클래스 정의에서 `name`이라는 변수이름은 객체 `'환자정보'`를 가리키게 된다. 다시 말해 이름 공간 (클래스) `Patient4`의 `name`은 `'환자정보'`를 가리킨다. 

# %%

# %% [markdown]
# 이제 인스턴스 `a`의 이름공간에서 `name`을 찾으면 없다. 이런 경우 파이썬은 인스턴스의 클래스의 이름공간(즉, `Patient4`)에서 `name`을 찾는다. 그래서 `a.name`과 `Patient4.name`은 같은 객체를 가리킨다. 

# %%
Patient4.name = '환자들'

# %%
a.name

# %% [markdown]
# `Patient4.name`과 `a.name`이 이름만 다르는 동일한 객체라는 것을 다음과 같이 확인할 수 있다.

# %%
Patient4.name is a.name

# %% [markdown]
# 하지만 `a.name`을 변경해도 `Patient4.name`는 바뀌지 않는다. 왜냐하면 `a.name`에 어떤 객체를 할당하면 `a.name`은 `Patient4.name`과 별개로 존재한다. 다시 말해 `a`의 이름 공간에 `name`이 생긴 것이다.

# %%
a.name = 'a'

# %%
Patient4.name

# %%
a.name is Patient4.name

# %% [markdown]
# 클래스에서 생성될 수 있는 인스턴스는 여럿이지만, 클래스에서 `name`이란 이름을 한 속성은 단 하나 존재할 수 있다. 따라서 같은 클래스의 모든 인스턴스가 공유하는 값이 필요하다면 클래스 속성으로 할 수 있다.

# %%
a = Patient4()
b = Patient4()
c = Patient4()

# %%
a.name, b.name, c.name

# %%
a.name = 'patients'

# %%
Patient4.name, a.name

# %%
Patient4.name = '환자리스트'

# %%
Patient4.name, a.name


# %%
# 참고 : https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide

# %% [markdown]
# ## 인스턴스 메소드, 클래스 메소드, 정적 메소드

# %% [markdown]
# 인스턴스 메소드는 클래스의 속성으로 존재하는 함수를 인스턴스를 통해 접근하여 첫 번째 인자가 자동으로 인스턴스가 되는 것이다. 클래스 메소드는 첫 번째 인자로 클래스가 된다. 

# %% [markdown]
# 만약 클래스 아래 정의된 함수를 클래스를 통해 접근하면 그 함수는 그냥 일반적인 함수이다.

# %%
class Patient5():
    n = 0
    def BMI(w, h):
        return w**2 / h
    def __init__(self):
        Patient5.n = Patient5.n + 1
        


# %%
Patient5.n

# %%
a = Patient5()

# %%
Patient5.n

# %%

# %%
b = Patient5()
c = Patient5()

# %%

# %%

# %% [markdown]
# 위에서 클래스 `Patient5` 아래 정의된 함수 `BMI()`는 그냥 함수이다.

# %%
Patient5.BMI(80,170)

# %% [markdown]
# 물론 인스턴스를 통해 접근하면 인스턴스 메소드로 작동하기 때문에 매개변수 `w`에 인스턴스가 입력되는 불상사가 생긴다.

# %%
a.BMI(170)

# %% [markdown]
# 여기서 위의 `__init__()`을 보자. `Patient5`의 클래스 속성 `n`을 이용하여 생성된 인스턴스를 카운트하고 있다.

# %%
Patient5.n


# %% [markdown]
# 그런데 이렇게 클래스의 이름을 사용하면 동일한 코드를 다른 클래스에서 사용하지 못한다.

# %% [markdown]
# 이런 문제를 해결한 것이 클래스 메소드다 다음의 예를 보자.

# %%
class Patient6():
    n = 0
    def count():
        Patient6.n = Patient6.n + 1
    @classmethod
    def count2(cls):
        cls.n = cls.n + 1
    def __init__(self):
        #Patient6.count()
        Patient6.count2()


# %% [markdown]
# 위의 `Patient5`와 거의 동일하다. 인스턴스를 만들 때마다 `Patient6.n`은 하나씩 증가한다. `def count():`는 이를 클래스 아래 정의된 함수로 정의했다. 여기에서는 클래스 이름인 `Patient6`가 직접 등장하기 때문에 이 코드를 다른 클래스에서 바로 사용할 수 없다.

# %% [markdown]
# 반면 `def count2():`는 위에 `@classmethod`를 붙임으로 클래스 메소드로 정의한다. 클래스 메소드는 클래스를 통해 접근 가능하며 첫 인자로 현재 클래스를 받는다. 따라서 `Patent6.count2()`도 `Patient6.count()`와 동일한 역할을 한다. 단지 클래스메소드라는 점만 다르다.

# %%
a = Patient6()
b = Patient6()
c = Patient6()
Patient6.n

# %% [markdown]
# 그런데 인스턴스 이름공간에서 찾지 못한 이름은 클래스 이름공간에서 찾게 되므로, 클래스 메소드는 인스턴스를 통해 접근할 수도 있다. 하지만 이때에도 첫 번째 인자는 인스턴스가 아니라 인스턴스가 속한 클래스이다.

# %%
a.count2()

# %%
Patient6.n, a.n, b.n, c.n

# %%
Patient6.n is a.n


# %% [markdown]
# 위의 `class Patient6():` 정의에서 한 가지 수정하고 싶은 것은 `def __init__(self):` 아래 `Patient6.count2()`에서 클래스 이름을 바로 사용하는 부분이다.

# %% [markdown]
# 다음과 같이 수정할 수 있다. `a.count2()`에서 `count2()`의 첫 인자로 클래스를 받을 수 있는 이유도 `a.__class__`를 사용할 수 있기 때문일 것이다.

# %%
class Patient7():
    n = 0
    
    @classmethod
    def count2(cls):
        cls.n = cls.n + 1
    def __init__(self):
        cls = self.__class__
        cls.count2()


# %% [markdown]
# 이렇게 작성된 클래스는 다른 클래스에 복사 붙여넣기를 해도 잘 작동하게 된다.

# %%
class Patient8():
    n = 0
    
    @classmethod
    def count2(cls):
        cls.n = cls.n + 1
    def __init__(self):
        cls = self.__class__
        cls.count2()
    @classmethod
    def printn(cls):
        print("* Number of patients ", cls.n)


# %%
d = Patient8()
Patient8.printn()

# %%
d.printn()


# %% [markdown]
# 앞에서 클래스 `Patient5`에서 정의된 `BMI()`는 인스턴스 메소드를 염두하지 않았다. 이렇게 인스턴스 메소드도 아니고, 클래스 메소드도 아님에도 클래스 아래 정의된 함수는 정적메소드로 지정할 수 있다. 이렇게 정적메소드로 지정하면 인스턴스를 통해 접근해도 첫 번째 인자로 인스턴스가 자동 입력되지 않기 때문에 그냥 함수로 쓸 수 있다. 다음을 보자.

# %%
class Patient5b():
    n = 0
    @staticmethod
    def BMI(w, h):
        return w**2 / h
    def __init__(self):
        cls = self.__class__
        cls.n = cls.n + 1


# %%
ab = Patient5b()

# %%
Patient5b.BMI(170,80)

# %%
ab.BMI(170,80)


# %% [markdown]
# ### 정적 메소드, 클래스 메소드, 인스턴스 메소드 : 정리

# %% [markdown]
# 메소드는 모두 클래스 아래에서 함수와 같은 방식으로 정의된다.

# %% [markdown]
# 정적 메소드와 클래스 메소드, 인스턴스 메소드의 차이는 첫 인자로 자동으로 입력되는 값이다. 정적 메소드는 일반적인 함수처럼 첫 인자로 자동으로 입력되는 값이 없다. 클래스 메소드는 클래스가 첫 인자가 되고, 인스턴스 메소드는 첫 인자로 인스턴스가 입력된다. 세 메소드는 모두 클래스를 통해 접근할 수도 있고, 인스턴스를 통해 접근할 수도 있다.

# %% [markdown]
# ## 상속

# %% [markdown]
# 다음의 `Patient8`과 `Patient8b`를 비교해보자.

# %%
class Patient8():
    n = 0
    def __init__(self):
        cls = self.__class__
        cls.n = cls.n + 1
        
        
class Patient8b():
    n = 0
    def __init__(self, name):
        cls = self.__class__
        cls.n = cls.n + 1
        
        self.name = name
        
    def __repr__(self):
        return self.name



# %% [markdown]
# `Patient8b`는 `Patient8`과 공통점이 있다. 속성을 보면 둘 다 `n`이 있다. 함수로 보자면 `__init__()`은 공통적이고, `Patient8b`는 `__repr__()`이 추가되었다.

# %% [markdown]
# 이런 클래스 사이의 공통점을 활용하여 좀더 편하게 클래스 정의를 작성할 수 있다.

# %%
class Patient8c(Patient8):
    pass


# %% [markdown]
# 다시 위의 클래스 `Patient8c`를 보자. 앞에서 정의한 깡통 클래스처럼 보이지만, 사실은 `Patient8`과 동일하게 작동한다.
#
# 일단 `class Patient8c(Patient8):`의 의미를 이해할 필요가 있다. `class Patient8c(Patient8):`은 클래스 `Patient8c`는 `Patient8`을 상속한다는 의미이다. 이때 상속이란, `Patient8c`의 이름 공간 다음에 `Patient8`의 이름 공간을 찾는다는 의미이다.
#
# 그래서 `Patient8c()`을 하면 `Patient8c.__init__`을 찾고 없다면 `Patient8.__init__`을 찾아 실행한다. 여기서 `self`는 `Patient8c()`로 생성될 인스턴스가 된다.

# %%
Patient8c.n

# %%
Patient8.n is Patient8c.n

# %%
a = Patient8()
b = Patient8c()

# %%
a.n, b.n


# %% [markdown]
# 그런데 뭔가 이상하다?

# %% [markdown]
# 다시 시도해보자.

# %%
class Patient8():
    n = 0
    def __init__(self):
        cls = self.__class__
        cls.n = cls.n + 1
        
    @classmethod
    def printn(cls):
        print('* Number of patients = ', cls.n)
        
    def printn2(self):
        print(self.n)
        
        
class Patient8b():
    n = 0
    def __init__(self, name):
        cls = self.__class__
        cls.n = cls.n + 1
        
        self.name = name
        
    @classmethod
    def printn(cls):
        print('* Number of patients = ', cls.n)
        
    def __repr__(self):
        return self.name

class Patient8c(Patient8):
    pass


# %%
Patient8.n is Patient8c.n

# %%
b = Patient8c()

# %%
Patient8.n, Patient8c.n

# %% [markdown]
# 여기서 주의할 점은 `Patient8c.n =` 과 `Patient8c.n`이 전혀 다르게 행동할 수 있다는 점이다. 먼저 `Patient8c`에 속성 `n`이 없을 때 `Patient8c.n`은 상속받은 `Patient8`에서 속성 `n`을 찾는다. 그리고 값을 반환한다. 하지만 `Patient8c.n = 1`로 쓰면 `Patient8c`에 속성 `n`이 없더라도 만들어서 객체 `1`을 가리키게 한다.

# %% [markdown]
# 그래서 `a = Patient8()`를 한 후 `b = Patient8c()`를 하면 `def __init__(self):`의 `cls.n = cls.n + 1`은 `Patient8.n`에 1을 더한 후 `Patient8c.n`에 결과를 저장하게 되고, 이때 부터 `Patient8.n`과 `Patient8c.n`은 별개로 움직이게 되는 것이다.

# %%
Patient8.printn is Patient8c.printn

# %%
Patient8.printn2 is Patient8c.printn2

# %%
a = Patient8()
b = Patient8c()

# %%
a.printn2(), b.printn2()

# %%
a.printn2 is b.printn2


# %% [markdown]
# ### 이름 공간 확인

# %%
def dir_class(cls, indent = ''):
    print()
    print('0*1*2*3*4*5*6*7*8*9********************')
    
    print(indent + '* CLASS : ', cls.__name__)
    for x in cls.__dict__:
        if x == "__dict__":
            continue
        #print(x)
        print(indent + f"{x:20s}:{str(getattr(cls, x)):40s}")
    
    indent = indent + '  '
    if len(cls.__bases__):
        for bcls in cls.__bases__:
            dir_class(bcls, indent)

def dir2(x, indent = ''):
    
    if isinstance(x, type):
        dir_class(x)
    elif isinstance(x, object):
        print()
        print('i*0*1*2*3*4*5*6*7*8*9********************')
        print(indent + '* INSTANCE : ')
        for a in x.__dict__:
            if a == "__dict__":
                continue
            #print(x)
            print(indent + f"{a:20s}:{str(getattr(x, a)):40s}")
        indent = indent + '  '
        dir_class(x.__class__, indent)



# %%
dir2(a)

# %% [markdown]
# ### END OF DOCUMENT

# %%

# %%

# %%

# %%

# %% [markdown]
# 클래스 속성 `n`도 동일하게 존재한다.  그래서 결국 `Patient8b.n`은 
#
# a.n is b.n

# %%

# %%

# %%

# %%

# %%
a.n

# %%
b.n


# %%

# %%

# %%
class Dictionary(object):

    words = ""

    def __init__(self, word):
        self.words = self.words + word

    def print_list(self):
        print(self.words)

d = Dictionary('x')

# %%
d.print_list()

# %%
e = Dictionary('y')

# %%
e.print_list()


# %%
class Dictionary(object):

    words = []

    def __init__(self, word):
        self.words.append(word)

    def print_list(self):
        print(self.words)

d = Dictionary('x')

# %%
d.print_list()

# %%
e = Dictionary('y')
e.print_list()


# %%

# %%
class Dictionary(object):

    words = ['']

    def __init__(self, word):
        self.words[0] = self.words[0] + word

    def print_list(self):
        print(self.words)

d = Dictionary('x')

# %%
d.print_list()

# %%
e = Dictionary('y')

# %%
e.print_list()

# %% [markdown]
#

# %%

# %%

# %%

# %%

# %%

# %%

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
