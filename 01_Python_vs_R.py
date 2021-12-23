# -*- coding: utf-8 -*-
# # Python과 R의 차이점
# ## 들여쓰기(indentation)의 구성도 중요함
#
# 문서 편집기에서 눈에 보기에 줄이 맞아도 IndentationError가 발생할 수 있다. 코드 편집기에 따라 tab의 스페이스 개수가 다를 수 있다. 그리고 tab과 space는 다른 문자로 취급되기 때문에 이 둘을 혼용할 경우에도 IndentationError가 발생한다. PEP(Python Enhancement Proposal)에 따르면 들여쓰기로 space 4개를 권장한다. 그리고 tab은 최대한 지양하는 것을 스타일 가이드로 제시했다.
# ## 여러 줄에 걸쳐 쓰기
#
# R에 하나의 표현식을 여러 줄에 걸쳐 쓰기 위해서는 단지 표현식 또는 함수가 그 줄에서 끝나지 않으면 된다.
#
# ```{r}
# x = 1 + 
#     2
# ```
#
# 하지만 Python에서는 명시적인 줄바꿈 표시로 `\`가 필요하다.
#
# ```{python}
# x = 1 + \
#     2
# ```
#
# 그리고 `\` 이후에는 어떤 문자도 없어야 한다. 공란(space)조차 SyntaxError를 발생시킨다. 
#
# ```{python}
# x = 1 + \
#     2 + \
#     3
# ```
#
# 그리고 주석 처리가 약간 복잡해지는데, 다음을 보자.
#
# ```{python}
# x = 1 + \
# #   2 + \
#     3
# ```
#
# 위의 코드를 실행시키면, SyntaxError가 발생하는데, 위의 코드는 사실 `x = 1 + #   2 + 3`가 같기 때문이다(여러 줄로 쓰인 코드에서 `\`과 `\n`(또는 `\r\t`)을 생략한 결과이다). 
#
# Python에서 여러 줄에 걸쳐 쓰는 다른 방법은 괄호를 미쳐 끝내지 않는 것이다. 이 방법은 주석 처리도 쉽기 때문에 요즘에는 이 방법이 권장된다.
#
# ```{python}
# x = (1 + 
#      2 + 
#      3)
# ```
#
# ```{python}
# x = (1 + 
# #     2 + 
#      3)
# ```


#
# ## 함수에서 return을 생략할 수 없다
#
# R의 함수에서는 명시적으로 return을 쓰지 않더라도, 가장 마지막에 계산된 값이 반환된다.
#
# ```R
# test <- function(x){sum(x)/length(x)}
# print(test(c(3,2,1)))
# ## [1] 2
# ```
#
# 하지만 python에서는 명시적으로 return을 하지 않으면 `None`이 반환된다.
#
# ```python
# def test(x):
#     sum(x)/len(x)
# print(test([3,2,1]))
# ## None
# ```
#
# 다시 말해 python에서 `return`은 선택적이 아니라 필수적이다.
#
# ```python
# def test(x):
#     return sum(x)/len(x)
# print(test([3,2,1]))
# ## 2.0
# ```
#
#

# ## pandas DataFrame의 메쏘드의 기본인자값은 `axis=0`이다.
#
# DataFrame의 축(컬럼 등) 이름을 변경하는 메쏘드 `.rename()`과 같이 많은 데이터 프레임의 메쏘드는 `axis=` 매개변수가 있고, 이들의 기본값은 `axis=0`이다. 예를 들어 `df.rename({'x':'x1', 'y':'y1'})`라고 하면 행이름 중에서 `x`를 `x1`으로 바꾸고, `y`를 `y1`으로 바꾼다. 만약 열이름을 수정하고 싶다면, `axis=1`을 쓰거나, `columns=`에 수정할 열이름을 적어야 한다.
#
# ```{python}
# df.rename({'x':'x1', 'y':'y1'}, axis=1)
# df.rename(columns = {'x':'x1', 'y':'y1'})
# ```

# ## pandas DataFrame의 메쏘드는 기본적으로 `na.rm=TRUE`이다
#  
# R의 경우 대부분의 함수, 연산에서 `NA`가 포함된 경우 결과는 `NA`이다.
# Python의 경우 `np.nan`이 포함된 경우에 대부분 `np.nan`를 제외하고 결과를 산출한다.

# ## 파이썬의 import는 화일이름에 따라 달라야 한다
#
# R에서 다른 화일의 소스를 사용하고자 하면 `source()`를 하면 된다. Python에서는 화일이름에 따라 방법을 달리 해야 한다.
#
# ### `pwd.py`, `sys.py`, `time.py`와 같이 Python의 기본 모듈과 화일이름이 같을 경우
#
# 이런 이름을 화일명으로 사용하면 Python의 기본 모듈과 겹치기 때문에 사용할 수 있는 방법이 없다!
# `import time`을 하면 Python의 기본 모듈 time이 import된다.
#
# ### 숫자로 시작하는 화일명
#
# 예를 들어 `01_test.py`이 있다면 이를 `import 01_test`로 불러들일 수 없다. 왜냐하면 `01_test`가 객체 이름으로 부적절하기 때문이다. `from 01_test import test_module`과 같이 쓸 수도 없다. 이때에는 아래에 소개하는 방법을 써야 한다. 이때 중요한 것은 모듈을 가리키는 변수 이름이 숫자로 시작하지 않아야 한다는 점이다.
#
# #### `__import__` 내장함수 할용
#
# ```{python}
# # 01_test 모듈을 가리키는 변수명을 module로 함.
# module = __import__('01_test')
# module.test_module()
# ```
#
# #### `importlib` 내장패키지 활용
#
# ```{python}
# import importlib
# module = importlib.import_module('01_test')
# module.test_module() 
# ```
#
# #### `getattr`을 이용하여 모듈 내 함수만 불러들이기
#
# ```{python}
# import importlib
# module = importlib.import_module('01_test')
# test = getattr(module, 'test_module')
# test()
# ```
#
#

