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
# ## 텍스트 데이터 파일

# %% [markdown]
# 앞에서 소개한 텍스트 데이터 파일을 출력해보자.

# %%
with open('data/movies.csv', encoding = 'UTF-8') as f:
    for x in f.readlines():
        print(x, end='')    

# %% [markdown]
# 파일의 텍스트 출력을 잘 살펴보자. 특히 행을 구분하는 방법과 열을 구분하는 방법을 확인하자. 그리고 행이름, 열이름의 존재도 확인하자.

# %% [markdown]
# ### 수치 데이터를 텍스트 파일로 저장하기

# %% [markdown]
# 많은 데이터가 행과 열로 이루어진 직사각형의 형태이다.
# 파이썬에서 데이터프레임과 같은 형태이다. 수치 데이터로만 이루어진 데이터프레임을 생각
# 해보자. 데이터 프레임을 텍스트로 저장할 때 결정할 사항은 무엇일까?
#
# 가장 먼저 **수를 어떻게 텍스트로 표시할 것인지**를 결정해야 한다. 부록 <수표기>를 참조
# 하면 수를 텍스트로 표기하는 데에도 다양한 방법이 존재함을 확인할 수 있다. 여기서는
# 논의의 편의상 가장 일반적인 방법, 즉 소수점은 점(.) 을 사용하고 천단위 자리 기호는
# 사용하지 않는다고 가정하자.
#
# 데이터 프레임에는 여러 개의 수가 저장되어 있기 때문에 이들을 어떻게 구분할 지 결정
# 해야 한다. 데이터 프레임은 직사각형의 형태임을 상기하자. 따라서 중요한 결정사항은
# 행구분과 열구분을 어떻게 하느냐이다. 텍스트 데이터 파일의 가장 큰 장점이 사람들이
# 데이터를 쉽게 읽을 수 있다는 점이라고 할 때, 사람이 가장 읽기 쉬운 방법은 fwf(fixed
# with file) 형식을 사용하는 것이다.
# 이 방법은 행의 구분은 "\n"(줄바꿈)으로 하고, 각 열의 위치가 고정되어 있다. 예를 들어
# 다음과 같은 방법이다.

# %% [raw]
# # data/numeric.fwf
# 170 65
# 185 101
# 190 110
# 166 45

# %% [markdown]
# 네 사람의 키와 체중 자료를 텍스트로 작성했다. 각 줄의 처음 세 글자는 키를 나타내고, 그
# 뒤의 (공백을 포함한) 네 글자는 체중을 나타낸다. 사실 컴퓨터의 입장에서 중간의 공백은
# 불필요하지만 사람이 데이터를 읽을 때에는 크게 도움이 된다.
#
# 이런 방식의 데이터 저장 방법은 사람이 읽기는 좋지만 저장 효율은 좋지 않다. 중간에
# 공백 문자가 많이 들어가기 때문이다. 그리고 수의 길이를 미리 정해줘야 한다는 단점도
# 있다. 위의 예에서 소수점이 들어간 수(예. `167.45`) 를 추가해야 한다면, 이전의 자료를
# 새로 다시 써야 한다. 이런 문제를 해결하기 위해 열구분문자로 탭을 사용한다면 어떨까?

# %% [raw]
# # data/numeric.tsv
# 170	65
# 185	101
# 190	110
# 166	45

# %% [markdown]
# 탭은 스페이스 등의 공백 문자와 구분되지 않지만 Notepad++와 같은 편집기에서 `보기>기호보기>공백과 탭 표시` 설정을 켜면 두 문자(공백 문자와 탭 문자)를 구분해서 볼 수 있다. 하지만 하나의 수를 표현하기 위해 사용하는 숫자의 갯수가 행마다 크게 다르다면 열을 구분하기가 쉽지 않게 된다. 그리고 열의 갯수가 많아질 수록 열의 구분은 더욱 더
# 힘들어진다. 다음의 데이터를 보자. 같은 열에 속하는 숫자를 확인하기가 쉽지 않다.

# %% [raw]
# # data/numeric2.tsv
# 199000 43 34532.112 331231231111
# 29991443 32 123342111 11334
# 441233 11253411211.23411 11231 1111.00071

