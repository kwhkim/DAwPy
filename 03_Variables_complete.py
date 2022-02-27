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
# ### 이 장의 내용
#
# #### 변수, 자료형, 연산/함수
# - 변수
#     - 변수 이름(이름 짓기 관례)
#     - 변수 할당 
#     - 변수 관리 : 목록, 제거, 타입 확인
# - 데이터 타입(자료형)
#     - 데이터 타입(Data types) : 숫자, 문자, 범주, 논리, 날짜, 위치(?)
#     - 타입마다 한계, 범위
#     - 데이터 타입 확인
# - 연산(Operations)과 함수(Functions)
#     - 수치형 : 산술연산, 함수, 연산, 비교 연산
#     - 문자형 
#     - 날짜/시간
#     - 논리형
#     - 데이터 타입에 따른 연산과 함수
# - 특별한 값 : NA, NaN, Inf
#     - 발생 원인
#     - 몇 가지 유의사항

# %% [markdown]
# **변수**는 어떤 값을 담긴 위해 사용한다. 컴퓨터 공학에서는 "변수에 특정한 값을 할당한다"는 표현을 자주 쓴다. 
#
# **변수 이름**은 사용자가 맘대로 정할 수 있지만, 몇 가지 제약이 있다. 왜냐하면 `3`이나 `"A"`와 같은 이름을 지으면 숫자 `3` 또는 문자열 `"A"`와 **구분**할 수 없기 때문이다. 그래서 보통 변수 이름은 숫자로 시작할 수 없고, 밑줄(`_`)을 제외한 기호도 사용할 수 없다.   
#
# 변수를 결국 어떤 값을 저장하기 위해서 존재한다. 컴퓨터 메모리에 저장할 수 있는 값은 0과 1, 그리고 이들로 구성된 이진 정수뿐이다. 그리고 다른 값들은 모두 이진수와 대응을 통해 우리가 새로운 의미를 부여한 것이다. 예를 들어 $0041_{(16)}$은 문자 `"A"`와 대응시키거나 실수 $0.5$에 대응시킬 수 있다(문자와의 대응처럼 간단하게 이해할 수 있는 경우도 있고, 실수와의 대응처럼 복잡한 관계에 의해 결정되는 경우도 있다). 이때 컴퓨터 메모리 상의 이진수를 어떻게 해석하느냐는 **데이터 타입**이 결정한다. 데이터 분석에서 자주 쓰이는 타입은 숫자, 문자, 범주, 논리, 날짜 등이 있다. 
#
# 값의 타입이 달라지면 이 값에 **적용할 수 있는 연산과 함수**도 달라진다. 수 `2`은 제곱을 하거나 다른 수와 더할 수 있다. 반면 문자 `"2"`는 다른 문자와 더할 수 없다. 문자는 다른 문자와 합치는 등의 문자을 위한 연산이 가능하다. 
#
# 어떤 값에 연산을 적용했을 때 결과를 산출할 수 없는 경우가 있다(예. 1/0). 값을 측정하였지만 값이 중간에 분실되는 등의 이유로 값을 알 수 없는 경우도 있다. 이런 특수한 결과를 어떻게 표시하는가? **결측값, 무한을 나타내는 특별한 값**에 대해서도 알아본다.

# %% [markdown]
# # 3. 파이썬의 변수, 자료형, 연산/함수

# %% [markdown]
# ## 3.1 파이썬의 변수

# %% [markdown] tags=[]
# 파이썬의 변수는 어떤 값도 저장할 수 있다. (사실 엄밀히 말하면 파이썬의 변수는 어떤 값을 저장하지 않고 가리킬 뿐이다.[^varpointer] 예를 들어 `x=3`을 하면 변수 `x`는 수 `3`을 가리킨다. 하지만 이번 장에서는 변수에 값이 저장된다 생각해도 무방하다. 뒤에 클래스, 인스턴스, 가변객체를 다룰 때에는 엄밀한 설명이 필요하다.)
#
# [^varpointer]: 흔히 컴퓨터 언어에서 **포인터**(pointer)는 메모리의 주소를 저장하는 변수이다. 파이썬의 변수는 메모리의 어떤 객체를 가리킬 뿐이라는 점에서 포인터와 비슷하다. 하지만 포인터 `a`는 메모리 주소이고 파이썬에서 변수 `a`라고 하면 변수 `a`가 가리키는 객체를 나타낸다는 점에서 차이가 있다. 그래서 포인터 `a`에 `1`을 더한 `a+1`은 메모리 주소 `a`를 1 증가시킨 결과(**메모리 주소**)이고, 파이썬에서 `a+1`은 객체 `a`에 `1`을 더한 새로운 **객체**이다.

# %% [markdown] tags=[]
# ### 3.1.1 변수 이름

# %% [markdown]
# > 수학에서 미지수는 $x$, $y$ 등으로, 상수는 $a$, $b$ 등으로 쓴다. 그리고 $\sum_{i=1}^{10} i^2$와 같이 $\sum$을 쓸 때는 $i$, $j$ 등으로 쓴다. **컴퓨터 언어의 변수**는 $\sum_{i=1}^{10} i^2$의 $i$와 비슷하다. 그런데 미지수를 꼭 $x$, $y$ 등으로 써야 하는 것은 아니다. 미지수에 $a$나 $i$를 사용한 $a+4=3$ 이나 $i-1=4$와 같은 방정식은 유효하다. 단지 미지수를 나타낼 때 $x$, $y$, $z$와 같은 문자를 쓰는 것이 관례이기 때문에 미지수를 $x$, $y$ 등으로 쉽게 이해할 수 있다. 다시 말해 가독성(readability)이 높아진다.
#
# > 파이썬에도 변수 이름을 지을 때 비슷한 관례(convention)가 있다. 관례는 반드시 지켜야 하는 것은 아니지만 가독성을 높여준다.

# %% [markdown]
# * 파이썬에서 변수 이름은 알파벳, 숫자, `_`(밑줄; underbar)를 사용하여 구성할 수 있다. (사실 알파벳뿐 아니라 한글과 같이 다른 나라 문자도 변수 이름에 사용할 수 있지만 권장하지 않는다. 파이썬 표준 모듈은 변수 이름에 ASCII의 문자만 사용한다.) 그리고 대소문자를 구분한다.
# * R과 달리 `.`(점; dot)은 사용할 수 없다. 왜냐하면 파이썬에서 `.`은 특별한 기능(클래스의 속성을 나타내거나, 모듈의 객체를 나타내는 등)을 위해 사용되기 때문이다. 
# * 변수의 첫 글자로 숫자를 쓸 수 없다. (만약 첫 글자로 숫자를 허용한다면 `3j`는 변수인가 허수 $3i$인가?)
# * 파이썬의 예약어는 변수 이름으로 쓸 수 없다. 다음은 파이썬 3.8의 예약어 목록이다. 예약어 목록은 파이썬 표준 모듈 `keyword`의 `kwlist`에서 확인할 수 있다(혹시라도 다른 버전의 예약어를 확인하고 싶다면 `import keyword; keyword.kwlist`를 실행하자).

# %%
import keyword 
_ = [print(x, end=' ') for x in keyword.kwlist]

# %% [markdown]
# 다음의 파이썬 예약어 목록 그 기능을 정리한 것이다.

# %% [markdown]
# ```
# from import   # 모듈 관련
# None False True   # 진리값 등
# del in is   # 변수 관련
# not and or  # 논리 연산
# if else elif   # if-else-elif
# for while finally   # 반복문
# pass continue break # 반복문 관련
# with as   # 맥락(context) 관련
# try except raise  # 예외 처리
# class def lambda global nonlocal return yield
# # 클래스와 함수 정의
# assert # unit-testing 관련
# async await # 비동기 실행 관련
# ```
#
# * 파이썬에서 `_`로 시작하는 변수이름은 보통 내부용 변수에 사용한다(예. 클래스 또는 모듈의 내부에 존재하지만 외부에는 알리기 싫은 변수. 클래스와 모듈 작성에서 자세히 설명된다).

# %%

# %% [markdown]
# 그렇다면 파이썬에서 실제 어떤 이름이 쓰이고 있을까? 어떻게 이름을 지어야 할까?
#
# 컴퓨터 언어를 사용하는 사람들은 다양한 방식으로 이름을 짓는다. 우선 여기서 이들을 정리해 보자.
# 보통 변수의 이름은 그 의미를 쉽게 알 수 있도록 단어을 연결하여 짓는다. 예를 들어 지난 달 수입을 의미하는 income last month에서 income, last, month과 이번 달 수입을 의미하는 income this month에서 income, this, month을 사용하여 변수 이름을 지어보자. 다음과 같은 방식을 생각해 볼 수 있다.
#
# ```
# x X 
# incomelastmonth income_last_month
# INCOMELASTMONTH INCOME_LAST_MONTH
# IncomeLastMoth incomeLastMonth Income_Last_Month income_Last_Month
# income_lastmonth/income_thismonth
# income_last/income_this
# num_incomeLast/num_incomeThis
# ```
#

