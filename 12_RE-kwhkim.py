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
# # 정규표현식

# %% [markdown]
# 저자는 시나리오를 하나 쓰고 있다. 로맨스 장르이다. 박보검과 박소담이 주연 배우이다. 이 둘은 겨울에 만나 어떤 일(something?)이 벌어지는데, 그게 언제인지 깜빡했다. 그 부분의 시나리오를 수정해야 한다. 한 가지 기억나는 것은 그 날 날짜를 `~월 ~일`로 특정했던 기억이 있다. 그래서 문서 편집기의 검색 기능을 사용해서 `12월`, `1월`, `2월`을 검색하려고 한다. 그런데 이 방법이 최선일까?

# %% [markdown]
# 이 방법은 검색을 세 번이나 해야 한다. 그리고 `1월`을 검색하면 `11월`의 뒷 부분도 검색 결과에 포함되기 때문에 불필요한 부분은 눈으로 확인하여 건너뛰어야 한다.

# %% [markdown]
# **정규표현식**을 사용하면 단 한 번의 검색으로 저자가 원하는 부분을 정확하게 찾을 수 있다. 구체적으로 `\b(12|1|2)월`을 검색하면 해결된다.

# %% [markdown]
# 정규표현식에서 `\b`, 그리고 `(12|1|2)`의 괄호와 수직 막대기(vertical bar; `|`)는 실제 그 문자를 찾으라는 의미가 아니라 **특별한 의미**를 가지고 있다. 정규표현식은 이렇게 특별한 의미를 나타내는 문자를 사용해서 문자열에 존재하는 패턴을 나타낸다. 정규표현식 `\b(12|1|2)월`은 길고 복잡한 문자열에서 `12월`, `1월`, `2월`로 시작하는 부분을 나타낸다. 

# %% [markdown]
# 정규표현식은 어떻게 복잡한 문자열에서 원하는 패턴을 정확하게 나타낼 수 있을까?

# %% [markdown]
# ## 파이썬과 정규표현식

# %% [markdown]
# 영어로 Regular Expression(줄여서 Rex라고 하기도 한다)으로 표기하는 **정규표현식**은 대부분의 프로그래밍 언어에서 사용되는 흔한(?) 방법이다. 하지만 **정규표현식은 언어마다 조금씩 다르다.** 
#
# 특히 파이썬은 정규표현식을 위해 파이썬 표준 모듈 `re`를 사용하기도 하고, 3자 모듈인 `regex`를 사용할 수도 있다. 그리고 판다스에서도 `re`의 정규표현식을 사용할수 있다. 그리고 `re`와 `regex`은 비슷하지만 조금씩 다르다.
#
# 다른 언어를 배운 후에 파이썬에서 정규표현식을 사용한다면 헷갈리거나 실수를 하게 될 수도 있다. 
#
# 여기서는 먼저 파이썬의 표준 모듈의 `re`의 정규표현식을 알아보자.
#
#
#

# %% [markdown]
# ## 파이썬 표준 모듈 `re`의 정규표현식

# %% [markdown]
# 파이썬 표준 모듈 `re`의 정규표현식은 파이썬 공식 문서(https://docs.python.org/3.8/library/re.html)에 따르면 Perl의 정규표현식과 비슷하다고 한다. 하지만 완전히 동일하지는 않다고 한다.

# %% [markdown]
# ### 메타 문자

# %% [markdown]
# 정규표현식은 문자열 패턴을 나타내기 위해 다양한 기호를 사용한다. 예를 들어 `^`는 문자열의 처음을 의미한다. 따라서 `^a`는 문자열의 처음에 나타나는 `a`를 의미하고, `a`는 문자열의 어느 위치에서 등장해도 괜찮다. 다음의 코드를 보자.

# %%
txt1 = "abc"
txt2 = "This is a car."

# %%
import re
re.search("a", txt1)

# %%
re.search("a", txt2)

# %%
re.search("^a", txt1)

# %%
re.search("^a", txt2)

# %% [markdown]
# 위의 결과를 보자. `re.search("a", txt1)`은 문자열 `txt1`에서 문자열 패턴 `"a"`를 찾는다. 이때 `"a"`의 위치는 어느 위치에 등장해도 괜찮다. 결과를 보면 `<re.Match ... span=(0,1), match='a'>`에서 `'a'`가 등장하는 위치를 확인할 수 있다. `span=(0,1)`은 문자열 `txt1`의 0-번째 문자에서 1-번째 문자 직전까지가 우리가 찾고자 했던 패턴에 해당함을 알려주고 있다. `txt[0:1]`로 다시 한번 확인할 수 있다.

# %% [markdown]
# `re.search("^a", txt2)`를 `re.search("a", txt2)`와 비교해보면 `^`의 의미를 확인할 수 있다. `re.search("^a", txt2)`의 결과로 아무것도 표시되지 않는 것은 `re.search("^a", txt2)`의 결과가 `None`이기 때문이다. `None`은 문자열 `txt2`에서 정규표현식 패턴 `^a`를 찾지 못했다는 의미이며, 여기서 `^a`는 `a`로 시작하는 모든 문자열을 나타낸다.

# %% [markdown]
# 이렇게 문자열 패턴을 나타낼 때 특별한 의미를 나타내는 문자를 메타 문자라고 한다. 파이썬 표준 `re`에서 사용하는 메타 문자는 다음과 같다.

# %% [raw]
# . ^ $ * + ? { } [ ] \ | ( )
#
# # 책에 키보드 그림을 그려서 어떤 문자들이 메타문자인지 표시해줘도 좋을 것 같다
# # 메타문자의 기능과 의미를 하나의 표로 일목요연하게 정리해 줄 필요성
# (참조1: https://pat.im/821          ////// 참조2:https://gungadinn.github.io/data/2019/07/14/RegularExpression/)

# %% [markdown]
# 이들 문자는 문자 하나가 특별한 기능을 하기도 하고, 다음의 문자와 함께 그 의미가 정해지기도 한다. 예를 들어 `^`은 단독으로 쓰여 문자열의 시작을 나타내지만 `(`와 `)`는 단독으로는 의미가 없고 `(`와 `)` 사이에 어떤 문자열이 오느냐에 따라 그 의미가 달라진다.  
#
# 이들 메타 문자를 제외한 문자로 구성된 문자열의 경우에는 특별한 의미가 없기 때문에 **문자 그대로 문자**를 의미한다고 생각할 수 있다. 예를 들어 `10월`을 찾고 싶다면 다음과 같이 한다. 

# %%
patt = '10월' 
# 문자열 patt 안에 위의 메타 문자가 없기 때문에 
# 문자열 patt는 정규표현식으로 써도 "10월"을 그대로 의미한다.
txt = "그녀는 10월의 낙엽처럼 아름다웠다."

# %% [markdown]
# 문자열 `txt`에서 `patt`을 찾아보자.

# %%
re.search(patt, txt)

# %% [markdown]
# `txt`의 4-번째 문자에서 7-번째 문자 직전까지에서 `10월`을 찾을 수 있다.

# %%
txt[4:7]

# %% [markdown]
# ### 메타 문자를 문자 그대로

# %% [markdown]
# 이렇게 문자가 새로운 기능을 갖게 되면 그 문자를 문자 그대로 나타내기 위해 새로운 방법이 필요하다. 정규표현식에서는 두 가지 방법을 사용할 수 있다. 앞에 백슬래쉬를 붙이거나, `[`,`]`로 감싼다. `[`,`]`로 감싸는 방법은 `[`,`]`을 사용하는 방법(문자 집합 생성)에서 설명하기로 하고 백슬래쉬를 붙이는 방법에 대해 알아보자. 

# %% [markdown]
# 예를 들어 위의 문자열 `txt`에서 마침표(`.`)가 존재하는지 확인하고자 한다면 다음과 같이 쓸 수 있다.

# %%
patt = '\\.'

# %%
re.search(patt, txt)

# %% [markdown]
# 여기서 `patt = '\\.'`를 주목할 필요가 있다. 문자열 `patt`에는 어떤 내용이 들어가 있는가?

# %%
print(patt)

# %% [markdown]
# 문자열 `patt`의 길이는 2이며, 두 문자 `\`과 `.`로 이루어졌다.

# %%
len(patt), patt[0], patt[1]

# %% [markdown]
# 그런데 문자열을 큰 따옴표 또는 작은 따옴표로 나타낼 때에, `\`는 탈출 문자(escape letter)로 작용하여 다음과 같은 의미를 지닌다.

# %% [raw]
# `'\a'`
# `'\b'`
# `'\t'`
# `'\r'`
# `'\n'`
# `'\\'`
#

# %% [markdown]
# 그래서 `"\\"`는 문자 `\`를 따옴표로 감싸서 표현하는 방법이다. 따옴표 안에서 `\`가 탈출문자로 작동해서 `"\\"`가 문자 `\`를 의미하게 되는 것이다. 만약 `\`가 탈출 문자로 작동하지 않게 하려면 큰 따옴표 또는 작은 따옴표 앞에 `r`을 붙이면 된다. 이때 `r`은 **r**aw의 약자로 따옴표 안의 문자들을 모두 문자 그대로 인식하라는 의미이다(이때 한 가지 주의점은 마지막 글자가 `\`가 되어서는 안 된다).

# %% [markdown]
# 이 책에서는 의도적으로 따옴표로 감싸 안은 문자열과 그냥 문자열을 구분하였다. 따옴표로 감싸 안은 경우 백슬래쉬는 탈출 문자로 작동함을 의미한다. `"\n"`은 줄바꿈 문자를 의미하고 `\n`은 백슬래쉬와 `n`으로 이루어진 두 문자의 문자열을 의미한다.

# %% [markdown]
# 그리고 정규표현식으로 사용되는 `\.`는 문자 그대로의 마침표(`.`)를 의미한다. 다음의 두 결과를 비교해보자.

# %%
re.search('.', txt) # match = '그'가 되는 이유는, 일치 여부를 찾을 때 문자열의 처음부터 순차적으로 검색하기 때문이다. '.'은 모든 문자를 의미하기 때문에, 여기서 match 값은 문자열의 첫 번째 문자로 출력된다.

# %%
txt[0:1]

# %%
re.search('\\.', txt), re.search(r'\.', txt)

# %%
txt[19:20]

# %% [markdown]
# 위의 결과를 보면 정규표현식 `\.`은 문자 `.`을 의미하는 것이 분명하다. 하지만 정규표현식은 `.`는 어떤 의미일까?

# %% [markdown]
# ### 정규표현식 `.`

