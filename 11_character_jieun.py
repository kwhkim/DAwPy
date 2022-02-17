# -*- coding: utf-8 -*-
# %% [markdown]
# ### 기본적인 내용
#
# 먼저 다음 링크(https://wikidocs.net/13)에서 기본적인 내용을 확인하세요.
#
# * 문자열 연산하기
#   - `+`, `*`, `%`, `len()`
# * 문자열 인덱싱과 슬라이싱
#   - `s[index]`
#   - `s[start:stop:step]`
# * 문자열 포매팅
#   - `%`
#   - `.format()`
#   - `f''`
# * 문자열 관련 함수들
#   - `.count()
#   - `.find()` & `.index()` 
#     - `.rfind()` & `.rindex()`
#   - `.join()`
#   - `.upper()` & `.lower()`
#   - `.strip()` & `.lstrip()` & `.rstrip()`
#   - `.replace()`
#   - `.split()`

# %% [markdown]
# ### 추가 사항
#
# * 유니코드 관련(파이썬의 기본 타입 `str`은 유니코드를 쓴다. 정확히는 UTF-8?)
#     - 유니코드 관련 함수
#         - https://docs.python.org/ko/3.8/howto/unicode.html
#     - 문자열 정렬
#
# * `string` 모듈?
# * 인코딩 관련
#     - `bytes`, `bytearray` : R의 `raw`와 비슷
#     - 표준 인코딩 라이브러리 : https://docs.python.org/ko/3.8/library/codecs.html#standard-encodings
#
# * 글자 갯수. 화면에 비치는 너비. 바이트 수 구분
#     - `unicodedata.east_asian_width()`
#
# * 포맷팅?
#     - https://realpython.com/python-f-strings/
#     - https://realpython.com/python-string-formatting/
#                                                                                                                                                   

# %% [markdown]
# ## 도입
#
# 여기를 읽고 링크(https://wikidocs.net/13)에서 기본적인 내용을 확인하세요.

# %%
import rpy2.rinterface


# %%
# %load_ext rpy2.ipython

# %% [markdown]
# 컴퓨터에서 문자는 2진문자의 열, 즉 바이트 열로 바뀌어 저장된다. 이를 인코딩이라고 하며 글자와 숫자를 어떻게 대응시킬지를 인코딩으로 결정한다. 아스키(ASCII) 코드는 인코딩 방식 중에서 가장 기본적인 방식으로 미국에서 자주 쓰이는 알파벳과 숫자 등의 문자를 하나의 수와 대응시킨다. ASCII는 American Standard Code for Information Interchange의 약자로 미국 표준에 해당하지만 다른 나라에서도 자국 표준에 포함시켜서 대부분의 인코딩 방법은 ASCII를 포함한다. 
#
# 아스키 코드는 한글 등을 표현할 수 없기 때문에 우리나라는 한글을 표현할 수 있는 자체적인 인코딩 방식을 만들었다. 초기에는 필요에 따라 다양한 인코딩이 만들어졌지만 시간이 지나면서 국가 표준이 만들어지고, 여러 인코딩 방식이 통합되면서 현재 쓰이는 대표적인 방식은 EUC-KR, CP949 등이다. 
#
# 이렇게 나라마다, 그리고 필요에 따라 다양한 인코딩이 사용됨에 따라 문서를 교환할 때 인코딩이 맞지 않는 문제가 발생하게 되었다. 특히 인터넷이 상용되기 전에는 국가 간의 문서 교환이 드물었지만 인터넷이 널리 쓰이고, 이메일을 자주 사용함에 따라 국가를 넘어 전송된 문서가 인코딩이 맞지 않아 깨지는 현상이 늘어났다. 이에 따라 대한 대응으로 만들어진 것이 유니코드(Unicode)이다. 유니코드는 인간이 만든 모든 문자를 하나의 인코딩 방법으로 표현할 수 있도록 고안되었다. 
#
# 파이썬은 버전 3부터 유니코드를 기본 인코딩으로 사용한다. 사실 버전 2와 버전 3의 가장 큰 차이도 문자열을 저장하는 인코딩 방식의 차이라고 볼 수 있다. 파이썬 버전 2에서는 기본적으로 시스템의 기본 인코딩을 사용하였다. 
#
# 파이썬 3에서는 기본 문자열의 타입이 유니코드이며 타입의 이름은 `str` 이다. 비슷하지만 약간 다른 타입으로 `bytes`와 `bytesarray`가 있다. 이에 대해서는 차차 설명하겠다. 
#

# %% [markdown]
# ## 참고 자료
#
# * https://docs.python.org/ko/3/howto/unicode.html
#
#

# %% [markdown]
# ## 문자열 기본

# %% [markdown]
# 파이썬은 문자열과 문자의 구분이 없다. 문자열은 여러 문자가 순차적으로 이어진 것으로 생각할 수 있다. 그래서 리스트와 같은 순차 구조와 동일한 방식으로 다룰 수 있다. 다음은 리스트에서 사용했던 `len()`과 인덱싱 방법을 그대로 문자열에 적용할 수 있음을 보여준다.

# %%
s = 'I love you so much.'

# %%
len(s)

# %%
s[1:4] # 1-번째 부터 4-번째 직전까지 문자

# %%
s[20:3:-3] # 20-번째(또는 마지막) 부터 3-번째 직전까지 3문자마다 1문자

# %%
s[20], s[4]

# %%
s[20:19] # x[20]와 같지만 범위를 넘어가더라도 IndexError가 발생하지 않는다.

# %%
s[-1], s[4]

# %%
from mypack.utils import seq

# %%
help(seq)

# %%
seq(len(s)-1, 4, -3)

# %%
[s[i] for i in seq(len(s)-1, 4, -3)]

# %% [markdown]
# 사실 문자열은 불변(immutable)객체이기 때문에 리스트보다는 튜플과 가깝다.

# %%
s[0] = ''

# %% [markdown]
# ### 몇 가지 연산