# %% [markdown]
# 변수 이름 짓기는 언어마다 관례(convention)가 다르고, 회사마다, 그리고 개인마다 다를 수 있다. 보통 어떤 프로젝트를 시작한다면 사람들 사이의 혼동을 줄이기 위해 이름을 짓는 방식을 정하기도 한다. 그럼에도 거의 항상 적용되는 법칙은 대문자로만 이루어진 변수는 상수를 의미한다는 것이다(변수가 상수를 의미한다? 실제 상수일 수도 있고, 변수이지만 결코 수정을 하지 않겠다는 의미일 수도 있다).
#
# * 가장 간단한 변수 이름은 알파벳 한 글자를 사용한다. `x`, `y`, `i`, `j` 등. 만약 현재 **관심의 대상**이 분명하거나, **한번 쓰고 버릴 변수**(예. `for` 문의 루핑(looping) 변수)라면 한 글자로 쓰는 것이 편하다. 한글자로 변수 이름을 지으면 가능한 변수의 갯수가 너무 한정적이라는 단점이 있다. 그리고 소문자 엘(`l`), 대문자 아이(`I`), 대문자 오(`O`)는 쓰지 않는 것이 좋다. 일(`1`) 또는 영(`0`)과 구분이 힘들기 때문이다.
#
# * 둘 이상의 단어를 사용하여 변수 이름을 짓는다면 단어 사이를 연결할 때 바로 붙여 쓸 수 있다. 하지만 이 방법은 대체로 권장되지 않는다. 왜냐하면 단어의 구분이 힘들기 때문이다. 하지만 두 단어 정도라면 용인할 수 있다.
#
# * 단어 사이를 연결할 때 구분을 위해 `_`을 단어 사이에 추가하거나, 단어를 소문자로 쓰고, 첫 문자만 대문자로 쓰는 방법이 있다. `_`를 사용하는 방법을 snake_case(밑줄방법)이라고 하고, 단어의 첫 글자를 대문자로 쓰는 방법을 CamelCase 또는 CaptializedWords(CapWords)라고 부른다. 파이썬에서는 밑줄방법이 대세인 듯하다. 하지만 파이썬 표준 라이브러리 안에서도 한 가지 방법으로 통일되어 있지 않다.
#
# * 공통적인 성격(위의 예에서 수입)의 변수를 모아 이름을 짓기도 한다. 예를 들어 수입에 관한 변수라면 공통점을 앞에 적고 밑줄을 긋고 변수 이름을 적는 방식이다. `income_lastmonth`, `income_thismonth` 또는 `income_LastMonth`, `income_ThisMonth`와 같이 밑줄 뒤의 변수 이름은 다시 여러 방식을 사용할 수 있다. 하지만 파이썬에서는 이런 경우 클래스를 만들어서 `income.lastmonth`, `income.thismonth`와 같이 쓸 수 있기 때문에 자주 활용되지 않는 듯 하다.
#
# * 변수의 타입을 공통점으로 사용하기도 한다. 예를 들어 수입이 문자열로 저장되어 있는 변수와 수로 저장되어 있는 변수가 있다면 `num_income`, `str_income`으로 이름을 짓는 방식이다.
#
# * 던바(dunbar; double underbar)로 시작하고 끝나는 변수 이름에 대해서는 뒤에 설명된다.

# %% [markdown]
# 우리가 이번 장에서 사용하는 수, 문자열, 범주, 논리, 날짜시간과 같은 값(데이터)에 대해서는 **소문자를 사용하고 밑줄로 단어를 연결하는 방식**이 가장 많이 쓰인다. 다른 방식이 이름이 사용되는 경우도 있는데 이에 대해서는 뒤에서 설명하겠다. 
#
# 그리고 **예약어와 같은 단어**를 써야 할 경우에는 보통 뒤에 밑줄을 붙이는 방식이 권장된다(PEP ???). 예를 들어 from이라는 단어를 써서 변수 이름을 사용하고 싶다면 `from_`를 사용하거나 동의어를 사용한다. 예를 들어 R에서는 `seq(from=, to=)`과 비슷한 역할을 하는 파이썬 함수 `range()`는 매개변수로 `start=`, `stop=`을 사용한다. 
#
# 다음은 파이썬에서 여러 방식의 변수 이름을 사용하는 예를 보여준다. 주석 처리된 부분은 파이썬에서 사용할 수 없는 이름이 사용된 경우로 `SyntaxError` 또는 `NameError`가 발생한다.

# %%
myAge = 22
year = 2018
day_of_Month = 3
_hidden_value = 10.5
#stock.high = 13322
#if = 3
whatIGotForMy23thBirthday = "flowers"
print(myAge)
print(year)
print(_hidden_value)
print(day_of_Month)
print(whatIGotForMy23thBirthday)

# %% [markdown]
# ### 3.1.2 변수 할당

# %% [markdown]
# 변수 할당을 위해서는 `=`를 사용한다.
# `a=b=3`와 같이 여러 변수에 연쇄적으로 할당할 수도 있다.
#
# R과 다르게 `<-` 또는 `->`를 사용할 수 없다.
#
# 파이썬의 경우 **별칭**(alias)이란 말도 자주 쓰이는 데 이에 대해서는 다음 장에서 설명된다. (별칭이란 변수가 가리키는 대상이 동일한 경우에 **또다른 이름**이란 뜻이다. 이번 장에서는 별칭이 사용되지 않는다.)
#

# %%
a = 3
b = 2
d = -1
e1 = e2 = 7
print(a, b, d, e1, e2)

# %%
e1 = e2 = e3 = 10
e2 = 3
print(e1, e2, e3)

# %% [markdown]
# 파이썬은 여러 값을 여러 변수에 한꺼번에 할당할 수 있다. R에서는 사용할 수 없는 편한 기능이다. 예를 들어 변수 `a`에 수 `3`을, 변수 `b`에 문자열 `"three"`를 할당하고자 한다면 `a=3; b="three"`라고 쓸 수 있다. 이건 그냥 두 문장을 한 줄에 적기 위해 `;`을 사용한 것이다. 한꺼번에 할당하기 위해서는 `,`를 사용한다. 다음을 보자.

# %%
a, b = 3, "three"
print(a); print(b)

# %% [markdown]
# 이 방식은 튜플 언패킹(unpacking)이라고 부른다. 좀 더 자세히 설명하자면 `a, b= 3,"three"`는 `(a,b) = (3,"three")`와 같은 의미이다.[^op1] 그리고 `(3, "three")`를 파이썬은 튜플이라는 하나의 데이터로 취급하기 때문에 가능한 일이다. 튜플은 다음 장에서 소개된다. 우선은 `a,b = 3,4`와 같이 한번에 여러 값을 여러 변수에 할당하는 방법이 존재하며 이것이 가능한 이유는 `,`의 연산 순위가 `=`보다 빠르기 때문이라는 점을 기억하자(만약 `=`의 연산이 `,`보다 빠르다면, `a,b=3,4`는 `a, (b=3), 4`로 해석될 것이다).
#
# [^op1]: 이런 식의 해석이 가능하려면 `,`의 연산 순위가 `=`보다 빨라야 한다.

# %% [markdown]
# 다음은 변수 hzC5, hzD5, hzD5에 (5번째 옥타브) 도,레,미의 주파수 523.25, 587.33, 659.25를 할당한다.

# %%
hzC5, hzD5, hzE5 = 523.25, 587.33, 659.25
# 비교) hzC5=523.25; hzD5=587.33; hzE5=659.25
print(hzC5); print(hzD5); print(hzE5)

# %% [markdown]
# `a,b = 3,2`는 `a=3; b=2`와 큰 차이가 없어 보일 수 있다. 하지만 `a,b = b,a`와 `a=b; b=a`와 비교해보면 큰 차이가 분명하다.

# %%
print(a,b)
a,b = b,a # a와 b의 값이 서로 바뀐다.
print(a,b)
a=b; b=a  # a의 값이 b와 같아지고, b는 다시 a와 같아진다(이미 같다).
print(a,b)

# %% [markdown]
# 만약 변수 이름이 문자열 변수에 저장되어 있다면 어떻게 할당해야 하나? 예를 들어 `varname`에 `"myVar"`이라는 값이 저장되어 있다면 `myVar=10`을, `varname`에 `"amount"`가 저장되어 있다면 `amount=10`를 해야 한다면? R에서는 쉽게 `assign(varname, 10)`을 하면 되지만 파이썬에서는 간단한 함수가 존재하지 않는다. 약간 복잡한 방법으로 `globals()[varname] = 10`으로 쓸 수 있다. 여기서는 R의 `assign`과 같은 기능을 하는 함수 `assign`을 정의하여 간편하게 사용할 수 있도록 하였다.[^scope]

# %%
varname = 'amount'
globals()[varname] = 10
print(amount)

# %%
del amount


# %%
def assign(varname, value):
    globals()[varname] = value
assign(varname, 10)
print(amount)

# %% [markdown]
# [^scope]: 이때 할당은 전역 변수만 가능하다. 변수이름을 찾을 수 있는 **범위**는 보통 변수를 만든 장소에 따라 달라진다. 좀더 자세한 내용은 함수와 관련된 장(???)을 참고하자.

# %%
# !!!TODO : locals(), vars(), globals()

# globals()는 전역변수
# locals()는 현재 지역 변수(함수 안에서는 함수 내, 클래스 안에서는 클래스 속성 등)
#            저절로 update되지 않으며 assign도 되지 않는다
# vars()는 locals()와 비슷하지만 객체가 주어지면 객체의 속성

# %%
#del c
try:
    print('c=', c)
except:
    pass
a = 3
def f(b):
    print(locals())
    print(vars())
    print(dir(f))
    print(f.__closure__)
    #print(f.__globals__)
    print(f.__name__)
    print(f.__module__)
    print(f.__qualname__)
    f.__setattr__('c', 3)
    
    #vars()['c'] = b+3
    exec('c= b+3')
    
    print(a,b,c)


# %%
def f():
    exec('a=3')
    print(a)


# %%
f()

# %%
f(2)

# %%
dir(f)

# %%
# ?locals

# %% [markdown]
# ### 3.1.3. 변수관리

# %% [markdown]
# #### 변수의 존재 확인

# %% [markdown]
# 사용 가능한 변수의 목록은 `globals()`로 확인 가능하다. (이때 사용 가능한 변수의 목록은 맥락 의존적이다. 현재 모듈에서 사용 가능한 변수와 다른 모듈에서 사용가능한 변수가 다르고, 함수 밖에서와 함수 안에서, 그리고 객체 안에서, 밖에서 사용 가능한 변수가 다르다.) `globals()`는 현재 모듈의 어떤 함수 또는 객체에 속하지 않는 가장 최상의 수준에서의 가능한 변수 목록을 출력한다. 특정한 맥락을 가정할 경우에는 `locals()` 또는 `vars()`를 써서 사용 가능한 변수 목록을 확인할 수 있다.)
#
# `globals()`의 결과는 다음 장에서 소개될 딕 형태로 제공된다. 만약 변수 이름만 확인하고 싶다면 `globals().keys()`를 사용한다.

# %%
globals().keys()