# %% [markdown]
# 공백문자와 탭이 연결되어 있거나 여러 탭이 연이어 존재하는 경우에도 탭 하나 하나를
# 구분하기가 어려워진다. 만약 열구분문자를 쉼표로 쓴다면 이런 문제를 해소할 수 있다
# 물론 고정길이 형식처럼 각 열을 쉽게 구분할 수 있는 것은 아니지만, 고정길이 형식이
# 지나치게 큰 용량을 차지하는 경우 차선책이 될 수 있다. 실제로 요즘 널리 사용되는 열구
# 분문자 중의 하나가 쉼표이다.
#
# 다음의 예는 결측값이 여럿 존재할 때 열구분문자에 따른 텍스트 차이를 보여준다.

# %% [raw]
# # data/numeric2.tsv
# 199000		43 34532.112	331231231111
# 29991443			11334
# 441233	11253411211.23411		

# %% [raw]
# # data/numeric2.csv
# 199000,,34532.112,331231231111
# 29991443,,,11334
# 441233,11253411211.23411,,

# %% [markdown]
# ### 수치데이터 파일을 읽어오기 : `pd.read_fwf()`과 `pd.read_csv()`

# %% [markdown]
# 위의 데이터를 읽기 위해서는 다음과 같은 방법을 사용한다.

# %%
import pandas as pd

# %%
pd.read_fwf('data/numeric.fwf', # 파일이름
            header = None,      # 열이름을 포함하지 않음
            widths=[4,3])       # 각 열의 너비            

# %%
pd.read_csv('data/numeric.tsv', # 파일이름
            header = None,      # 열이름을 포함하지 않음
            sep = '\t')         # 열구분자 탭('\t')

# %%
pd.read_csv('data/numeric2.csv', # 파일이름
            header = None,       # 열이름을 포함하지 않음
            sep = ',')           # 열구분자 쉼표 : 기본값이므로 생략 가능

# %% [markdown]
# 만약 열이름을 지정하고 싶다면 `names=`로 지정할 수 있다.

# %%
pd.read_csv('data/numeric2.csv', # 파일이름
            header = None,       # 파일은 열이름을 포함하지 않음
            names = ['num1', 'num2', 'num3', 'num4'], # 열이름
            sep = ',')           # 열구분자 쉼표

# %% [markdown]
# ### 문자 데이터를 텍스트 파일로 저장하기

# %% [markdown]
# 위에서 봤던 수치 데이터의 경우, 수치를 표기하기 위해 사용하는 문자 (점과 숫자) 와
# 행과 열을 구분하는 문자가 겹치지 않았다. 하지만 문자 데이터를 저장하는 경우에는 항상
# 그렇지 않다.
# 예를 들어, `"You love me, don't you?"`라는 문자열 데이터의 경우 **쉼표**가 포함되어 있다.
# 만약 **열구분문자로 쉼표**를 사용할 경우에는 데이터에 속하는 **문자 쉼표**와 **열구분문자 쉼표**
# 를 구분하기 어렵다.

# %% [raw]
# 1,Mary,You love me, don't you?,love
# 2,John,I do love you.,dream
# 3,Suzy,Attention, please.,heart

# %% [markdown]
# 위의 데이터의 첫 번째 열은 순번, 두 번째 열은 이름, 세 번째 열은 **자신이 좋아하는 문장**,
# 그리고 마지막 열은 자신이 좋아하는 단어를 나타낸다. 이때 쉼표가 문장 안에서 쓰인
# 것인지 아니면 열구분문자로 쓰인 것인지를 기계적으로 확인하는 방법은 없다. 그래서 보통 텍스트 자료에서 쉼표가 포함된 열을 표기하기 위해 값 전체를 큰 따옴표로 묶는
# 방법을 사용한다. 위의 자료는 다음과 같이 쓸 수 있다.

# %% [raw]
# 1,Mary,"You love me, don't you?",love
# 2,John,"I do love you.",dream
# 3,Suzy,"Attention, please.",heart