# %% [markdown]
# 타입은 가능한 연산과 연산의 의미를 결정한다. 문자열(`str`) 타입에 대해 `+`는 문자열을 연결한다. 

# %%
'We ' + 'go'

# %% [markdown]
# 그렇다면 다른 사칙 연산도 시도해보자.

# %%
'We ' * 'go'

# %%
'We '-'go'

# %%
'We '/'go'

# %%
14 % 3 # 나머지 연산

# %%
'We' % 'go'

# %% [markdown]
# `-`와 `/`는 모두 `TypeError: unsupported operand type(s)`라는 오류가 발생했다. 영문을 해석해보면 주어진 타입에 대해 주어진 연산을 적용할 수 없다는 의미이다. 

# %% [markdown]
# `*`에 대해서는 약간 다른 오류 메세지를 확인할 수 있다. 해석을 해보면 `str` 타입을 `non-int` 타입으로 곱할 수 없다는 의미이다. 그렇다면 `int` 타입으로는 곱할 수 있다는 의미인가?

# %%
'We ' * 3

# %% [markdown]
# 문자열을 정수형으로 곱하면 해당 문자열을 정수번 반복한다는 의미이다. 다음의 결과도 유의하자.

# %%
'We ' * 0

# %%
'We ' * -2

# %% [markdown]
# 정수형과 실수형에서는 나머지를 구하는데 사용하는 연산자 `%`의 경우는 `string formatting`이라는 기능을 위해 쓰인다. 

# %% [markdown]
# `string formatting`이란 말 그대로 문자열을 특정한 형태로 만드는 것을 의미하는데, 특히 실수형처럼 여러 가지 표현이 가능한 경우, 표현방법을 지정하기 위해 쓰인다.

# %%
# 참고 : https://scienceon.kisti.re.kr/srch/selectPORSrchTrend.do?cn=SCTM00071827

# %% [markdown]
# 예를 들어 태양과 지구의 거리는 약 149597870.696 km라고 한다. 그런데 이는 지수표현으로 $1.495\ 978\ 706\ 96\times 10^8$으로 나타낼 수도 있고, 필요에 따라 소수점 이하를 생략하여 $1.49\times10^8$로 표현할 수도 있다.

# %%
d = 149597870.696

# %%
'태양과 달의 거리는 %f km 이다.' % d

# %% [markdown]
# 문자열 `'태양과 달의 거리는 %f km 이다.'`에서 `%f`는 실수형이 어떤 형식으로 문자열로 변환되는지를 나타내기 위해 쓰였다. 만약 소수점 이하를 제거한다거나 지수형으로 수를 나타내고자 한다면 다음과 같이 할 수 있다. 

# %%
'태양과 달의 거리는 %.0f km 이다.' % d

# %%
'태양과 달의 거리는 %e km 이다.' % d

# %%
'태양과 달의 거리는 %.3e km 이다.' % d

# %% [markdown]
# `%`을 통해 다양한 문자열 포매팅은 후에 다룬다.

# %%

# %% [markdown]
# ### 연습문제

# %% [markdown]
# 문자열의 인덱싱과 관련하여 위에서 정의된 `s`를 가지고 몇 가지 문제를 풀어보자.

# %% [markdown]
# 1. 문자열 `s`의 마지막 문자를 제외한 문자열을 구해보자.
# 2. 문자열 `s`의 1,3,5-번째 문자로 구성된 문자열을 구해보자.
# 3. 문자열 `s`의 1,3,7-번째 문자로 구성된 문자열을 구해보자.
# 4. 문자열 `s`를 거꾸로 쓴 문자열을 구해보자.
# 5. 문자열 `s`의 0-번째 문자를 `We`로 바꾼 문자열을 구해보자.
# 6. 문자열 `s`의 1-번째와 2-번째 문자 사이에 `always `를 넣어보자.

# %% [markdown]
# ### 해답

# %%
s = 'I love you so much.'

# %%
s[:-1]

# %%
s[1:6:2]

# %%
s[1:4:2] + s[7]

# %%
s[::-1]

# %%
''.join([x for x in reversed(s)]) # 뒤에서 배울 방법 

# %%
''.join(list(reversed(s))) # 뒤에서 배울 방법 2

# %%
'We' + s[1:]

# %%
# s의 1-번째와 2-번째 사이에 'always '
s[:2] + 'always ' + s[2:]

# %%

# %% [markdown]
# ### `list()`

# %% [markdown]
# 문자열에 `list()` 함수를 취하면 문자열의 문자 하나하나를 원소로 하는 리스트가 생성된다. 이때 리스트의 원소는 하나의 문자로 이루어진 문자열이 된다.

# %%
type(s)

# %%
lst = list(s)

# %%
type(lst), type(lst[0])

# %% [markdown]
# 문자열은 불변 객체이므로 `lst[0] = 'We'`로 하면 새로운 문자열 객체 `'We'`가 생성된 후, `lst[0]`가 `'We'`를 가리키게 된다.

# %%
lst[0] = 'We'

# %%
lst

# %% [markdown]
# `list()`의 역방향은 `''.join()`으로 할 수 있다. 
#
# #역방향이라는 설명보다는, 좀 더 풀어서 써 주면 좋을 것 같습니다. 가령,
#
# list() 함수가 문자열의 문자 하나하나를 원소로 하는 리스트를 생성하는 함수였다면, join()함수는 문자 하나하나를 원소로 하는 리스트를 하나의 문자열로 바꾸어 주는 함수다. `''.join()`으로 시행할 수 있다. 

# %%
''.join(lst)

# %% [markdown]
# 문자열 `s`에 대해 `.join()` 메소드의 의미는 다음과 같은 `for` 문으로 나타낼 수 있다.[^forstring]
#
# [^forstring]: 하지만 `.join()`은 좀더 효율적인 방식으로 구현된다. (# 하지만`.join()`은 같은 결과를 좀더 효율적인 방식으로 구현한다.) `for` 안의 `res = res + s + x`를 보면 `res`가 가리키는 객체는 조금씩 커져간다. 이렇게 조금씩 커져가는 객체를 생성하는 것보다 모든 구성요소를 모아서 한꺼번에 하나의 객체를 만드는 것이 훨씬 효율적이다. 데이터 프레임을 합칠 때에도 비슷하다.