# %% [markdown]
# 목록을 살펴보면 우리가 위에서 할당했던 변수들을 확인할 수 있다. 그 밖에서 `__`(dunbar; **d**ouble **un**der **bar**)로 시작하고 끝나는 변수를 볼 수 있다(`__name__`, `__doc__`, `__package__`, `__loader__`, `__spec__`). 이들은 거의 모든 모듈에서 자동적으로 생성되는 변수로 사용자가 수정하지 않는게 좋다(앞에서 모듈이 다른 모듈로 임포트되면 해당 모듈의 `__name__`은 모듈의 이름이 되고, 직접 실행되면 `__name__`은 `__main__`이 됨을 설명했다). 그 외에 `__builtin__` 또는 `__builtins__`는 모두 파이썬 내장 모듈의 하나인 `builtins` 모듈을 가리킨다. 
#
# 주피터 노트북(jupyter notebook)에서 사용할 경우 `_i1`, `_i2`와 같은 변수들도 보인다. 이 변수는 셀의 결과를 담고 있다(셀의 왼쪽을 보면 `In [1]:`, `Out[1]:`과 같이 몇 번째로 계산된 셀인지를 나타내는 표식이 있다. `Out[1]`의 결과는 `i_1`에도 저장된다). 쥬피터 노트북에서 `In`과 `Out`은 이때까지의 셀 입력과 셀 출력을 가리킨다. `exit`와 `quit`은 파이썬의 가장 기본적인 함수이다. 파이썬 콘솔에서 `exit()` 또는 `quit()`으로 파이썬 콘솔을 종료할 수 있다.

# %% [markdown]
# 어떤 변수 `x`의 존재 여부를 확인하고자 한다면 `"x" in globals().keys()`를 쓸 수 있다. 따옴표를 유의하자. 변수의 이름을 따옴표에 감싸 문자열로 제공해야 한다.

# %% [markdown]
# 다음 함수 `globals_user()`는 `globals().keys()`의 결과에서 밑줄이 `_`로 시작하는 변수를 제거하여 보여준다(`dict_=True`로 하면 목록의 딕형태로 반환하고, `dict_=False`로 하면 변수 목록만 리스트로 반환한다. 기본값은 `dict_=True`이다.)

# %%
def globals_user(dict_ = False):
    varnames = globals().keys()
    varnames2 = [varname for varname in varnames if not varname.startswith('_')]
    if dict_:
        return {k:globals()[k] for k in varnames2}
    else:
        return varnames2
globals_user()

# %% [markdown]
# `dir()`을 사용해도 목록을 뽑아 볼 수 있다. (`globals().keys()`, `locals().keys()`, `vars().keys()`, `dir()`의 결과는 상황에 따라 조금씩 달라진다. 이에 대해서는 후에 설명된다.)

# %% tags=[]
dir()

# %% [markdown]
# #### 변수 제거

# %% [markdown]
# 특정한 변수를 제거하려면 `del` 문을 사용한다. 변수 `a`를 제거하고자 한다면 `del a`라고 쓴다. 여러 변수를 한꺼번에 제거하고자 한다면 `del a, b, c`와 같이 쓸 수도 있다(`del(a,b,c)`도 가능하기 때문에 `del`을 함수로 오해할 수도 있지만, `if`문도 `if(1==1):`라고 쓸 수 있는 것과 비슷하다. `del`도 함수가 아니라 문(statement)이다).

# %%
a = 3; b=4; c=5
del a, c
'a' in globals().keys(), 'b' in globals().keys(), 'c' in globals().keys()

# %%
help("del")

# %% [markdown]
# 만약 변수에 변수이름이 저장되어 있는 상황이라면 다음과 같이 활용할 수 있다. `varname`에 변수이름이 문자열로 담겨 있다면 `del globals()[varname]`를 쓴다.

# %%
myVar = 'Hope you merry Christmas!'
varname = 'myVar'
del globals()[varname]
'myVar' in globals().keys() # varname in globals().keys()

# %% [markdown]
# 모든 변수를 제거하려면 어떻게 해야 할까? 앞에서 설명한 모든 변수 목록을 얻은 후 제거를 하면 될 것이다. 이때 사용자가 정의하지 않은 기본적인 변수는 제외하는 게 나을 것이다. 예를 들면 `exit`, `quit`과 같은 함수, `_`로 시작하는 변수, 그리고 파이썬 노트북의 `get_ipython`이란 함수가 대표적이다. 다음 함수는 `globals()`에서 `_`로 시작하는 변수, `exit`, `quit`, 그리고 `get_ipython`, 그리고 자기 자신(`delall`)을 제외한 모든 변수를 제거한다. 

# %%
import types
def del_all(types_skip=(type, types.FunctionType, types.ModuleType)):
    #print(types_skip)
    #print(type(types_skip))
    if types_skip is not None and not isinstance(types_skip, tuple):
        raise ValueError("types should be either 'all' or tuple of types to skip")
    varnames = set(globals().keys()) # 제거할 변수
    # 맥락에 따라 globals().keys()를 locals().keys(), dir() 등으로 교체할 수 있다.
    #varnames = varnames.difference({'exit', 'quit', 'get_ipython', 'delall', 'globals_user', 'builtins', 'In', 'Out'})
    varnames_underbar = [varname for varname in varnames if varname.startswith('_')]    
    varnames = varnames.difference(set(varnames_underbar))    
    if types_skip is None:
        for varname in varnames:
            del globals()[varname]
    else:
        for varname in varnames:
            if not isinstance(globals()[varname], types_skip):
                del globals()[varname]            


# %%
a = 3; b="xxx"; info='Python'

# %%
globals_user()

# %%
del_all()
globals_user()

# %% [markdown]
# 뒤에서 설명하겠지만 대부분의 경우 변수를 제거할 때 함수나 모듈은 제외한다. 그런 경우에는 `del_all()` 함수의 `types=` 매개변수를 활용하여 변수의 타입을 확인하여 제거할 수도 있다.

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
# globals()                       모든 객체 나열
# 'x' in globals().keys()         변수이름 `x`가 존재하는가?
# del_all()                       모든 객체 제거(_으로 시작하는 변수이름 등 예외)
# del x                           변수이름 'x' 제거
# type(x)                         객체 x의 데이터 타입(뒤에 설명된다)
#                                 모든 객체 저장
#                                 .RData 에 저장된 객체 불러오기

# %% [markdown]
# ## 3.2 파이썬의 데이터타입(자료형)

# %% [markdown]
# ### 3.2.1 내장 데이터타입(Data types)

# %% [markdown]
# 프로그래밍에서 가장 기본적인 변수 타입(`type`)에 대해 얘기해 보자.[^type]
#
# [^type]: 정확히는 변수가 가리키는 객체의 타입이다. 앞에서 얘기했듯이 이번 장에서는 변수에 값이 저장된다고 생각해도 무방하므로 **변수의 타입**(변수에 저장된 값의 타입)이라고 하였다. 

# %%
print(type(3), type(3.0))

# %% [markdown]
# 사람에게 $3$ 또는 $3.0$은 모두 정수 $3$을 의미한다(물론 정수는 실수이기도 하다. 어쨋든 둘은 표기의 차이만 있을 뿐 같은 값을 나타낸다). 컴퓨터 언어에서 타입이란 주어진 정보를 어떻게 메모리에 저장하고, 또 메모리의 내용을 어떻게 해석할지를 결정한다(메모리에 저장되는 것은 항상 0과 1, 그리고 이들의 조합일 뿐이다). 예를 들어 정수 $3$은 이진수 00000010으로 저장된다. 반면 실수(`float`)형 $3.0$은 이진수로 저장되지만 기수와 지수로 나뉘어 (0010, 0000)로 저장된다. 그리고 메모리의 이 내용은 $0010_{(2)}\times 2^{0000_{(2)}}$으로 해석된다. 이를 10진법으로 고쳐 쓰면 $3.0 \times 10^0$이 된다(사전 지식이 없다면 이 내용을 이해하기 힘들 것이다. 넘어가거나 전문가에게 문의하자).

# %% [markdown]
# 이렇게 컴퓨터가 저장하는 어떤 값에는 타입이 있다. 가장 대표적으로 정수형 `3`, 실수형 `3.0`, 문자열 `"three"`을 생각할 수 있다. 이들은 모두 메모리에 0과 1로 저장된다.[^store1] 그리고 이들은 모두 변수에 저장될 수 있다.
#
# 그런데 많은 언어가 일단 변수의 타입을 선언해야 변수를 사용할 수 있다. 예를 들어 C에서 `int my_var`라고 하면 정수타입의 변수 `my_var`를 선언한 것이다. 이는 "변수 `my_var`를 사용하겠다. 그리고 이 변수에는 정수형만을 담겠다"는 의미이다.
#
# 이에 반해 파이썬에서는 변수를 선언할 필요가 없다. 선언을 하지 않고 `my_var = 3`과 같이 바로 변수를 사용한다. 그리고 변수의 타입은 이렇게 변수에 어떤 값을 저장하느냐에 따라 달라진다.[^store2] 따라서 **동적 타입 언어**라고 한다. 변수의 타입이 고정적이지 않고 변할 수 있다. 
#
# 이제 변수에 대해 얘기해 보자. 
#
# [^store1]: 정확히 얘기하면 저장하는 것이라 아니라 변수가 해당 값(객체)를 가리킨다. 하지만 앞에서 얘기했듯이 이 장에서는 저장된다고 생각하겠다.
#
# [^store2]: 정확히 얘기하면 변수를 객체를 가리킬 뿐이고, 객체에 타입(클래스)이 존재한다. 이 얘기가 생소하다면 이 각주도 당분간 무시하자.

# %% [markdown]
# 파이썬의 기본적인(내장 모듈에서 정의된) 데이터 타입은 https://docs.python.org/ko/3.8/library/index.html 에서 확인할 수 있습니다. `dir(builtins)`을 통해서도 모듈 빌트인(`builtins`)에 정의된 클래스나 함수를 확인할 수 있습니다. 앞에서 설명했듯이 내장 모듈에 정의된 클래스, 객체, 함수 들은 파이썬 실행 후 바로 사용할 수 있습니다. 아마도 파이썬에서 `from builtins import *`를 하는 듯 합니다. 

# %%
import builtins

# %%
__builtins__ is builtins, __builtin__ is builtins

# %%
builtins

# %%
builtins.int is int, builtins.float is float, builtins.str is str

# %% [markdown]
# [파이썬 표준 라이브러리 사이트](https://docs.python.org/3.8/library/)에서 내장 타입(Built-in Types)를 확인해보세요. 숫자형(`int`, `float`, `complex`), 문자열(`str`), 시퀀스형(`list`, `tuple`), 매핑형(`dict`), 집합형(`dict`, `frozenset`) 등이 소개 되어 있는데, 이 중에 대표적인 데이터 타입은 **논리형**(`bool`), **숫자형**(`int`, `float`, `complex`)과 **문자열**(`str`; 파이썬 사이트에는 텍스트 시퀀스형이라고 표기됨)입니다.