# %% [markdown]
# 어떤 문자를 특수한 용도로 사용하게 되면, 그 문자를 **원래 문자 그대로** 사용하기 위해
# 다른 방법을 강구해야 한다. 행구분문자로 줄바꿈문자, 열구분문자로 쉼표를 사용할 경우
# 줄바꿈문자와 쉼표를 **문자 그대로** 쓰기 위해 따옴표7로 열의 시작과 열의 끝을 표시한다고
# 생각할 수 있다. 이때 따옴표는 열의 시작과 열의 끝을 나타내는 특별한 의미를 부여받았기
# 때문에, 이를 문자 그대로를 의미하기 위해 다시 특별한 방법이 필요하다(만약 따옴표가
# 문자열에 포함되지 않는다면 문제가 되지 않는다). 이때 보통은 **따옴표를 두번 연속** 사용
# 해서 문자 따옴표를 나타내는 방식을 사용한다. 예를 들어 다음과 같다.

# %% [raw]
# 1,Mary,"I asked him, ""How are you?""",love
# 2,Paul,"I entered room.
# He saw me and ran right away",run
# 3,Jim,"""Crazy!"" He spoke.
# 'Wonderful!'
# She agreed.",agree

# %% [raw]
# 첫 번째 줄은 첫 번째 행을 나타낸다. `"How are you?"`에서 앞쪽과 뒤쪽의 따옴표를 표기
# 하기 위해 **이중 따옴표**를 사용하고 있다. 두 번째 행에서는 행구분문자도 따옴표 안에서는
# 문자 그대로의 의미로 쓰였다. 네 번째 줄의 `"""`에서 첫 번째 따옴표는 열의 시작을 나타내
# 고, 두 번째와 세 번째 따옴표는 합쳐져(이중 따옴표) 문자 따옴표 하나를 나타내고 있다.

# %%
pd.read_csv('data/string.csv', 
            sep=',', header=None,
            quotechar = '"',  
# 열구분을 보조하기 위한 인용문자 : 인용문자 안의 열분리문자는 문자 그대로 인식된다.
            doublequote=True) # 이중인용문자는 인용문자 하나로 인식된다.

# %% [markdown]
# NA로 나타내는 결측값의 경우도 생각해보자. 수치형 데이터에서 결측값은 열구분문자
# 쉼표가 연속적으로 나타나는 것으로 확인할 수 있다.
#

# %%
pd.read_csv('data/numeric2.csv', header=None)

# %% [markdown]
# 하지만 문자열 데이터의 경우에 이런 방법을 추천하기 힘들다. 왜냐하면 ''(아무런 대답도
# 하지 않은 경우)와 구분이 힘들기 때문이다.[^pdreadcsv_nan]
#
# [^pdreadcsv_nan]: 어떤 질문에 대해 아무런 대답을 하지 않은 것(`''`)과 여러 가지 이유로 대답을 들을 수 없었던 경우(NA)는
# 엄연히 다른 상황이다. 어떤 대답을 했지만 여러 가지 사정으로 그 값을 알 수 없는 경우도 `NA`로 나타낼 수 있다.

# %%

# %% [raw]
# # string2.csv
# NA,1990,desire
# "NA",1985,
# "Grande-Butera, Ariana",1993,heart

# %%
pd.read_csv('data/string2.csv', header=None,
             sep=',')

# %% [markdown]
# `pd.read_csv()`의 도움말에 따르면 `pd.read_csv()`는 기본적으로 다음의 문자열을 결측값(`np.nan`)으로 인식한다.
#
#     '', '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan',
#     '1.#IND', '1.#QNAN', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a',
#     'nan', 'null'

# %% [markdown]
# 만약 `'NA'`를 제외한 모든 문자열을 문자열 그대로 인식하고 싶다면 다음과 같이 할 수 있다.[^readcsv_na]
#
# [^readcsv_na]: 이 방법은 문자열 `"NA"`를 텍스트 파일에 포함시키는 방법이 없다는 약점이 있다. `dat.loc[1,0] = "NA"`라면 이를 어떻게 텍스트 데이터 파일로 저장할 수 있을까? 한 가지 방법은 `"NA"`와 `NA`를 구분해서 문자열 `"NA"`는 `"NA"`로 저장하고, 결측값은 `NA`로 저장하는 것이지만, `pd.read_csv()`는 `"NA"`와 `NA`를 동일하게 인식하기 때문에 `pd.read_csv()`에서는 불가능한 방법이다.

# %%
dat = pd.read_csv('data/string2.csv', header=None,
                  sep=',', 
                  keep_default_na = False, na_values=['NA'])
dat

# %% [markdown]
# 다음과 같이 `''`는 결측값(`np.nan`)으로 인식되지 않고 공문자열(`''`) 그대로 인식되었다.