# %% [markdown]
# 정규표현식 `.`는 **모든 문자**를 의미한다. 다시 말해 `''`가 아니라면 모든 문자열은 문자를 하나 이상 가지고 있으니까 정규표현식 `.`에 해당하는 패턴을 포함하는 것이다. 그런데 이 모든 문자는 기본적으로 줄바꿈 문자 `\n`을 포함하지 않는다. 그래서 엄밀히 말해 정규표현식 `.`은 **줄바꿈을 제외한 모든 문자**란 의미이다. (하지만 다시 모드가 `re.DOTALL`이 아닐 때에만 해당한다. 조금 뒤에서 설명된다.)

# %%
txt = 'abc'
re.search('.', txt)

# %%
txt = '\n\n'

# %%
txt

# %%
re.search('.', txt)

# %% [markdown]
# 만약 `.`이 **줄바꿈 문자를 포함한 모든 문자**를 의미하게 하려면 다음과 같이 한다.

# %%
re.search('.', txt, flags = re.DOTALL)

# %%
txt[0:1]

# %% [markdown]
# `re.DOTALL`에서 그 의미가 분명하다. DOT(`.`)이 모든(`ALL`) 문자를 의미하게 만들어 준다.

# %% [markdown]
# ### 문자열의 시작과 끝을 의미하는 `^`와 `$`

# %% [markdown]
# 앞에서 봤듯이 정규표현식 `^`는 문자열의 시작을 의미한다. 이와 반대로 `$`는 문자열의 끝을 의미한다.

# %%
txt1 = "그는 나를 채근했다."
txt2 = "채소 많이"
txt3 = "집 한 채"
txt4 = """집 한 채
를 사고 싶었다!"""

# %%
patt = "채$"

# %% [markdown]
# 정규표현식 `채$`는 문자열의 마지막에 등장하는 `채`를 의미한다.

# %%
re.search(patt, txt1)

# %%
re.search(patt, txt2)

# %%
re.search(patt, txt3)

# %%
re.search(patt, txt4)

# %% [markdown]
# 문자열 `txt4`에는 `채`가 포함되어 있지만 문자열의 마지막이 아니다. 만약 각 줄의 끝에 `채`가 포함되어 있는지를 확인하려면 다음과 같이 할 수 있다.

# %%
re.search(patt, txt4, flags = re.MULTILINE)

# %% [markdown]
# `flags=`의 `re.MULTILINE`은 `^`과 `$`는 각 줄의 처음과 끝을 의미하도록 바꿔준다. 여러 줄(`MULTILINE`)에서 각 줄을 마치 하나의 문자열처럼 취급한다고 생각할 수 있다. 만약 여러 줄에서도 문자열의 처음과 끝을 나타내려면 `\A`와 `\Z`를 사용한다. 이에 대해서는 뒤에서 설명된다.

# %% [markdown]
# ### OR을 의미하는 `|`

# %% [markdown]
# `|`는 "또는" 또는 "OR"을 의미한다. 예를 들면 `그러나|하지만`은 `그러나` 또는 `하지만`을 의미한다. 어떤 패턴을 의미할 때 **가능한 모든 문자열을 나열하는 방식**을 사용할 수도 있지 않은가? 만약 가능한 모든 문자열이 소수라면 가장 손쉽게 사용할 수 있는 정규표현식이다.

# %%
patt = "그러나|하지만"
txt1 = "그는 놀라웠다. 하지만 그에게도 약점이 있었다."
txt2 = "그녀는 눈부시게 아름다웠다. 그리고 우아했다."
txt3 = "모든 일은 성공적이었다. 그러나 한 가지 우려되는 점이 있었다."

# %%
re.search(patt, txt1)

# %%
re.search(patt, txt2)

# %%
re.search(patt, txt3)

# %% [markdown]
# ### `{` `}`와 그 뒤의 `?`

# %% [markdown]
# `{`과 `}`는 그 사이에 숫자 또는 숫자와 쉼표를 사용해 반복되는 횟수를 나타낸다. 정규표현식에서 `aaa`와 `a{3}`은 같은 의미이다. 그렇다면 굳이 `{`, `}`를 사용할 필요가 있을까 싶기도 한데, `aaaaaaaaaaaaaaaaaa`와 같은 패턴을 `a{18}`로 나타낼 수 있으므로 이 경우에는 훨씬 간단하고 이해하기도 쉽다. 그리고 `aaa|aa|a`를 `a{1,3}`으로 나타낼 수도 있는데, `aaa|aa|a`(또는 `a{1,3}`)가 어떤 의미인지 생각해보자. 

# %%
patt1 = 'aaa|aa|a'
patt2 = 'a{1,3}'

txt1 = 'This is aan apple'

# %%
re.search(patt1, txt1)

# %%
re.search(patt2, txt1)

# %% [markdown]
# `a{1,3}`에서 `1`과 `3`은 반복 횟수의 최소값과 최대값을 나타낸다. 그래서 정규표현식 `a{1,3}`을 만족하는 문자열은 `a` 또는 `aa` 또는 `aaa`를 의미한다. 그런데 동일한 정규표현식으로 `aaa|aa|a`로 쓴 이유는 무엇일까? `aaa|aa|a`는 `a|aa|aaa`와 어떻게 다른가?

# %% [markdown]
# 정규표현식 `|`는 `|`로 구분된 문자열을 처음부터 찾는다. `aaa|aa|a`에 적용해보면 먼저 `aaa`를 찾고 실패할 경우에 `aa`를 찾고, 다시 실패할 경우에 마지막으로 `a`를 찾는다. 그리고 `a{1,3}`의 경우도 최소 1개에서 최대 3개의 `a`를 찾는다고 했지만, 가능하면 최대 횟수의 반복을 찾는다. 이렇게 최대 반복을 가장 먼저 찾는 방식을 **탐욕적인?(greedy) 방식**이라고 한다.

# %% [markdown]
# 그렇다면 다른 방식도 존재하는가? `{`,`}` 다음에 `?`를 살짝 붙여주면 가장 적은 반복을 찾는다. 이를 탐욕적인 방식과 대비해 **게으른(lazy) 방식**이라고 부른다.

# %%
patt2b = 'a{1,3}?'

# %%
re.search(patt2b, txt1)

# %% [markdown]
# 위의 결과에서 확인할 수 있듯이 `a{1,3}?`에서 `?`는 `{1,3}`의 반복 횟수 중 가장 적은 횟수를 가장 먼저 찾게 한다.

# %% [markdown]
# 혹자는 `{1,3}?`에서 가장 짧은 것은 항상 `1`이지라고 말할 수도 있겠지만 다음과 같은 경우도 있다는 것을 이해할 필요가 있다.

# %%
patt3 = 'a{1,3}?n'
re.search(patt3, txt1)

# %% [markdown]
# 그래서 `a{1,3}?`을 `|`로 표현하면? `a|aa|aaa`가 될 것이다.

# %%
patt3b = '(a|aa|aaa)n'
re.search(patt3b, txt1)

# %% [markdown]
# 이때 `a|aa|aaa`와 `n`을 연결하기 전에 괄호로 감싸안았다. 왜냐하면 `|`의 연산이 가장 느리기 때문에 `a|aa|aaan`이라고 쓰면 `a` 또는 `aa` 또는 `aaan`을 의미하기 때문이다. (`(a|aa|aaa)n`은 `an` 또는 `aan` 또는 `aaan`을 의미한다.)

# %%
patt3c = 'a|aa|aaan'
re.search(patt3c, txt1)

# %% [markdown]
# ### `*`, `+`, `?`

# %% [markdown]
# `*`와 `+`, `?`는 모두 `{`, `}`와 비슷하게 **반복**을 의미한다. 구체적으로 다음과 같다.
#
# | 정규표현식 | 반복횟수 |  다른 표현 
# |:--------|:------|:----------|
# |`*`      |0번 이상 | `{0,}`   |
# |`+`      |1번 이상 |`{1,}`   |
# |`?`      |0번 또는 1번 |`{0,1}` |
#
#

# %% [markdown]
# 먼저 `{0,}`과 같은 표현을 보자. 위에서 설명한 대로 최소 반복 횟수는 0번이고 최대 반복 횟수는 특정하지 않았다. 따라서 **최소 0번 반복**이란 의미이다. `*`은 `{0,}`과 동일한 의미이다. 그리고 `*?`는 `{0,}?`와 동일한 의미이다.

# %%
re.search('a*', txt1)

# %% [markdown]
# 위의 결과를 보자. `span=(0,0)`으로 `txt1[0:0]`에 정규표현식 패턴 `a*`가 존재한다는 의미이다.

# %%
txt1[0:0]

# %% [markdown]
# `txt1[0:0]`은 빈 문자열이다. `a`가 0번 반복된 것으로 생각할 수 있다.

# %% [markdown]
# 따라서 `a*`과 같은 정규표현식은 단독으로 쓰이진 않는다. (단독으로 쓰인다면 모든 문자열에서 정규표현식 패턴 `a*`를 찾을 수 있다. 빈문자열에서도!) 다음과 같이 선택적인 상황에서 많이 쓰인다.

# %%
re.search('a*n', txt1)

# %% [markdown]
# 게으른 방법을 쓴다면?

# %%
re.search('a*?n', txt1)

# %%
re.search('(|a|aa|aaa)n', txt1)

# %% [markdown]
# 여기서 정규표현식 `a*?n`을 찾은 결과는 `n`(`a`가 0번 반복되고 `n`이 있는)이어야 할 것 같지만 그렇지 않았다. 왜 그럴까? 이는 정규표현식을 찾아가는 과정을 이해해야 한다.

# %% [markdown]
# 정규표현식 패턴을 찾는 과정은 주어진 문자열의 첫 글자부터 순차적으로 이루어진다. 그리고 정규표현식 안에서도 순차적으로 이루어지는데 이 과정을 조금 상세히 설명해보자.

# %%
txt1

# %% [markdown]
# 위의 문자열에서 `a*?n`을 찾아보자. 문자열에서 현재 위치는 `T`가 시작하기 직전이다. `a*?`에서 `a`가 0번 반복된 지점이다. 게으른 방법이므로 다음 문자 `n`를 찾는다. (만약 탐욕방법이라면 `a`를 찾아야 한다.) `T`와 `n`은 일치하지 않는다. `a`는 1번 반복될 수도 있으므로 `a`를 찾아본다. 역시 실패다. 다음 위치로 넘어간다. 이제 `h` 직전 위치이다. `a`가 0번 반복된 지점이라고 생각할 수 있고 다시 `n`을 찾는다. 역시 실패다. `a`가 1번 반복될 수도 있으므로 다시 확인하지만 실패다. 이런 식으로 `aan` 직전 위치까지 진행한다. (두 번째 `s` 직후 지점까지를 시작으로 해서 정규표현식 `a*?n`을 찾지 못했다는 의미이다.) `aan` 직전 위치에서 다시 시작해보자. 이 위치는 `a`가 0번 반복된 지점으로 생각할 수 있다. 하지만 다음 글자 `n`은 일치하지 않는다. `a`가 1번 반복할 수 있다. 그리고 `n`을 찾는다. 실패다. `a`가 2번 반복할 수 있다. 그리고 글자 `n`을 찾는다. 일치한다. 그 결과는 `aan`이다. 

