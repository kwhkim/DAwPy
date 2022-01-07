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
# **변수 이름**은 사용자가 맘대로 정할 수 있지만, 몇 가지 제약이 있다. 왜냐하면 `3`이나 `"A"`와 같은 이름을 지으면 숫자 `3` 또는 문자열 `"A"`와 구분할 수 없기 때문이다. 
#
# 변수를 결국 어떤 값을 저장하기 위해서 존재한다. 컴퓨터 메모리에 저장할 수 있는 값은 0과 1, 그리고 이들로 구성된 이진 정수뿐이다. 그리고 다른 값들은 모두 이진수와 대응을 통해 우리가 새로운 의미를 부여한 것이다. 예를 들어 $0041_{(16)}$은 문자 `"A"`와 대응시키거나 실수 $0.5$에 대응시킬 수 있다(문자와의 대응처럼 간단하게 이해할 수 있는 경우도 있고, 실수와의 대응처럼 복잡한 관계에 의해 결정되는 경우도 있다). 이때 컴퓨터 메모리 상의 이진수를 어떻게 해석하느냐는 **데이터 타입**이 결정한다. 데이터 분석에서 자주 쓰이는 타입은 숫자, 문자, 범주, 논리, 날짜 등이 있다. 
#
# 값의 타입이 달라지면 이 값에 **적용할 수 있는 연산과 함수**도 달라진다. 수 2은 제곱을 하거나 다른 수와 더할 수 있다. 반면 문자 `"2"`는 다른 문자와 더할 수 없다. 문자는 다른 문자와 연결하는 것은 자연스럽다. 
#
# 어떤 값에 연산을 적용했을 때 결과를 산출할 수 없는 경우도 있다(예. 1/0). 또는 값을 측정하였지만 값이 중간에 분실되든지 등의 이유로 값을 알 수 없는 경우도 있다. 이런 특수한 결과를 어떻게 표시하는가? **결측값, 무한을 나타내는 특별한 값**에 대해 알아보자.

# %% [markdown]
# # 3. 파이썬의 변수, 자료형, 연산/함수
#

# %% [markdown]
# ## 3.1 파이썬의 변수
#
# 파이썬의 변수는 어떤 값도 저장할 수 있다. (사실 엄밀히 말하면 파이썬의 변수는 어떤 값을 가리키는 지시자일 뿐이다. 예를 들어 `x=3`을 하면 변수 `x`는 수 `3`을 가리킨다. 하지만 이번 장에서는 변수에 값이 저장된다고 무방하다. 뒤에 클래스, 인스턴스, 가변객체를 다룰 때에는 엄밀한 설명이 필요하다.)

# %% [markdown]
# ## 3.1.1 변수 이름
#
# > 수학에서 미지수는 $x$, $y$ 등으로, 상수는 $a$, $b$ 등으로 쓴다. 그리고 $\sum_{i=1}^{10} i^2$와 같이 $\sum$을 쓸 때는 $i$, $j$ 등으로 쓴다. **컴퓨터 언어의 변수**는 $\sum_{i=1}^{10} i^2$의 $i$와 비슷하다. 그런데 미지수를 꼭 $x$, $y$ 등으로 써야 하는 것은 아니다. 미지수에 $a$나 $i$를 사용한 $a+4=3$ 이나 $i-1=4$와 같은 방정식은 유효하다. 단지 미지수를 나타낼 때 $x$, $y$, $z$와 같은 문자를 쓰는 것이 관례이기 때문에 미지수를 $x$, $y$ 등으로 쉽게 이해할 수 있다. 다시 말해 가독성(readability)이 높아진다.