# %%
dat.loc[1,2]

# %% [markdown]
# `pd.read_csv()`에서 `keep_default_na=True`로 하면 위에서 나열한 모든 문자열에 대해 결측값으로 인식한다. 추가적으로 결측값으로 인식해야 할 문자열이 있다면 `na_values=`에 리스트로 나열한다. 만약 `keep_default_na=False`로 하고, `na_values=`를 설정한다면 `na_values=`에 지정한 문자열만 결측값으로 지정된다. 

# %% [markdown]
# 인용문자 `"`는 문자열에 열구분문자(쉼표)가 포함될 때 사용하지만, 그렇지 않은 경우에도 사용할 수 있으며, 문자열에 영향을 주지 않는다. 다시 말해 `string2.csv`의 마지막 단어 `heart`는 `"heart"`로 바뀌어도 데이터에는 영향이 없다. 
#

# %%
dat2 = pd.read_csv('data/string3.csv', header=None,
                   sep=',', 
                   quotechar='"',
                   keep_default_na = False, na_values=['NA'])
dat2

# %%
dat.loc[2,2] == dat2.loc[2,2]

# %% [markdown]
# 이렇게 열구분문자(쉼표)가 문자열에 포함되지 않은 경우에 인용문자(큰 따옴표)는 선택적이다. 있어도 되고 없어도 그만이다. 만약 파일 용량을 조금이라도 줄이고 싶다면 생략하면 된다. 문제는 문자열에 인용기호(큰 따옴표)가 포함된 경우이다. 이때에도 인용기호는 생략할 수 있을까? 다음의 텍스트 데이터 파일을 보자.

# %% [raw]
# # string4.csv
# I am ok.,You are fine.,"Thank you, sir."
# "A,B","A,B"

# %% [markdown]
# 위의 텍스트는 열의 갯수가 3인 데이터를 텍스트로 나타낸 것이다. 첫 행의 두 값(첫 번째
# 열과 두 번째 열)은 쉼표를 포함하지 않기 때문에 열의 시작과 끝을 나타내기 위해 따옴표가
# 필요하지 않다. 세번째 값은 쉼표를 포함하기 때문에 두 따옴표로 값을 감싸 안았다. 두
# 번째 행을 보자. 만약 첫 번째 값이 따옴표와 대문자 A라면, 쉼표가 포함되어 있지 않기
# 때문에 따옴표로 감싸 안지 않았다. 두 번째 값은 대문자 B와 따옴표로 구성된 문자열이며,
# 이 역시 쉼표를 포함하지 않기 때문에 따옴표로 감싸지 않았다. 세 번째 값은 대문자 A,
# 쉼표, 대문자 B로 이루어진 문자열이며 이 값은 쉼표를 포함하기 때문에 따옴표로 감싸
# 안았다. 하지만 이 행은 두 번째 쉼표를 기준으로 앞과 뒤가 동일하기 때문에 첫 번째 값이
# 대문자 A, 쉼표, 대문자 B이고, 두 번째 값이 따옴표, 대문자 A, 세 번쨰 값이 대문자
# B, 따옴표로 해석될 수도 있다. 다시 말해 쉼표가 포함되지 않은 값에도 문자 따옴표가
# 포함되어 있다면 그 값을 다음과 같이 따옴표로 감싸 안아야 이런 모호함을 방지할 수 있다.

# %% [raw]
# # string5.csv
# I am ok.,You are fine.,"Thank you, sir."
# """A","B""","A,B"

# %%
pd.read_csv('data/string4.csv',
            header = None,
            sep=',', quotechar='"')

# %%
pd.read_csv('data/string5.csv',
            header = None,
            sep=',', quotechar='"')


# %% [markdown]
# ### 텍스트 데이터 파일을 불러읽을 때 고려해야 할 사항

# %% [markdown]
# 텍스트 데이터 화일을 불러 읽을 때에는 데이터를 저장할 때 고려 사항이 그대로 적용된다.
# 그 외에도 다음과 같은 고려사항이 있다.

# %% [markdown]
# #### 인코딩

# %% [markdown]
# 먼저 화일을 정확히 텍스트로 읽기 위해서는 텍스트 화일의 인코딩을 알아야 한다. 최근에
# 생성된 화일은 대부분 UTF-8를 사용한다. 하지만 그렇지 않은 경우도 있다. 확실치 않을
# 때에는 다음에 정의하는 `guess_encoding01()` 또는 `guess_encoding02()` 함수를 활용할 수 있다. 