# %% [markdown]
# 그러니까 `a*?n`는 가능한 모든 결과 중에서 가장 짧은 결과를 내놓는 것이 아님을 이해할 필요가 있다. 문자열 내에서 순차적으로 정규표현식 패턴을 찾고, 정규표현식 내에서도 순차적으로 문자열로 대응시키게 된다.

# %% [markdown]
# 탐욕방법과 게으른 방법의 차이점은 `a{1,3}n`에서 `a`를 찾은 후 `a`의 반복을 먼저 찾을 것이냐 아니면 `n`을 먼저 찾을 것이냐의 문제이다.

# %% [markdown]
# `+`는 1번 이상 반복된다는 의미고, 마찬가지로 `?`를 붙여 게으른 방법으로 사용할 수 있다.

# %% [markdown]
# `?`는 0번 또는 1번 반복된다는 의미이다. 선택적으로 존재하는 경우에 쓸 수 있다. 예를 들어 1 이하의 수를 소수점으로 표시하면 소수점 앞의 0을 쓰기도 하고 안 쓰기도 하지 않는가? 그런 경우에 쓸 수 있다. 그리고 `??`는 게으른 `?`라고 생각할 수 있다.

# %% [markdown]
# ### 문자집합을 구성하는 `[`과 `]`

# %% [markdown]
# `가` 또는 `갔`를 정규표현식으로 어떻게 나타낼까?

# %%
txt1 = '너 어디 가니?'
txt2 = '거기.'
txt3 = '올 때 물 좀 사 오지.'

# %%
re.search('가|갔', txt1), \
re.search('가|갔', txt2), \
re.search('가|갔', txt3)

# %% [markdown]
# `가` 또는 `갔` 또는 `오` 또는 `왔`은 어떻게 할까?

# %%
re.search('가|갔|오|왔', txt1), \
re.search('가|갔|오|왔', txt2), \
re.search('가|갔|오|왔', txt3)

# %% [markdown]
# 이렇게 `|`를 사용할 수도 있지만, `|`는 보통 두 문자 이상의 문자열 중에서 하나를 나타낼 때 자주 쓴다. 그리고 앞에서와 같이 한 문자를 선택하는 경우에는 `[`,`]`을 써서 다음과 같이 쓴다.

# %%
re.search('[가갔오왔]', txt1), \
re.search('[가갔오왔]', txt2), \
re.search('[가갔오왔]', txt3)

# %% [markdown]
# `[`, `]`는 여러 문자 중의 하나를 의미할 때 `|`가 지나치게 많아지는 것을 방지한다. 알파벳 대문자를 찾아보자.

# %%
patt1a = 'A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|Y|W|X|Z'
patt1b = '[ABCDEFGHIJKLMNOPQRSTUVWXYZ]'
txt1 = 'sam smith'
txt2 = 'Sam Smith'
txt3 = 'meet SS.!'

# %% [raw]
# re.search(patt1a, txt1), \
# re.search(patt1b, txt1)

# %%
re.search(patt1a, txt2), \
re.search(patt1b, txt2)

# %%
re.search(patt1a, txt3), \
re.search(patt1b, txt3)

# %% [markdown]
# 그리고 `|`는 우선 순위가 마지막이라 다른 문자열과 연결하려면 괄호로 묶어야하는 불편함이 있다. (여기서 당연한 듯 말하고 있지만 정규표현식에서 괄호는 우선순위를 바꾸기 위해 사용할 수 있다.) 그에 반해 `[`,`]`는 우선 순위가 최우선이다. 여기서 `\.`는 문자 마침표(`.`)를 나타낸다. 

# %%
patt2a = r' (A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|Y|W|X|Z)+\.'
patt2b = r' [ABCDEFGHIJKLMNOPQRSTUVWXYZ]+\.'

# %%
re.search(patt2a, txt1), \
re.search(patt2b, txt1)

# %%
re.search(patt2a, txt3), \
re.search(patt2b, txt3)

# %% [markdown]
# 그리고 `[`,`]`를 사용하면 유니코드 코드포인트가 연속되는 문자들은 한꺼번에 다음과 같이 지정할 수 있다는 장점도 있다.

# %%
patt2c = r' [A-Z]+\.'

# %%
re.search(patt1a, txt3), \
re.search(patt2c, txt3)

# %% [markdown]
# 이 밖에도 문자집합 `[`,`]`를 정확히 사용하기 위해서는 필요한 사항은 뒤에서 좀더 자세히 설명된다.

# %% [markdown]
# ### `\` : 정규표현식의 탈출 문자
#
#

# %% [markdown]
# 시작이 `r`로 시작하지 않는 따옴표 안에서 `\`는 다음 문자와 합쳐져 제어 문자 등을 나타낸다. 정규표현식 안에서도 `\`는 다음 문자와 합쳐져 새로운 의미를 나타낸다. 다음의 표를 보자. 좀더 구체적인 의미는 뒤에 설명된다. 

# %% [markdown]
# | 정규표현식 | 의미 |
# |:--------|:-------|
# |`\A`,`\Z`    | 문자열의 처음과 끝 |
# |`\b`,`\B`    | 단어 경계, 단어 비경계 |
# |`\d`,`\D`      | 숫자와 비숫자 |
# |`\s`,`\S`    | 공백문자와 비공백문자 |
# |`\w`, `\W`   | 단어를 구성하는데 사용되는 문자(문자와 숫자) |
#

# %% [markdown]
# 이 밖에도 따옴표 안에서 쓰이는 탈출 문자가 정규표현식 안에서도 동일한 기능의 탈출 문자로 사용된다(다음표).

# %% [markdown]
# | 정규표현식 | 의미 |
# |:--------|:-------|
# |`\a`    |  |
# |`\b`    | **b**ackspace |
# |`\f`      | **f**eedforward |
# |`\n`    | **n**ewline |
# |`\N{}`    | 문자 이름(**N**ame) |
# |`\r`    | carriage **r**eturn |
# |`\t`    | **t**ab |
# |`\u`(`\uhhhh`)      | **u**nicode codepoint 16진수 `hhhh`|
# |`\U`(`\Uhhhhhhhh`)    | **U**nicode codepoint 16진수 `hhhhhhhh`|
# |`\v`    | **v**ertical tab |
# |`\x`(`\xhh`)   |  |
# |`\\`    | 문자 `\` |

# %% [markdown]
# 이제 정규표현식에서 `\` 뒤에 올 수 있는 문자를 확인해보자.

# %% [markdown]
# **a** ***b*** c *d* e **f** g h i j k l m **n** o p q **r** *s* **t u v** y *w* **x** z
#
# *A B* C *D* E F G H I J K L M **N** O P Q R *S* T **U** V *W* X Y *Z* \

# %% [markdown]
# 이때 `\b`를 주목해보자. 위에서 `\b`는 단어 경계(word **b**oundary)라고 했는데, 아래에서는 백스페이스(**b**ackspace)라고 했다. 무엇이 맞을까?

# %% [markdown]
# 이에 대해 말하기 전에 먼저 정규표현식 `\A` 등은 모두 `[`, `]` 안에서의 의미를 나타낸다. `[`,`]` 안에서 문자 `\` 또는 `A`를 나타내려면 `[\\A]`로 써야 한다. `[\A]`는 오류를 발생시킨다. `[`, `]`의 의미를 생각한다면 이해할 수 있다. `[`,`]`는 그 안에 특정한 문자를 나열하여 문자 집합을 생성한다. `\A`는 특정한 집합이 아니지 않은가?

# %% [markdown]
# 반면 두 번째 테이블의 `\a`, `\t` 등은 모두 특정한 문자를 나타내면 `[`, `]` 안에서도 다른 문자와 동일한 방식으로 사용할 수 있다.

# %% [markdown]
# 결론적으로 `\A` 등과 같은 정규표현식은 `[`,`]` 밖에서만 사용할 수 있고, `\a` 등과 같이 특정한 문자를 나타내는 정규표현식은 `[`,`]` 안과 밖에 모두 사용할 수 있다. 유일한 예외는 `\b`이다. `\b`는 `[`, `]` 밖에서는 단어 경계(word **b**oundary)를 의미하고, `[`, `]` 안에서는 백스페이스(**b**ackspace)를 의미한다.

# %% [markdown]
# ### `(`, `)`

# %% [markdown]
# 정규표현식에서 `(`, `)`는 굉장히 다양한 의미로 사용된다.
#
# #### 우선순위 변경과 부분 문자열 저장 
#
# 1. 오로지 우선순위 변경을 위해
#    - 비저장 부분 문자열 : `(?: ... )`
# 2. 우선순위 + 부분 문자열 저장
#    - 순번 부분 문자열 저장 : `( ... )` -> 참조시 `\1`, `\2`, ...
#    - 이름 부분 문자열 저장 : `(?P<name> ... )` -> 참조시 `(P=name)`
# 3. 부분 문자열 존재 여부에 따른 선택 : `(?(id/name)yes-pattern|no-pattern)`
#
# #### 주석, 모드
#
# 1. 주석 : `(?# ... )`
# 2. 정규표현식 모드 설정 : `(?aiLmsux)`
#
# #### 주변 확인
#
# 1. Lookahead : positive `(?= ...)`, negative `(?=!...)`
# 2. Lookbehind : positive `(?<...)`, negative `(?<!...)`
#
#
#
#

# %% [markdown]
# 가장 먼저 알아둘 것은 `(`,`)`는 안에 정규표현식이 있다면, 정규표현식을 먼저 해석한 후 `(`, `)` 밖의 정규표현식을 해석하게 된다는 점이다. 예를 들어 정규표현식 `a.*(a|b)`는 (`a`로 시작하고 `a` 또는 `b`로 끝나는 패턴)을 찾는다. 만약 `a.*a|b`로 쓴다면 (`a`로 시작하고 `a`로 끝나는 패턴)이나 (`b`)를 찾게 된다.

# %%
txt = 'before abba'

# %%
re.search('a.*(a|b)', txt)

# %%
re.search('a.*a|b', txt)

# %% [markdown]
# 괄호는 우선순위를 바꾸는 역할뿐 아니라 괄호 안에 정규표현식에 해당하는 문자열을 저장하여 다음에 쓸 수 있게 한다.

# %%
patt = r"([ab]).*\1"

# %% [markdown]
# 위의 정규표현식은 괄호 안의 `[ab]`(문자 `a` 또는 문자 `b`)에 해당하는 문자열을 찾아 저장한다. 그리고 번호를 매긴다. 첫 번째 괄호이므로 첫 번째로 저장된 문자열이며 이는 정규표현식에서 `\1`로 표시할 수 있다.