# %% [markdown]
#
# | 데이터 타입  |    예  |
# |:-------------:|:-------------|
# | 정수형(`int`) | `0`, `-1`, `1`, `3`, `-100`, `10_000`, `0b0010`, `0o32`, `0xff` |
# | 실수형(`float`) | `1.0`, `0.45`, `1e-7`, `1E-7`, `math.pi`, `math.exp(1)` |
# | 복소수형(`complex`) | `0+0j`, `1+4j`, `1.4+3j` |
# | 논리형(`bool`) | `True`, `False` |
# | 문자열(`str`) | `"a"`, `"\r"`, `"\x41"`, `\N{INVERTED EXCLMATION MARK}"`, `"\u0041"`, `"\U00000041"`| 
#
# https://docs.python.org/3/reference/lexical_analysis.html

# %% [markdown]
# #### 정수형(`int`)
#
# 정수형은 정수를 나타낸다. 파이썬 3+(???)에서 정수는 (메모리가 허용한다면) 최소값이나 최대값이 존재하지 않는다. 메모리만 허용한다면 임의의 큰 양수, 임의의 작은 음수를 저장할 수 있다. 정수형 수를 나타내는 방법은 `16`과 같이 10진수로 표기하는 방법이 가장 기본적이다. 그외에도 2진수, 8진수, 16진수로 표기할 수 있다. `0b`는 2진수, `0o`는 8진수, `0x`는 16진수를 나타내기 위해 앞에 쓴다. 자릿수가 많은 숫자를 읽기 쉽게 표기하기 위해 숫자 사이에 `_`를 넣을 수 있다. 

# %%
# 정수를 표기하는 여러 가지 방법
a = 0; b=-1; c=1; d=3; e=-100; f=10_000_0_0_0; g=0b0010; h=0o32; i=0xff;
# 0, -1, 1, 3, -100, 이진수 0010, 팔진수 32, 16진수 ff
print(a,b,c,d,e,f,g,h,i) # print() 결과는 모두 10진수로 출력된다.
type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i)

# %%
# _를 사용해서 수를 좀더 쉽게 읽을 수 있는 방식으로 표기할 수 있다.
# 숫자 사이의 원하는 곳에 _를 추가할 수 있다. 하지만 _를 두 번 연속 쓸 수 없다.
a = 0; b=0o_32; c=0x_f_f; d=10_000_000; e=10_00000
print(a, b, c, d, e)
type(a), type(b), type(c), type(d), type(e)

# %%
100_0000 == 1000000, 1_0_0 == 100

# %% [markdown]
# 뒤에서 보겠지만 너무 큰 수를 표기하기 위해 지수법을 사용한다. 파이썬에서 지수법을 사용하여 수를 표기할 경우 그 수는 실수형으로 인식된다. 만약 정수형으로 바꾸고자 한다면 `int()`로 정수형으로 변환해준다.

# %%
print(12.3e7, 12.30e7)

# %%
print(int(12.3e7), int(12.30e7))

# %% [markdown]
# 하지만 실수형의 할당은 (많은 경우) 정확한 값이 할당되지 않는다는 점을 유의해야 한다. 예를 들면 `1.1e+300`은 정확하게 1.1e+300이 아니고, 따라서 `int(1.1e+300)`를 하면 생소한 수가 나타난다

# %%
int(1e+300)

# %% [markdown]
# 정확한 1e+300은 뒤에서 배울 문자열을 활용하여 다음과 같이 쓸 수 있다.

# %%
int('3'+'0'*300)

# %% [markdown]
# #### 실수형(`float`)
#
# 소수점이 포함된 수는 소수점 이하가 없거나 소수점 이하가 `0`으로만 되어 있어도 소수로 인식한다(예. `1.`, `1.0`). `1.4e-7`은 $1.4 \times 10^{-7}$을 의미한다. `e`는 대문자 `E`로 써도 된다. `2.10e4` 또는 `2.10e+4` 또는 `2.10E4` 또는 `2.10E+4`는 모두 $2.10 \times 10^4$를 의미한다. `e` 앞에는 실수, `e` 뒤에는 **정수**를 써야 한다. 원주율 $\pi$는 `math` 모듈의 변수 `pi`에 저장되어 있다.

# %%
import math
#x = (0., 1.0, 0.45, 1e-7, 1E-7, math.pi, math.exp(1))
#types_list(x)
a = 0.; b=1.0; c=0.45; d=1e-7; e=1.4E-8; f=math.pi; g=math.exp(1)
print(a,b,c,d,e,f,g)
type(a), type(b), type(c), type(d), type(e), type(f), type(g)

# %% [markdown]
# #### 복소수형
#
# 복소수형은 `a+bj`로 쓴다. 이때 `a`와 `b`는 실수형 수이다.

# %%
a = 0+0j; b = 1+4j; c = 1.4 + 3j
print(a,b,c)
type(a), type(b), type(c)

# %% [markdown]
# 여기서 문제! `a=3.2; b=-2.5`일 때 `3.2-2.5j`를 어떻게 표현해야 할까?

# %%
a =  3.2
b = -2.5

# %%
a - b j


# %%
a - b*(1j)

# %% [markdown]
# `bj`로 쓰면 변수명 `bj`로 구분이 되지 않으며 `b*j`로 써도 변수 `b`와 변수 `j`를 곱하는 것과 구분이 되지 않는다. `j`를 허수로 쓸 수 있는 이유는 `j` 앞에 숫자가 오기 때문이다. 그래서 `j`는 변수명 `j`를 의미하고 `1j`는 허수 $i$를 의미하게 된다.

# %%
j = 3

# %% [markdown]
# 위와 같이 `j=3`을 했을 때 `j`은 3을 저장하고 있으며, `1j`는 허수 $i$를 의미한다. 

# %% [markdown]
# #### 논리형
#
# `True`, `False`는 참/거짓을 의미한다. 앞에서 살펴봤듯이 `True`, `False`는 파이썬의 키워드이기 때문에 변수 이름으로 사용할 수 없다.

# %%
a = True; b = False
print(a,b)
type(a), type(b)

# %%
True = 3


# %% [markdown]
# #### 문자열형
#
#

# %% [markdown]
# 문자열 값은 `"`(큰 따옴표) 또는 `'`(작은 따옴표)를 사용한다. 예를 들어 알파벳의 첫 세 글자 abc를 나타낼 때, 그냥 `abc`라고 쓰면 변수 `abc`를 나타낸다(`abc`라는 변수에는 어떤 값도 저장될 수 있다). 문자열 abc는 `"abc"`라고 써야 한다. 파이썬에서는 "string literal"이라고 표현한다. 문자열 상수라고도 표현한다(`"abc"`는 언제나 알파벳 소문자 a,b,c가 이어진 세 문자를 가리킨다).
#
# 큰 따옴표 또는 작은 따옴표로 문자 상수를 나타낼 때, 직접 입력하기 힘든 문자들도 있다. 이런 문자를 위해 탈출 문자(escape character)를 사용한다. 파이썬에서 `\`는 탈출문자로 뒤에 오는 문자(들)과 합쳐 새로운 문자를 의미한다. 예를 들어 `'\r'`은 `\`(백슬래쉬)와 `r`(알파벳 알)의 두 문자가 아니라 합쳐져서 하나의 문자(C**R**; Carriage **R**eturn)을 의미한다. 탈출문자는 특히 제어문자를 나타내기 위해 사용한다. 그밖의 제어문자로는 `"\a"`(Beep), `"\b"`(**b**ackspace), `"\n"`(**n**ewline), `"\r"`(carriage **r**eturn), `"\t"`(**t**ab) 등이 있다. 

# %% [markdown]
# 시작과 끝을 `"` 따옴표로 할 경우 따옴표 사이에 문자 따옴표를 사용하면 문자열의 끝을 의미하는 따옴표와 구분이 되지 않기 때문에 탈출문자를 써서 `"\""`로 표기한다. 문자 백슬래쉬 역시 비슷한 이유로 `"\\"`로 쓴다. 
#
# 탈출 문자로 표기할 수 있는 제어 문자는 대여섯개에 불과하다. 그에 비해 자주 사용되지 않는 제어문자, 키보드로 입력할 수 없는 문자들도 많다. 키보드로 입력해도 폰트가 없어서 화면에 출력되지 않을 수도 있다. 가장 확실한 방법은 문자에 해당하는 코드(수)를 적어주는 것이다. 편의를 위해 코드는 16진수, 8진수 등의 다양한 방법으로 지정해 줄 수 있다.
#
# `"\x41"`은 16진수 41에 해당하는 문자, `"\101"`은 8진수 101에 해당하는 문자를 나타낸다. 대부분의 컴퓨터에서 16진수 41에 해당하는 문자는 `'a'`이다. 그냥 `a`를 사용하지 왜 `\x41` 또는 `\101`을 사용하느냐고? 이 방법은 어떤 문자에도 사용할 수 있다. 예를 들면 `"\n"`(newline)은 `"\x0a"` 또는 `"\012"`로 쓸 수 있다. 왜냐하면 newline에 해당하는 문자가 ASCII(아스키) 코드에서 10번에 해당하기 때문이다(10진수 10은 16진수로 0a, 8진수로는 12이다).
#
# 유니코드 문자는 문자마다 이름이 있다. INVERTED EXCLAMATION MARK라는 유니코드 이름(label)을 가진 문자는 `"\N{INVERTED EXCLAMATION MARK}"`로 나타낸다. "\uxxxx"는 유니코드 코드 포인트가 16진수 0000xxxx인 문자, "\UXXXXXXXX"는 유니코드 코드포인트가 16진수 XXXXXXXX인 문자를 나타낸다. 
#
# `\x`과 `\u`, 그리고 `\U`는 뒤에 오는 문자 몇 개를 문자 코드(문자에 대응하는 코드)로 읽을 것인지에서 다르다. `print('\u0041')`을 해보자. `print('\x0041')`과 어떻게 다른가? 이에 대한 자세한 사항은 문자열 관련 장(???)에서 다룬다.

# %%
print('\u0041')

# %%
print("\x0041")

# %% [markdown]
# 마지막으로 큰 따옴표 또는 작은 따옴표 안에서 **백슬래쉬를 탈출 문자로 쓰지 _않고_** 문자 그대로 사용하려면 큰 따옴표 또는 작은 따옴표 앞에 `r`이라는 문자를 덧붙인다. 예를 들면 `r'\n'`라고 쓰면 newline 문자 하나가 아니라 백슬래쉬(`\`)와 알파벳 소문자 엔(`n`)으로 구성된 두 문자를 의미한다. 만약 백슬래쉬가 많이 포함된 문자열을 따옴표 안에 적으려면 이중 백슬래쉬(`\\`)를 써야 한다. 따옴표 안에 백슬래쉬가 지나치게 많아져 문자열을 읽기가 쉽지 않을 때 도움이 된다. 예를 들어 `C:\Windows\Temp`를 의미하기 위해 따옴표를 써서 `"C:\\Windows\\Temp"`로 나타내야 할 문자열을 `r"C:\Windows\Temp"`로 쓸 수 있다.