# %% [markdown]
# * 파이썬에서 변수 이름은 알파벳, 숫자, `_`(밑줄; underbar)를 사용하여 구성할 수 있다. (사실 알파벳뿐 아니라 한글과 같이 다른 나라 문자도 변수 이름에 사용할 수 있지만 권장하지 않는다. 특히 파이썬 표준 모듈은 변수 이름에 ASCII의 문자만 사용한다.) 그리고 대소문자를 구분한다.
# * R과 달리 `.`(점; dot)은 사용할 수 없다. 왜냐하면 파이썬에서 `.`은 특별한 기능(클래스의 속성을 나타내거나, 모듈의 변수를 나타내는 등)을 위해 사용되기 때문이다. 
# * 변수의 첫 글자로 숫자를 쓸 수 없다. (만약 첫 글자로 숫자를 허용한다면 `3j`는 변수인가 허수 $3i$인가?)
# * 파이썬의 예약어는 변수 이름으로 쓸 수 없다. 다음은 파이썬 3.8의 예약어 목록이다. 예약어 목록은 파이썬 표준 모듈 `keyword`의 `kwlist`에서 확인할 수 있다(혹시라도 다른 버전의 예약어를 확인하고 싶다면 말이다).
#
# ```
# from import 
# None False True 
# del in is
# not and or
# if else elif 
# for while finally 
# pass continue break
# with as 
# try except raise
# class def lambda global nonlocal return yield 
# assert
# async await
# ```
#
# * 파이썬에서 `_`로 시작하는 변수이름은 보통 내부용 변수에 사용한다(예. 클래스 또는 모듈의 내부에 존재하지만 외부에는 알리기 싫은 변수. 클래스와 모듈 작성에서 자세히 설명된다).

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
# 변수 이름 짓기는 언어마다 관례(convention)가 다르고, 회사마다, 그리고 개인마다 다를 수 있다. 보통 어떤 프로젝트를 시작한다면 사람들 사이의 혼동을 줄이기 위해 이름을 짓는 방식을 정하기도 한다. 그럼에도 거의 항상 적용되는 법칙은 대문자로만 이루어진 변수는 상수를 의미한다는 것이다(변수가 상수를 의미한다? 그 이름은 실제 상수일 수도 있고, 변수이지만 결코 수정을 하지 않겠다는 의미이기도 하다).
#
# * 가장 간단한 변수 이름은 알파벳 한 글자를 사용한다. `x`, `y`, `i`, `j` 등. 만약 현재 **관심의 대상**이 분명하거나, **한번 쓰고 버릴 변수**(예. `for` 문의 루핑(looping) 변수)라면 한 글자로 쓰는 것이 편하다. 한글자로 변수 이름을 지으면 가능한 변수의 갯수가 너무 한정적이라는 단점이 있다. 그리고 소문자 엘(`l`), 대문자 아이(`I`), 대문자 오(`O`)는 쓰지 않는 것이 좋다. 일(`1`) 또는 영(`0`)과 구분이 힘들기 때문이다.
#
# * 단어 사이를 연결할 때 바로 붙여 쓸 수 있다. 하지만 이 방법은 대체로 권장되지 않는다. 왜냐하면 단어의 구분이 힘들기 때문이다. 하지만 두 단어 정도라면 용인할 수 있을 것이다.
#
# * 단어 사이를 연결할 때 구분을 위해 `_`을 단어 사이에 추가하거나, 단어를 소문자로 쓰고, 첫 문자만 대문자로 쓰는 방법이 있다. `_`를 사용하는 방법을 snake_case(밑줄방법)이라고 하고, 단어의 첫 글자를 대문자로 쓰는 방법을 CamelCase 또는 CaptializedWords(CapWords)라고 부른다. 파이썬에서는 밑줄방법이 대세인 듯하다. 하지만 파이썬 표준 모듈을 봐도 한 가지 방법으로 통일되어 있지 않다.
#
# * 공통적인 성격(위의 예에서 수입)의 변수를 모아 이름을 짓기도 한다. 예를 들어 수입에 관한 변수라면 공통점을 앞에 적고 밑줄을 긋고 변수 이름을 적는 방식이다. `income_lastmonth`, `income_thismonth` 또는 `income_LastMonth`, `income_ThisMonth`와 같이 밑줄 뒤의 변수 이름은 다시 여러 방식을 사용할 수 있다. 하지만 파이썬에서는 이런 경우 클래스를 만들어서 `income.lastmonth`, `income.thismonth`와 같이 쓸 수 있기 때문에 자주 활용되지 않는 듯 하다.
#
# * 변수의 타입을 공통점으로 사용하기도 한다. 예를 들어 수입이 문자열로 저장되어 있는 변수와 수로 저장되어 있는 변수가 있다면 `num_income`, `str_income`으로 이름을 짓는 방식이다.
#
# * 던바(dunbar; double underbar)로 시작하고 끝나는 변수 이름에 대해서는 뒤에 설명된다.

# %% [markdown]
# 우리가 이번 장에서 사용하는 수, 문자열, 범주, 논리, 날짜시간과 같은 값(데이터)에 대해서는 **소문자를 사용하고 밑줄로 단어를 연결하는 방식**이 가장 많이 쓰인다. 다른 종류의 값(또는 객체)에 대해서는 다른 방식이 이름이 쓰인다. 이에 대해서는 후에 설명된다.
#
# 그리고 **예약어와 같은 단어**를 써야 할 경우에는 보통 뒤에 밑줄을 붙이는 방식을 사용한다. 예를 들어 from이라는 단어를 써서 변수 이름을 사용하고 싶다면 `from_`를 사용하거나 동의어를 사용한다. 예를 들어 R에서는 `seq(from=, to=)`과 비슷한 역할을 하는 파이썬 함수 `range()`는 매개변수로 `start=`, `stop=`을 사용한다. 
#
# 다음은 파이썬에서 여러 방식의 변수 이름을 사용하는 예를 보여준다. 주석 처리된 부분은 파이썬에서 사용할 수 없는 이름이 사용된 경우로 `SyntaxError` 또는 `NameError`가 발생한다.

# %%
myAge = 22
year = 2018
day_of_Month = 3 #Alphabets, numbers, '_'
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
# ## 3.1.2 변수 할당

# %% [markdown]
# 변수 할당을 위해서는 `=`를 사용한다.
# `a=b=3`와 같이 여러 변수에 연쇄적으로 할당할 수도 있다.
#
# R과 다르게 `<-` 또는 `->`를 사용할 수 없다.
# !!!R과 다르게 별칭(alias)이란 말도 자주 쓰이는 데 이에 대해서는 다음 장에서 설명된다. (별칭이란 변수가 가리키는 대상이 동일한 경우에 또다른 이름이란 뜻이다. 이번 장에서는 별칭이 사용되지 않는다.)
#

