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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## 들어가기

# %%
import numpy as np
import pandas as pd

# %%
dat = pd.DataFrame(
    {"num":[1, 2, 5, 6],
    "genre":pd.Categorical(['액션', '코메디', '액션', '애니메이션']),
    "foreign":[False, False, True, True],
    "release":[pd.Timestamp('2014-07-30 00:00:00'), 
               pd.Timestamp('2019-01-23 00:00:00'), 
               pd.Timestamp('2019-04-24 00:00:00'), 
               pd.Timestamp('2019-11-21 00:00:00')],
    "gross":[1357.4839891, 1396.47979516, 1221.8269416, 1148.1042145],
    "audience":[1761.3682, 1626.4944, 1393.4592, 1374.7792],
    "screen":[1587, 1978, 2835, 2648]}
   )
dat

# %%
dat.dtypes

# %%

# %%
dat = pd.DataFrame(
    {"rank":[1, 2, 4, 6],
     "title":['명량', '극한직업', '어벤져스', '겨울왕국'],
    "genre":pd.Categorical(['액션', '코메디', '액션', '애니메이션']),
    "foreign":[False, False, True, True],
    "release":pd.to_datetime(['2014-07-30','2018-01-23','2019-04-24','2019-11-21']),
    "gross":[1357.4839891, 1396.47979516, 1221.8269416, 1148.1042145],
    "audience":[1761.3682, 1626.4944, 1393.4592, 1374.7792],
    "screen":[1587, 1978, 2835, 264]}
   )
dat

# %%
dat.dtypes

# %% [markdown]
# 위의 데이터프레임 `dat`에는 2021년 12월 기준 개봉영화의 흥행 성적 데이터가 담겨 있다. 이를 파일로 저장하려고 한다. 

# %% [markdown]
# 파이썬의 데이터는 파이썬을 종료하거나 컴퓨터가 종료되면 흔적도 없이 사라진다. 만약 데이터를 보존하고 싶다면 여러 가지 방법을 쓸 수 있다. 노트를 가져와서 적어 놓을 수도 있지만, 데이터가 용량이 크다면 현실적인 방법은 아니다. 보통은 데이터를 파일에 저장한다. 

# %% [markdown]
# 데이터를 파일에 저장하는 방법은 크게 텍스트 파일로 저장하는 방법과 바이너리(이진수) 파일로 저장하는 방법이 있다. 여기서는 먼저 두 방법의 대표격인 `.csv` 파일과 파이썬의 `.pkl` 파일로 저장하는 방법을 예시로 보여준다. 그리고 본격적으로 데이터를 저장하고, 읽어오는 방법에 대해 설명한다. 

# %% [markdown]
# ### `.to_csv()`와 `to_pickle()`
#
# 데이터프레임을 텍스트 파일로 저장하는 가장 대표적인 방법은 `.to_csv()` 메쏘드를 활용하는 것이다. 파일 이름과 인코딩 방법을 적어준다. 인코딩 방법을 생략하면 운영체제의 기본 인코딩 방법을 사용한다. 요즘은 `encoding = 'UTF-8'`로 UTF-8 인코딩을 사용하는 것이 좋다. 뒤에서 설명하겠지만 UTF-8은 전세계적으로 가장 많이 쓰이는 인코딩 방법이다(윈도우에서 UTF-8로 설정하지 않으면 윈도우의 기본 인코딩인 `CP949`로 설정된다).
#
# 파이썬에서 바이너리 파일로 저장하는 가장 효율적인 방법은 `.to_pickle()` 메쏘드로 피클(`.pkl`) 파일로 저장하는 것이다. 
#

# %%
dat.to_csv('data/movies.csv', encoding = 'UTF-8')
dat.to_pickle('data/movies.pkl')

# %% [markdown]
# 이제 동일한 내용이 서로 다른 두 형식의 파일 `movies.csv`와 `movies.pkl`로 저장되었다. (여기서 `csv`는 **c**omma **s**eperated **v**alue의 약자로 여러 값이 쉼표(comma)로 구분된다는 의미이다. `pkl`은 피클(pickle)의 약자이다.)
#
# 이들 파일의 내용을 확인해 보자. 운영체제의 편집기를 사용할 수도 있고, 다음과 같이 파이썬 안에서 파일을 읽어서 출력해볼 수도 있다. 
#
#

# %%
with open('data/movies.csv', encoding = 'UTF-8') as f:
    for x in f.readlines():
        print(x, end='')    

# %%
with open('data/movies.pkl', 'rb') as f:
    x = f.read()
    print(x)
    
    #'rb'는 파일을 여는 mode인데, r은 read, w는 write, b는 binary, t는 텍스트를 의미한다.
    # rb rt wb wt 같은 조합도 가능하다. 