# %% [markdown]
# (삭제 예정)하지만 UTF-8-BOM과 UTF-8의 구분은 불가능하다. notepad++라는 프로그램을 쓰면 BOM의 존재를 확인할 수 있다.[^bom] 아래에서 정의하는 `check_bom_file()` 함수는 파일의 첫 부분을 읽어서 BOM이 존재하는지 확인한다. 
#
# [^bom]: BOM이란 Byte Order Mark의 약자로 바이트 순서를 나타내는 표식이다. 자세한 내용은 <문자열>을 참조하라.

# %%
# https://stackoverflow.com/questions/436220/how-to-determine-the-encoding-of-text
def guess_encoding01(file_path, n_lines=20):
    '''Predict a file's encoding using chardet'''
    import chardet

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        #rawdata = b''.join([f.readline() for _ in range(n_lines)])
        rawdata = b''.join([f.read() for _ in range(n_lines*79)])

    return chardet.detect(rawdata)['encoding']


# %%
from bs4 import UnicodeDammit

def guess_encoding02(filename):    
    with open(filename, 'rb') as file:
        content = file.read()

    suggestion = UnicodeDammit(content)
    return suggestion.original_encoding   


# %%
guess_encoding01('R/서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv')

# %%
guess_encoding02('R/서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv')

# %% [markdown]
# 위의 결과는 정확하지 않다. `서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv`는 윈도우에서 작성되어 `CP949`로 인코딩되었다. 하지만 아래에서 확인할 수 있듯이 인코딩을 `EUC-KR`과 `CP949` 중 하나로 설정하면 결과는 동일하다.

# %% [markdown]
# (아래 삭제 예정)

# %%
## Check for BOM Markers    
from codecs import BOM_UTF8, BOM_UTF16_BE, BOM_UTF16_LE, BOM_UTF32_BE, BOM_UTF32_LE

BOMS = (
    (BOM_UTF8, "UTF-8-BOM"),
    (BOM_UTF32_BE, "UTF-32-BE-BOM"),
    (BOM_UTF32_LE, "UTF-32-LE-BOM"),
    (BOM_UTF16_BE, "UTF-16-BE-BOM"),
    (BOM_UTF16_LE, "UTF-16-LE-BOM"),
)

def check_bom(data):
    return [encoding for bom, encoding in BOMS if data.startswith(bom)]

def check_bom_file(filename):
    with open(filename, 'rb') as f:
        data = f.read(10)
    return [encoding for bom, encoding in BOMS if data.startswith(bom)]


# %%
#fn = 'R/서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv'
fn = 'data/서울시 한강공원 이용객 현황 (2009_2013년).csv'
check_bom_file(fn)

# %% [markdown]
# 인코딩을 확인해보자.