# %%
# s.join(lst)

s = ''
res = lst[0]
for x in lst[1:]:
    res = res + s + x
res

# %%

# %%

# %%

# %% [markdown]
# ### 유니코드 관련
#
# 파이썬 버전 3+에서는 문자열을 저장하기 위해 유니코드를 사용한다.
#
# +++ 유니코드에 대한 기본적인 내용

# %%
import unicodedata

# %%
# dir(unicodedata)

# UCD, bidirectional, category, combining, decimal,
# decomposition, digit, east_asian_width, is_normalized
# lookup, mirrored, name, normalize, numeric, ucd_3_2_0
# ucnhash_CAPI, unidata_version

# %% [markdown]
# 주어진 문자열이 어떤 문자로 구성되었으며, 문자별로 유니코드 코드포인트, 유니코드 범주, 유니코드 문자이름을 확인하려면 다음과 같이 한다. 

# %%
# Adopted from https://docs.python.org/ko/3.8/howto/unicode.html

u = '한글 ' + chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)

print("no let. UNICODE category  num letter name")
print("=========================================")
for i, c in enumerate(u):
    #print(i, c, '%04x' % ord(c), unicodedata.category(c), end=" ")
    #print(f'{i:02d} {c:2s} {ord(c):04x}') 
    # 완벽히 맞출 수 없을 듯... GUI의 역할이라서??? # tab을 쓰면?
    print(f'{i:02d} {c:2s} \t{ord(c):06x}\t{unicodedata.category(c):4s} ', end='') 
    try:
        print('%8.2f ' % unicodedata.numeric(c), end='')
    except:
        print(' '*(8+1), end='')
    print(unicodedata.name(c))
    #print(unicodedata.east_asian_width(c))
# Get numeric value of second character
#print(unicodedata.numeric(u[1]))

# %%

# %% [raw]
#
# # https://stackoverflow.com/questions/32555015/how-to-get-the-visual-length-of-a-text-string-in-python
# # unicodedata.east_asian_width()
# ea ; A         ; Ambiguous
# ea ; F         ; Fullwidth
# ea ; H         ; Halfwidth
# ea ; N         ; Neutral
# ea ; Na        ; Narrow
# ea ; W         ; Wide

# %%
dir(unicodedata)


# %%
# Adopted from https://docs.python.org/ko/3.8/howto/unicode.html
def unicode_info(u):
    if not type(u)==str:
        raise ValueError('! input u should be unicode string')
    print('* str input = ')
    print('  '+ u)
    print('* str normalized = ')
    print('  '+ unicodedata.normalize('NFC', u))
    print("no let. wid UNICODE     category  num letter name")
    print("=================================================")
    for i, c in enumerate(u):
        print(f'{i:02d} {c:2s}\t{unicodedata.east_asian_width(c):3s} {ord(c):06x}\t{unicodedata.category(c):4s} ', end='') 
        try:
            print('%8.2f ' % unicodedata.numeric(c), end='')
        except:
            print(' '*(8+1), end='')
        print(unicodedata.name(c))



# %%
unicode_info(u)

# %% [markdown]
# * 참고 : 유니코드 카테고리 
#   - http://www.unicode.org/reports/tr44/#General_Category_Values

# %% [markdown]
# ## 유니코드 문자열 정규화

# %%
unicodedata.normalize('NFD', s)
# NFC, NFKC
# NFD, NFKD
# NFD : 웹표준

# %% [raw]
# # 출처 : https://unicode.org/reports/tr15/
# The W3C Character Model for the World Wide Web 1.0: Normalization [CharNorm] and other W3C Specifications (such as XML 1.0 5th Edition) recommend using Normalization Form C for all content, because this form avoids potential interoperability problems arising from the use of canonically equivalent, yet different, character sequences in document formats on the Web. See the W3C Character Model for the Word Wide Web: String Matching and Searching [CharMatch] for more background.

# %% [markdown]
# ## 유니코드 문자열 비교

# %% [markdown]
# * ??? 근데 문자열 비교에는 로케일에 대한 내용이 있어야???

# %%
# from https://docs.python.org/ko/3.8/howto/unicode.html
import unicodedata

def compare_strs(s1, s2):
    def NFD(s):
        return unicodedata.normalize('NFD', s)

    return NFD(s1) == NFD(s2)

single_char = 'ê'
multiple_chars = '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
print('length of first string=', len(single_char))
print('length of second string=', len(multiple_chars))
print(compare_strs(single_char, multiple_chars))

# %% [markdown]
# ### 알파벳 대소문자를 무시하고 비교

# %%
import unicodedata

def compare_caseless(s1, s2):
    def NFD(s):
        return unicodedata.normalize('NFD', s)

    return NFD(NFD(s1).casefold()) == NFD(NFD(s2).casefold())

# Example usage
single_char = 'ê'
multiple_chars = '\N{LATIN CAPITAL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'

print(compare_caseless(single_char, multiple_chars))

# %% [markdown]
# ## 유니코드 문자열 정렬

# %%

# %% language="R"
# Sys.getlocale('LC_COLLATE') #알파벳 순서에 대한 정보
# x <- c("ä", "A", "D", "P", "Z", "CH", "C", "H", "Ü")
# x <- stringi::stri_trans_nfkc(x)
# cat(paste0(x, collpase=" "), "\n")
# sort(x)


# %%
import locale
x = ["ä", "A", "D", "P", "Z", "CH", "C", "H", "Ü"]
sorted(x)
sorted(x, key=locale.strxfrm)

# %% [markdown]
# ??? 한글의 경우???