# %%
a = 3
b = 2
# d <- -1
d = -1
# e1 <- e2 <- 7 : R에서만 가능
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
# 이 방식은 튜플 언패킹(unpacking)이라고 부른다. 좀 더 자세히 설명하자면 `a, b= 3,"three"`는 `(a,b) = (3,"three")`와 같은 의미이다.[^op1] 그리고 `(3, "three")`를 파이썬은 튜플이라는 하나의 데이터로 취급하기 때문에 가능한 일이다. 튜플은 다음 장에서 소개된다. 우선은 `a, b=3, 4`와 같이 여러 값을 여러 변수에 한꺼번에 할당하는 방법이 존재하며 이것이 가능한 이유는 `,`의 연산 순위가 `=`보다 빠르기 때문이라는 점을 기억하자(만약 `=`의 연산이 `,`보다 빠르다면, `a,b=3,4`는 `a, (b=3), 4`로 해석될 것이다).
#
# [^op1]: 이런 식의 해석이 가능하려면 `,`의 연산 순위가 `=`보다 빨라야 한다.

# %% [markdown]
# 다음은 변수 hzC5, hzD5, hzD5에 (5번째 옥타브) 도,레,미의 주파수 523.25, 587.33, 659.25를 할당한다.

# %%
hzC5, hzD5, hzE5 = 523.25, 587.33, 659.25
# hzC5=523.25; hzD5=587.33; hzE5=659.25
print(hzC5); print(hzD5); print(hzE5)

# %% [markdown]
# 만약 변수 이름이 문자열 변수에 저장되어 있다면 어떻게 할당해야 하나? 예를 들어 `varname`에 `"myVar"`이라는 값이 저장되어 있다면 `myVar=10`을, `varname`에 `"amount"`가 저장되어 있다면 `amount=10`를 해야 한다면? R에서는 쉽게 `assign(varname, 10)`을 하면 되지만 파이썬에서는 쉽지 않다. 이 장의 마지막에 R의 `assign`과 같은 기능을 하는 함수를 몇 개 정의하여 소개하였다. (간단하게 설명하면 `globals()[varname] = 10`으로 쓴다.)

# %%
globals()

# %% [markdown]
# ## 3.1.3. 변수관리

# %% [markdown]
# ### 변수의 존재 확인

# %% [markdown]
# 사용 가능한 변수의 목록은 `globals()`로 확인 가능하다. (이때 사용 가능한 변수의 목록은 맥락 의존적이다. 현재 모듈에서 사용 가능한 변수와 다른 모듈에서 사용가능한 변수가 다르고, 함수 밖에서와 함수 안에서, 그리고 객체 안에서, 밖에서 사용 가능한 변수가 다르다.) 여기서는 현재 모듈의 어떤 함수 또는 객체에 속하지 않는 가장 최상의 수준에서의 가능한 변수 목록을 출력한다. 특정한 맥락을 가정할 경우에는 `locals()` 또는 `vars()`를 써서 사용 가능한 변수 목록을 확인할 수 있다.)
#
# `globals()`의 결과는 다음 장에서 소개될 딕 형태로 제공된다. 만약 변수 이름만 확인하고 싶다면 `globals().keys()`를 사용한다.

# %%
globals()

# %%
globals().keys()


# %% [markdown]
# 목록을 살펴보면 우리가 위에서 할당했던 변수들을 확인할 수 있다. 그 밖에서 `__`(dunbar; **d**ouble **un**der **bar**)로 시작하고 끝나는 변수를 볼 수 있다(`__name__`, `__doc__`, `__package__`, `__loader__`, `__spec__`). 이들은 거의 모든 모듈에서 자동적으로 생성되는 변수로 사용자가 수정하지 않는게 좋다. 그 외에 `__builtin__` 또는 `__builtins__`는 모두 파이썬 내장 모듈 중 `builtins`라는 모듈을 가리킨다. 
#
# 주피터 노트북(jupyter notebook)에서 사용할 경우 `_i1`, `_i2`와 같은 변수들도 보인다. 이 변수는 셀의 결과를 담고 있다(셀의 왼쪽을 보면 `In [1]:`, `Out[1]:`과 같이 몇 번째로 계산된 셀임을 나타내는 표식이 있다. `Out[1]`의 결과는 `i_1`에도 저장된다). 쥬피터 노트북에서 `In`과 `Out`은 가장 최근 셀의 입력과 출력을 가리킨다. `exit`와 `quit`은 파이썬의 가장 기본적인 함수이다. 파이썬 콘솔에서 `exit()` 또는 `quit()`으로 파이썬 콘솔을 종료할 수 있다.

# %% [markdown]
# 특정 변수의 존재 여부를 확인하고자 한다면 `in globals().keys()`를 쓸 수 있다. 만약 변수 `x`가 존재하는지 확인하고자 한다면 `"x" in globals().keys()`라고 쓴다. 

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

# %%
dir()

# %% [markdown]
# ### 변수 제거

# %% [markdown]
# 특정한 변수를 제거하려면 `del` 문을 사용한다. 변수 `a`를 제거하고자 한다면 `del a`라고 쓴다(`del(a)`도 가능하다). 여러 변수를 한꺼번에 제거하고자 한다면 `del a, b, c`와 같이 쓸 수도 있다(`del(a,b,c)`도 가능하다).

# %%
a = 3; b=4; c=5
del a, c
'a' in globals().keys(), 'b' in globals().keys(), 'c' in globals().keys()

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
def del_all(types='all'):
    if types != 'all' and not isinstance(types, tuple):
        raise ValuerError("types should be either 'all' or tupe of types")
    varnames = set(globals().keys()) # 제거할 변수
    # 맥락에 따라 globals().keys()를 locals().keys(), dir() 등으로 교체할 수 있다.
    varnames = varnames.difference({'exit', 'quit', 'get_ipython', 'delall', 'globals_user', 'builtins', 'In', 'Out'})
    varnames_underbar = [varname for varname in varnames if varname.startswith('_')]    
    varnames = varnames.difference(set(varnames_underbar))    
    if types == 'all':
        for varname in varnames:
            del globals()[varname]
    else:
        for varname in varnames:
            if isinstance(globals()[varname], types):
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
# globals()                       모든 객체 나열
# 'x' in globals().keys()         변수이름 `x`가 존재하는가?
# del_all()                       모든 객체 제거(_으로 시작하는 변수이름 등 예외)
# del x                           변수이름 'x' 제거
# type(x)                         객체 x의 데이터 타입(뒤에 설명된다)
#                                 모든 객체 저장
#                                 .RData 에 저장된 객체 불러오기