# %%
a = "Letter"; b='1'; c='"Hello?", says he'; d = r"Hi?\tHello?"
e = '\'This is great.\''
f = 'a'; g ='\r'; h='\x41'; i='\101';
j = "\N{INVERTED EXCLAMATION MARK}" 
k = "\u0041"; m= "\U00000041" # 여기서 왜 변수이름 l을 쓰지 않았을까?
print(a,b,c,d,e,f,g,h,i,j,k,m)
type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j), type(k), type(m)

# %% [markdown]
# 그 밖에 `builtins` 모듈의 데이터 타입에는 포함되어 있지 않지만, 데이터 분석에 자주 사용되는 데이터형에는 **범주형**, **날짜시간형**이 있다. 

# %% [markdown]
# ### 범주형과 날짜시간형

# %% [markdown]
# #### 범주형

# %% [markdown]
# 범주형은 특정한 값(수준)만을 가질 수 있는 값이다. 예를 들어 "커피를 드릴까요? 아니면 차를 드릴까요?"라는 질문에 대답은 "커피" 또는 "차"만 가능하다. 이때 질문의 답을 범주형으로 생각할 수 있다. **범주형**에는 수준 사이에 우위 또는 선후가 없는 **명목형**(nominal)와 "저", "중", "고"처럼 수준 사이에 비교가 가능한 **순위형**(ordered)으로 나뉜다. 
#
# 여기서는 여러 용도로 쉽게 사용할 수 있는 `pandas`의 `Series`에서 `dtype='category'`로 설정하여 범주형 또는 순위형을 사용하는 방법을 소개한다. 
#

# %%
import pandas as pd
a = pd.Series(['Coffee', 'Tea', 'Tea'], dtype='category')
print(a)

from pandas.api.types import CategoricalDtype
b = pd.Series(['low', 'medium', 'high', 'high', 'low'], 
              dtype = CategoricalDtype(categories=['low', 'medium', 'high'], 
                                       ordered=True))


# %% [markdown]
# 명목형 자료를 만드는 방법은 뒤에서 자주 사용할 `pd.Series()`에 `dtype='category'`만 설정하면 된다. 순위형 자료를 만드는 법은 다소 복잡하다. 복잡하게 `import`하고, 다시 다소 복잡한 과정으로 `dtype=`을 설정해야 한다. 필자라면 다음과 같은 함수를 만들어 쓸 것이다(자세한 사항은 <범주형>장에서 소개된다).

# %%
def ordered(categories):
    #print(categories)
    from pandas.api.types import CategoricalDtype
    return CategoricalDtype(categories=categories, ordered=True)

b = pd.Series(['low', 'medium', 'high', 'high', 'low'],
              dtype=ordered(['low', 'medium', 'high']))
b

# %% [markdown]
# 범주형은 컴퓨터에 자료를 저장할 때 범주 목록과 범주 따로 저장한다. 그리고 범주는 정수 코드로 변환하여 저장한다. 위에서 커피는 `0`으로 차는 `1`로 저장하는 식이다. 이런 저장 방법은 범주의 갯수가 자료의 갯수보다 작을 때 저장공간을 절약할 수 있다.

# %% [markdown]
# #### 날짜시간형

# %% [markdown]
# 날짜시간형은 여러 가지 방식으로 저장될 수 있다. 파이썬 표준 라이브러리에는 datetime 패키지가 있고, 제3자 패키지인 numpy나 pandas를 사용할 수도 있다. 여기서는 파이썬 표준 라이브러리인 datetime 패키지의 `date`, `time`, `datetime` 클래스를 사용하여 날짜형, 시간형, 날짜시간형 값을 저장해보자.

# %%
import datetime
a = datetime.date(2022, 3, 4)
b = datetime.time(19,30,0)
c = datetime.datetime(2022, 3, 4, 19, 30, 0)
print(a,b,c)
a, b, c

# %%
type(a), type(b), type(c)

# %% [markdown]
# 보통은 년, 월, 일을 한꺼번에 문자열로 저장하는 경우가 많다. 이런 경우에는 다음과 같이 날짜/시간/날짜시간형으로 변환한다.

# %%
str_date = "2022-03-04"
str_time = "19:30:00"
str_datetime = "2022-03-04 19:30:00"
v_date = datetime.datetime.strptime(str_date, "%Y-%m-%d").date()
print(v_date)
v_date


# %%
v_time = datetime.datetime.strptime(str_time, "%H:%M:%S").time()
print(v_time)
v_time

# %%
v_datetime=datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
print(v_datetime)
v_datetime

# %%

# %% [markdown]
# ### 3.2.2 변수의 데이터 타입 확인하기

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
# 파이썬(???변환???)

# 데이터타입              확인하는 함수                  변환하는 함수
# 논리(bool)             isinstance( , bool)         
# 정수                   isinstance( , int)               int()
# 실수                   isinstance( , float)             float()
# 문자                   isinstance( , str)               str()
# 범주                   isinstance( , pd.Series) and     pd.Categorical()    
# 순위범주                isinstance(x, pd.Categorical) and x.ordered
#                                                        pd.Cateogrical( , orderd=True, categories=[])
# 날짜                   isinstance( , datetime.date)     datetime.date(년,월,일)     
# 시간                   isinstance( , datetime.time)     datetime.time(년,월,일)
# 날짜시간                isinstance( , datetime.datetime) datetime.datetime(년,월,일,시,분,초) 

# %% [markdown]
# 변수에 저장된 값의 타입을 확인하기 위해서는 `isinstance()`함수를 사용한다. 만약 변수 `x`의 값이 논리형(`bool`)인지 확인하려면 `isinstance(x, bool)`로 쓴다. 만약 `x`가 논리형이라면 `isinstance(x, bool)`은 참(`True`)가 될 것이다(영문으로 Is instance `x` `bool`?와 같은 의미이다). 여기서 instance는 객체와 같은 의미라고 생각하면 된다(자세한 내용은 <클래스> 장을 참조하자).
#
# 위에서 소개한 타입은 다음과 같다. 타입을 확인하기 위해서 앞에서와 마찬가지로 `isinstance()`에 변수와 타입을 넣어 사용한다(범주형과 순위형은 약간 복잡하다).

# %% [markdown]
#
# |  자료형  |    타입(Python)   |
# |:---------|:------------------|
# |  논리형     |  `bool`         |
# |  정수형     |  `int`         |
# |  실수형     |  `flaot`         |
# |  문자형     |  `str`         |
# |  범주형     |  `pd.Series` and `.dtype=="category"` and `cat.ordered ==False`         |
# |  순위형     |  `pd.Series` and `.dtype=="category"` and `cat.ordered ==True`      |
# |  날짜형     |  `datetime.date`         |
# |  시간형     |  `datetime.time`         |
# |  날짜시간형 |  `datetime.datetime`         |

# %%
import datetime
import pandas as pd
x1 = 23; print(type(x1))
x2 = 22.3; print(type(x2))
x3 = "strings"; print(type(x3))
x4 = pd.Series(['Hi', 'Lo', 'Lo'], dtype='category'); print(type(x4))
x5 = pd.Series(['Hi', 'Lo', 'Lo'], dtype=ordered(['Hi', 'Lo'])); print(type(x5))
x6 = datetime.date(2020, 1, 1); print(type(x6))
x7 = datetime.time(9, 0, 0); print(type(x7))
x8 = datetime.datetime(2020, 1, 1, 12, 11, 11); print(type(x8))
isinstance(x1, int), isinstance(x2, float), isinstance(x3, str), \
isinstance(x4, pd.Series) and x4.dtype=="category" and x4.cat.ordered == False, \
isinstance(x5, pd.Series) and x5.dtype=="category" and x5.cat.ordered == True, \
isinstance(x6, datetime.date), isinstance(x7, datetime.time), isinstance(x8, datetime.datetime)

# %% [markdown]
# 참고로 범주형을 확인하기 위해 `pandas`의 공식문서의 추천 방법은 다음과 같다.

# %%
# pandas documentation 추천 방법 : 범주형 확인
isinstance(x4, pd.Series) and hasattr(x4, 'cat') and x4.cat.ordered == False
isinstance(x5, pd.Series) and hasattr(x5, 'cat') and x5.cat.ordered == True

# %% [markdown]
# 아래를 보면 각 조건식이 서로 다른 타입일 때에도 오류를 발생시키지 않고 잘 작동하고 있음을 보여준다(이 부분은 뒤에서 리스트를 배운 후에 봐야 이해할 수 있다).

# %%
lst = [x1, x2, x3, x4, x5, x6, x7, x8]
for x in lst:
    print(isinstance(x, int), # 정수형인가?
          isinstance(x, float), # 실수형인가?
          isinstance(x, str), # 문자열인가?
          isinstance(x, pd.Series) and x.dtype=="category" and x.cat.ordered == False, # 명목형인가? 
          isinstance(x, pd.Series) and x.dtype=="category" and x.cat.ordered == True,  # 순위형인가?
          isinstance(x, datetime.date), # 날짜형인가?
          isinstance(x, datetime.time), # 시간형인가?
          isinstance(x, datetime.datetime)) # 날짜시간형인가?

# %% [markdown]
# 여기서 다시 한번 유의할 점은 다음과 같다. 범주형, 순위형의 경우 파이썬의 builtins 모듈에서 제공되는 타입이 아니다. 제3자 패키지인 pandas에서 제공되는 타입이고, 다른 제3자 패키지에서 제공되는 타입을 사용하여 값을 저장할 수도 있다. 날짜형, 시간형, 날짜시간형의 경우는 파이썬 표준 라이브러리의 하나인 datetime 패키지에서 제공되는 타입이지만 효율적인 데이터 처리가 필요한 경우에는 제3자 패키지인 numpy나 pandas을 사용할 수도 있다. 그래서 `isinstance(x, datetime.datetime)`이 거짓으로 나온다고 `x`가 날짜시간형이 아니라고 확신하기 힘들다. 다음의 예를 보자.