# %% [markdown]
# 그래서 위의 정규표현식은 `patt`은 `a.*a|b.*b`로 바꿔쓸 수 있다.

# %% [markdown]
# 하지만 `(ab+?c).*\1`을 `\1`을 쓰지 않고 정규표현식으로 표현하려면  `abc.*abc|abbc.*abbc|abbbc.*abbbc`와 같이 한없이 길어진다. 따라서 이런 경우에는 괄호로 부분문자열을 저장하고 `\1`, `\2` 등으로 재활용하는 방식이 필요하다.

# %% [markdown]
# 위의 경우 만약 재활용할 필요가 없다면 `(?:ab+?c)`로 쓸 수 있다. 이 경우 정규표현식 `ab+?c`에 해당하는 문자열은 `\1` 등으로 재활용될 수 없다. `\1` 등으로 재활용할 수 있는 문자열의 갯수는 99개까지로 한정되어 있기 때문에 저장해야 하는 갯수가 많다면 저장하지 않고 우선순위 변경만 필요하다면 `(?:)`를 사용해야 한다.

# %% [markdown]
# 다음의 예는 9개 이상의 문자열을 저장하려면 `\1`, `\2`, ... , `\9`, `\10`, `\11` 등으로 저장된 문자열을 재활용할 수 있음을 보여준다.

# %%
patt = r"(w|W)(o|O)(n|N)(d|D)(e|E)(r|R)(f|F)(u|U)(l|L) (t|T)(o|O)(d|D)(a|A)(y|Y) \1\2\3\4\5\6\7\8\9 \10\11\12\13\14"

# %%
re.search(patt, "Wonderful Today wonderful today")

# %%
re.search(patt, "Wonderful Today Wonderful Today")

# %% [markdown]
# 순번을 사용하는 것이 불편하다면 저장된 문자열에 이름을 지어줄 수 있다.

# %%
patt1a = r"(?P<first>w|W)(?P<middle>o|O)(?P<last>n|N) (?P=first)(?P=middle)(?P=last)"

# %%
re.search(patt1a, "Won Won"), \
re.search(patt1a, "Won won")

# %% [markdown]
# 정규표현식 `patt`에서 `(?P<first>w|W)`는 본질적으로 `(w|W)`과 같은 기능을 한다. 단지 저장되는 문자열의 이름을 `first`로 정해준다. 이 저장된 문자열은 여전히 순번 `\1`으로 재활용될 수 있다. 그리고 `(?P=first)`와 같이 앞에서 지정한 이름 `first`로도 재활용될 수 있다.

# %%
patt1b = r"(?P<first>w|W)(?P<middle>o|O)(?P<last>n|N) \1(?P=middle)(?P=last)"

# %%
re.search(patt1b, "Won Won"), \
re.search(patt1b, "Won won")

# %% [markdown]
# 여기서 이런 식의 작명과 재활용이 가능한 이유는 평상시에 괄호 안에 첫 글자로 `?`가 나올 일이 없기 때문이다. 만약 `?` 없이 `(P=first)`를 쓴다면 이게 문자열 `P=first`를 찾으라는 의미이다.

# %% [markdown]
# 이렇게 저장된 문자열은 재활용될 수 있다. 마지막으로 저장된 문자열을 활용하는 또 다른 방법은 다음과 같은 형식을 활용하는 것이다.

# %% [raw]
# (?(id/name)yes-pattern|no-pattern)

# %% [markdown]
# 위의 형식 만약 순번 `id`로 저장된 문자열이 있다면 `yes-pattern`, 그렇지 않다면 `no-pattern`을 의미한다.

# %% [markdown]
# 다음에서 여러 문자열(`'소리는'`, `'소리은'` 등)에서 한글 보조사 "은"/"는"을 정확하게 사용한 문자열을 찾고자 한다. 한글 보조사 "은"/"는"은 앞에 오는 단어가 종성이 존재하는지에 따라 달라진다. 이를 확인하기 앞에서 소개한 유니코드 decomposition을 사용한다. `unicodedata.normalize('NFKD', x)`를 사용하면 한글 문자열 `x`의 각 문자를 초성/중성/종성으로 분할한다.   

# %%
import unicodedata

# %%
x = '한글'

# %%
y = unicodedata.normalize('NFKD', x)

# %%
from mypack.utils import unicode_info

# %% [raw]
# %load_ext autoreload
# %autoreload 2

# %%
unicode_info(y)

# %% [markdown]
# 위에서 문자열 `y`를 출력하면 문자열 `x`와 동일하지만 구성은 다르다. 문자열 `x`는 한글 한 글자씩 구성되어 있으며(`unicode_info(x)`를 해보자), 문자열 `y`는 한글이 분해되어 초성,중성,종성으로 구성되어 있다.

# %% [markdown]
# 다음의 `patt_jongseong`, `patt_jungseong`은 한글 중성과 종성을 나타내는 정규표현식이다.

# %%
patt_jongseong = r'[\u11a8-\u11ff\ud7cb-\ud7fb]'
patt_jungseong = r'[\u0ebf-\u0f06\ud1c0-\ud1d6]'

# %%
print('\u11a8\u11a9 ... \u11ff, \ud7cb\ud7cc ... \ud7fb')
print('\u0ebf\u0ec0 ... \u0f06, \ud1c0\ud1c1 ... \ud1d6')

# %% [markdown]
# 지원되는 폰트에 따라 출력 결과가 이상할 수 있으므로 다시 `unicode_info()`를 활용해서 확인하거나 Unicode chart에서 확인해보자.

# %%
unicode_info('\u11a8\u11a9\u11fe\u11ff \ud7cb\ud7cc\ud7fa\ud7fb')

# %% [markdown]
# 이제 종성이 존재하는 경우에 `은`, 그렇지 않을 경우에 `는`을 다음의 패턴을 사용하여 정규표현식으로 나타내는 방법을 생각해보자. 

# %% [raw]
# (?(id/name)yes-pattern|no-pattern)

# %% [markdown]
# 저자가 생각해 낸 방법은 다음과 같다.

# %%
patt2a = f'(({patt_jongseong})|({patt_jungseong}))(?(2)은|는)'
print(patt2a)

# %% [markdown]
# 마지막에 `(?(2)은|는)`을 정규표현식으로 해석하자면 `2`번째 괄호로 시작된 문자열이 저장되어 있다면 `은`, 그렇지 않다면 `는`을 의미한다. 그렇다면 `2`번째로 시작하는 괄호는 `(([\u11a8-\u11ff\ud7cb-\ud7fb])...`에서 `([\u11a8-\u11ff\ud7cb-\ud7fb])`를 가리키고 이는 분해된 문자열에서 종성을 의미한다. 

# %%
txt1 = '소리는'
txt2 = '소리은'
txt3 = '집는'
txt4 = '집은'

# %%
xs = [txt1, txt2, txt3, txt4]

# %%
ys = [unicodedata.normalize('NFKD', x) for x in xs]
ys

# %%
import re

# %%
patt2a = unicodedata.normalize('NFKD', patt2a)

# %%
[re.search(patt2a, y) for y in ys]

# %% [markdown]
# 여기서 분해된 문자열에서 `은` 또는 `는`을 찾기 때문에 정규표현식의 `은`과 `는`도 분해를 해야함을 주지할 필요가 있다. 

# %% [markdown]
# #### `(`, `)`의 기능 : 주석, 모드
#
# * 주석 : `(?# ... )`
# * 정규표현식 모드 설정 : `(?aiLmsux)`

# %% [markdown]
# 정규표현식에 `(?#`과 `)`로 둘러싸인 부분은 주석으로 기능하기 때문에 정규표현식에 어떤 영향도 주지 못한다.

# %%
txt = 'abcdefg'
patt1a = 'abc(?#alphabet starts with abc)defg(?#till g)'
patt1b = 'abcdefg'

# %%
re.search(patt1a, txt)

# %%
re.search(patt1b, txt)

# %% [markdown]
# `patt1a`에서 `(?#`과 `)`로 둘러싸인 부분을 제거해보자.

# %% [markdown]
# 뒤에서 자세히 다루겠지만 `re.sub(pattern, repl, string)`은 `string`에서 정규표현식 패턴 `pattern`을 찾아 `repl`로 치환한다. 

# %%
re.sub('[(][?]#[^)]*?[)]', '', patt1a)

# %% [markdown]
# 정규표현식을 읽어보자. `[(]`는 문자 왼쪽 괄호, `[?]`는 문자 `?`를 의미하고, `#`는 문자 `#`, `[^)]`는 오른쪽 괄호(`)`)를 제외한 모든 문자를 의미한다. `*?`는 게으르게 0번 또는 그 이상 반복, `[)]`는 오른쪽 괄호를 의미한다. 따라서 이들을 모두 합친 정규표현식 `[(][?]#[^)]*?[)]`는 `patt1a`와 같은 정규표현식의 주석 부분을 의미한다. 그리고 `patt1a`의 모든 주석부분을 제거하니 `patt1a`는 `patt1b`와 같음을 확인할 수 있다.

# %% [markdown]
# #### 정규표현식 모드 설정 : `(?aiLmsux)`

# %% [markdown]
# 앞에서 `re.search(, flags = re.DOTALL)`을 함으로써 정규표현식이 작동하는 모드를 변경할 수 있었다. 하지만 `flags=`는 정규표현식과 별도로 지정하는 것이라는 번거로움이 있다. `(?`,`)` 안에 `a`, `i`, `L`, `m`, `s`, `u`, `x` 등 정규표현식의 모드를 나타내는 문자를 써서 `flags=`를 사용하지 않고 바로 정규표현식의 모드를 정해줄 수도 있다. 예를 들어 `(?s)`는 `re.DOTALL`과 동일한 기능을 한다. 이렇게 정규표현식 안에 모드를 변경할 경우 정규표현식의 종류에 따라 그 이후의 정규표현식에만 적용되는 경우도 있는데[^remode], 파이썬의 `re` 모듈은 전체 정규표현식에 적용이 되며 `(?s)`와 같은 모드 변경은 정규표현식의 처음에 있어야 한다. `flags=`로 지정하는 방법과 정규표현식 내의 표현을 비교해보자.
#
# [^remode]: 예를 들어 `(?s+)`는 `.`가 모든 문자를 의미하고 , `(?s-)`는 `.`가 새줄문자(`"\n"`)를 제외한 모든문자를 의미해서 `(?s+).(?s-).`라고 쓰면 "모든 문자 1개와 새줄문자를 제외한 모든 문자 1개"를 나타내게 된다.