# %% [markdown]
# # 3.2 파이썬의 데이터타입(자료형)

# %% [markdown]
# # 3.2.1 데이터타입(Data types)

# %% [markdown]
# 프로그래밍에서 가장 기본적인 변수 타입(`type`)에 대해 얘기해 보자.

# %%
print(type(3), type(3.0))

# %% [markdown]
# 사람에게 $3$ 또는 $3.0$은 모두 정수 $3$을 의미한다(물론 정수는 실수이기도 하다. 어쨋든 둘은 표기의 차이만 있을 뿐 같은 값을 나타낸다). 컴퓨터 언어에서 타입이란 주어진 정보를 어떻게 메모리에 저장하고, 또 메모리의 내용을 어떻게 해석할지를 결정한다(메모리에 저장되는 것은 항상 0과 1, 그리고 이들의 조합일 뿐이다). 예를 들어 정수 $3$은 이진수 00000010으로 저장된다. 반면 실수(`float`)형 $3.0$은 이진수로 저장되지만 기수와 지수로 나뉘어 (0010, 0000)로 저장된다. 그리고 메모리의 이 내용은 $0010_{(2)}\times 2^{0000_{(2)}}$으로 해석된다. 이를 10진법으로 고쳐 쓰면 $3.0 \times 10^0$이 된다.

# %% [markdown]
# 이렇게 컴퓨터가 저장하는 어떤 값에는 타입이 있다. 가장 대표적으로 정수형 `3`, 실수형 `3.0`, 문자열 `"three"`을 생각할 수 있다. 이들은 모두 메모리에 0과 1로 저장된다.[^store1] 그리고 이들은 모두 변수에 저장될 수 있다.
#
# 그런데 많은 언어가 일단 변수의 타입을 선언해야 변수를 사용할 수 있다. 예를 들어 C에서 `int my_var`라고 하면 정수타입의 변수 `my_var`를 선언한 것이다. 이는 변수 `my_var`를 사용하겠다. 그리고 이 변수에는 정수형만을 담겠다는 의미이다.
#
# 이에 반해 파이썬에서는 변수를 선언할 필요가 없다. 선언을 하지 않고 `my_var = 3`과 같이 바로 변수를 사용한다. 그리고 변수의 타입은 이렇게 변수에 어떤 값을 저장하느냐에 따라 달라진다.[^store2] 따라서 **동적 타입 언어**라고 한다. 변수의 타입이 고정적이지 않고 변할 수 있다. 
#
# 이제 변수에 대해 얘기해 보자. 
#
# [^store1]: 정확히 얘기하면 저장하는 것이라 아니라 변수가 해당 값(객체)를 가리킨다. 하지만 앞에서 얘기했듯이 이 장에서는 저장된다고 생각하겠다.
#
# [^store2]: 정확히 얘기하면 변수를 객체를 가리킬 뿐이고, 객체에 타입(클래스)이 존재한다. 이 얘기가 생소하다면 이 각주도 당분간 무시하자.

# %% [markdown]
# 파이썬의 기본적인(내장 모듈에서 정의된) 데이터 타입은 https://docs.python.org/ko/3.8/library/index.html 에서 확인할 수 있습니다. `dir(__builtins__)`을 통해서도 모듈 빌트인(`builtins`)에 정의된 클래스나 함수를 확인할 수 있습니다. 앞에서 설명했듯이 내장 모듈에 정의된 클래스, 객체, 함수 들은 파이썬 실행 후 바로 사용할 수 있습니다. 아마도 파이썬에서 `from builtins import *`를 하는 듯 합니다. 

# %%
builtins.int is int, builtins.float is float, builtins.str is str

# %% [markdown]
# 파이썬 사이트에는 숫자형(`int`, `float`, `complex`), 문자열(`str`), 시퀀스형(`list`, `tuple`), 매핑형(`dict`), 집합형(`dict`, `frozenset`) 등이 소개 되어 있는데, 이 중에 대표적인 데이터 타입은 논리형(`bool`), 숫자형과 문자열(파이썬 사이트에는 텍스트 시퀀스형이라고 표기됨)입니다.

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
# 정수형은 정수를 나타낸다. 파이썬 3+에서 정수는 최소값이나 최대값이 존재하지 않는다(메모리가 허용하는 한 매우 큰 정수 또는 매우 작은 정수를 사용할 수 있다). 정수형 수를 나타내는 방법은 `16`과 같이 10진수로 표기하는 방법과 더불어 2진수, 8진수, 16진수로 표기할 수 있다. `0b`는 2진수, `0o`는 8진수, `0x`는 16진수를 나타내기 위해 앞에 쓴다. 자릿수가 많은 숫자를 읽기 쉽게 표기하기 위해 숫자 사이에 `_`를 넣을 수 있다. 