# %%
#x <- c("ä", "A", "D", "P", "Z", "CH", "C", "H", "Ü")
#x <- stringi::stri_trans_nfkc(x)
#stri_sort(x, opts_collator = stri_opts_collator(locale='de'))
# stri_sort(x, opts_collator = stri_opts_collator(locale='fi'))
# stri_sort(x, opts_collator = stri_opts_collator(locale='en'))
# stri_sort(x, opts_collator = stri_opts_collator(locale='cs'))
# stri_sort(x, opts_collator = stri_opts_collator(locale='ko'))

import icu
# package pyicu & pycld2?
# https://github.com/aboSamoor/polyglot/issues/10

collator = icu.Collator.createInstance(icu.Locale('de_DE.UTF-8'))
sorted(x, key=collator.getSortKey)
#['A', 'ä', 'C', 'CH', 'D', 'H', 'P', 'Ü', 'Z']

collator = icu.Collator.createInstance(icu.Locale('fi_FI.UTF-8'))
sorted(x, key=collator.getSortKey)
#['A', 'C', 'CH', 'D', 'H', 'P', 'Ü', 'Z', 'ä']

collator = icu.Collator.createInstance(icu.Locale('en_EN.UTF-8'))
sorted(x, key=collator.getSortKey)
#['A', 'ä', 'C', 'CH', 'D', 'H', 'P', 'Ü', 'Z']

# %%

# %% [markdown]
# ## `bytes`, `bytearray`

# %% [markdown]
# 바이트(byte)란 정보의 기본단위 비트(bit)가 8개 모여 만들어진다. `bytes` 타입은 이 바이트가 여러 개 모여 만들어진다. 문자(character)와 문자열(string)의 차이와 비슷하다. 문자열은 흔히 character array라고도 한다 

# %% [markdown]
# `bytes`와 `bytesarray`는 거의 비슷하다. 한 가지 다른 점은 `bytes`는 `str`과 비슷하게 불변(immutable) 객체이고, `bytesarray`는 가변 객체이다

# %% [markdown]
# `bytes` 타입의 객체를 생성하기 위해 보통 문자열과 비슷한 방법을 사용한다. 단지 앞에 `b`를 붙여 `bytes`임을 나타낸다.

# %%
x = b'abc'

# %%
x

# %% [markdown]
# 하지만 문자열과는 다르다. `bytes`의 목적은 하나 또는 여러 바이트를 저장하는 것이다. 단지 편의에 의해 바이트를 문자열로 나타내는 것뿐이다.

# %%
x

# %%
x[0], x[1], x[2]

# %%
x[0] = 0x40

# %% [markdown]
# 다음은 변수 `x`의 `bytes` 객체를 `bytearray` 타입으로 변환한다.

# %%
y = bytearray(x)

# %%
type(y)

# %%
y

# %%
y[0], y[1], y[2]

# %% [markdown]
# `y`는 `bytearray`이기 때문에 수정이 가능하다.

# %%
y[0] = 0x41  # 알파벳 대문자 A의 ASCII 코드는 0x41

# %%
y

# %% [markdown]
# 위에서 확인할 수 있듯이 `y[0]`를 `0x41` 또는 `65`로 바꿔도 출력시에는 해당하는 ASCII 코드의 문자가 출력된다. 

# %% [markdown]
# `bytes`와 `bytearray`는 모두 8바이트 정수의 나열이지만, 출력 또는 생성할 때 편의를 위해 ASCII 문자를 사용한다고 생각하면 된다. 

# %% [markdown]
# * 참고 : https://docs.python.org/3.8/reference/lexical_analysis.html#strings

# %%
for i in range(255):
    x = bytearray(1)
    x[0] = i
    print(f"{i:03d} {hex(i)[2:]:3s} {chr(i):2s}\t",x)

# %% [markdown]
# 위의 결과에서 확인할 수 있듯이 16진수 20(`' '`)부터 7e(`'~'`)까지는 ASCII 문자로 출력된다(이때 `\`는 `'\\'`로 출력된다). 16진수 20 이전의 제어 문자나 7e 이후는 '\x7f'와 같이 탈출문자를 사용하여 16진수를 그대로 적어 출력된다. 예외적으로 탭(16진수 09)은 `'\t'`, 뉴라인(16진수 0a)은 `'\n'`, 캐리지리턴(16진수 13)은 `\r'`로 출력된다. 입력할 때에는 `'\x0a'` 꼴과 `'\t`를 모두 사용할 수 있다.

# %%
x = b'\x0a'; y = b'\n'

# %%
x, y

# %% [markdown]
# ## 문자 인코딩

# %% [markdown]
# 컴퓨터는 다양한 방식으로 문자를 인코딩한다. 여기서 인코딩이란 주어진 문자 또는 문자열을 수로 변환하는 방식을 의미한다. 유니코드 역시 인코딩 방법이다. 

# %% [markdown]
# 문자열(`str`)의 `.encode()` 메소드를 사용한다.

# %%
x = 'abc'
x.encode('UTF-8')

# %%
x.encode('CP949')

# %% [markdown]
# ASCII 코드 문자는 대부분 인코딩에 관계없이 동일한 방식으로 인코딩된다. 한글과 같은 비로마자는 다르다.

# %%
x = '한글'
x.encode('UTF-8')

# %%
x.encode('CP949')

# %% [markdown]
# 주어진 바이트 또는 바이트 어레이를 문자로 디코드할 수도 있다. (여기서 decode란 encode의 역을 의미한다.)

# %%
x.encode('UTF-8').decode('UTF-8')

# %%
x.encode('CP949').decode('CP949')

# %% [markdown]
# UTF-8로 인코딩한 16진수를 CP949로 생각하여 디코딩을 하면 엉뚱한 결과를 얻을 수밖에 없다. 따라서 인코딩 또는 디코딩을 할 때에는 어떤 인코딩을 사용할 지 결정하는 것이 중요하다.

# %%
x.encode('UTF-8').decode('CP949')