# %% [markdown]
# | 플래그     |     의미    |
# |:---------|:-----------|
# | `re.ASCII` 또는 `re.A` | `\w`, `\b` 등의 정규표현식이 ASCII 문자에만 대응 |
# | `re.DOTALL` 또는 `re.S` | 정규표현식 `.`가 새줄문자를 포함한 모든 문자와 대응 |
# | `re.IGNORECASE` 또는 `re.I` | 알파벳의 대소문자 구분 무시 |
# | `re.LOCALE` 또는 `re.L` | `\w`, `\b` 등의 정규표현식이 로케일을 고려하도록 함. 사용이 권장되지 않음[^relocale] |
# | `re.MULTILINE` 또는 `re.M` | `^`, `$`이 한 줄 안에서 시작과 끝을 나타냄 |
# | `re.VERBOSE` 또는 `re.X` | 가독성을 위해 `[ ]` 또는 `\ `을 제외하고 무시. `#`는 주석 |
#
#
# [^relocale]: https://docs.python.org/3.8/howto/regex.html
#
#

# %%

# %%
txt = 'abcdefg'
re.search('(?i)CD', txt)

# %%

# %%

# %%
re.search(f"({patt_jongseong})은", ys[1])

# %% [markdown]
# 물론 한가지 방법은 다음과 같이 풀어 쓰는 것이다.

# %%
re.search('a.*A|b.*B', "a team A")

# %%
문제는 

# %% [markdown]
#

# %%

# %%

# %%

# %%

# %%
re.search(r'\t', '\t')

# %%

# %%

# %%

# %%

# %%
re.findall('.', txt)

# %%

# %%

# %%
re.search('.', txt, flags = re.MULTILINE), \
re.search('.', txt)

# %%
dir(re)

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ## TO-DO
#
# * `x = regex.findall('(a.c).*(ab.)', 'abc...abc \n  axc...abc \n adc...abd')`
# 를 생각할 때, 문장들을 list로 입력하는 것과 그냥 `'\n'.join()`으로 넣는 것과 차이? 속도?
#
# back-tracking(?)의 한계가 있으니, 작은 단위로 쪼개는 게 나을 듯? 아니면 multiline으로 해도 비슷하지 않을까?
#
# * `Series.str`에서 정규표현식을 받는 메쏘드와 그렇지 않은 메쏘드?
#
# * `Series.str.____` 꼴에서 각 functions의 용례?
#   capitalize, casefold, cat, center, contains, count, decode,
#   encode, endswith, extract, extractall, find, findall, fullmatch,
#   get, get_dummies, index, isalum, isalpha, isdecimal, isdigit
#   islower, isnumeric, isspace, istitile, isupper, join,
#   len, ljust, lower, lstrip, match, normalize, pad, partition, repeat,
#   replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, slice, 
#   slice_replace, split, startswith, strip, swapcase, title, translate,
#   upper, wrap, zfill
#   - regex.compile('[.]str[.](capitalize|casefold|cat|center|contains|count|decode|encode|endswith|extract' + \
#                             'extractall|find|findall|fullmatch|get|get_dummies|index|isalum|isalpha|isdecimal|' + \
#                             'isdigit|islower|isnumeric|isspace|istitle|issuper|join|len|ljust|lower|lstrip|' + \
#                             'match|normalize|pad|partition|repeat|replace|rfind|rindex|rjust|rpartition|rsplit|' + \
#                             'slice|slice_replace|split|startswith|strip|swapcase|title|translate|upper|wrap|' + \
#                             'zfill)')
#
# * java 명령 is...와 unicode property를 비교하던 싸이트?
#   https://www.fileformat.info/info/unicode/char/2028/index.htm
#
# * os.path.join과 같은 directory와 filename 관련 함수를
#   regex로 나타내려면? .split('/') 등
#
#
# ### Reading list
#
# * Python Documentation
#     - [정규식 HOWTO](https://docs.python.org/ko/3/howto/regex.html)
#     - [re-syntax](https://docs.python.org/3/library/re.html#re-syntax)
#     - [regular-expressions.info](https://www.regular-expressions.info/tutorial.html)
# * Unicode Groups
#     - Testing
#                   
# * [Unicode Charater Properties](https://www.php.net/regexp.reference.unicode)
#     - https://www.regular-expressions.info/unicode.html#category
# * [Unicode Regular Expressions](http://unicode.org/reports/tr18/)

# %% [markdown]
# ### Reference
# * [regex101.com](regex101.com)
# * [debuggex.com](debuggex.com)

# %%
import pandas as pd

# %%
x = pd.Series(['a', 'bb', 'ccc'])

# %%
from mypack.utils import dir2

# %%
print(pd.Series.str.__doc__)

# %%
dir2(x)

# %% [markdown]
# # 12. 정규표현식

# %% [markdown]
# ### 전체 구조
#
# * 도입부
#   - 패턴 매칭이 필요한 경우
#     - 탐지(detect)
#     - 치환(replace)
#     - parsing
#     - 필요한 정보 추출
#     - 
#     
#    
#
# * 공통적인 Regular expression
#   - `[]` : 문자열 집합
#   - `*`, `+`, `?`, `{m,n}`, `*?`, `+?`, `??` : 수량, lazy-greedy-하나 더?
#     
#   - `표현식|표현식` : OR
#   - `(표현식)` : groups - `\1` (groups are numbered starting from 1, 헷갈릴 듯...)
#     - `(?P<그룹이름>표현식)` - `(?P=그룹이름)`
#     - `(?:표현식)` : non-capturing group
#   - 옵션 설정
#     - `(?aiLmsux)`
#     - 
#   - `()...\1` : pairing
#   - `(#...)` : comments
#   - Look around
#       - `(?=...)`, `(?!...)`
#       - `(?<=...)`, `(?<!...)`
#   - if-else
#       - `(?(id/name)yes-pattern|no-pattern)` : 그룹이름으로 P를 쓰면 안 되겠네? 괄호가 있으니 괜찮다?
#       
# * 기능을 기준으로 함수?
#
#   
# * 다른 정규표현식과의 차이 : `regex` 모듈, 판다스 시리즈의 `.str.<method>`, R
#   - escape letters
#   - mode
#   - 
# * 특별히 주의할 점
#   - greedy matching : `<[^<]+>`
#   - back tracking
#   - look around에 들어가는 제약
#

# %%
txt = ":[:]"
re.search("[[:punct:]]", txt)

# %% [markdown]
# ### 
#
# * 위치 
#   - `^`(문자열의 처음, 줄의 처음(multiline))
#   - `$`(문자열의 마지막, 줄의 마지막(multiline))
#   - `\A`(문자열의 처음)
#   - `\Z`(문자열의 마지막)
#   - `(?<   )`(Positive Lookbehind)
#   - `(?<!   )`(Negative Lookbehind)
#   - `(?=   )`(Positive Lookahead)
#   - `(?!   )`(Neagative Lookahead)
#   - `\b`(Word boundary)
#   - `\B`(No Word boundary)
#   - 
#     
# * 문자 집합 
#

# %%

# %%
txt = "3a"

# 1.*
# 2\d{2}
# 3\w

re.search(r"((1)|(2)|(3))(?(2).*)(?(3)\d{2})(?(4)\w)",txt)

# %% [markdown]
# ## 아이디어
#
# * 두 가지 반복 
#   - 패턴 반복
#     - 예 : 정수 반복 : `\d+(,\s+\d+)*`
#   - 그래도 반복
#     - 예 : `(\d+)(,\s+\1)*`

# %%
txt1 = "13,24, 342,  22"
txt2 = "13,  13,13,13"

# %%
import re

# %%
print(re.search(r"^\d+(,\s*\d+)*$", txt1))
print(re.search(r"^\d+(,\s*\d+)*$", txt2))

# %%
match = re.finditer(r"^\d+(,\s*\d+)*$", txt1)
# 이렇게 하면 ()*의 반복되는 패턴에 매칭한 문자열을 알 수 없다????
for x in match:
    print(x.groups())

# %%

# %%
match = re.finditer(r"^(\d+)(,\s*(\d+))?(,\s*(\d+))?(,\s*(\d+))?(,\s*(\d+))?$", txt1)
for x in match:
    for xsub in x.groups():
        print(xsub)


# %%
print(re.search(r"^(\d+)(,\s*\1)*$", txt1))
print(re.search(r"^(\d+)(,\s*\1)*$", txt2))

# %%
re.findall(r"^\d+(,\s*\d+)*$", txt1) # 왜 결과가 다른 듯 보이는가?

# %%

# %%
# unicode에서는 괜찮은 escape letter, bytes에서는 안 되는 escape letter

# %% [markdown]
# ## 몇 가지 caveats

# %%
x = "\032\033"

# %%
re.search("\\032", x)

# %%
re.search(r"\032", x)

# %%
re.search(r"[\32]", x)

# %%
re.search(r"[\2]", "\x02")

# %%

# %%

# %%

# %% [markdown]
# 정규표현식은 화일 내용에서 특정한 패턴의 문자열을 찾기 위해 사용된다. linux, ubuntu 등에서는... windows에서도 ack를 사용할 수 있다. powershell에서 `choco install ack`를 실행하자

# %% [markdown]
# python에서는 정규표현식을 활용하는 가장 기본적인 방법은 기본 모듈인 `re` 모듈을 사용하는 것이다. `re` 모듈의 정규표현식은 Perl의 정규표현식과 비슷하지만 완전히 동일하지는 않다. (자세한 차이점은 뒤에서 설명된다.) `re` 모듈의 문자열과 패턴은 `str` 또는 `bytes` 타입을 모두 사용할 수 있지만 두 타입을 섞어 쓸 수는 없다.

# %%
import re
import regex
import numpy as np
import pandas as pd

# %%

re.findall('[Pp]ython', 'Which do you think is better, R or Python? A python is a kind of snakes, I guess.')

# %%
patt = '[Pp]ython'
sent = 'Which do you think is better, R or Python? A python is a kind of snakes, I guess.'

# %%
re.findall(patt, sent)

# %%
bPatt = patt.encode('UTF-8')
bSent = sent.encode('UTF-8')

# %%
bPatt, bSent

# %%
re.findall(bPatt, bSent)