# %% [markdown]
# 출력하는 방식이 약간 다르긴 하지만 지금은 크게 중요하지 않다. 텍스트 데이터 파일인 `movies.csv`의 내용은 출력했을 때 쉽게 읽고 이해할 수 있다. 하지만 바이너리 파일인 `movies.pkl`의 내용은 출력을 해도 `pandas.core.frame` 또는 `DataFrame`과 같은 일부를 제외하고는 그 의미를 알 수가 없다.[^binaryx]
#
# [^binaryx]: `movies.pkl`의 출력 내용을 보면 앞에 `b`가 있고 `\x80`, `\x05` 등이 있다. `b`는 **b**inary의 약자로 이진수를 의미한다. 메모리에 저장된 내용이 정수(`int`)도 아니고, 문자열(`str`)도 아니고 이진수임을 나타낸다. 그럼에도 `pandas.core.frame`와 같은 내용을 확인할 수 있는 것은 아스키 코드로 나타낼 수 있는 이진수는 문자로 출력하기 때문이다. `\x80`과 `\x05`는 16진수 `80`과 `05`를 의미한다. 아스키 코드는 16진수 `00`에서 `7f`를 사용하기 때문에 `80` 이상의 16진수는 아스키 코드 문자에 대응하지 않으며 아스키 코드 `05`는 제어문자 중 하나에 해당한다. 이와 같이 문자로 표시할 수 없는 1바이트 16진수 `80`를 `\x80`와 같이 네 글자로 표시하기 때문에 출력 결과가 많아 보인다는 점을 유의하자. 

# %% [markdown]
# 다음의 방법은 모든 데이터를 16진수 1바이트씩 출력한다. 

# %%
with open('data/movies.pkl', 'rb') as f:
    s = f.read()
    for x in s:
        print(f'{x:02x}', end=' ')

# %% [markdown]
# 이제 두 파일의 크기를 비교해보자.

# %%
import os
os.path.getsize('data/movies.csv'), \
os.path.getsize('data/movies.pkl')

# %%
dat

# %% [markdown]
# 그런데 위의 데이터는 몇 군데 오류가 있다. 영화 "명량"의 장르는 "역사"이고, "어벤져스"의 순위는 4가 아니라 5다. "극한직업"의 개봉일은 2018년이 아니라 2019년이고, "겨울왕국"의 개봉 스크린 수는 264가 아니라 2648이다. 이를 수정해보자.

# %%
dat.loc[2, 'rank'] = 5

# %%
dat['genre'] = dat['genre'].cat.add_categories('역사')
dat.loc[0, 'genre'] = '역사'

# %%
dat.loc[1, 'release'] = pd.Timestamp('2019-01-23')

# %%
dat.loc[3, 'screen'] = 2648

# %% [markdown]
# 그리고 이를 다시 `movies2.csv`와 `movies2.pkl`로 저장한 후 앞의 파일 내용과 비교해보자.

# %%
dat.to_csv('data/movies2.csv')

# %%
dat.to_pickle('data/movies2.pkl')

# %%
with open('data/movies2.csv', encoding = 'UTF-8') as f:
    for x in f.readlines():
        print(x, end='')
        
        #end=''는 end가 기본적으로 \n이 포함되어 있어서 그런 거고, 그걸 바꿔 주면 print 마지막에 붙여지는 게 달라진다.

# %%
with open('data/movies2.pkl', 'rb') as f:
    s = f.read()
    print(s)

# %%
with open('data/movies2.pkl', 'rb') as f:
    s = f.read()
    for x in s:
        print(f'{x:02x}', end=' ')

# %% [markdown]
# `movies.csv`와 `movie2.csv`의 차이는 우리가 데이터를 어떻게 수정했는지를 알면 쉽게 찾아낼 수 있다. 하지만 `movies.pkl`과 `movie2.pkl`는 어떻게 다른가? 왜 그런 차이점이 나타나는지 알 수 있는가?
#
#

# %% [markdown]
# ### 텍스트 데이터 파일과 바이너리 데이터 파일 비교

# %% [markdown]
# 위에서 확인했듯이 텍스트 데이터 파일은 사람이 내용을 쉽게 확인할 수 있다는 장점이 있다. 그리고 위에서는 파이썬에서 내용을 수정했지만 텍스트 파일에서 바로 사람이 내용을 수정할 수정할 수도 있다.[^modify_file] 
#
# 바이너리 파일은 그 내용을 직접 확인하기도 어렵고 수정하기도 어렵다. 바이너리 파일을 수정하는 것은 어렵지 않지만 그 수정 사항이 데이터에 어떻게 반영될지 미리 예측하기 어렵기 때문이다. 
#
# [^modify_file]: 이 점은 장점일 수도 있고 단점일 수도 있다. 컴퓨터 문외한도 텍스트 파일을 읽어서 내용을 확인할 수 있다는 점에서 장점이지만, 컴퓨터 문외한도 편집기에서 내용을 실수로 수정할 수 있다는 점에서는 단점이다. 

# %% [markdown]
# 그리고 대부분의 경우 텍스트 파일은 바이너리 파일보다 용량이 크다는 단점이 있다. 위의 예에서는 바이너리 파일의 용량이 더 컸지만 데이터의 크기가 증가함에 따라 대부분 바이너리 파일의 용량은 텍스트 파일보다 훨씬 용량이 작기 마련이다. 다음의 예를 보자.

# %%
# 영화 흥행 순위 500위
# 출처 : 영화진흥위원회 통합전산망(http:///www.kobis.or.kr) 2021년 12월 현재 
dat = pd.read_csv('data/KOBIS_역대_박스오피스_2021-12.csv', encoding = 'EUC-KR',
                  parse_dates = ['개봉일'],
                  thousands = ',') 
dat.tail()

# %%
dat.to_csv('data/movies_full.csv')

# %%
dat.to_pickle('data/movies_full.pkl')

# %%
os.path.getsize('data/movies_full.csv'), \
os.path.getsize('data/movies_full.pkl')

# %%