# %% [markdown]
# 위의 오류를 보자. `UniocdeDecodeError:` 이하를 보면 `x.encode("UTF-8")`의 첫 번째 값 `0xed`를 유니코드로 해석(디코드)할 수 없음을 나타낸다. 이렇게 주어진 인코딩으로 적절하게 해석할 수 없는 숫자를 처리하는 방법은 `.decode('', errors=)`의 `errors=`로 정할 수 있다. 기본값은 `'strict'`이다.
#
# * `errors='strict'` : 오류를 발생시킨다.
# * `errors='ignore'` : 무시한다.
#

# %%
x.encode('UTF-8').decode('CP949', errors='ignore')

# %% [markdown]
# ### 파이썬 파일의 인코딩

# %% [markdown]
# 현재 파이썬 파일의 인코딩은 다음과 같이 확인할 수 있다.

# %%
import sys
sys.getfilesystemencoding()

# %% [markdown]
# 파이썬 파일의 인코딩은 파일 처음에 다음의 문구 중 하나를 넣어서 지정할 수 있다([PEP 263](https://www.python.org/dev/peps/pep-0263/)). 
#

# %% [raw]
# # coding=<encoding name>

# %% [raw]
# !/usr/bin/python
# # -*- coding: <encoding name> -*-

# %% [raw]
# !/usr/bin/python
# # vim: set fileencoding=<encoding name> :

# %%

# %% [markdown]
# ## 파이썬에서 텍스트 파일 열 때 인코딩?

# %%

# %% [markdown]
# ### === END OF DOCUMENT

# %%

# %%

# %%

# %% [markdown]
# ## string 상수

# %%
import string

# %%
string.ascii_letters
# 아래에 나오는 ascii_lowercase와 ascii_uppercase 상수를 이어붙인 것입니다. 이 값은 로케일에 의존적이지 않습니다.

# %%
string.ascii_lowercase
# 소문자 'abcdefghijklmnopqrstuvwxyz'. 이 값은 로케일에 의존적이지 않고 변경되지 않습니다.

# %%
string.ascii_uppercase
#대문자 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. 이 값은 로케일에 의존적이지 않고 변경되지 않습니다.

# %%
string.digits
# 문자열 '0123456789'.

# %%
string.hexdigits
# 문자열 '0123456789abcdefABCDEF'.

# %%
string.octdigits
# 문자열 '01234567'.

# %%
string.punctuation
# C 로케일에서 구두점 문자로 간주하는 ASCII 문자의 문자열: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.

# %%
string.printable
# 인쇄 가능한 것으로 간주하는 ASCII 문자의 문자열. digits, ascii_letters, punctuation, whitespace 의 조합입니다.

# %%
string.whitespace
# 공백으로 간주하는 모든 ASC
# 참고 : '\0x0b' : vertical tab
#       '\0x0c' : feed-forward
#.      '\0x08' : backspace

# %%
print('a'.join(list(string.whitespace)))

# %%

# %%
str.capitalize('aaa')

# %%
'foobar'.endswith('bar')

# %%
'foobar'.endswith('bar')

# %%
'foobar'[:3].endswith('foo')

# %%
'aabfoobar'.endswith('foo', 0,6) #

# %%
'aabfoobar'[:6].endswith('foo')

# %%

# %%
'aabfoobar'.index('bfo')

# %%
'aabfoobar'.find('bfo')

# %%
# same as .find, .index : -1 or IndexError

# %%
bytes(3).decode('UTF-8') # python은 '\x00'도 포함 가능...

# %%

# %%

# %%
lst = list(x)

# %%

# %%
x[1:4]

# %%
lst[1:4]

# %%
list(x[1:4])

# %%

# %%
list('ABCD')

# %%

# %%
# 문자열 'ABCD'는 하나 하나의 문자로 구성되기 때문에,
# # iterable(?)이다???

# %%
'ABCD'.split('\\b')

# %%
'ABCD'.split('C')
# .split(x)는 문자열을 x를 기준으로 분리하여 리스트를 구성한다.
# .split()의 경우는 모든 문자를 분리하는 게 아니라,
#                   공란을 기준으로 분리한다.
# 위에서 봤듯이 모든 문자를 분리하여면 list('ABCD')를 쓰면 된다.

# %%
'ABCD'.split('BC')

# %%
'ABCD'.split() # 프로그램을 짜다 보면 경계 상황(또는 극단적인 상황)에 대비할 필요가 있다.

# %%
'ABCD'.split(None)

# %%
'ABCD'.split('')

# %%
'ABCD'.split('ABCD')

# %%

# %%
'ABCD'[2]

# %%
'ABCD'[:-1] #마지막 문자를 제외

# %%
l = ['abcdefg', '12345678']
# l의 모든 문자열에 대해 x[c(2,4,6,7)], 2,4,6,7번째 문자를 뽑으려면?
y = 'abcdefg'
[y[x] for x in [1,3,5,6]]

# %%
[[y[x] for x in [1,3,5,6]] for y in l]

# %%
lst1 = []
for y in l:
    lst2 = []
    for x in [1,3,5,6]:
        lst2.append(y[x])
    lst1.append(lst2)
lst1

# %% [markdown]
# # 11.4 R에서 인코딩 다루기
#

# %%
# x <- '한글사랑'
# Encoding(x) 
# Encoding(x) <- 'UTF-8'; x; Encoding(x)
# Encoding(x) <- 'latin1'; x; Encoding(x)
# Encoding(x) <- ''; x; Encoding(x)
# Encoding(x) <- 'CP949'; x; Encoding(x)

# %%
x = "한글사랑"
type(x) #str
#y = b'한글사랑' # 한글은 오류(bytes can only contain ASCII literal characters.)
#type(y)


# %%
x.encode()     # str을 bytes로 변환 # 그래서 bytes가 뭐가 다른거라고???

# %%
x.encode('utf-8')  # str을 해당 인코딩으로 된 바이트 객체로 만든다.

# %%
# ?x.encode

# %%
bytes(x, encoding='utf-8')

# %%
bytearray(x, encoding='utf-8') # bytes와 내용은 같고, 형식이 다르다? 어떤 형식?