# %%
a = 0; b=-1; c=1; d=3; e=-100; f=10_000_0_0_0; g=0b0010; h=0o32; i=0xff;
# 0, -1, 1, 3, -100, 이진수 0010, 팔진수 32, 16진수 ff
print(a,b,c,d,e,f,g,h,i) # print() 결과는 모두 10진수로 출력된다.
type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i)

# %%
# _를 사용해서 수를 좀더 쉽게 읽을 수 있는 방식으로 표기할 수 있다.
a = 0; b=0o_32; c=0x_f_f; d=10_000_000; e=1_00_0000
print(a, b, c, d, e)
type(a), type(b), type(c), type(d), type(e)

# %%
100_0000 == 1000000, 1_0_0 == 100

# %%
## 저장 
## 정확한 값, 근사값

# %%
x = 0.2
print(f'{x:.18f}')

# %%
import math
math.isclose(1e-18, 1e-19)

# %%

# %%
# R> print(x,digits=3)
# 123000, 1.23, ...

# %%
print(12.3e7, 12.30e7)

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
# 큰 따옴표 또는 작은 따옴표로 문자 상수를 나타낼 때, 직접 입력하기 힘든 문자들도 있다. 이런 문자를 위해 탈출 문자(escape character)를 사용한다. 파이썬에서 `\`는 탈출문자로 뒤에 오는 문자(들)과 합쳐 새로운 문자를 의미한다. 예를 들어 `'\r`은 `\`(백슬래쉬)와 `r`(알파벳 알)의 두 문자가 아니라 합쳐져서 하나의 문자(C**R**; Carriage **R**eturn)을 의미한다. 탈출문자는 특히 제어문자를 나타내기 위해 사용한다. 그밖의 제어문자로는 `"\a"`(Beep), `"\b"`(**b**ackspace), `"\n"`(**n**ewline), `"\r"`(carriage **r**eturn), `"\t"`(**t**ab) 등이 있다. 
#
# 시작과 끝을 `"` 따옴표로 할 경우 따옴표 사이에 문자 따옴표를 사용하면 문자열의 끝을 의미하는 따옴표와 구분이 되지 않기 때문에 탈출문자를 써서 `"\""`로 표기한다. 문자 백슬래쉬 역시 비슷한 이유로 `"\\"`로 쓴다. 
#
# 탈출 문자로 표기할 수 있는 제어 문자는 대여섯개에 불과하다. 그에 비해 자주 사용되지 않는 제어문자, 키보드로 입력할 수 없는 문자들도 많다. 키보드로 입력해도 폰트가 없어서 화면에 출력되지 않을 수도 있다. 가장 확실한 방법은 문자에 해당하는 코드를 적어주는 것이다. 편의를 위해 코드는 16진수, 8진수 등의 다양한 방법으로 지정해 줄 수 있다.
#
# `"\x41"`은 16진수 41에 해당하는 문자, `"\101"`은 8진수 101에 해당하는 문자를 나타낸다. 대부분의 컴퓨터에서 16진수 41에 해당하는 문자는 `'a'`이다. 그냥 `a`를 사용하지 왜 `\x41` 또는 `\101`을 사용하느냐고? 이 방법은 어떤 문자에도 사용할 수 있다. 예를 들면 `"\n"`(newline)은 `"\x0a"` 또는 `"\012"`로 쓸 수 있다. 왜냐하면 newline에 해당하는 문자가 ASCII에서 10번에 해당하기 때문이다(10진수 10은 16진수로 0a, 8진수로는 12이다).
#
# 유니코드 문자는 문자마다 이름이 있다. INVERTED EXCLAMATION MARK라는 유니코드 이름을 가진 문자는 `"\N{INVERTED EXCLAMATION MARK}"`로 나타낸다. "\uxxxx"는 유니코드 코드 포인트가 16진수 0000xxxx인 문자, "\UXXXXXXXX"는 유니코드 코드포인트가 16진수 XXXXXXXX인 문자를 나타낸다. 
#
# `\x`과 `\u`, 그리고 `\U`의 차이는 뒤에 오는 문자 몇 개를 문자 코드(문자에 대응하는 코드)로 읽을 것인지로 구분할 수 있다. `print('\u0041')`을 해보자. `print('\x0041')`과 어떻게 다른가? 이에 대한 자세한 사항은 문자열 관련 장(???)에서 다룬다.
#
#

# %%
print('\u0041')

# %%
print("\x0041")

# %% [markdown]
# 마지막으로 큰 따옴표 또는 작은 따옴표 안에서 백슬래쉬를 탈출 문자로 쓰지 않고 문자 그대로 사용하려면 큰 따옴표 또는 작은 따옴표 앞에 `r`이라는 문자를 덧붙인다. 예를 들면 `r'\n'`라고 쓰면 newline 문자 하나가 아니라 백슬래쉬(`\`)와 문자 엔(`n`)으로 구성된 두 문자를 의미한다. 만약 백슬래쉬가 많이 포함된 문자열을 따옴표 안에 적으려면 이중 백슬래쉬(`\\`)를 써야 하고 따옴표 안에 백슬래쉬가 지나치게 많아져 문자열을 읽기가 쉽지 않을 때 도움이 된다. 예를 들어 C:\Windows\Temp를 의미하기 위해 따옴표를 써서 `"C:\\Windows\\Temp"`로 나타내야 할 문자열을 `r"C:\Windows\Temp"`로 쓸 수 있다.