# %%
x = pd.Series(pd.to_datetime(['2022-12-01 13:00']))
print(x)
isinstance(x, datetime.datetime)

# %% [markdown]
# 이 경우 다음과 같이 시간자료형 데이터(값)을 저장하고 있음을 확인할 수 있다. (자세한 내용은 <넘파이 배열>장에서 확인하자.)

# %%
isinstance(x, pd.Series) and str(x.dtype).startswith('datetime') # !!!???

# %% [markdown]
# 다시 한번 강조할 필요가 있다. 앞에서 말한 정수형, 실수형, 복소수형, 논리형, 문자열형, 범주형, 날짜시간형은 우리가 어떤 값을 분류한 추상적인 구분이다. 실제 컴퓨터에 저장되고, 해석되는 방식은 `int`, `float`, `complex` 등과 같은 데이터 타입이 결정한다. 정수형을 `int`로 저장할 수도 있지만 뒤에서 소개하는 넘파이 배열에서 `dtype='int'`로도 저장할 수 있다. 따라서 데이터 타입을 확인하거나 구분할 때에도 이런 다양성을 고려해야 한다. 

# %% [markdown]
# ### 데이터 타입 변환

# %% [markdown]
# 타입을 변환하는 것은 원래 타입에 따라 다른 방법을 사용해야 한다. 빌트인 타입 내에서는 동일한 함수를 사용할 수 있다. 예를 들어 `int()`는 실수형을 정수형을 변환할 때에도, 문자열형을 정수형으로 변환할 때에도 사용한다. 하지만 소수점 이하가 포함된 문자열을 바로 정수형으로 변환할 수는 없다. `int(float())`을 사용하자.

# %%
int(32.4)

# %%
int("32") 

# %%
int(float("32.4")) # int("32.4") <- Error

# %% [markdown]
# ## 3.3 연산과 함수

# %% [markdown]
# 어떤 값의 데이터 타입은 값을 저장하는 방식을 결정한다. 우리가 추상적으로 생각하는 값과 컴퓨터에 저장되는 값을 분리해서 생각할 필요가 있었다. 데이터 타입은 컴퓨터에 저장된 이진수가 어떤 의미를 갖는지를 알려준다.
#
# 데이터 타입은 가능한 연산과 적용 가능한 함수도 결정한다. 보통 연산은 같은 타입 안에서만 가능하다. 예를 들어 정수형 `123`과 정수형 `456`을 더해보자. 그 결과는 `579`가 된다. 하지만 문자열 `"123"`과 문자열 `"abc"`를 더해보자. 데이터 타입에 의해 덧셈(`+`)의 의미가 결정되고, 결과는 `123abc`가 된다. 
#
# 다시 말해 데이터 타입에 의해 가능한 함수 또는 연산이 결정되고, 그 의미도 결정된다. 여기서는 각 데이터 타입별로 가능한 연산/함수, 자주 사용하는 연산/함수를 간단하게 소개한다. 자세한 활용법은 뒤의 각 장에서 상세하게 소개할 것이다.

# %% [markdown]
# ### 3.3.1 정수(`int`)형

# %% [markdown]
# #### 3.3.1.1. 산술연산

# %% [markdown]
# 산술연산으로 별다른 라이브러리 활용없이 기본적인 사칙연산을 제공한다. 
# 가감승제, 거듭제곱, 몫, 나머지는 `+`, `-`, `*`, `/`, `**`, `//`, `%`로 쓴다.
# 우선 순위는 수학에서와 조금 다르다. 곱셈, 나누기가 덧셈, 뺄셈보다 빠른 것은 동일하다.
# 모든 산술연산의 우선 순위는 다음과 같다.
#
# |  우선 순위   | 연산자    |  내용    |
# |:---:|:-----:|:------:|
# | 1 | `**` | 거듭제곱 |
# | 2 | `*`,`/`,`//`, `%` | 곱셈, 나눗셈, 몫, 나머지 |
# | 3 | `+`, `-` | 덧셈, 뺄셈 |

# %% [markdown]
# 우선 순위를 PEMDAS라고 설명하기도 한다. 괄호(Parentheses)가 가장 우선이며, 그 다음은 거듭제곱(Exponentiation)이다. 그리고 곱셈(Multiplication)과 나눗셈(Division)이 같은 순위이고, 마지막 순위가 덧셈(Addition)과 뺄셈(Subtraction)이다.

# %% [markdown]
# 몫과 나머지는 다음의 식으로 확인할 수 있다.