# %%
x.encode('cp949')

# %%
bytes(x, encoding='cp949')

# %%
bytearray(x, encoding='cp949')

# %%
bSent = bytes(x, encoding='cp949')
baSent = bytearray(x, encoding='cp949')

# %%
bSent[0]

# %%
bSent[0]=164
# TypeError: 'bytes' object does not support item assignment


# %%
# 왜 TypeError: 'bytes' object does not support item assignment
# 무엇 때문에, 무엇을 위해 만들어졌나? 그냥 byte를 확인하려고?

# %%
baSent[0]

# %%
baSent[0]=17
# bSent[0]=17은 불가능하고, baSent[0]=17은 가능하다
# bytes는 수정이 불가능하고, bytearray는 수정이가능하다. 
# bytes의 문제를 해결하려고, bytearray가 만들어졌다?
# STICK의 방법론을 활용한다면?

# %%
baSent

# %%
## ---- collapse=TRUE---------------------------------------------------------------------------
#x <- 'English'
#Encoding(x) 
#Encoding(x) <- 'UTF-8'; x; Encoding(x)
#Encoding(x) <- 'latin1'; x; Encoding(x)
#Encoding(x) <- 'CP949'; x; Encoding(x)

# %%
x = "English"
type(x)     # str
y = b'English'
type(y)     # bytes

# %%
x.encode()     # str을 bytes로 변환
# 그래서 str과 bytes의 차이점?
# 출력 결과는 'English'와 b'English' 뭐가 다르지?

# %%
x.encode('utf-8')  # str을 해당 인코딩으로 된 바이트 객체를 만든다.

# %%
bytes(x, encoding='utf-8')

# %%
bytearray(x, encoding='utf-8')

# %%
x.encode('euc-kr')

# %%
bytes(x, encoding='euc-kr')

# %%
bytearray(x, encoding='euc-kr')

# %%
x ='이 문장의 첫 글자는 ASCII로 나타낼 수 없다!'
a = x.encode('utf-8')[0]
b = x.encode('euc-kr')[0]
print(a,b)

# %%
## ---------------------------------------------------------------------------------------------
#Sys.getlocale('LC_CTYPE')

import sys
sys.getfilesystemencoding()


# %% [markdown]
# # 11.5 R에서 문자열 입력
#

# %% language="R"
# cat("'\\b'는 백슬래쉬를 의미한다\n")
# cat('"어떻게 해?"라고 말했다. \'음...\'\n')
# cat("\"어떻게 해?\"라고 말했다. '음...'\n")
# cat('좋아요\041\n')
# cat('좋아요\x21\n')
# cat('\u00a9는 copyright 표시이다.\n')

# %%
print("'\\b'는 백슬래쉬를 의미한다\n")
print('"어떻게 해?"라고 말했다. \'음...\'\n') 
# ??? tibble의 출력이 보여주듯이 따옴표를 구분해서 보여줄 수 있다면 좋을 듯
# 가장 외곽의 따옴표는 연하게, escape letter는 또 다른 색(외곽선 포함), literal letter는 다른 색
print("\"어떻게 해?\"라고 말했다. '음...'\n")
print('좋아요\041\n')
print('좋아요\x21\n')
print('\u00a9는 copyright 표시이다.\n')

# %% language="R"
# x <- c('\u00b1\u00bd-\u00be')
# x #"±½¾"
# Encoding(x) #"UTF-8"
# charToRaw(x) # c2 b1 c2 bd c2 be
#
# readr패키지의 guess_encoding(charToRaw())하면 인코딩 유형 가능성 높은 순서대로 추측해줌
# guess_encoding(charToRaw(x))

# %%
msg = '\u00b1\u00bd-\u00be'
msg, type(msg)

# %% [markdown]
# * python의 문자열(`str`)은 모두 유니코드로 저장한다.
# * 유니코드는 UTF-8, UTF-16, UTF-32 등 여러 가지 방법으로 인코딩할 수 있다.
# * `.encode()` 메쏘드를 쓰면 특정 인코딩 방법으로 인코딩을 할 수 있다.

# %%
# `ord()`는 한 문자에 대해 유니코드 코드 포인트를 구해준다.
[ord(x) for x in msg]

# %%
# `hex()`는 정수를 16진수 표현으로 바꿔준다.
[hex(ord(x)) for x in msg] 

# %%
# 주어진 문자열을 UTF-8로 인코딩한 결과를 보고 싶다면,
msgUTF8 = msg.encode('UTF-8')
msgUTF8

# %%
[hex(x) for x in msgUTF8]

# %%
x = "\u00b1\u00bd-\u00be"
# 문자를 합쳐 문자열로 만들고자 한다면 `.join()` 메쏘드를 활용할 수 있다.
''.join([chr(ord(i)) for i in x])

# %% [raw] language="R"
# scan(what="", sep='\n', quote='')
# # ##1: 영어 한글 \\ "How can you", I thought 'Hmmm"\\'
# # ## 2:
# # ## Read 1 item
# # ## [1] "영어 한글 \\\\ \"How can you\", I thought 'Hmmm\"\\\\'"
# scan(what="", sep='\n', quote='') # 윈도우 R의 경우 û, é가 제대로 입력되지 않는다.
# # ## 1: 불어 brûlée 한자 鬼 \ 와 ", '
# # ## 2:
# # ## Read 1 item
# # ## [1] "불어 brulee 한자 鬼 \\ 와 \", '"

# %%
# 공백을 기준으로 여러개 입력받기 위해
a,b,c = input().split()
# 이를 print(a,b,c sep='', end='') 로 프린트할 수 있다.

# raw_input 은 무조건 string타입의 입력을 받는다.

# %% [markdown]
# # 11.6 유니코드 정규화

# %% [markdown]
# ### Glossary
#
# ??? 아래 약어 정확한지 확인 필요
# * NFC: **N**ormalization **F**orm **C**anonical Composition
# * NFD: Normalization Form Canonical Decomposition
# * NFKC: Normalization Form Compatibility Composition
# * NFKD: Normalization Form Compatibility Decomposition