# %%
a = "Letter"; b='1'; c='"Hello?", says he'; d = r"Hi?\tHello?"
e = '\'This is great.\''
f = 'a'; g ='\r'; h='\x41'; i='\101';
j = "\N{INVERTED EXCLAMATION MARK}" 
k = "\u0041"; m= "\U00000041" # 여기서 왜 변수이름 l을 쓰지 않았을까?
print(a,b,c,d,e,f,g,h,i,j,k,m)
type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j), type(k), type(m)

# %% [markdown]
# 그 밖에 builtins 모듈의 데이터 타입에는 포함되어 있지 않지만, 데이터 분석에 자주 사용되는 데이터형에는 **범주형**, **날짜시간형**이 있다. 

# %% [markdown]
# 범주형은 특정한 값(수준)만을 가질 수 있는 값이다. 예를 들어 "커피를 드릴까요? 아니면 차를 드릴까요?"라는 질문에 대답은 "커피" 또는 "차"만 가능하다. 이때 질문의 답을 범주형으로 생각할 수 있다. **범주형**에는 수준 사이에 우위 또는 선후가 없는 경우와 "저", "중", "고"처럼 수준 사이에 비교가 가능한 **순위형**으로 나뉜다. 
#
# 파이썬에서 범주형을 저장하기 위해 가장 많이 사용하는 방법은 패키지 `pandas`의 `Categorical`이라는 클래스를 사용하는 것이다. 

# %%
import pandas as pd
a = pd.Categorical(['Right', 'Left', 'Middle', 'Middle', 'Right'])
b = pd.Categorical(['low', 'medium', 'high', 'high', 'low'], 
                   categories= ['low', 'medium', 'high'],
                   ordered=True)

print(a, b)
type(a), type(b)

# %% [markdown]
# 날짜시간형은 여러 가지 방식으로 저장될 수 있다. 파이썬 표준 라이브러리에는 datetime 패키지가 있고, 제3자 패키지인 numpy나 pandas를 사용할 수도 있다. 여기서는 파이썬 표준 라이브러리인 datetime 패키지의 `date`, `time`, `datetime` 클래스를 사용하여 날짜형, 시간형, 날짜시간형 값을 저장해보자.

# %%
import datetime
a = datetime.date(2022, 3, 4)
b = datetime.time(19,30,0)
c = datetime.datetime(2022, 3, 4, 19, 30, 0)
print(a,b,c)
type(a), type(b), type(c)

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
# 논리(bool)             isinstance( , bool)         
# 정수                   isinstance( , int)               int()
# 실수                   isinstance( , float)             float()
# 문자                   isinstance( , str)               str()
# 범주                   isinstance( , pd.Categorical)    pd.Categorical()    
# 순위범주                isinstance(x, pd.Categorical) and x.ordered
#                                                        pd.Cateogrical( , orderd=True, categories=[])
# 날짜                   isinstance( , datetime.date)     datetime.date(년,월,일)     
# 시간                   isinstance( , datetime.time)     datetime.time(년,월,일)
# 날짜시간                isinstance( , datetime.datetime) datetime.datetime(년,월,일,시,분,초) 

# %% [markdown]
# 변수에 저장된 값의 타입을 확인하기 위해서는 `isinstance()`함수를 사용한다. 만약 변수 `x`의 값이 논리형(`bool`)인지 확인하기 위해서는 `isinstance(x, bool)`로 쓴다. 만약 `x`가 논리형이라면 `isinstance(x, bool)`은 참(`True`)가 될 것이다(영문으로 Is instance `x` `bool`?와 같은 의미이다). 여기서 instance는 객체와 같은 의미라고 생각하면 된다.
#
# 위에서 소개한 타입은 다음과 같다. 타입을 확인하기 위해서 앞에서와 마찬가지로 `isinstance()`에 변수와 타입을 넣어 사용한다.

# %% [markdown]
#
# |  자료형  |    타입(Python)   |
# |:---------|:------------------|
# |  논리형     |  `bool`         |
# |  정수형     |  `int`         |
# |  실수형     |  `flaot`         |
# |  문자형     |  `str`         |
# |  범주형     |  `pd.Categorical`         |
# |  순위형     |  `pd.Categorical` 그리고 `.ordered`         |
# |  날짜형     |  `datetime.date`         |
# |  시간형     |  `datetime.time`         |
# |  날짜시간형 |  `datetime.datetime`         |

# %%
import datetime
import pandas as pd
x1 = 23; print(type(x1))
x2 = 22.3; print(type(x2))
x3 = "strings"; print(type(x3))
x4 = pd.Categorical(['Hi', 'Lo', 'Lo']); print(type(x4))
x5 = datetime.date(2020, 1, 1); print(type(x5))
x6 = datetime.time(9, 0, 0); print(type(x6))
x7 = datetime.datetime(2020, 1, 1, 12, 11, 11); print(type(x7))
isinstance(x1, int), isinstance(x2, float), isinstance(x3, str), isinstance(x4, pd.Categorical), \
isinstance(x5, datetime.date), isinstance(x6, datetime.time), isinstance(x7, datetime.datetime)

# %% [markdown]
# 여기서 다시 한번 유의할 점은 다음과 같다. 범주형, 순위형의 경우 파이썬의 builtins 모듈에서 제공되는 타입이 아니다. 제3자 패키지인 pandas에서 제공되는 타입이고, 다른 제3자 패키지에서 제공되는 타입을 사용하여 값을 저장할 수도 있다. 날짜형, 시간형, 날짜시간형의 경우는 파이썬 표준 라이브러리의 하나인 datetime 패키지에서 제공되는 타입이지만 효율적인 데이터 처리가 필요한 경우에는 제3자 패키지인 numpy나 pandas의 타입을 더 많이 사용하는 경향이 있다. 그래서 `isinstance(x, datetime.datetime)`이 거짓으로 나온다고 `x`가 날짜시간형이 아니라고 확신하기 힘들다. 다음의 예를 보자.