# %% [markdown]
# 정규표현식을 위해 `regex` 모듈을 사용할 수도 있다. `regex`는 `re`의 확장판으로 생각할 수 있다.
# `re`와 호환되지만, 더 많은 기능을 지원한다.
#
# 정규표현식을 파이썬에서 따옴표 안에 표현하기 위해서는 백슬래쉬(`\`)을 중복해서 사용해야 하는 불편이 있다.
# 왜냐하면 따옴표 안에서 탈출 문자인 `\`는 문자 그대로의 `\`를 나타내기 위해서는 `"\\"` 또는 `'\\'`로 써야 하기 때문이다.
#
# raw string을 사용하면 이런 불편을 해결할 수 있다. 따옴표 바로 앞에 `r`로 붙여주면 `\`는 더이상 따옴표 안에서 
# 탈출 문자로 기능하지 않고 문자 그대로의 `\`를 의미한다. 다시 말해 `\`를 나타내기 위해 `"\\"`로 쓸 필요없이
# `"\"`로 쓸 수 있다. 정규표현식에서는 `\`가 자주 나타나기 마련이므로 raw string으로 나타낸 정규표현식은
# 짧고 간결하게 표현된다. 
#
#     python에서 `"\\"`은 문자 `\`을 나타낸다. 이 결과를 다시 정규표현식 해석한다면, [ESC](탈출문자)가 된다.
#     python에서 `"\\\\"`은 문자열 `\\`을 나타내고. 이 결과를 다시 정규표현식 해석한다면, 문자 `\`가 된다.
#
#     반면 `r"\"`는 곧바로 문자 `\`를 의미한다. `r"\"`는 정규표현식으로 해석하면, [ESC](탈출문자)가 된다.
#     마찬가지로 `r"\\"`는 문자 `\\`를 의미하고, 정규표현식은 문자 `\`로 해석한다. 

# %% [markdown]
# 정규표현식은 여러 변종(ERE, PCRE1, PCRE2 등)이 존재한다. 그렇다면 Python은 정확하게 어떤 정규표현식을 사용하는가? 공식 문서에 따르면, 펄(Perl)과 비슷한 정규표현식을 사용한다고 한다. 하지만 무엇이 같고 무엇이 다른지에 대한 정확한 설명은 찾을 수 없었다. 정규표현식 전문사이트[^2]에 따르면  파이썬의 `re` 모듈은 펄과 비슷하지만, atomic grouping, possessive quantifiers, Unicode 특성을 사용할 수 없다고 한다. 하지만 이게 무엇을 의미하는가? 그리고 어떤 의미가 있을까?
#
# 특히 중요한 차이는 파이썬의 `re` 모듈이 PCRE(Perl Compatible Regular Expression)과 비슷하지만 완전히 호환되지는 않으며, 특히 유니코드 지원이 되지 않는다는 점일 것이다. 이에 반해 `regex`란 패키지는 PCRE과 좀 더 호환이 되고 다른 부가 기능들도 있기 때문에, 이를 추천하기도 한다[^3].
#
# 판다스 시리즈는 문자열 관련 함수를 벡터화해서 `.str` 액세서(accessor)를 통해 제공하고 있다. 여기에는 정규표현식 함수도 있는데 이때 사용되는 정규표현식은 모듈 `re`의 정규표현식과 같다. 
#
# [^2]: http://www.regular-expressions.info/python.html
# [^3]: https://stackoverflow.com/questions/7063420/perl-compatible-regular-expression-pcre-in-python

# %% [markdown]
# ## 참고 문헌
# * https://docs.python.org/3/library/re.html
# * https://python.readthedocs.io/en/stable/library/text.html
# * 

# %%

# %%
import rpy2.rinterface

# %%
# %load_ext rpy2.ipython

# %% language="R"
# str <- c("인터스텔라의 장면 62.",
#          "부모가 되면[5-7],",
#          "아이들-내 아이는 10살이다.-이 안심하고 자랄 수 있게 하고 싶다.",
#          "2027년 2월 3일.")
# ## 숫자를 나타내는 문자 "1", "2", "3"
# grepl("1", str, fixed=TRUE) | grepl("2", str, fixed=TRUE) | 
#   grepl("3", str, fixed=TRUE) 

# %% [markdown]
# 다음은 python에서 문자열에 `1` 또는 `2` 또는 `3`이 존재하는지를 판정한다. 

# %%
msg = ['인터스텔라의 장면 62.', \
      "부모가 되면[5-7],", \
      "아이들-내 아이는 10살이다.-이 안심하고 자랄 수 있게 하고 싶다.", \
      "2027년 2월 3일."]
[('1' in x or '2' in x or '3' in x) for x in msg]

# %% [markdown]
# `1` 또는 `2` 또는 `3`은 정규표현식으로 `[123]`으로 쓸 수 있다. 다음 `re` 모듈을 사용하여 정규표현식 `[123]`에 해당하는 문자(열)의 존재를 확인한다.

# %%
import re

msg = ['인터스텔라의 장면 62.', \
      "부모가 되면[5-7],", \
      "아이들-내 아이는 10살이다.-이 안심하고 자랄 수 있게 하고 싶다.", \
      "2027년 2월 3일."]
[re.search('[123]',x) is not None for x in msg]


# %%
[re.search('[123]',x) for x in msg]

# %%
# #%conda install regex

# %% [markdown]
# 앞에서 말했듯이 `regex` 모듈을 사용할 수도 있다. `regex` 모듈은 대부분의 경우 `re`를 `regex`로 바꿔서 사용할 수 있다는 장점이 있다. 흔히 말하듯 하위 호환이 가능하다. `re`의 방법에 확장된 방법을 포함한다고 생각하자.

# %%
import regex
[regex.search('[123]', x) is not None for x in msg]

# %% [markdown]
# `re.compile`은 정규표현식을 미리 해석해놓고, 필요할 때 재사용한다.

# %%
pat = re.compile('[123]')
[pat.search(x) is not None for x in msg]

# %%
pat = regex.compile('[123]')
[pat.search(x) is not None for x in msg]

# %% [markdown]
# `re`와 `regex`를 하나의 문자열을 대상으로 작동한다. 
# 앞에서 봤듯이 list comprehension을 통해 리스트의 모든 원소에 대해 적용할 수 있다.
# R의 vector와 비슷한 기능을 담당하는 pd.Series에 대해 정규표현식을 바로 적용할 수는 없을까? 

# %%
import pandas as pd

msgSeries = pd.Series(msg)
msgSeries.str.contains('[123]')

# %%
msgSeries.str.cat(others = pd.Series(['1', '3', '5', '7']))

# %%
msgSeries.str.cat(others = pd.Series(['1', '3', '5', '7']), sep='+')

# %%
msgSeries.str.split('[5-7]')

# msgSeries.str.split(patt, regex=False)
# R의 fixed와 비슷하게, regex=False를 하면 patt는 문자 그대로 문자를 의미하게 된다. 

# %%
# .partition(), .split()와 비슷하지만 처음 나오는 것을 중심으로 한 번만 
# .rpartition()

# %%
# .contains() # 어디라도
# .match()    # 처음부터 시작해서
# .fullmatch() # 처음부터 끝까지

# .replace()  # 대체
# .strip()    # (공란) 제거

# .count()

# .findall()   # re.
# .extract     # capturing groups
# .extractall() 


# 개념
# flags, capturing groups

# 문자열 메소드와 겹치는 부분?
# re의 함수와 겹치는 부분?

# %%
from mypack.utils import summary_set

# %%
import re

# %%
summary_set(set(dir('a')), set(dir(re))) # re와 문자열의 공통 메소드는 split뿐

# %%
summary_set(set(dir('a')), set(dir(msgSeries.str)))

# %%
# 문자열과 공유하는 메소드
# capitalize, casefold, center, count, encode, endswith, find, index, isalnum
# isalpha, isdecimal, isdigit, islower, isnumeric, isspace, istitle, isupper, 
# join, ljust, lower, lstrip, parition, replace, rfind, rindex, rjust, rpartition,
# rsplit, rstrip, split, startswith, strip, swapcase, title, translate
# upper, zfill
# 하지만 문자열은 정규표현식을 사용하지 않음...

# %%
summary_set(set(dir(re)), set(dir(msgSeries.str)))
# re와 pd.Series.str의 공통 메소드
# 
# ['__doc__', 'contains', 'findall', 'fullmatch', 'match', 'split']

# %% [markdown]
# dir(mypack.utils)

# %%
# ?msgSeries.str.find

# %%
# ?msgSeries.str.strip

# %%
# ?msgSeries.str.cat

# %%

# %%
# .str의 정규표현식 관련 함수
# split
# 
# cat, 
# get, join,  
# removeoprefix, removesuffix, wrap
# count, startswith, endswith, 
# findall, extract, extractall
# find, rfind, index, rindex,   

# %%
from mypack.utils import dir2

# %% language="R"
# ## 숫자 "1", "2", "3"을 나타내는 정규표현식 "[1-3]"
# grepl(pattern = "[1-3]", str)

# %%

# %%
[regex.search('[1-3]', x) is not None for x in msg]

# %%
pat = re.compile('[1-3]')
[pat.search(x) is not None for x in msg]

# %%
pd.Series(msg).str.match('[123]')

# %%
import pandas as pd
df = pd.read_feather('books.ftr')
df.shape
sel = df.extent.str.contains(r"\d+\s*p") 
sel.value_counts()
# True     454585
# False    194759
sel.value_counts(dropna=False)
# True     454585
# False    194759
# NaN          14

# you can do
df.extent.str.contains(r"\d+\s*p", na=False) 
# https://m.blog.naver.com/nilsine11202/221914848911

# None이 들어 있는 경우, str.contains()의 결과는 na가 되어 버림...
# pd.Series에서 string의 경우 None이 NA를 대신하는가?
# pd.Series dtype='O'에서 np.nan과 None은 모두 na로 취급되는 듯.
# 예) .isnull() .str.contains(na=True) 등에서...
# 
# 어쨋든
# df.extent.apply(lambda x: x is None)
# df.loc[df.extent.apply(lambda x: x is None), "extent"] = ""

pages = df.extent.str.extract(r"(\d+)\s*p").iloc[:, 0]
type(pages)
pd.to_numeric(pages)

pages = df.extent.str.extract(r"(\d+)\s*p").iloc[:, 0]
pages.astype(int) # int는 NA를 쓸 수 없음으로

pages[~pd.isna(pages)].astype(int).plot(kind='hist')

pages_num = pages[~pd.isna(pages)].astype(int)
df.loc[pages_num[pages_num>1000].index, :]

df.loc[pages_num[pages_num>1000].index, :].extent

# %%
## 참고: 이메일을 확인하는 정규표현식

# https://gist.github.com/gregseth/5582254
# https://news.ycombinator.com/item?id=8360388

# %%

# %% language="R"
# x <- c('I dare to love you', 'I dare to love you!', 
#        'Oh1', 'Dear, my love.2', '!!?!')
# grep('[[:punct:]]', x) # 문장부호가 포함되었는가?

# %% language="R"
# grep('[[:punct:]1]', x) # 문장부호 또는 1이 포함되었는가?
# grep('[1[:punct:]]', x) # 1 또는 문장부호가 포함되었는가?
# grep('[^[:punct:]]', x) # 문장부호가 아닌 문자가 포함되었는가?

# %%
def c(*arg):
    l = []
    for x in arg:
        l.append(x)
    return l


# %%
def which(l):
    s = pd.Series(l)
    i = pd.Series(range(len(l)))
    return i[s]


# %%
which([True, False, False, True])