# ## R에서는 다른 패키지를 언급할 일이 거의 없지만,
#
# R에서 어떤 패키지를 쓸 때, 다른 패키지를 언급할 일이 거의 없다. 물론 의존 관계에 있는 패키지들을 먼저 읽거나 할 순 있다. 하지만 python에서 pandas를 쓰려면 numpy를 먼저 import하는 게 좋다. 왜냐하면 pandas에서 np.nan을 쓸 일이 있는데, pandas를 import했다고 해서 numpy가 자동으로 import되거나 np.nan의 nan을 자동으로 사용할 수 있는게 아니기 때문이다. 


# ## function의 default argument로 list를 쓰는 경우
#
# R의 경우를 기본값으로 리스트를 쓰면 다음과 같다.
#
# ```{r}
# f = function(y, x= list()) {
#     x = append(x,y)
#     return(x)
# }
# f(1)
# ## [[1]]
# ## [1] 1
# f(2)
# ## [[1]]
# ## [1] 2
# ```
#
# Python의 경우, 기본값으로 리스트를 쓰면, 기본값이 변할 수 있다.
#
# ```python
# def f(y, x=[]):
#     x.append(y)
#     return x
# f(1)
# ## [1]
# f(2)
# ## [1, 2]
# ```
#
# 함수 `f`의 디폴트(default) 인자는 `f.__defaults__`에 저장되어 있다. 그래서 원한다면 함수 `f` 인자의 기본값을 원하는대로 바꿀 수도 있다. 어쨋든 `x=[]`는 함수가 생성될 때 `f.__defaults__`에 저장되고, 그 이후로는 `f.__defaults__`의 값을 기본값으로 사용한다. 그런데 인자를 리스트로 할 경우, `f.__defaults__`가 계속 변하게 될 수 있다. 그래서 되도록 함수의 인자 기본값은 리스트를 사용하지 않는다. 


# # 10. closure를 사용하는 경우 (late-binding)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ## `7`을 `07`로 쓰지 못한다.
#
# 자릿수를 맞추기 위해 소수점 아래에 혹은 수의 처음에 `0`을 붙이고 한다. 하지만 Python에서는 수 앞에 `0`을 붙일 수 없다. 
#
# R에서는 01, 02, 001 등의 숫자를 입력시 각각 수 1,2,1로 인식한다. Python은 다르다.
#
# python은 기본 10진수를 사용하고 있다. 2.x 버전까지는 8진수 정수를 나타낼 때 접두어 0을 붙였기 때문에, `010`, `011`를 수 8, 9로 인식했었다.
# 하지만, 3.x 버전으로 넘어오면서 접두어 0에서 0o로 변경되어 `0o10`, `0o11`은 수 8,9를 의미하고, `010`과 `011`은 SyntaxError를 발생시킨다. `oct()`함수는 주어진 수를 8진수 표현으로 바꿔준다.  
#
# ```{python}
# #python 2.x
# >>> oct(10)
# '012'
# #python 3.x
# >>> oct(10)
# '0o12'
# ```
#
#

# +
# 그 밖에도 이진수(`0b`,`0B`), 16진수(`0x`, `0X`)를 나타내는 방법은 다음과 같다.

0b11110, 0B11110
0o36, 0O36
0x1e, 0X1E
# 0x1e12과 01e12은 어떻게 다른가?
# 웃긴 건 0013은 안 되고 0013e0은 된다
# -

# ## 정수의 한계
#
# R의 최대 정수값은 다음과 같이 확인할 수 있다.
#
# ```{r}
# .Machine$integer.max
# ## 2147483647
# ```
#
# 만약 2147483647+1을 한다면? 결과가 나오긴 하지만 정수가 될 수 없다.
#
# ```{r}
# class(2147483647+1)
# ## [1] "numeric"
# as.integer(2147483647+1)
# ## [1] NA
# ## Warning message:
# ## NAs introduced by coercion to integer range 
# ```
#
# 파이썬 정수는 이런 한계가 없다. (어떻게 이게 가능한지는 https://rushter.com/blog/python-integer-implementation/ 을 참조하자.)
#
# ```{python}
# import sys
# sys.maxsize
# ## 9223372036854775807
# class(9223372036854775807+1)
# ## int
# class(100000000000000000000000000000000)
# ## int
# ```
#
# `sys.maxsize`는 리스트 원소의 최대갯수이다.
#
#

# ## 행렬 또는 배열의 원소

# R의 행렬 또는 배열은 첫 번째 차원이 가장 빠르게 바뀐다.
# 무슨말이냐면, c(1,2,3,4)를 2차원(2x2)의 배열 a로 만들면 
# a[1,1] = 1; a[2,1] = 2; a[1,2] = 3; a[2,2] = 4가 된다.
# 이런 방식은 fortran의 방식이므로 간단하게 F라고 쓴다.

# Python에서는 선택할 수 있지만,
# 기본값은 가장 마지막 차원이 가장 빠르게 바뀐다.
# 위의 예에서 a[0,0] = 1; a[0,1] = 2; a[1,0] = 3; a[1,1] = 4가 되는 방식.
# 이런 방식 C의 방식이므로 간단하게 C라고 쓴다.