# %%
import numpy as np
x= np.array(['2022-12-01 13:00'], dtype='datetime64') # 64비트로 저장하겠다
isinstance(x, datetime.datetime)

# %% [markdown]
# 이 경우 다음과 같이 시간자료형 데이터(값)을 저장하고 있음을 확인할 수 있다. (이에 대해서는 넘파이 배열에서 확인한다.)

# %%
isinstance(x, np.ndarray) and str(x.dtype).startswith('datetime64')

# %% [markdown]
# 타입을 변환하는 것은 원래 타입에 따라 다른 방법을 사용해야 한다. 빌트인 타입 내에서는 동일한 함수를 사용할 수 있다. 예를 들어 `int()`는 실수형을 정수형을 변환할 때에도, 문자열형을 정수형으로 변환할 때에도 사용한다. 하지만 소수점 이하가 포함된 문자열을 바로 정수형으로 변환할 수는 없다. `int(float())`을 사용하자.

# %%
int(32.4)

# %%
int("32") # int("32.4") <- Error

# %%
int(float("32.4"))

# %% [markdown]
# # 3.3 연산과 함수

# %% [markdown]
# 어떤 값의 데이터 타입은 값을 저장하는 방식을 결정한다. 우리가 추상적으로 생각하는 값과 컴퓨터에 저장되는 값을 분리해서 생각할 필요가 있었다. 데이터 타입은 컴퓨터에 저장된 이진수가 어떤 의미를 갖는지를 알려준다.
#
# 데이터 타입은 가능한 연산과 적용 가능한 함수도 결정한다. 보통 연산은 같은 타입 안에서만 가능하다. 예를 들어 정수형 `123`과 정수형 `456`을 더해보자. 그 결과는 `579`가 된다. 하지만 문자열 `"123"`과 문자열 `"abc"`를 더해보자. 데이터 타입에 의해 덧셈(`+`)의 의미가 결정되고, 결과는 `123abc`가 된다. 
#
# 다시 말해 데이터 타입에 의해 가능한 함수 또는 연산이 결정되고, 그 의미도 결정된다. 여기서는 각 데이터 타입별로 가능한 연산/함수, 자주 사용하는 연산/함수를 간단하게 소개한다. 자세한 활용법은 뒤의 각 장에서 상세하게 소개할 것이다.

# %% [markdown]
# ## 3.3.1 정수형

# %% [markdown]
# ### 3.3.1.1. 산술연산

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
# ### 3.3.1.2. 비교연산
#
# 비교 연산은 크기가 같음 또는 크기의 대소를 비교한다. 그 결과는 `True`(참) 또는 `False`(거짓)이 된다.

# %%
x = 5
x < 6, x <= 6, x == 6, x != 6, x >= 6, x > 6

# %% [markdown]
# `==`은 같음, `!=`는 같지 않음을 나타낸다.

# %% [markdown]
# ### 3.3.1.3 할당 연산

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
# ### 3.3.1.4 비트 연산
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
# ### 3.3.1.4 수학 함수

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
    return [k for k, v in vars(module).items() if callable(v) and not k.startswith('_')]


# %%
lsf(math)

# %% [markdown]
# ## 3.3.2 실수형

# %% [markdown]
# ### 3.3.2.1 산술연산, 비교연산, 할당연산, 수학함수

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
# 실수형에서 유의할 점은 실수형은 정확성에 한계가 존재한다는 점이다. 

# %%
print(math.sqrt(2)**2 == 2)
#R> sqrt(2)^2 == 2

num = math.sqrt(2)**2
print(num)
#R> print(sqrt(2)^2)

# %% [markdown]
# 0.1, 0.2와 같은 소수는 2진법의 부동소수점으로 저장되기 때문에
# 약간의 오차가 발생할 수 있다.
# 약간의 오차를 무시하고 두 수의 크기를 비교하고자 한다면,
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

# %%
math.isclose(1e-23, 1e-24) # rel_tol = 1e-09
# R> all.equal(1e-23, 1e-24)
# R> dplyr::near(1e-23, 1e-24)
# R> near <- dplyr::near; near(1e-23, 1e-24)

# %% [markdown]
# ### 실수 출력 형식 지정
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
# ## 3.3.2 문자열
#
# 문자열 타입을 출력하기 위해 `print()`와 `repr()`을 사용할 수 있다. `print()`는 문자열의 탈출문자가 적용된 결과를 출력하고 `repr()`은 문자열이 따옴표 사이에 탈출문자가 포함하여 표기된 형태로 출력된다. 
#
# R에서의 `print()`와 `cat()`을 파이썬에서는 `repr()`과 `print()`를 쓴다. 파이썬에서 `repr()`은 출력 내용을 복사해서 어떤 변수에 할당할 수 있는 경우가 많다. `repr()` 없이 변수만 써도 콘솔에서 `repr()` 결과가 나온다.
#
#

# %%
x = "I \nDo\tLove You\N{INVERTED EXCLAMATION MARK}"
x

# %%
repr(x)

# %%
print(x)

# %%
repr("\"Hello\", says he.\tI can do!")

# %%
print("\"Hello\", says he.\tI can do!")

