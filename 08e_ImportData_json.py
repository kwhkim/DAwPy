# -*- coding: utf-8 -*-
# ## JSON

# JSON(**J**ava**S**cript **O**bject **N**otation)은 인터넷을 통해 데이터를 주고 받을 때 많이 쓰
# 이는 데이터 형식으로 텍스트로 저장된다. 많은 Open API는 XML(e**X**tensible **M**arkup
# **L**anguage)과 JSON을 지원한다.[^xml]
#
# [^xml]: XML은 W3C(World-Wide Web Consortium)이 추천하는 데이터 전송 방식이지만, 같은 내용을 담은
# csv 또는 json 화일보다 용량이 크고, 복잡하기 때문에 요즘에는 json이 좀 더 많이 쓰이는 추세이다.

# JSON의 JS가 의미하는 JavaScript는 주로 인터넷 브라우저에서 실행되는 프로그램을
# 위한 프로그래밍 언어로, JSON은 JavaScript(자바 스크립트)에서 객체를 정의하는 방식
# 으로 데이터가 표현되지만, JSON이라는 데이터 형식은 JS(자바스크립트)와 독립적으로
# 활용될 수 있다.
#
# JSON 형식에 대한 명세서는 사이트[^jsonspec]에서 확인할 수 있다. 명세서 자체는 매우 간단하고
# 명확하다. JSON은 텍스트 화일로 저장되며, 사람이 읽기 쉽고, 또 쉽게 변형이 가능하다.
# 예를 들어, JSON에서 문자열은 처음과 끝을 겹따옴표로 구분해야 하지만, 홑따옴표로
# 구분되어 있다고 사람이 읽을 수 없는 것은 아니다(아래 예시를 보자).
#
# [^jsonspec]: https://www.json.org/json-en.html

# + active=""
# # s1.json: JSON
# {"이름":"김다미",
# "전화번호":"0104432104x"}

# + active=""
# # s2.json: JSON 형식이 아니지만, 사람이 읽기에는 불편이 없음
# {'이름':'김다미',
# '전화번호':'0104432104x'}
# -

import json

with open('data/s1.json', 'rt', encoding = 'UTF-8') as f:
    datJson = json.loads(f.read())
datJson

with open('data/s2.json', 'rt', encoding = 'UTF-8') as f:
    datJson = json.loads(f.read())
datJson
# JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
# 해결책? https://stackoverflow.com/questions/25707558/json-valueerror-expecting-property-name-line-1-column-2-char-1

# 이번 장에서는 JSON 형식에 대한 공식 문서를 살펴보고, 파이썬에서 JSON 형식을 활용할
# 때 나타날 수 있는 문제와 해결 방법에 대해 알아본다.
#
# [^jsondoc]: https://www.json.org/json-en.html

# ### JSON 데이터 타입

# JSON 공식 문서[^jsondoc]에 따르면 JSON이 지원하는 데이터 타입은 4가지로 문자열, 수, 논리값
# (`true`/`false`), 널(`null`)이다.
#
# [^jsondoc]: https://www.json.org/json-en.html

# ####  문자열

# 겹따옴표로 시작하고 끝난다. 사용 가능한 문자는 유니코드 코드포인트 20에서 10FFFF
# 까지로 정해져 있다. 이는 가능한 모든 유니코드 코드포인트를 모두 포함하는데, 유니코드
# 코드포인트 00에서 1F까지는 백스페이스, 수평탭과 같은 제어 문자들이 포함되어 있다.
# 이들 중 코드포인트 08번부터 0C까지의 대부분은 탈출문자를 써서 문자열에 포함시킬
# 수 있다. JSON의 문자열은 파이썬과 마찬가지로 `\`를 탈출 문자로 쓰는데, `\"`, `\\`, `\b`, `\f`,
# `\n`, `\r`, `\t`와 유니코드 코드포인트 hhhh를 써서 `\uhhhh`를 쓸 수 있다. `\"`는 문자열의 시
# 작과 끝을 표시하는 겹따옴표(`"`) 와 문자 곁따옴표를 구분하기 위해, 그리고 `\\`는 탈출
# 문자로 백슬래쉬(`\`) 를 쓰기 때문에 필요하다. `\b`(backspace), `\t`(tab), `\n`(new line),
# `\f`(feedforward), `\r`(carraige return)은 ASCII 코드 08번부터 0C까지의 제어문자에
# 서 수직탭을 제외한 문자들이다. 사용 가능한 문자에 개행문자(Line Feed; `"\n"` 또는
# `"\u000a"`)와 캐리지리턴(Carriage Return; `"\r"` 또는 `"\u000d"`)가 빠져 있기 때문에
# 다음과 같은 JSON 화일은 엄밀하게 말해 JSON 형식에 어긋난다(겹따옴표 안에 코드포
# 인트 10 또는 13의 줄바꿈문자가 포함되어 있다). 이런 경우에는 `strict=False`를 설정을 하면 무사히 파일을 읽을 수 있다.