# %%

# %%
msg = c('I dare to love you', 'I dare to love you!', \
        'Oh1', 'Dear, my love.2', '!!?!')

# %%
msg = ['I dare to love you', 'I dare to love you!', 
       'Oh1', 'Dear, my love.2', '!!?!']
patt1 = re.compile('[[:punct:]]') # '[[:punct:]]'를 사용할 수 없다?! 
[patt1.search(x) for x in msg] # None 은 찾지 못했음을 의미한다.

# %%
patt2 = re.compile('\p{P}') # re에서는 UNICODE category로 사용할 수 없다. 
[patt2.search(x) for x in msg] # None 은 찾지 못했음을 의미한다.

# %%
patt1 = regex.compile('[[:punct:]]') # 반면 regex에서는 POSIX Bracket Expressions을 사용할 수 있다. 
[patt1.search(x) for x in msg] # None 은 찾지 못했음을 의미한다.

# %%
patt1 = regex.compile('\p{P}') # regex에서는 Unicode Category도 사용 가능하다.
[patt1.search(x) for x in msg] # None 은 찾지 못했음을 의미한다.

# %%
import numpy as np

# %%
which([regex.search('\p{P}', x) is not None for x in msg])

# %%
pd.Series(msg).str.contains('\\p{P}') # pd의 str.contains는 "\p{P}"를 지원하지 않는가?
# str.contains()는 unicode를 지원하지 않는가?

# %%
msg

# %%
pd.Series(msg).str.contains('[[:punct:]]')  # POSIX는 지원? 하지만 결과는... 다르다

# %% [markdown]
# ## python의 Regular Expression과 Perl-Compatible RE
# * 참고
# https://stackoverflow.com/questions/7063420/perl-compatible-regular-expression-pcre-in-python
#
# https://stackoverflow.com/questions/12022443/which-regular-expression-flavour-is-used-in-python
#
# [Python RE Overview](http://www.regular-expressions.info/python.html)

# %% [markdown]
# * [Unicode category, mUnicode blocks, Unicode scripts](http://www.regular-expressions.info/unicode.html)

# %% [markdown]
# https://unicode.org/reports/tr18/

# %%
msg

# %%

# %%

# %%
ex = '"Hey, how are you?"\n He asked me, and I murmured."'

# %%
regex.findall('\p{P}', ex)

# %%
regex.finditer('\p{P}', ex)

# %%
regex.fullmatch('\p{P}', ex)

# %%
regex.match('\p{P}', ex)

# %%
regex.purge()  # Clear the regular expression caches

# %%
regex.search('\p{P}', ex)

# %%
regex.split('\p{P}', ex)

# %%
regex.sub('\p{P}', "*", ex)

# %%
regex.subn('\p{P}', "*", ex)

# %%
## 몇 가지 예시 : 마지막 숫자 1 증가시키기
def postfix_add_one(x):
    xsplit = x.split('_')
    nlast = len(xsplit[-1])
    xsplit[-1] = int(xsplit[-1])+1
    #xsplit[-1] = '{:02d}'.format(xsplit[-1])
    xsplit[-1] = ('{:0'+str(nlast)+'d}').format(xsplit[-1])
    return '_'.join(xsplit)

## 수정본
import regex
def postfix_add_one(x):    
    xsplit = x.split('_')
    if regex.match('^[0123456789]+$', xsplit[-1]):
        nlast = len(xsplit[-1])
        xsplit[-1] = int(xsplit[-1])+1
        #xsplit[-1] = '{:02d}'.format(xsplit[-1])
        xsplit[-1] = ('{:0'+str(nlast)+'d}').format(xsplit[-1])
        return '_'.join(xsplit)
    else:
        return '_'.join(xsplit)+'_1'


postfix_add_one('abc_1')
postfix_add_one('MyHomeWork_005')
postfix_add_one('My_Journey_A_001_12')

## Vectorize

def str_postfix_add_one_(xsplit):    
    nlast = len(xsplit[-1])
    xsplit[-1] = int(xsplit[-1])+1
    #xsplit[-1] = '{:02d}'.format(xsplit[-1])
    xsplit[-1] = ('{:0'+str(nlast)+'d}').format(xsplit[-1])
    return '_'.join(xsplit)

## 수정본

def str_postfix_add_one_(xsplit):    
    if regex.match('^[0123456789]+$', xsplit[-1]):
        nlast = len(xsplit[-1])
        xsplit[-1] = int(xsplit[-1])+1
        #xsplit[-1] = '{:02d}'.format(xsplit[-1])
        xsplit[-1] = ('{:0'+str(nlast)+'d}').format(xsplit[-1])
        return '_'.join(xsplit)
    else:
        return '_'.join(xsplit)+'_1'

x = pd.Series(['abc_1', 'MyHomeWork_005', 'My_Journey_A_001_12'])
x.str.split('_').apply(str_postfix_add_one_)


# %%
## ---- tidy=FALSE, results='hold'--------------------------------------------------------------
x <- c('Idaretoloveyou', 'I dare to love you!', 
       'Oh1', 'Dear, my love.1', '!!?!')
grep('\\w', x)
grep('\\W', x)
# vetorize가 되었다는 점이 가장 크게 다르다...

# %% [markdown]
# ### 리스트

# %%
lst = ['Idaretoloveyou', 'I dare to love you!', 
       'Oh1', 'Dear, my love.1', '!!?!']
[i for i,x in enumerate(lst) if regex.search(r'\w', x) is not None]

# %% [markdown]
# ### 넘파이 어레이

# %%
arr = np.array(['Idaretoloveyou', 'I dare to love you!', 
                'Oh1', 'Dear, my love.1', '!!?!'], dtype='O')
#arr = np.array(['Idaretoloveyou', 'I dare to love you!', 
#                'Oh1', 'Dear, my love.1', '!!?!'], dtype=str)

# %%
[i for i,x in enumerate(lst) if regex.search(r'\w', x) is not None]

# %% [markdown]
# ### 판다스 시리즈
# * https://stackoverflow.com/questions/52173161/getting-a-list-of-indices-where-pandas-boolean-series-is-true

# %%
ser = pd.Series(['Idaretoloveyou', 'I dare to love you!', 
                 'Oh1', 'Dear, my love.1', '!!?!'])

# %%
np.where(ser.str.contains(r'\w'))[0]

# %% [markdown]
# ### 판다스 데이터 프레임

# %%
df = pd.DataFrame(
    {'sent':['Idaretoloveyou', 'I dare to love you!', 
             'Oh1', 'Dear, my love.1', '!!?!']})

# %%
df.sent.str.contains(r'\w')

# %%
np.where(df.sent.str.contains(r'\w'))[0]

# %%
## ---- tidy=FALSE, results='hold'--------------------------------------------------------------
grep('\\s', x)
grep('\\S', x) 

# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
x <- c('\a', '\b')
grep('\a', x)
grep('\\a', x)

# %%
lst = ['\a', '\b']
for x in lst:
    print(x)

# %%

# %%
## ---- error=TRUE, tidy=FALSE------------------------------------------------------------------
x <- c('\x1b', '\x1c')
grep('\\e', x)

# %%
lst = ['\x1b', '\x1c']
[print(x) for x in lst]

# %%
## ---- error=TRUE, tidy=FALSE------------------------------------------------------------------
grep('\e', x)

# %%
[i for i,x in enumerate(lst) if regex.search('\e', x) is not None]

# %%
print('\e') # python에서는 R과 달리 에러가 발생하지 않는다!