# %% language="R"
#
# x <- c("He sni\ufb99ed. sniffed!", "\u00fc and u\u0308")
# cat(x, "\n")
# y <- stringi::stri_trans_nfkc(x)
# cat(y, "\n")

# %%
# Question,
#   strip, lstrip, rstrip and Unicode space?
# 
# Unicode has White_Space, Line_Break, Grapheme_Cluster_Break,
#             Senetence_Break, Word_Break
# White_Space, \u0020 \u00a0 \u1680 \u2000 \u2001 \u2002
#              \u2003 - \u200a \u202f(NNBSP) \u205f \u3000
#              모두 해당!
# print하면 \u1680(ogham space mark,  )의 경우는 white space로 보이지 않음에 유의!
# 
# windows에서는 alt+numpad? mac에서는 option+key 

# %%
import unicodedata
x = ["He sni\ufb99ed. sniffed!", "\u00fc and u\u0308"]
print(x)
y=[unicodedata.normalize('NFKC', i) for i in x]
print(y)
import pandas as pd
x = pd.Series(x)
print(x)
y = x.str.normalize('NFKC')
print(y)

# %% [markdown]
# # 11.7 문자열의 정렬

# %% language="R"
# Sys.getlocale('LC_COLLATE') #알파벳 순서에 대한 정보
# x <- c("ä", "A", "D", "P", "Z", "CH", "C", "H", "Ü")
# x <- stringi::stri_trans_nfkc(x)
# cat(paste0(x, collpase=" "), "\n")
# sort(x)


# %%
import locale
x = ["ä", "A", "D", "P", "Z", "CH", "C", "H", "Ü"]
sorted(x)
sorted(x, key=locale.strxfrm)

# %% [markdown]
# ??? 한글의 경우???

# %%
#x <- c("ä", "A", "D", "P", "Z", "CH", "C", "H", "Ü")
#x <- stringi::stri_trans_nfkc(x)
#stri_sort(x, opts_collator = stri_opts_collator(locale='de'))
# stri_sort(x, opts_collator = stri_opts_collator(locale='fi'))
# stri_sort(x, opts_collator = stri_opts_collator(locale='en'))
# stri_sort(x, opts_collator = stri_opts_collator(locale='cs'))
# stri_sort(x, opts_collator = stri_opts_collator(locale='ko'))

import icu
# package pyicu & pycld2?
# https://github.com/aboSamoor/polyglot/issues/10

collator = icu.Collator.createInstance(icu.Locale('de_DE.UTF-8'))
sorted(x, key=collator.getSortKey)
#['A', 'ä', 'C', 'CH', 'D', 'H', 'P', 'Ü', 'Z']

collator = icu.Collator.createInstance(icu.Locale('fi_FI.UTF-8'))
sorted(x, key=collator.getSortKey)
#['A', 'C', 'CH', 'D', 'H', 'P', 'Ü', 'Z', 'ä']

collator = icu.Collator.createInstance(icu.Locale('en_EN.UTF-8'))
sorted(x, key=collator.getSortKey)
#['A', 'ä', 'C', 'CH', 'D', 'H', 'P', 'Ü', 'Z']

# %% [markdown]
# # 11.8 문자열을 다루는 함수들 

# %%
##기능

## 알파벳 대/소문자 변환     str.upper() str.lower()
## 문자수                    len()
## 문자열 내 공란 제거       str.strip()
## 문자열 연결               +, ''.join()
## 문자열의 일부             
## 문자열 분해               str.split()
## 부분 문자열의 존재 여부   
## 부분 문자열의 횟수        str.count()
## 부분 문자열의 위치        str.find/str.index
## 부분 문자열의 교체        str.replace()
## 부분 문자열의 추출/배제


# %%
## ---------------------------------------------------------------------------------------------
# 알파벳 15번째 소문자와 대문자는?
#c(letters[15], LETTERS[15])
from string import ascii_lowercase
from string import ascii_uppercase
alpha_lower = list(ascii_lowercase)
alpha_upper = list(ascii_uppercase)


# %%
print(ascii_lowercase)
print(ascii_uppercase)


# %%
## ---- results='hold'--------------------------------------------------------------------------
#str <- "BoYs, Be aMbiTioUS!"
#tolower(str)
#toupper(str)
#str_to_title(str)

str = "BoYs, Be aMbiTioUS!"
str.upper()
str.lower()
str.title() # 단어의 첫글자만 대문자로


# %%
import string
string.capwords(str) # title()의 따옴표도 공백으로 인식하는 문제 보완 #??? 문제가 드러나는 예는?


# %%
str.capitalize() # 문자열 맨 첫글자만 대문자로


# %%
# str <- "\U903a9 딸기!"
#nchar(str)
#nchar(str, type='bytes')
#nchar(str, type='width')

s = "\U000903a9 딸기!"
byt = s.encode()

print(s)
len(s) #4 򐎩 딸기

# %%
# 글자의 너비 구하기
# 참조: https://www.programcreek.com/python/example/5938/unicodedata.east_asian_width

# %%
for c in s:
    print(unicodedata.east_asian_width(c))
    # F, Na, W, Na

# %%
len(byt) #11 b'\xf2\x90\x8e\xa9 \xeb\x94\xb8\xea\xb8\xb0'

# %% language="R"
# str <- c("  Books", "Coffee\t", "Co ff ee", "\tBook", "I   like coffee.")
# s1 <- trimws(str); s1
# s2 <- trimws(str, which='left'); s2
# s3 <- trimws(str, which='right'); s3
# s4 <- stringr::str_squish(str); s4


# %%
x = ["  Books", "Coffee\t", "Co ff ee", "\tBook", "I   like coffee."]

x1 = [i.strip() for i in x]
print(x1)
x2 = [i.lstrip() for i in x]
print(x2)
x3 = [i.rstrip() for i in x]
print(x3)
x4 = [" ".join(i.split()) for i in x]
print(x4)