# %% [markdown]
# ### 문자열 함수
#
# 다음은 몇 가지 대표적인 문자열 연산과 함수를 보여준다.

# %%
x = "ABC" + "abc" + "123"; print(x)

# %%
len('hello?') # 문자 갯수 R> nchar()

# %%
x[:5] # 처음부터 5번째 글자 R> substring(x, 1, 5)

# %% [markdown]
# ## 3.3.3 날짜/시간 연산/함수
#
# 날짜시간/날짜/시간은 과거, 현재, 미래로 이어지는 시간의 흐름 속에 한 점을 나타낸다. 그래서 날짜 사이에는 차이를 구하는 것은 자연스러운 연산이다.
#
# 뒤에서 살펴보겠지만 날짜, 시간은 시간 흐름의 직선 위의 한 점을 다소 복잡한 방식으로 표기한다. 1분은 1초의 60배이고, 1시간은 1분의 60배이다. 1일은 1시간의 24배이고, 1주는 1일의 7배이지만, 달, 년은 일에 일정한 배를 해서 구할 수 없다. 

# %%
import datetime

# %%
print(datetime.date.today())
datetime.date.today()
# R> Sys.Date() # 현재 날짜

# %%
print(datetime.datetime.now())
datetime.datetime.now()
# R> Sys.time() # 현재 날짜와 시간(POSIXct 형식)

# %%
# 문자열 "2022/12/31"을 날짜 형식으로
x = datetime.datetime.strptime("2022/12/31", "%Y/%m/%d").date()
x
# R> as.Date("2018/12/31") 

# %%
# 문자열 "2018/12/31 23:59:59"을 날짜시간 형식으로
x = datetime.datetime.strptime("2022/12/31 23:59:59", "%Y/%m/%d %H:%M:%S")
x
# R> as.POSIXct("2022/12/31 23:59:59") 

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
# 현재 날짜 시간과 2022년 12월 31일 23시 59분 59초와의 차이(일)
a = datetime.datetime(2022,12,31,23,59,59)
b = datetime.datetime.today()
print((a-b).days, "일") 
# R> difftime(as.POSIXct("2018/12/31 23:59:59"), Sys.time()

# %%
# 현재 날짜 시간과 2022년 12월 31일 23시 59분 59초와의 차이(분 단위로)
print((a-b).seconds/60, "분")
print(f"{(a-b).seconds/60:.2f}분") # 소수점 이하 숫자 두 개
# R> difftime(as.POSIXct("2022/12/31 23:59:59"), Sys.time(), units='mins')

# %%
# 현재 날짜 시간과 2022년 12월 31일 23시 59분 59초와의 차이(초 단위로)
# 파이썬 : timedelta 값은 날짜, 초, 밀리초를 days, seconds, miliseconds 속성 이용해 접근할 수 있다.
a = datetime.datetime.today()
b = datetime.datetime(2022,12,31,23,59,59)
print((a-b).seconds, "초")
# R> difftime(as.POSIXct("2022/12/31 23:59:59"), Sys.time(), units='secs')
#    R에서 units은 다음 중 하나: 'auto', 'secs', 'mins', 'hours', 'days', 'weeks'

# %% [markdown]
# ## 3.3.4 논리형 연산/함수

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
not (7 < 3)

# %%
# R>
#(7 < 3) & (4 > 3)
#(7 < 3) | (4 > 3)
#!(7 < 3)
#xor(T, T) # XOR
#x = NA
#isTRUE(x == 3) # robust to NAs

# %% [markdown]
# 특히 결측치를 나타내는 `np.nan`을 주목하자. 빌트인 모듈 또는 내장 모듈을 사용하여 결측치를 나타낼 방법이 없기 때문에 제3자 패키지인 `numpy`를 사용했다. 계산 결과도 R과 다름을 유의하자.
#
# R에서 `NA`를 포함한 거의 모든 계산 결과는 `NA`이다. 왜냐하면 어떤 값인지 모르므로 결과 또한 어떤 값인지 모르게 된다. 예를 들어 `NA==3`의 결과는 `NA`인데, `NA`가 어떤 수인지 모르기 때문이다(3일 수도, 아닐 수도 있다).
#
# 파이썬의 `np.nan`이 이와 다소 다르게 작동한다. 다음을 보자. R이라면 모두 `NA`가 나올 논리식이 `FALSE`임을 유의하자.

# %%
print(np.nan == np.nan)
print(3==np.nan)
print(math.isclose(np.nan, np.nan)) # np.isclose(np.nan, np.nan)


# %% [markdown]
# 그래서 파이썬의 `x==3`은 R의 `isTRUE(x==3)`과 비슷하다고 생각할 수 있다. 

# %% [markdown]
# 만약 `x`와 `y`를 비교할 때 `np.nan`을 고려하여 R과 비슷한 결론을 얻어 내고 싶다면,

# %%
def eq(x, y):
    if np.isnan(x) or np.isnan(y):
        return np.nan
    elif x == y:
        return True
    else:
        return False
eq(3, np.nan), eq(3,4), eq(np.nan, 4)

# %%
eq(np.array([3,4]), np.array([np.nan, 4])) # 이렇게 np.ndarray에도 사용할 수 있도록 수정해야 할 듯 !!!

# %%
import numpy as np
np.isnan


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
lsf(pd)

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
eq(3, np.nan)

# %%



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

# %%
0b1100 | 0b0011

# %%
import sys
sys.float_info.max 

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

# %%

# %%

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