# %%
15 == (15 // 4)*4 + 15 % 4

# %% [markdown]
# 내장 builtins 모듈의 `divmod()`을 사용하면 몫과 나머지를 한꺼번에 구한다.

# %%
divmod(15,4) == (15//4, 15%4)

# %% [markdown]
# #### 3.3.1.2. 비교연산
#
# 비교 연산은 크기가 같음 또는 크기의 대소를 비교한다. 그 결과는 `True`(참) 또는 `False`(거짓)이 된다.

# %%
x = 5
x < 6, x <= 6, x == 6, x != 6, x >= 6, x > 6

# %% [markdown]
# `==`은 같음, `!=`는 같지 않음을 나타낸다.

# %% [markdown]
# 파이썬의 비교 연산은 `a > b > c`와 같은 표현도 지원한다. `a > b > c`는 `(a > b) > c`와 같지 않음을 유의하자. `a > b > c`는 수학의 $a > b > c$와 비슷한 의미를 가지는데, 수학에서 "$a > b > c$"는 "$a > b$ 그리고 $b > c$"를 의미한다.[^chainedcomp] 다음의 비교 결과를 확인하자. 
#
# [^chainedcomp]: `a > b > c`는 만약 `a>b`가 거짓이라면 `b>c`를 계산하지 않고 바로 거짓을 산출한다. 이는 `and`의 특성이다.

# %%
3 > 2 == 1   # FALSE
(3 > 2) == 1 # TRUE : (3 > 2)의 결과는 TRUE, TRUE == 1은 1 == 1로 변환되어 TRUE
3 > (2 == 1) # TRUE : (2 == 1)의 결과는 FALSE, 3 > FALSE는 3 > 0으로 변환되어 TRUE

# %% [markdown]
# `a == b == c == d`와 같은 식 또는 `a > b <= c > d`와 같은 식도 `a==b and b==c and c==d`와 `a>b and b<=c and c>d`로 해석된다. 이때 `3 > 2 <= 4 > 3.5`와 같은 식도 `True`가 된다.

# %% [markdown]
# #### 3.3.1.3 할당 연산

# %% [markdown]
# `**`, `*`, `/`, `//`, `%`, `+`, `-`와 같은 기본적인 산술연산의 경우 `x=x+1`과 같이 어떤 변수의 값에 연산을 한 후 다시 변수에 넣는 작업이 자주 필요하다. 그런 경우에 다음과 같이 축약형으로 쓸 수 있다.
#
# | 기본형 | 축약형 |
# |:------:|:------:|
# | `x = x ** 2` | `x **= 2` |
# | `x = x * 2` | `x *= 2` |
# | `x = x / 2` | `x /= 2` |
# | `x = x // 2` | `x //= 2` |
# | ... | ... |
# | `x = x - 2` | `x -= 2` |
#

# %% [markdown]
# #### 3.3.1.4 비트 연산
#
# 비트 연산은 메모리에 저장된 이진수를 각 비트별로 연산을 적용한다. 예를 들어 `0b10`과 `0b11`에 대해 비트 연산 AND를 행하면, 첫 번째 수의 첫 번째 자리 `1`과 두 번째 수의 첫 번째 자리 `1`에 AND 연산을 한 결과 `1`이 결괏값의 첫 번째 자리 수가 된다. 그리고 첫 번째 수의 두 번째 자리 `0`과 두 번째 수의 두 번째 자리 `1`의 AND 결과 `0`이 결괏값의 `0`이다. 그 결과는 `0b10`이고 이를 10진수로 나타내면 `2`가 된다. 

# %%
x = 0b10
y = 0b11
x & y

# %% [markdown]
# 파이썬의 비트 연산은 다음의 기호를 활용한다.

# %% [markdown]
# |비트 연산  |   파이썬 기호|
# |:----------|:-------------|
# | NOT        | `~`   |
# | AND        | `&`  |
# | OR         | ` \| `  |
# | XOR        | `^`  |
# | SHIFT      | `<<`, `>>` |

# %% [markdown]
# 다음은 비트 연산을 실시한 결과를 보여준다.

# %%
x = 0b1100
y = 0b0111
print(type(x))
print(f'{x:04b}')      # 형식을 4자리 2진수로 
print(f'{~x :04b}')    # NOT
print(f'{x & y:04b}')  # AND
print(f'{x | y:04b}')  # OR
print(f'{x ^ y:04b}')  # XOR
print(f'{x >> 1:04b}') # SHIFT
print(f'{x >> 2:04b}') # SHIFT

# %% [markdown]
# #### 3.3.1.4 수학 함수

# %% [markdown]
# 그 밖의 다양한 수학 함수는 내장 모듈인 `math`에서 찾을 수 있다. `math.pow()`, `math.sqrt()`는 거듭제곱을 하는 함수, 거듭제곱근을 구하는 함수이다. 
# `math.pow()`, `math.sqrt()`처럼 항상 `math` 모듈을 써야 하므로 불편하게 느낄 수도 있지만, 자신만의 `pow()`, `sqrt()`를 만들어 쓸 수 있다는 장점도 있다(Zen of Python을 다시 한 번 읽어보자). 

# %%
math.pow(2,3), math.sqrt(2)

# %% [markdown]
# 지수(`math.exp()`), 로그(`math.log()`, `math.log10()`), 삼각함수(`math.sin()`, `math.cos()` 등) 등도 제공한다.

# %%
math.exp(1)
# R> exp(1)

math.log(180, 2)
# R> log(180, base=2); log2(180)

math.log(180, 10)
math.log10(180)
# R> log10(180)

math.sin(2)
# R> sin(2)

# %% [markdown]
# 모듈 `math`에는 여러 함수가 존재하므로 한번 찬찬히 살펴보자. `math`에 포함된 함수는 다음에 정의하는 `lsf`(list function)을 사용하여 출력할 수 있다. 

# %%
def lsf(module):
    import types
    if not isinstance(module, (types.ModuleType, type)):
        raise ValueError("argument should be module type")
    return [k for k, v in vars(module).items() 
            if not k.startswith('_') and callable(v) and not isinstance(v, type)] 
    # '_'로 시작하지 않는 함수 종류만 출력


# %%
# lsf(__builtins__)의 결과를 조금 정리하면
' '.join(lsf(__builtins__))

# %%
' '.join(lsf(math))


# %% [markdown]
# 다음의 `lst_doc()`은 모듈의 함수와 함수의 `.__doc__`(문서)를 같이 보여준다. 어떤 함수가 있는지 천천히 살펴보고, 어떤 함수를 어떻게 활용할 수 있을지 생각해보자.

# %%
def lsf_doc(module):
    funcs = lsf(module)
    funcs_dic = {func:vars(module)[func].__doc__ for func in funcs}
    for k,v in funcs_dic.items():
        #print(k,v.split('\n')[0])
        try:
            dochead = v.split('\n')[0]
            print(f"{k:10}: {dochead:30}")
            # SyntaxError: f-string expression part cannot include a backslash
            # 왜 backslash는 포함하지 못하나?
        except Exception as e:
            print(f"{k:10}:")


# %% [markdown]
# 모든 내장 모듈에 대해 함수와 문서 첫 줄을 출력해보면 다음과 같다.

# %%
import sys
for x in sys.builtin_module_names:
    if not x.startswith('_'):
        print('*'*(len(x)+4))
        print('* '+x+' *')
        print('*'*(len(x)+4))
        module = __import__(x)
        lsf_doc(module)
        print()

# %% [markdown]
# ### 3.3.2 실수(`float`)형

# %% [markdown]
# #### 3.3.2.1 산술연산, 비교연산, 할당연산, 수학함수

# %% [markdown]
# **산술연산**, **비교연산**, **할당연산**, **수학함수**는 정수형과 마찬가지로 실수형에도 동일하게 적용된다. **비트연산**은 실수형에 적용되지 않는다.

# %%
x = 14.1; y = 2.714e+2
x + y, x > y, math.sin(x)

# %%
x -= y; x

# %%
x >> 1

# %% [markdown]
# #### 3.3.2.2 `float`타입의 한계

# %% [markdown]
# 실수형에서 유의할 점은 실수형은 정확성에 한계가 존재한다는 점이다. 

# %%
print(math.sqrt(2)**2 == 2)
#R> sqrt(2)^2 == 2

num = math.sqrt(2)**2
print(num)
#R> print(sqrt(2)^2)

# %% [markdown]
# 0.2처럼 간단한 실수조차도 정확하지 않다. 사실 2진수로 소수점 몇 째자리까지 딱 떨어지는 값이 아닌 이상 `float` 타입은 입력한 값과 미세하게 다르다(0.5, 0.25, 0.125, 0.0625) 등은 정확하게 저장할 수 있다).

# %%
x = 0.2; y = 0.25
#y = 0.000000476837158203125
print(f'{x:.24f}')
print(f'{y:.24f}')

# %% [markdown]
# 이렇게 `float` 타입에 내재된 오차를 
# 무시하고 두 수의 크기를 비교하고자 한다면,
# `math.isclose()`를 사용할 수 있다.

# %%
a = 0.1 + 0.2
print(a, a == 0.3, math.isclose(a, 0.3))

# %% [markdown]
# 아래의 결과에서 보듯이 컴퓨터가 계산한 0.1+0.2와 직접 생성한 0.3은 $10^{-16}$보다 작은 오차가 있다.
#     

# %%
(0.1+0.2)-0.3
# 5.551115123125783e-17

# %% [markdown]
# `math.isclose()`는 이렇게 작은 차이는 무시한다. 허용 가능한 오차의 크기는 `math.isclose(a,b, *, rel_to=1e-09,, abs_tol=0.0)`의 `rel_tol=`, `abs_tol=` 매개변수로 조정가능하다.
# `rel_tol`은 relative tolerance, `abs_tol`은 absolute tolerance로 두 수의 상대적 차이, 절대적 차이를 얼마나 허용할 것인가를 결정한다

# %%
math.isclose(math.sqrt(2)**2, 2)
# R> all.equal(sqrt(2)^2, 2)

# %% [markdown]
# `math.isclose()`는 유한한 정확성의 컴퓨터로 계산을 하면서 나타나는 작은 오차를 의도적으로 무시하여`(math.sqrt(2))**2`($\sqrt{2}^2$의 근삿값)과 `2`을 거의 같다고 판단하다.

# %% [markdown]
# 계산에 의한 오차뿐 아니라 `float` 타입은 내재적으로 정확성의 한계가 존재한다. 그 정확성은 `0` 근처에서 가장 정확하고 수가 커질 수록 낮아진다.

# %%
0 == 1e-324, 0 == 1e-323 
# 0과 1e-324는 구분하지 못하고, 0과 1e-323은 구분한다.

# %%
1e300 == 1e300 + 1e283, 1e+300 == 1e300 + 1e284

# %% [markdown]
# 그리고 `float` 타입은 `int`과 다르게 한정된 크기만을 저장할 수 있다. `float`타입이 저장할 수 있는 가장 큰 값과 가장 0과 가까운 값은 다음으로 확인할 수 있다.

# %%
import sys
sys.float_info.max 

# %%
sys.float_info.min

# %% [markdown]
# #### 3.3.2.3 실수 출력 형식 지정
#
# 정수형은 항상 정확한 값이 저장되지만 실수형은 근사값이 저장되는 경우가 많다. 예를 들어 `x=0.2`조차도 소수점을 늘려가면서 출력해보면 0.2와 미세하게 차이가 남을 확인할 수 있다.
#
# 예를 들어 `x`를 소수점 20자리까지 출력해보면 다음과 같다.

# %%
x = 0.2
print(f'{x:.20f}') # .20f는 소수점 14자리까 출력하는 의미

# %%
0.20000000000000001110 == 0.2

# %% [markdown]
# 실수의 경우 출력값의 형식을 원하는대로 바꾸고 싶을 때가 많다. 대표적으로 소수점 이하의 자릿수를 정하거나 유효숫자의 갯수를 정하고 싶을 때 어떤 방법을 사용하는가? 먼저 위에서 봤듯이 소수점 이하의 숫자 갯수는 다음과 같이 정한다.  

# %%
x = 1.325; y = 13.25; z = 0.1325; u = 1.325e18; v = 0.000001325; w = 0
print(f"{x:.6f}")
print(f"{y:.6f}")
print(f"{z:.6f}")
print(f"{u:.6f}")
print(f"{v:.6f}")
print(f"{w:.6f}")

# %% [markdown]
# 만약 단순히 소수점 이하의 숫자가 아니라 유효숫자의 갯수를 정하고 싶다면 다음을 활용한다. 

# %%
print(f"{x:#.6g}")
print(f"{y:#.6g}")
print(f"{z:#.6g}")
print(f"{u:#.6g}")
print(f"{v:#.6g}")
print(f"{w:#.6g}")

# %% [markdown]
# 실수를 다양한 형식으로 출력하는 방법은 뒤(???)에서 설명된다.

# %% [markdown]
# ### 3.3.3 문자열
#
# 문자열 타입 변수를 출력하기 위해 콘솔에서 변수를 그냥 입력하거나 `print()`를 적용할 수 있다. 그냥 변수를 입력하면 따옴표 안에 문자열 내용을 보여주고, `print()`는 문자열의 탈출문자가 적용된 결과를 출력한다. 그냥 변수를 입력하여 출력된 내용은 복사를 하여 코드로 사용할 수 있다. 
#
# R 사용자라면 파이썬에서는 `print(x)`와 `x`는 R의 `cat(x)`와 `print(x)`와 비슷함을 알 수 있을 것이다. 파이썬에서 콘솔에 `x`를 치면 내부적으로 `print(repr(x))`를 수행한다.

# %%
x = "I \nDo\tLove You\N{INVERTED EXCLAMATION MARK}"
x

# %%
print(x)

# %%
print(repr(x))

# %%
y = "\"Hello\", says he.\tI can do!"
print(y)

# %%
print(repr(y))
y

# %% [markdown]
# #### 3.3.3.1 문자열 함수
#
# 다음은 몇 가지 대표적인 문자열 연산과 함수를 보여준다.
#
# |   문자열 연산 |  기호    |
# |:---------:|:-------------:|
# |   `+`    |    문자열 연결   |
# |   `*`    |    문자열 반복   |
# |   `len()`    |    문자열의 문자 갯수  |

# %%
x = "ABC" + "abc" + "123"; print(x)

# %%
x = '='*20; print(x)

# %%
len('hello?') # 문자 갯수 R> nchar()

# %%
x[:5] # 처음부터 5번째 글자 R> substring(x, 1, 5)

# %% [markdown]
# ### 3.3.3 날짜/시간 연산/함수
#
# 날짜시간/날짜/시간은 과거, 현재, 미래로 이어지는 시간의 흐름 속에 한 점을 나타낸다. 그래서 날짜 사이에는 차이를 구하는 것은 자연스러운 연산이다.
#
# 뒤에서 살펴보겠지만 날짜, 시간은 시간 흐름의 직선 위의 한 점을 다소 복잡한 방식으로 표기한다. 1분은 1초의 60배이고, 1시간은 1분의 60배이다. 1일은 1시간의 24배이고, 1주는 1일의 7배이지만, 달, 년은 일에 일정한 배를 해서 구할 수 없다(달의 길이는 달마다 다르고, 년의 길이도 년마다 다르다!). 따라서 2022년 3월 1일의 400일 후가 몇 월 몇 일, 그리고 요일이 무엇인지 쉽게 확인하기 어렵다. 하지만 파이썬은 이런 계산도 척척 박사다.

# %%
import datetime

# %%
print(datetime.date.today()) 
datetime.date.today() # 현재 날짜
# R> Sys.Date() 

# %% [markdown]
# 어떤 변수 `x`를 콘솔에 입력하여 얻은 출력 결과는 흔히 그 결과를 바로 코드로 활용할 수 있다. 예를 들어 위의 `datetime.date.today()` 결과 `datetime.date(2022, 1, 8)`은 바로 변수 `dt`에 다음과 같이 할당할 수 있다.
#
# `dt = datetime.date(2022, 1.8)`
#
# `print(x)`의 결과는 `x`의 값을 인간이 이해하기 싶게 출력하는 경향이 있다.

# %%
# 현재 날짜와 시간
print(datetime.datetime.now())
datetime.datetime.now()
# R> Sys.time() # 현재 날짜와 시간(POSIXct 형식)

# %%
# 2023년 1월 1일과 현재 날짜의 차이
a = datetime.date(2023,1,1)
b = datetime.date.today()
print(a-b)  # a-b는 datetime.timedelta 자료형을 가진다.
a-b
# Sys.Date() - as.Date("2023-01-01") 

# %%
# 2023년 1월 1일 09시 00분 00초와 현재 시간의 차이
a = datetime.datetime(2023,1,2,9,0,0)
# datetime.datetime(2023,01,02,09,00,00)으로 쓸 수 없음을 유의하자.
# 10진수 수는 첫 글자를 0으로 쓸 수 없다(0.1과 같이 1 미만의 소수 제외)
b = datetime.datetime.today()
print(a-b) # a-b는 datetime.timedelta 자료형을 가진다.
a-b
# R> as.POSIXct("2023/01/02 09:00:00")-Sys.time() 

# %%
# 현재 날짜 시간과 2022년 12월 31일 23시 59분 59초와의 차이(초 단위로)
# 파이썬 : timedelta 값은 날짜, 초, 밀리초를 days, seconds, miliseconds 속성 이용해 접근할 수 있다.
a = datetime.datetime.today()
b = datetime.datetime(2022,12,31,23,59,59)
print((a-b).seconds, "초")
# R> difftime(as.POSIXct("2022/12/31 23:59:59"), Sys.time(), units='secs')
#    R에서 units은 다음 중 하나: 'auto', 'secs', 'mins', 'hours', 'days', 'weeks'

# %%
# 2022년 3월 1의 400일 후
dt = datetime.date(2022,3,1)
dt2 = dt + datetime.timedelta(days=400)
print(dt2) # 2023년 4월 5일

# %%
dt2.strftime("%Y-%m-%d %A")


# %% [markdown]
# 2022년 3월 1일의 400일 후는 2023년 4월 5일이며 수요일이다.

# %% [markdown]
# ### 3.3.4 논리형 연산/함수

# %% [markdown]
# 논리형 연산 AND, OR, NOT 등은 파이썬에서 `and`, `or`, `not`으로 표기한다. 논리형 연산 XOR은 `(x and not y) or (not x and y)`로 쓸 수 있다. 논리형 연산 XOR은 둘 중 하나만 참일 때 참이다.

# %%
def xor(x, y):
    return (x and not y) or (not x and y)


# %%
xor(True, True), xor(True, False), xor(False, False)


# %% [markdown]
# `not`, `and`, `or`의 우선순위는 `not`, `and`, `or`이다. 따라서 위의 XOR 연산(`(x and not y) or (not x and y)`)은 우선순위만으로 괄호없이 `x and not y or not x and y`로 써도 된다.

# %%
def xor2(x, y):
    return x and not y or not x and y
xor2(True, True), xor2(True, False), xor2(False, False)

# %% [markdown]
# 정수형, 실수형 연산까지 모두 포함하면 논리형 연산 `not`, `and`, `or`은 앞에서 소개한 모든 연산 `**`, `*`, `/`, `//`, `%`, `+`, `-`보다 낮다.

# %%
(7 < 3) and (4 > 3), \
(7 < 3) or (4 > 3),  \
not (7 < 3), \
7 >= 3

# %%
# R>
#(7 < 3) & (4 > 3)
#(7 < 3) | (4 > 3)
#!(7 < 3)
#xor(T, T) # XOR
#x = NA
#isTRUE(x == 3) # robust to NAs

# %% [markdown]
# ~파이썬에는 결측치를 나타낼 수 있는 내장 타입이 없다.~ readinglist 참조. 결측값과 비슷해 보이는 `None`이라는 값이 있지만 이는 결측치라기 보다는 아예 없다는 의미가 더 적절해 보인다. (결측값은 있지만 측정을 못한 것이고, 아예 없는 것은 측정이 애초에 불가능하다. 참고로 `None == 3`은 `False`이고 `None > 3`은 타입오류`TypeError`가 발생한다.)

# %% [markdown]
# 보통은 결측치를 나타내기 위해 제3자 패키지 `numpy`의 `np.nan`를 활용한다(`import numpy as np`). 이때 계산 결과가 R과 다름을 유의하자.

# %% [markdown]
# R에서 `NA`를 포함한 거의 모든 계산 결과는 `NA`이다. 왜냐하면 어떤 값인지 모르므로 결과 또한 어떤 값인지 모르게 된다. 예를 들어 `NA==3`의 결과는 `NA`인데, `NA`가 어떤 수인지 모르기 때문이다(3일 수도, 아닐 수도 있다).
#
# 파이썬의 `np.nan`이 이와 다르게 작동한다. 다음을 보자. R이라면 모두 `NA`가 나올 논리식이 `FALSE`임을 유의하자.

# %%
import numpy as np
print(np.nan == np.nan)
print(3==np.nan)
print(math.isclose(np.nan, np.nan)) # np.isclose(np.nan, np.nan)

# %% [markdown]
# 결정적으로 다음의 결과를 보자. 뭔가 의심쩍지 않은가

# %%
(7 < np.nan) and (4 > np.nan), \
(7 < np.nan) or (4 > np.nan),  \
not (7 < np.nan), \
7 >= np.nan

# %% [markdown]
# `not(7 < np.nan)`을 풀어쓰면 `7>=np.nan`이다. 다시 말해 논리적으로 `not(7 < np.nan)`와 `7>=np.nan`의 진릿값은 항상 값다(이해가 되지 않는다면 `np.nan` 대신 어떤 수를 넣어보라. 언제나 `not(7<x)`와 `7>=x`의 진릿값은 같다. 하지만 `not (7 < np.nan)`과 `7 >= np.nan`의 진릿값은 다르다. 이런 차이를 어떻게 설명할 수 있을까? 

# %% [markdown]
# 필자가 좀더 찾아보니 오히려 실수형 연산에 대한 국제 표준인 IEEE 754에 따르면 오히려 `7 >= np.nan`와 같은 비교 연산 결과가 `False`이다. 해설에 따르면 `np.nan`와 어떤 비교에 대해서도 결과가 `False`(실패) 실패여야 한다는 것이다. 즉 `7 >= x`가 `x = np.nan`일 때 `False`(실패)인 것은 `x`가 `7`보다 작을 때에만 실행되어야 하는 무엇인가가 있을 때, `x=np.nan`이라면 `7`보다 작다는 확신이 없으므로 `False`(실패)가 된다는 의미이다. R 사용자로서, 그리고 논리학, 통계학에 조예가 있는 사람으로서 솔직히 깊이 와닿지는 않는다. 컴퓨터 공학만의 **표준**인 듯 하다(컴퓨터 공학만의 어떤 특수성이 있는지는 잘 모르겠다). 어쨋든 뭔가 성공과 실패를 반드시 결정해야 하는 경우에 `np.nan`를 성공으로 처리할 순 없을 것이다. 
#
# https://en.wikipedia.org/wiki/NaN

# %% [markdown]
# 이런 점에서 파이썬의 `x==3` 또는 `x<3`은 R의 `isTRUE(x==3)` 또는 `isTRUE(x<3)`과 비슷하다고 생각할 수 있다. 

# %% [markdown]
# 만약 `x`와 `y`를 비교할 때 `np.nan`을 고려하여 R과 비슷한 결론을 얻어 내고 싶다면 다음의 `eq()` 함수를 활용하자. `np.nan`이나 `None`과 같이 결측값을 나타내는 값을 비교하면 결과는 `np.nan`이 된다.

# %%
import pandas as pd
def eq(a,b):
    if isinstance(a, np.ndarray):
        a = pd.Series(a)
    if isinstance(b, np.ndarray):
        b = pd.Series(b)
    vnan = pd.isna(a) | pd.isna(b) # numpy일 수 있으니 bool이 아닐 수 있다..
    res = a == b
    if isinstance(vnan, pd.Series):
        res[vnan] = np.nan
        return res
    elif vnan:
        return np.nan
    else:
        return res


# %%
eq(1,1), eq(1.4, 1.4), eq(1+3j, 1+3j), eq(True,True), eq('equals', 'equals')

# %%
eq(1,0), eq(1.4, 1.45), eq(1+3j, 1+2.5j), eq(True, False), eq('equals', 'equal')

# %%
eq(1,np.nan), eq(np.nan, 1.4), eq(1+3j, np.nan), eq(np.nan,True), eq('equals', np.nan)

# %%
eq(None,0), eq(1.4, None), eq(None, 1+2.5j), eq(True, None), eq(None, 'equal')

# %%
eq(np.nan, np.nan), eq(None, None)

# %% [markdown]
# 하지만 `3 > np.nan`과 같은 경우에는 여전히 결괏값이 `False`이다!

# %% [markdown]
# ### 3.3.5 데이터 타입에 따른 연산과 함수 정리

# %% [markdown]
# | 연산 기호 | 연산 종류 | 
# |:--------:|:---------:|
# |   x`**` y |   거듭제곱  |
# | `+`x, `-`x, `~`x | **단항** 연산 |
# |  x`*` y, `/`, `//`, `%` | **산술**연산(곱셈, 나눗셈 등)  |
# |  x `+` y, `-`          | **산술**연산(덧셈, 뺄셈) |
# | `<<`, `>>`             | **비트** 연산 SHIFT |
# | `&`             | **비트** 연산 AND |
# | `^`             | **비트** 연산 XOR |
# | `\|`             | **비트** 연산 OR |
# |  `<`, `<=`, `==`, `>=`, `>`, `!=` | **비교** 연산 |
# |  `not`          | **논리** 연산 NOT |
# |   `and`         | **논리** 연산 AND |
# |   `or`         | **논리** 연산 OR|
#
#
#

# %%
# !!!
# 데이터 타입          대표적인 연산과 함수 
# 숫자(numeric)         ^(**), *, /, +, -, <, ==, >, exp(), log()
# 문자(character)         nchar(), paste(), substring()
# 날짜(Date)            Sys.Date(), -, difftime()
# 날짜시간(POSIXct)      Sys.time(), -, difftime()
# 논리(logical)          &, |, !, xor(), &&, ||

# %%
# !!!
# 데이터 타입                 대표적인 연산과 함수 
# 실수(float)                 **, *, /, +, -, <, ==, >, math.exp(), math.log()
# 문자(str)                   len(), .count(), .find(), index(), .join(), .upper(), .lower(), .split()
# 날짜(datetime.date)         datetime.date.today(), -
# 시간(datetime.time)         -
# 날짜시간(datetime.datetime)  datetime.datetime.now(), -
# 논리(bool)                  not, and, or