# + active=""
# # s1b.json
# {"이름":"김다미",
#  "전화번호":"0104432104x",
#  "좌우명":"멋지게 살자.
# 그리고 베풀며 어울리자."}

# + active=""
# # https://realpython.com/python-json/
# -

with open('data/s1b.json', 'rt', encoding = 'UTF-8') as f:
    datJson = json.loads(f.read())
datJson
# JSONDecodeError: Invalid control character at: line 3 column 16 (char 51)

with open('data/s1b.json', 'rt', encoding = 'UTF-8') as f:
    datJson = json.loads(f.read(), strict = False)
datJson

# #### 수
#
# 수는 정수, 소수, 지수 형식을 띌 수 있다.
#
# * 정수 : `-3`, `20`, `7000`
# * 소수 : `-3.24`, `20.35`, `7000.121`
# * 지수 형식 : `-3e10`, `20e+30`, `-20E-40`

# #### 논리값 : `true`/`false`
#
# 파이썬과 다르게 모두 소문자임을 유의하자. `True` 또는 `TRUE`도 허용할 수 있을까?

# ###  여러 값
# 이제 이런 값을 모아보자. 값을 모으는 방법에는 여러 값을 일렬로 늘어뜨리는 방법(파이썬 리스트로 생각할 수 있다) 과 일렬로 늘어뜨린 값에 이름을 붙이는 방법이
# 있다. 다음의 예를 보자.

# + active=""
# ## vector or list
# # s3a.json
# [1, 3, 5, 10]

# + active=""
# # s3b.json
# [1, 4, null, true, "Jung"]

# + active=""
# ## dictionary
# # s3c.json
# {"A":1, "B":4, "C":null, "D":true, "E":"Jung"}
# -

with open('data/s3a.json', 'rt', encoding = 'UTF-8') as f:
    dat = json.loads(f.read(), strict = False)
dat

with open('data/s3b.json', 'rt', encoding = 'UTF-8') as f:
    dat = json.loads(f.read(), strict = False)
dat

with open('data/s3c.json', 'rt', encoding = 'UTF-8') as f:
    dat = json.loads(f.read(), strict = False)
dat

# ### 계층 구조

# 일련의 값을 모으는 두 방법에서 값이 쓰일 위치에 다른 일련의 값을 쓰면 계층적 구조를
# 만들 수 있다.

# + active=""
# ## vector or list
# # s3b.json
# [1, 4, null, true, "Jung"]

# + active=""
# # s3b2.json
# [1, 4, null, {"A":1, "B":4}, [false, "Mike"]]

# + active=""
# ## dictionary
# # s3c.json
# {"A":1, "B":4, "C":null, "D":true, "E":"Jung"}

# + active=""
# # s3c2.json
# {"A":1, "B":[4,5,2], "C":{"C1":null, "C2":"Yes"}}
# -

with open('data/s3b2.json', 'rt', encoding = 'UTF-8') as f:
    dat = json.loads(f.read(), strict = False)
dat

with open('data/s3c2.json', 'rt', encoding = 'UTF-8') as f:
    dat = json.loads(f.read(), strict = False)
dat

# ### 그 밖의 

import json

datJsonOrig = {'a':'b', 'num':[1,2,3],
               'dict':{'a':24, 'c':[2,4,5], '숫자들':['하나', '둘', '셋']}}
with open('data/dat_dict.json', 'wt') as f:
    f.write(json.dumps(datJsonOrig, indent=2))

with open('data/dat_dict.json', 'rt') as f:
    lst = f.readlines()
    for x in lst:
        print(x, end='')

# 한글을 읽기가 어렵다. 한글을 그대로 파일에 저장하고자 한다면 `ensure_ascii=False`를 한다. 모든 문자를 ASCII 문자로 만들지 않겠다는 의미이다.

with open('data/dat_dict2.json', 'wt') as f:
    f.write(json.dumps(datJsonOrig, 
                       ensure_ascii=False,
                       indent = 2))

with open('data/dat_dict2.json', 'rt') as f:
    lst = f.readlines()
    for x in lst:
        print(x, end='')