# %%
print('\')

# %%

# %%
## ---- results='hold', tidy=FALSE--------------------------------------------------------------
x <- c('\u00b1', '\u00b2')
grep('\u00b1', x)
grep('\\x{00b1}', x)
grep('[\u00b1]', x)
grep('[\\x{00b1}]', x) # grep("[\\x{000b1}]", "{")의 결과를 예측해보자.

# %%
lst = ['\u00b1', '\u00b2']
for x in lst:
    print(x)

# %%
ser = pd.Series(lst)

# %%
ser.str.contains('\u00b1')

# %%
ser.str.contains('\\x{00b1}') # '\x{00b1}'꼴의 정규표현식이 작동하지 않는다!

# %%
regex.search('\\X{00b1}', '\u00b1') # 하지만 무슨의미?
# re에서는 불가능하지만 regex에서는 \X{}를 쓸 수 있다. X는 대문자임을 주목하자.
regex.search('\\X{00b1}', '\u00b2')

# %%
regex.search('\\X{00b1}', 'X') # 단순히 글자 \, X, {, 0, 0, b, 1, }은 아닌 듯...

# %%
#grep('[\u00b1]', x)
#grep('[\\x{00b1}]', x) # grep("[\\x{000b1}]", "{")의 결과를 예측해보자.

ser.str.contains('[\u00b1]')

# %%
ser.str.contains('[\\x{u00b1}]') #'\\X{u00b1}'도 안됨

# %%
lst

# %%
[x for x in lst if regex.search('\\x{00b1}', x) is not None] # \\x{}꼴은 re, regex에서 모두 지원하지 않는다!!??

# %%
## ---- results='hold'--------------------------------------------------------------------------
x <- ("Test On. <h> Hi! </h> Test Off.", "<p This is about ... ")
grepl("<.+>", x)
grepl("<.+?>", x)

# %%
lst = ["Test On. <h> Hi! </h> Test Off.", 
       "<p> This is about ... </p>\n<p> Another ... </p>",
       "<img href=This is header ...",
       "<img a >"]
[regex.search('<.+>', x) is not None for x in lst ]

# %%
arr = np.array(lst)
np.array([regex.search('<.+>', x) is not None for x in lst])

# %%
ser = pd.Series(lst)
ser.str.contains('<.+>')

# %%
df = pd.DataFrame(ser, columns = ['sent'])
df

# %%
df.sent.str.contains('<.+>')

# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
regmatches(x, regexpr("<.+>", x)) 
# stringr::str_extract(x, "<.+>")을 사용하면 편하다.
regmatches(x, regexpr("<.+?>", x))

# %%
[regex.findall('<.+>', x) for x in lst]

# %%
lst2 = [regex.findall('<.+>', x) for x in arr]
max_item = max([len(x) for x in lst2])

# %%
lst3 = [x + [np.nan] * (max_item - len(x)) for x in lst2]

# %%
lst3

# %%
np.array(lst3, dtype=str)

# %%
# np.array DOES NOT support np.nan?!!

# %%
ser.str.extract('(<.+>)') # capture group을 괄호로 감싸야 함

# %%
ser.str.extractall('(<.+>)') # . DOES NOT include \n

# %%
ser.str.extractall('(<.+>)', flags=re.DOTALL) # flags에 re.DOTALL를 쓰는 것을 보니 기본적으로 re 모듈을 따르는 듯...

# %%
ser.str.extractall('(<.+?>)') # +? -> Nongreedy

# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
x <- c("hook", "I have a hook", "He shook me")

grepl("hook", x)
grepl("^hook", x)
grepl("hook$", x)

# %%
lst = ['hook', 'I have a hook', 'He shook me']
[re.search('hook', x) is not None for x in lst]
[re.search('^hook', x) is not None for x in lst]
[re.search('hook$', x) is not None for x in lst]

# %%
patt = re.compile('hook$')

# %%
type(patt) == re.Pattern

# %%
isinstance(lst, list)

# %%
isinstance(np.array([1,2,3]), np.ndarray)

# %%
isinstance(np.array([[1],[2],[3]]), np.ndarray)

# %%
np.array([[1]]).ndim

# %%
isinstance([1,2,3], np.ndarray)

# %%
isinstance('str', str)

# %%
isinstance(3, str)

# %%
isinstance(np.array('3'),str)


# %%
def contains(patt, lst):
    if type(patt) == re.Pattern:
        if isinstance(lst, list):
            return [patt.search(x) is not None for x in lst]
        elif isinstance(lst, np.ndarray) and lst.ndim==1:
            return np.array([patt.search(x) is not None for x in lst])
        elif isinstance(lst, str):
            return patt.search(lst) is not None
        else:
            raise ValueError('lst should be list or 1-dim np.array')
    else:
        if isinstance(lst, list):
            return [re.search(patt, x) is not None for x in lst]
        elif isinstance(lst, np.ndarray) and lst.ndim==1:
            return np.array([re.search(patt, x) is not None for x in lst])
        elif isinstance(lst, str):
            return re.search(patt, lst) is not None
        else:
            raise ValueError('lst should be list or 1-dim np.array')


# %%
contains('hook', lst)

# %%
contains('^hook', lst)

# %%
contains('^hook', 'hook is here')

# %%
contains('hook', np.array(lst))  # 하지만 NA가 필요한 곳에서는???

# %%
# 만약 method로 붙이고 싶다면???
# import numpy as np
# np.x = np.array와 같은 방식으로 아예 바꿔버릴 수도...


# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
grepl("\\bhook", x)
grepl("\\Bhook", x)

# %%
contains('\\bhook', lst)

# %%
contains('\\Bhook', lst)

# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
x <- c("abcxabc", "abxab", "abcxab", "abxabc")

grepl("[abc]{2,3}x[abc]{2,3}", x)
grepl("([abc]{2,3})x\\1", x)

# %%
lst = ['abcxabc', 'abxab', 'abcxab', 'abxabc']

contains("[abc]{2,3}x[abc]{2,3}", lst)

# %%
contains("([abc]{2,3})x\\1", lst)

# %%

# %%
## ---------------------------------------------------------------------------------------------
x <- c('abba', '2xx2', 'a22z', 'xaxx')
grepl('(\\w)(\\w)\\2\\1', x)

# %%
lst = ['abba', '2xx2', 'a22z', 'xaxx']
contains('(\\w)(\\w)\\2\\1', lst)

# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
x <- c('axxbba', 'axybba', '2yyxx2', 'cxy22c')
grepl('(\\w)(xx|yy)(\\w)\\3\\1', x)
grepl('(\\w)(?:xx|yy)(\\w)\\2\\1', x)

# %%
lst = ['axxbba', 'axybba', '2yyxx2', 'cxy22c']
contains('(\\w)(xx|yy)(\\w)\\3\\1', lst)

# %%
contains('(\\w)(?:xx|yy)(\\w)\\2\\1', lst)

# %%

# %%
## ---------------------------------------------------------------------------------------------
names <- c('김남수', '하이연', '정진성', '김우주',
           '박구수', '성우장', '박의수')
grep('^박.*수$', names)

# %%
names = ['김남수', '하이연', '정진성', '김우주',
           '박구수', '성우장', '박의수']
np.where(contains('^박.*수$', names))[0]

# %%

# %%
## ---- tidy=FALSE------------------------------------------------------------------------------
names <- c('김남수', '하이연', '정진성', '김우주',
           '박구수', '성우장', '박의수')
sub(pattern='^([김박])(.*)([주수])$', 
    replacement="\\1\\2수\\\\김\\2\\3", names)

# %%

# %%
names = ['김남수', '하이연', '정진성', '김우주',
         '박구수', '성우장', '박의수']
[re.subn('^([김박])(.*)([주수])$', '\\1\\2수\\\\김\\2\\3', x)[0] for x in names]
# pattern에 해당하지 않는 경우는 그대로

# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
grepl("[\\d]", c("3", "d", "\\"))
grepl("[\\d]", c("3", "d", "\\"), perl=TRUE)

# %%
lst = ['3', 'd', '\\']
contains('[\\d]', lst)


# %%

# %%
def func_contains(module):
    def contains(patt, lst):
        if type(patt) == module.Pattern:
            if isinstance(lst, list):
                return [patt.search(x) is not None for x in lst]
            elif isinstance(lst, np.ndarray) and lst.ndim==1:
                return np.array([patt.search(x) is not None for x in lst])
            elif isinstance(lst, str):
                return patt.search(lst) is not None
            else:
                raise ValueError('lst should be list or 1-dim np.array')
        else:
            if isinstance(lst, list):
                return [module.search(patt, x) is not None for x in lst]
            elif isinstance(lst, np.ndarray) and lst.ndim==1:
                return np.array([module.search(patt, x) is not None for x in lst])
            elif isinstance(lst, str):
                return module.search(patt, lst) is not None
            else:
                raise ValueError('lst should be list or 1-dim np.array')
    return contains


# %%
regex.contains = func_contains(regex)
re.contains = func_contains(re)

# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
grepl("(?i)[abc]", c("a", "A", "e", "E"), perl=TRUE)
grepl("(?i)[abc](?-i)[abc]", c("aa", "AA", "ee", "EE"), perl=TRUE)

# %%
re.contains('(?i)[abc]', ['a', 'A', 'e', 'E'])

# %%
#regex.contains('(?i)[abc](?-i)[abc]', ['aa', 'AA', 'ee', 'EE']) # ERROR!
# ERROR
regex.contains('(?i:[abc])(?-i:[abc])', ['aa', 'AA', 'ee', 'EE'])
# WORKS OK, slight difference???

# %%

# %%
## ---- results='hold'--------------------------------------------------------------------------
grepl("^I", c("You\nI\nHe", "I\nYou\nHe"))
grepl("(?m)^I", c("You\nI\nHe", "I\nYou\nHe"), perl=TRUE)

# %%
re.contains('^I', ['You\nI\nHe', 'I\nYou\nHe'])

# %%
regex.contains("(?m)^I", ["You\nI\nHe", "I\nYou\nHe"])

# %%

# %%
# # grepl('\\d+*!*+\\d', c("3+*!*+2", "2!!!2"), perl=TRUE)
# # ## Error in grepl("\\d+*!*+\\d", c("3+*!*+2", "2!!!2"), perl = TRUE) :
# # ##   invalid regular expression '\d+*!*+\d'
# # ## ...
# # grepl('\\d\\Q+*!*+\\E\\d', c("3+*!*+2", "2!!!2"), perl=TRUE)
# # ## [1] TRUE FALSE

# %%
#re.contains('\\d+*!*+\\d', ['3+*!*+2', '2!!!2'])  # ERROR
#regex.contains('\\d\\Q+*!*+\\E\\d', ['3+*!*+2', '2!!!2']) # ERROR
# re or regex does not support \Q, |E
regex.contains('\\d'+re.escape('+*!*+')+'\\d', ['3+*!*+2', '2!!!2'])

# %%

# %%

# %%
## ---- echo=FALSE------------------------------------------------------------------------------
txt <- "여기에 자료가 있습니다. 
자료에는 이름 정보가 숨어 있습니다. 
name = 김이박 이름 정보를 찾았습니까?"
stri_extract(txt, regex='(?<=name [=] )[^ ]*')

# %%
txt = "여기에 자료가 있습니다. \
자료에는 이름 정보가 숨어 있습니다. \
name = 김이박 이름 정보를 찾았습니까?"
re.findall('(?<=name [=] )[^ ]*', txt)

# %%
txt = "여기에 자료가 있습니다. \
자료에는 이름 정보가 숨어 있습니다. \
name = 김이박 이름 정보를 찾았습니까?"
re.findall('name [=] ([^ ]*)', txt)

# %%

# %%
# # ---- results='hold', tidy=FALSE, eval=FALSE--------------------------------------------------
# # stri_replace(txt, regex='(?<=name [=] )[^ ]*', replacement='아무개')
# # str_replace(txt, '(?<=name [=] )[^ ]*', '아무개')

## ---- echo=FALSE------------------------------------------------------------------------------
stri_replace(txt, regex='(?<=name [=] )[^ ]*', replacement='아무개')

# %%
re.sub('(?<=name [=] )[^ ]*', '김아무개', txt)

# %%
help(re.sub)

# %%
re.sub('(.*name [=] )[^ ]*(.*)', '\\1김아무개\\2', txt, flags=re.DOTALL)

# %% [markdown]
# ## BRE vs ERE vs PCRE vs [UTF#18](http://unicode.org/reports/tr18/) vs ICU
#
# * https://stackoverflow.com/questions/7063420/perl-compatible-regular-expression-pcre-in-python
#
# * module `regex` : meets or exceeds the UTF#18 level 1 requirements
# * module `pythone-pcre` : PCRE for python?
#
# R에서 4.0.0 이후에는 `perl=TRUE`로 했을 때 `PCRE2` 라이브러리를 사용한다. R은 기본적으로 Extended POSIX를 사용한다고 했는데, 사실은 Ville Laurikari's TRE engine을 수정해서 사용한다고 한다.(https://www.regular-expressions.info/rlanguage.html)
#
#
#

# %%
import re
re.search('(Prefix|PrefixSuffix)', 'PrefixSuffix')

# %%
re.search('(PrefixSuffix|Prefix)', 'PrefixSuffix')

# %%
import regex

# %%
pattern_string = 'ATAGGAGAAGATGATGTATA'
query_string = 'ATAGAGCAAGATGATGTATA'
r = regex.compile('(%s){e<=2}' % pattern_string)  # error 한계? fuzzy matching
r.match(query_string)
#<regex.Match object; span=(0, 20), match='ATAGAGCAAGATGATGTATA', fuzzy_counts=(0, 1, 1)>

# %%
'(%s){e<=2}' % pattern_string

# %%
pattern_string = '우내놀자'
query_string = '너야놀자너놀자'
r = regex.compile('(%s){e<=2}' % pattern_string)
r.match(query_string)

# %%
query_string[r.match(query_string).start():r.match(query_string).end()]

# %%
mat = r.match(query_string)

# %%
mat.string

# %%
dir(mat)

# %%

# %%