# %% language="R"
# paste0('I have ', 'a car')
# paste0(c('I have ', 'I want '), c('a car', 'a cake'))


# %%
x = ['I have ', 'a car']
''.join(x)

x = ['I have ', 'I want ']
y = ['a car', 'a cake']
[i+j for i, j in zip(x,y)]


# %% language="R"
# paste(c('ab', 'cd'), c('cd', 'ab'))
# paste(c('ab', 'cd'), c('cd', 'ab'), sep='__')


# %%
x = ['ab', 'cd']
y = ['cd', 'ab']
[i+j for i,j in zip(x,y)]
[i+'__'+j for i,j in zip(x,y)]


# %% language="R"
# print(paste(c('ab', 'cd'), c('ef', 'gh'), collapse='**'))
# print(paste(c('ab', 'cd'), c('ef', 'gh'), sep='__', collapse=''))
# print(paste(c('ab', 'cd'), c('ef', 'gh'), sep='__', collapse=NULL))


# %%
abcd = [i+'__'+j for i,j in zip(x,y)]
print('**'.join(abcd))
print(''.join(abcd))


# %% language="R"
# x1 <- c(0, -1, exp(1), -pi*10, exp(1)*1e+6)
# x2 <- c(0, 1, 314, 9923, -1123224)
# x3 <- c(0, 314.413, pi*100, -1123224*0.123)
# print(x1); print(x2); print(x3)
# sprintf("%6.2f", x1); sprintf("%6.2f", x2) ;sprintf("%6.2f", x3)
#
#

# %%
[f'{i:6.2f}' for i in x1]

# %%
import math
x1 = [0, -1, math.exp(1), -math.pi*10, math.exp(1)*1e+6]
x2 = [0, 1, 314, 9923, -1123224]
x3 = [0, 314.413, math.pi*100, -1123224*0.123]
print(x1); print(x2); print(x3)

[format(i, "6.2f") for i in x1]
[format(i, "6.2f") for i in x2]
[format(i, "6.2f") for i in x3]


# %%
x1 = pd.Series(x1)
x2 = pd.Series(x2)
x3 = pd.Series(x3)
x1.apply(lambda x: "{:6.2f}".format(x))
x2.apply(lambda x: "{:6.2f}".format(x))
x3.apply(lambda x: "{:6.2f}".format(x))


# %% language="R"
# sprintf(c("%10.2f", "%010.2f", "%+10.2f", "%+010.2f"), pi) # 우측 정렬
# sprintf(c("%-10.2f", "%-+10.2f"), pi) # 좌측 정렬
# sprintf(c("%10.2f", "%+10.2f"), pi*1e+06) # 좌측 정렬


# %%
fmt1 = ["%10.2f", "%010.2f", "%+10.2f", "%+010.2f"]
fmt2 = ["%-10.2f", "%-+10.2f"]
fmt3 = ["%10.2f", "%+10.2f"]
[i % math.pi for i in fmt1]
#['      3.14', '0000003.14', '     +3.14', '+000003.14']
[i % math.pi for i in fmt2] 
#['3.14      ', '+3.14     ']
x = math.pi*1000000
[i % x for i in fmt3] 
#['3141592.65', '+3141592.65']


# %% language="R"
# x <- c("abcdefg", "hijklmnop")
# substring(x, 1, 4)
# substring(x, 1, 4) <- c("aaaa", "bbbb"); x


# %%
sents = pd.Series(["abcdefg", "hijklmnop"])
replace = pd.Series(['aaaa', 'bbbb'])

for i,x in enumerate(sents):
    sents[i] = replace[i] + x[4:]
sents

# %%
sents = replace[:4] + x[4:]
sents

# %% language="R"
# library(stringr)
# patt = 'xxxx'
# str = c("I don't know", "How the xxxx do I know?", "Wow, x is 5!",
#         "xxxx xxxx xxxx", "Don't say xxxx to me, xxxx.")
# str_detect(str, pattern = fixed(patt)) # [1] FALSE  TRUE FALSE  TRUE  TRUE
# str_count(str, pattern = fixed(patt))  # [1] 0 1 0 3 2
# str_split(str, pattern = fixed(patt))
# [[1]]
# [1] "I don't know"
# [[2]]
# [1] "How the "    " do I know?"
# [[3]]
# [1] "Wow, x is 5!"
# [[4]]
# [1] ""  " " " " "" 
# [[5]]
# [1] "Don't say " " to me, "   "."    
# str_locate(str, pattern = fixed(patt))
#     start end
# [1,]    NA  NA
# [2,]     9  12
# [3,]    NA  NA
# [4,]     1   4
# [5,]    11  14
# str_replace(str, pattern = fixed(patt), replacement='yyyy')
# [1] "I don't know"                "How the yyyy do I know?"    
# [3] "Wow, x is 5!"                "yyyy xxxx xxxx"             
# [5] "Don't say yyyy to me, xxxx."


# %%
patt = 'xxxx'
str = ["I don't know", "How the xxxx do I know?", "Wow, x is 5!",
        "xxxx xxxx xxxx", "Don't say xxxx to me, xxxx."] 
strpd = pd.Series(str)
strpd.str.contains(patt) # F T F T T
strpd.str.count(patt)    # 0 1 0 3 2
strpd.str.split(patt)    
#0               [I don't know]
#1      [How the ,  do I know?]
#2               [Wow, x is 5!]
#3                   [,  ,  , ]
#4    [Don't say ,  to me, , .]
#dtype: object
strpd.str.find(patt)     # -1 8 -1 0 10
#strpd.str.index(patt) ???
strpd.str.replace(patt,"yyyy", n=1)  # n은 몇 개나 치환할지 결정한다.
#0                   I don't know
#1        How the yyyy do I know?
#2                   Wow, x is 5!
#3                 yyyy xxxx xxxx
#4    Don't say yyyy to me, xxxx.
#dtype: object


# %%