# %%
dat = pd.read_csv('R/서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb4 in position 1: invalid start byte

# %%
dat = pd.read_csv('R/서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv',
                 encoding = 'EUC-KR')
dat.head()

# %%
dat2 = pd.read_csv('R/서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv',
                 encoding = 'CP949')
dat2.head()

# %%
dat.equals(dat2)

# %% [markdown]
# 인코딩을 `UTF-8`로 설정하면 파일을 읽을 수 없다. 인코딩을 `EUC-KR` 또는 `CP949`로 하면 파일을 정확하게 읽을 수 있으며 내용도 동일하다.

# %% [markdown]
# #### 행이름(index)과 열이름(columns)

# %% [markdown]
# 텍스트 데이터 파일 안에 행이름과 열이름을 포함시킬 수 있다. 보통은 첫 행에 열이름을 적고 첫 열에 행이름을 적는다. 이를 `pd.read_csv()`의 인자로 표현하면 다음과 같다.
#
#     pd.read_csv(filename, header=0, index_col=0)
#     
# `header=`는 열이름이 나타나는 행순번을 나타내고, `index_col=`을 열이름이 나타나는 행순번을 나타낸다. `header=`는 기본값이 `'infter'`인데, 이는 알아서 추측하라는 의미이다. `index_col=`의 기본값은 `None`으로 행이름은 데이터 파일에 포함되지 않음을 의미한다.

# %% [markdown]
# 만약 데이터 프레임을 `.to_csv()` 메쏘드를 통해 텍스트 파일로 저장한다면 기본적으로 행이름과 열이름을 포함하게 된다. 

# %%
dat.to_csv('R/Seoul_public_bicycle.csv', encoding = 'UTF-8')

# %%
with open('R/Seoul_public_bicycle.csv', 'rt', encoding = 'UTF-8') as f:
    txt = f.readlines()
    for x in txt[:5]:
        print(x, end='')

# %% [markdown]
# `.to_csv()`로 작성된 파일 `Seoul_public_bicycle.csv`의 처음을 보면 첫 줄에 열이름이 있고, 첫 열은 행이름이 있음을 확인할 수 있다. 그래서 이렇게 `to_csv()`로 작성된 데이터 파일을 읽을 때에는 `index_col=0`으로 행이름이 포함되어 있음을 알려줘야 한다. 그렇지 않으면 행이름이 새로운 열로 포함되게 된다. 다음의 두 결과를 비교해보자.

# %%
dat2 = pd.read_csv('R/Seoul_public_bicycle.csv', encoding = 'UTF-8')
dat2.head()


# %%
dat2 = pd.read_csv('R/Seoul_public_bicycle.csv', encoding = 'UTF-8',
                  index_col=0)
dat2.head()

# %% [markdown]
# #### 수를 표기하는 방법

# %% [markdown]
# 수를 표기하는 방법은 나라마다 다르다. 우리나라는 소수점으로 점, 천단위 기호로 쉼표를 사용하지만, 반대인 경우도 많다. 부록 <수표기>를 확인하자. 

# %% [markdown]
# `pd.read_csv()`의 매개변수 `decimal=`과 `thousands=`를 통해 소수점과 천단위 기호를 설정해줄 수 있다. 
#

# %% [markdown]
# #### 그 밖에

# %% [markdown]
# 그 밖에서 주석을 의미하는 기호, 날짜형 자료의 표기 방법 등을 설정할 수 있다. 주석을 의미하는 기호는 `comment=`를 사용하여, 날짜형 자료의 표기 방법은 `infer_datetime_format=`, `dayfirst=` 등을 통해 조정할 수 있다.

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ### === END OF DOCUMENT

# %%

# %%

# %%

# %%

# %%
txt = """
#1234567891123456789212345678931234567894123456789512345678961234567897123456789
#         *         *         *         *         *         *         *
  rank    title      genre foreign   release          gross  audience screen
0    1     명량       액션   False 2014-07-30  1357.4839891 1761.3682   1587
1    2 극한직업     코메디   False 2018-01-23 1396.47979516 1626.4944   1978
2    4 어벤져스       액션    True 2019-04-24  1221.8269416 1393.4592   2835
3    6 겨울왕국 애니메이션    True 2019-11-21  1148.1042145 1374.7792    264
"""
with open('data/movies.fwf', 'wt', encoding = 'UTF-8') as f:
    f.write(txt)

# %%
print(txt)

# %%
with open('data/movies.fwf', encoding = 'UTF-8') as f:
    for x in f.readlines():
        print(x, end='')    

# %%
pd.read_fwf('data/movies.fwf', encoding = 'UTF-8', 
            colspecs = [(0,1), (2,6), (6,15), (16,26),
                        (27,34)],
           comment='#')

# %%
import numpy as np
x = np.array([2,4,12,23,29,40,54,64,69])

# %%
print(x[1:] - x[:-1])

# %%
import pandas as pd

# %%
pd.read_fwf('data/movies.fwf', encoding = 'UTF-8',
            comment = '#')

# %%
pd.read_fwf('data/movies.fwf', widths=[1,5,8,11,8,11,14,10,7], encoding = 'UTF-8',
           comment = '#', header = 0)

# %%

# %%

# %%

# %% [markdown]
# 텍스트로 데이터(특히 데이터프레임과 같이 직사각형 형태의 데이터)를 저장할 때 가장 중요한 결정 사항은 행구분자(row seperator, row delimiter)와 열구분자이다. 텍스트 데이터 파일에서 대부분 행구분자는 `'\r'`, `'\n'` 또는 `'\r\n'`이다. 그리고 열구분자로 많이 쓰이는 것은 `","`(쉼표, comma), `"\t"`(탭, tab) 등이다.

# %%
