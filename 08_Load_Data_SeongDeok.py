# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: rtopython3-pip
#     language: python
#     name: rtopython3-pip
# ---

# %% [markdown]
# ## 8장
#
# * TO-DO
#     - 문자열 관련 : `str()`, `.decode('cp949')` ...

# %% [markdown]
# ### 들어가기
#
# 파이썬 데이터 프레임에 저장된 내용은 파이썬을 종료함과 동시에 사라지게 된다. 자료를 나중에 사용하거나, 다른 사람에게 넘겨주려면 데이터를 화일로 저장하고, 다음에 저장된 데이터를 화일로부터 읽어야 한다.
#
# 데이터를 화일에 저장하는 방식에는 여러 가지가 있지만, 크게 **텍스트 화일(text file)** 로 저장하는 방식과 **이진 화일(binary file)** 로 저장하는 방식으로 구분해 볼 수 있다. 텍스트 화일은 사람이 화일을 열어서 내용을 읽을 수 있는 화일이다. 텍스트 화일은, 이진수로 쓰여서 컴퓨터만 읽을 수 있는 이진 화일과 다르게 사람이 전체적인 내용을 확인하거나, 오류를 직접 수정할 수 있다는 장점이 있다. (반면 이진 화일에 비해 텍스트 화일은 용량이 커지는 단점이 있지만, 텍스트로 쓰여진 확인할 수 없는 데이터의 타입 등을 저장할 수 있다는 장점도 있다.)
#
# 이번 장에서는 파이썬으로 데이터 화일을 불러 읽는 방법에 대해 설명한다. 데이터 분석은 외부의 데이터를 파이썬으로 불러 읽는 것부터 시작하기 마련이다. 하지만 여러 가지 이유로 외부 데이터를 파이썬으로 불러들이는 데에 문제가 생기는 경우를 종종 목격하게 된다. 
#
# 특히 텍스트 화일로 저장된 데이터의 경우, 사람들이 읽을 수 있고, 확인할 수 있다는 점에서 큰 어려움이 없어보이지만, 항상 그런 것은 아니다. 왜냐하면 동일한 내용을 텍스트 화일로 저장하는 방법에는 여러 가지 다양한 방법이 존재하며, 특히 사람이 직접 고칠 수 있다는 점 때문에 컴퓨터만이 생성할 수 있는 이진 화일에 비해 오류가 발생하는 빈도도 높다. 
#
# 따라서 텍스트 화일을 불러들이는 방법은 조금 자세하게 설명할 필요가 있다. 특히 화일 읽기의 여러 옵션이 왜 필요한지를 이해할 수 있어야 텍스트 화일을 읽을 때 오류가 생기더라도 문제를 해결할 수 있다. 필자는 우선 어떤 데이터를 텍스트 화일로 저장할 때 고려해야 할 사항이 어떤 것이 있는지를 설명하고, 이런 고려 사항이 텍스트 데이터 화일을 읽을 때 어떻게 반영되는지를 설명하려고 한다.
#

# %% [markdown]
# ## 8.0.1

# %% [markdown]
# ## 데이터 불러오기 
#
# * 데이터
#     - R 내장 데이터 : `pydataset.data()`
#     - 싸이킷-런(scikit-learn)의 `datasets`
# * 기본적인 방법 
#     - 텍스트 데이터 화일 : `df.to_csv()`, `pd.read_csv()`
#     - 이진 데이터 화일 : `df.to_pickle()`, `pd.read_pickle()` 
# * 텍스트로 저장된 화일 읽어오기
#     - `pd.read_csv()`
#     - 빅데이터 : `dt.fread()`
# * 엑셀화일 : `pd.read_excel()`
# * 웹에서 긁어오기 : `pd.read_html()`
# * 그 밖에
#     - 문자열에서 바로 읽기 : `pd.read_csv(io.StringIO("...   "))`

# %% [markdown]
# ## 8.1

# %% [markdown]
# ### `pydataset` package

# %%
import numpy as np
import pandas as pd
from dataset_pydataset import data
data().head() # 전제 데이터 리스트

# %%
## 파이썬에 BankWages 라이브러리 동일하지 않음
Wages1 = data('Wages1')
Wages1.head()

# %%
import matplotlib.pyplot as plt
plt.scatter('exper', 'wage', data=Wages1)

# %%
Bwages = data('Bwages')
plt.scatter('exper', 'wage', data=Bwages)

# %% [markdown]
# ### 모듈 `sklearn`(scikit-learn)의 `datasets`

# %%
from sklearn import datasets
# 사용 가능한 데이터 리스트
[x for x in dir(datasets) if x.startswith('load')]

# %%
skdat = datasets.load_boston()
# skdat = datasets.load_breast_cancer()
# skdat = datasets.load_diabetes()
# skdat = datasets.load_digits()  
# skdat = datasets.load_iris()
# skdat = datasets.load_linnerud()
# skdat = datasets.load_wine()
print(skdat.keys()) #'data', 'target', ('frame', 'target_names',) 'feature_names', 'DESCR', 'filename'('data_filename', 'target_filename')
pd.DataFrame(data=skdat['data'], columns = skdat['feature_names']).head()

# %% [markdown]
# ## 8.2 파이썬에서 생성된 텍스트 데이터 화일 불러읽기
#
# 1. 판다스 데이터 프레임을 화일로 쓰기 : `dat.to_csv(FILENAME)`
# 2. 저장된 데이터 화일을 데이터 프레임으로 읽기 : `pd.read_csv(FILENAME, index_col=0)`
#
# * csv = **c**omma(`,`) **s**perated **v**alue
#
# 1. 먼저 파이썬의 데이터 프레임에 저장된 데이터를 화일로 저장하고, 다시 파이썬으로 불러들이는 방법을 알아봅시다. 판다스 데이터 프레임의 내용은 `.to_csv()` 메쏘드를 써서 화일로 저장할 수 있습니다. 메쏘드의 첫 번째 인자로 화일 이름을 적습니다.
#
# 2. 이렇게 저장된 데이터 화일은 텍스트 편집기로 그 내용을 확인할 수 있고, 수정도 가능합니다. 그리고 이 데이터 화일을 다시 파이썬으로 불러들이기 위해서는 `pandas`의 `read_csv()` 함수를 사용합니다. 이때 첫 번째 인자로 화일 이름을 적어줍니다. 이렇게 불러들인 데이터를 확인해 보면, 저장한 데이터와 크게 차이가 없지만 조금 다릅니다. 만약 저장한 데이터 프레임과 동일한 데이터 프레임을 얻고 싶다면 화일 이름 다음에 `index_col=0`을 써야 합니다. `index_col=`은 인덱스가 데이터 화일의 몇 번째 열, column에 있는지를 나타냅니다. 데이터 프레임에 `.to_csv()` 메쏘드를 사용한 결과 화일을 보면 데이터 프레임의 인덱스가 저장되어 있음을 확인할 수 있습니다. 그래서 `index_col=0`을 써주면 0번째 열은 데이터 프레임의 인덱스가 됩니다.

# %%
dat = data("mtcars")

# %%
dat.head(3)

# %%
type(dat)

# %%
dat.to_csv('dat.txt')

# %%
dat02 = pd.read_csv('dat.txt', index_col=0)  # rowname 대신 index란 용어를 사용한다!
# dat.to_csv('dat.txt') 는 pd.read_csv('dat.txt', index_col=0)과 대응된다!

# %%
dat.equals(dat02)
(dat - dat02).iloc[14:17]

# %%
np.savetxt(r'dat.txt', dat.values, fmt='%d') # %d : 정수꼴 
#np.savetxt(r'dat.txt', dat.values, fmt='%d', header='', footer='') # header, footer 기본값
# dat.txt 내용
# 21 6 160 110 3 2 16 0 1 4 4
# 21 6 160 110 3 2 17 0 1 4 4
# 22 4 108 93 3 2 18 1 1 4 1

dat02 = pd.read_table("dat.txt", header=None, sep=' ')
dat02.head()


# %%
np.savetxt(r'dat.txt', dat.values, fmt='%10.5f') 
# __23.44521 꼴 (전체 10개 문자로 구성(소수점 포함). 소수점 이하 5개 )
# fmt='%.18e' 기본값
dat02 = pd.read_table("dat.txt", header=None, sep='\\s+') # 1 or more spaces
dat02.head()

# %%
dat02.columns = dat.columns
dat02.index = dat.index
dat02.head()

# %%
dat.equals(dat02)


# %%
(dat - dat02).head()
#(dat - dat02).iloc[14:17]


# %%
# 그 밖의 numpy의 데이터 저장 함수
#save : Save an array to a binary file in NumPy ``.npy`` format
#savez : Save several arrays into an uncompressed ``.npz`` archive
#savez_compressed : Save several arrays into a compressed ``.npz`` archive

# %%
# 텍스트 데이터 화일에서 담아내지 못하는 부분 
# 예) data type(categorical vs. string, int32 vs int64)

# %%
mtcars['am2'] = np.where(mtcars['am'] == 1, 'auto', 'manual')
mtcars['am3'] = pd.Categorical(mtcars['am2'])
mtcars.info()

# %%
mtcars.to_csv('mtcars.csv')
dat = pd.read_csv('mtcars.csv', index_col=0)
dat.equals(mtcars)

# %%
dat = pd.read_csv('mtcars.csv', index_col=0,
                  dtype={'am3':'category'})
dat.equals(mtcars)

# %%
dat.info()

# %%
# 이진수로 저장하기 : pandas.to_pickle, pandas.read_pickle

# %%
dat.to_pickle('dat.pkl')
dat2 = pd.read_pickle('dat.pkl')
dat.equals(dat2)

# %%
# 이진수로 저장하기 : pickle package
import pickle
pickle.dump(dat, open('dat.pkl', 'wb'))
dat2 = pickle.load(open('dat.pkl', 'rb'))
dat.equals(dat2)

# %%
import os
os.path.getsize("dat.txt")
os.path.getsize("dat.pkl")

# %%
dat = data('Gasoline')

# %%
dat.to_csv('Gasoline.txt')

# %%
pickle.dump(dat, open('Gasoline.pkl', 'wb'))

# %%
print(os.path.getsize('Gasoline.txt'))
print(os.path.getsize('Gasoline.pkl'))


# %% [markdown]
# ## 8.3 외부에서 작성된 텍스트 데이터 화일 불러읽기 : `pd.read_csv()`
#
# * 고려해야 할 사항
#   * 열을 어떻게 구분할 것인가?
#   * 행이름과 열이름도 포함되어 있는가?
#
# * 그 밖에 고려해야 할 사항([판다스 `pd.read_csv` 도움말](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) 참조)
#   * 인용부호 : 열구분기호를 데이터에 포함시키려면?
#     * 인용부호를 데이터에 포함시키려면? 
#   * 숫자 표기 방법
#     - 소수점 기호 : `decimal="."`
#     - 1000단위 자리 기호 : `thousands=None`

# %% [markdown]
# ## 8.3.1

# %%
datMsg = pd.DataFrame({
    'name':['BTS', '트와이스', '케이티 킴'],
    'phone':['010-4342-584x', '010-5821-443x', '010-5532-443x'],
    'usageLastMonth':[38000, 58000, 31000],
    'message':['안녕, 날씨 좋다! "너무 좋다"라고 노래 부르고 싶다',
              '달빛 아래 춤추자! \'너무너무너무\'라고 노래 부를래',
              'Memorable'],
    'price':[30, 10, np.nan]
})


# %% [markdown]
# R에서 처음 위의 구문을 보게 되면, 엄청 복잡하고, 불편하게 보인다.
# 중괄호(`{`)에 따옴표(`'`)에 대괄호(`[`)까지...
# 다음의 함수를 정의하면, R 스타일로 데이터프레임을 만들 수 있다. 

# %%
def pdDataFrame(**kwargs):
    return pd.DataFrame(kwargs)

# %%
datMsg =pdDataFrame(
    name =  ["BTS", "트와이스", "케이티 킴"],
    phone = ['010-4342-584x', '010-5821-443x', '010-5532-443x'],
    usageLastMonth = [38000, 58000,31000],
    message = ['안녕, 날씨 좋다! "가즈아!"라고 말하고 싶다.',
                '달빛 아래 춤추자! \'너무너무너무\'라고 노래 부를래.',
                'Memorable'],
    price = [30, 10, np.nan])
datMsg

# %% [markdown]
# 만약 `pd.DataFrame`의 옵션이 필요하다면, 다음의 함수르

# %%
def pdDataFrame(**kwargs):
    ar_opt = {}
    ar_data = {}    
    for k in kwargs:
        #print(k)
        if k.startswith('_'):
            ar_opt[k[1:]] = kwargs[k]
        else:
            ar_data[k] = kwargs[k]
    
    #print(ar_opt)
    #print(ar_data)
    
    return pd.DataFrame(ar_data, **ar_opt)

# %%
pdDataFrame(
    _index =  ["BTS", "트와이스", "케이티 킴"],
    phone = ['010-4342-5842', '010-5821-4433', '010-5532-4432'],
    usageLastMonth = [38000, 58000,31000],
    message = ['안녕, 날씨 좋다! "가즈아!"라고 말하고 싶다.',
                '달빛 아래 춤추자! \'너무너무너무\'라고 노래 부를래.',
                'Memorable'],
    price = [30, 10, np.nan])    
#pd.DataFrame(ar_data, **{'index':[], })
#pd.DataFrame(ar_data, index = [], )

# %% [markdown]
# ## 8.3.2 

# %%
datMsg.to_csv("dat.csv")

# %%
datMsg02 = pd.read_csv("dat.csv")

# %%
datMsg.equals(datMsg02)

# %%
datMsg02.head(3)

# %%
datMsg03 = pd.read_csv("dat.csv", index_col=0)

# %%
datMsg.equals(datMsg03)


# %% [raw]
# %pip install tables

# %% [raw]
# Collecting tables
#   Downloading tables-3.6.1-cp36-cp36m-manylinux1_x86_64.whl (4.3 MB)
#      |████████████████████████████████| 4.3 MB 2.8 MB/s eta 0:00:01
# Collecting numexpr>=2.6.2
#   Downloading numexpr-2.7.1-cp36-cp36m-manylinux1_x86_64.whl (162 kB)
#      |████████████████████████████████| 162 kB 33.3 MB/s eta 0:00:01
# Requirement already satisfied: numpy>=1.9.3 in /home/publishingkwon/anaconda3/envs/pytorch/lib/python3.6/site-packages (from tables) (1.18.1)
# Installing collected packages: numexpr, tables
# Successfully installed numexpr-2.7.1 tables-3.6.1
# Note: you may need to restart the kernel to use updated packages.

# %%
datMsg.to_hdf('datMsg.h5', key='a') # key for multiple objects

# %%
pd.read_hdf('datMsg.h5')

# %%
store = pd.HDFStore('store.h5')

# %%
store.root

# %%
store['a'] = datMsg

# %%
store['b'] = dat

# %%
store

# %%
store.close()

# %%

# %%
pd.read_hdf('store.h5', key='a')

# %% [markdown]
# 위의 함수를 실행할 때, 다음과 같은 에러가 발생할 수 있다. 
#
# `ValueError: The file 'store.h5' is already opened, but not in read-only mode (as requested).`
#
# 이 경우, `pytables`와 관련된 패키지의 버전 문제일 수 있으니, 패키지를 업그레이드한다.
#
# * 참조: https://stackoverflow.com/questions/14591855/pandas-hdfstore-how-to-reopen

# %% [raw]
# %conda install pytables

# %% [raw]
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
#
#
# ==> WARNING: A newer version of conda exists. <==
#   current version: 4.7.10
#   latest version: 4.8.4
#
# Please update conda by running
#
#     $ conda update -n base -c defaults conda
#
#
#
# ## Package Plan ##
#
#   environment location: /home/publishingkwon/anaconda3/envs/pytorch
#
#   added / updated specs:
#     - pytables
#
#
# The following packages will be downloaded:
#
#     package                    |            build
#     ---------------------------|-----------------
#     blosc-1.20.0               |       hd408876_0          71 KB
#     bzip2-1.0.8                |       h7b6447c_0          78 KB
#     lzo-2.10                   |       h7b6447c_2         184 KB
#     mock-4.0.2                 |             py_0          32 KB
#     pytables-3.6.1             |   py36h71ec239_0         1.3 MB
#     snappy-1.1.8               |       he6710b0_0          40 KB
#     ------------------------------------------------------------
#                                            Total:         1.6 MB
#
# The following NEW packages will be INSTALLED:
#
#   blosc              pkgs/main/linux-64::blosc-1.20.0-hd408876_0
#   bzip2              pkgs/main/linux-64::bzip2-1.0.8-h7b6447c_0
#   lz4-c              pkgs/main/linux-64::lz4-c-1.9.2-he6710b0_1
#   lzo                pkgs/main/linux-64::lzo-2.10-h7b6447c_2
#   mock               pkgs/main/noarch::mock-4.0.2-py_0
#   pytables           pkgs/main/linux-64::pytables-3.6.1-py36h71ec239_0
#   snappy             pkgs/main/linux-64::snappy-1.1.8-he6710b0_0
#
# The following packages will be UPDATED:
#
#   libtiff                                  4.1.0-h2733197_0 --> 4.1.0-h2733197_1
#   xz                                       5.2.4-h14c3975_4 --> 5.2.5-h7b6447c_0
#   zstd                                     1.3.7-h0b5b093_0 --> 1.4.5-h9ceee32_0
#
#
#
# Downloading and Extracting Packages
# blosc-1.20.0         | 71 KB     | ##################################### | 100% 
# mock-4.0.2           | 32 KB     | ##################################### | 100% 
# bzip2-1.0.8          | 78 KB     | ##################################### | 100% 
# lzo-2.10             | 184 KB    | ##################################### | 100% 
# snappy-1.1.8         | 40 KB     | ##################################### | 100% 
# pytables-3.6.1       | 1.3 MB    | ##################################### | 100% 
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
#
# Note: you may need to restart the kernel to use updated packages.

# %%
pd.read_hdf('store.h5', key='b')


# %% [markdown]
# ## 8.3.3

# %%
# 1. 텍스트 인코딩
#   readr::guess_encoding 을 통해 유추 가능. 하지만 확실치 않음
#
#   notepad++^3 등의 문서작성 프로그램을 활용하여 인코딩을 확인할 수도 있다.
#   특히 UTF-8BOM과 UTF-8의 구분은 readr::guess_encoding()에서는 불가능 하지만 notepad++에서는 가능
#
# 2. 전체적인 형식: 아래에서 c(,) 로 묶인 원소 중 하나를 선택해야 한다.
#   예) header=TRUE 또는 header = FALSE
#   
#   행이름을 포함하는가? header=c(TRUE,FALSE)
#   열이름을 포함하는가? row.names = c(1,NULL)
#   열 구분자(delimiter) sep=c('\t',',','')
#
# 3.데이터를 표기하는 방법
#   주석은 어떻게 구분하는가? comment.char =
#   따옴표(quotation mark; 문자열 속에 열 구분자를 포함시켜야 할 경우를 생각해보자): quote=
#   소수점 표기 방법(decimal seperator): dec=(나라마다 소수점 표기방법이 다르다.)
#
# 4.그밖에
#   stringsAsFactors = c(TRUE,FALSE)

# %%
import magic
# # !pip3 install magic
# https://stackoverflow.com/questions/436220/how-to-determine-the-encoding-of-text
def predict_encoding(file_path, n_lines=20):
    '''Predict a file's encoding using chardet'''
    import chardet

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        rawdata = b''.join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)['encoding']

predict_encoding('dat.csv')

# %%
import sys
if int(sys.version[0]) != 3:
    print('Aborted: Python 3.x required')
    sys.exit(1)

def bomType(file):
    """
    returns file encoding string for open() function

    EXAMPLE:
        bom = bomtype(file)
        open(file, encoding=bom, errors='ignore')
    """

    f = open(file, 'rb')
    b = f.read(4)
    f.close()

    if (b[0:3] == b'\xef\xbb\xbf'):
        return "utf8"

    # Python automatically detects endianess if utf-16 bom is present
    # write endianess generally determined by endianess of CPU
    if ((b[0:2] == b'\xfe\xff') or (b[0:2] == b'\xff\xfe')):
        return "utf16"

    if ((b[0:5] == b'\xfe\xff\x00\x00') 
              or (b[0:5] == b'\x00\x00\xff\xfe')):
        return "utf32"

    # If BOM is not provided, then assume its the codepage
    #     used by your operating system
    return "cp1252"
    # For the United States its: cp1252


def OpenRead(file):
    bom = bomType(file)
    return open(file, 'r', encoding=bom, errors='ignore')


# %%
#######################
# Testing it
#######################
fout = open("myfile1.txt", "w", encoding="cp1252")
fout.write("* hi there (cp1252)")
fout.close()

fout = open("myfile2.txt", "w", encoding="utf8")
fout.write("\u2022 hi there (utf8)")
fout.close()

# this case is still treated like codepage cp1252
#   (User responsible for making sure that all utf8 files
#   have a BOM header)
fout = open("badboy.txt", "wb")
fout.write(b"hi there.  barf(\x81\x8D\x90\x9D)")
fout.close()

# Read Example file with Bom Detection
fin = OpenRead("myfile1.txt")
L = fin.readline()
print(L)
fin.close()

# Read Example file with Bom Detection
fin = OpenRead("myfile2.txt")
L =fin.readline() 
print(L) #requires QtConsole to view, Cmd.exe is cp1252
fin.close()

# Read CP1252 with a few undefined chars without barfing
fin = OpenRead("badboy.txt")
L =fin.readline() 
print(L)
fin.close()



# %%

# %%
import requests
import lxml.html as lh
import pandas as pd

url = 'http://pokemondb.net/pokedex/all'
url = 'http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.csv'
page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')

[len(T) for T in tr_elements[:12]]

# %%
# ?open

# %%
## 인터넷에서 읽어오기

# %%
from urllib.request import urlopen
textPage = urlopen("http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.csv")
txt1 = textPage.read()
#txt2 = str(textPage.read(), 'UTF-8')

# %%
txt1

# %%
str(txt1)

# %%
#txt1.decode('ascii')
#txt1.decode('utf-8')
txt1.decode('cp949')

# %%
from io import StringIO
import pandas as pd

txtio1 = StringIO(txt1.decode('cp949'))

dat = pd.read_csv(txtio1, sep=";")
dat

# %%
page


# %%

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

guess_encoding01('dat.csv')

# %%
guess_encoding01('서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv')
# EUC-KR과 CP949의 차이?

# %%
from bs4 import UnicodeDammit

def guess_encoding02(filename):    
    with open(filename, 'rb') as file:
        content = file.read()

    suggestion = UnicodeDammit(content)
    return suggestion.original_encoding   

guess_encoding02('서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv')

# %%
import magic
# pip install python-magic-bin # windows

def guess_encoding03(filename):
    blob = open(filename, 'rb').read()
    m = magic.Magic(mime_encoding=True)
    encoding = m.from_buffer(blob)
    return encoding

guess_encoding03('서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv')


# %%
# https://unicodebook.readthedocs.io/guess_encoding.html

## isASCII
def isASCII(data):
    try:
        data.decode('ASCII')
    except UnicodeDecodeError:
        return False
    else:
        return True
    
## Check for BOM Markers    
from codecs import BOM_UTF8, BOM_UTF16_BE, BOM_UTF16_LE, BOM_UTF32_BE, BOM_UTF32_LE

BOMS = (
    (BOM_UTF8, "UTF-8"),
    (BOM_UTF32_BE, "UTF-32-BE"),
    (BOM_UTF32_LE, "UTF-32-LE"),
    (BOM_UTF16_BE, "UTF-16-BE"),
    (BOM_UTF16_LE, "UTF-16-LE"),
)

def check_bom(data):
    return [encoding for bom, encoding in BOMS if data.startswith(bom)]

## isUTF8
def isUTF8(data):
    try:
        data.decode('UTF-8')
    except UnicodeDecodeError:
        return False
    else:
        return True


# %%
n_lines = 20
with open('서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv', 'rb') as f:
    # Join binary lines for specified number of lines
    #rawdata = b''.join([f.readline() for _ in range(n_lines)])
    rawdata = b''.join([f.read() for _ in range(n_lines*79)])
isASCII(rawdata), check_bom(rawdata), isUTF8(rawdata)

# %%

# %%
dat01 = pd.read_csv('Seoul_Hangang_Tourist_2009_2013.csv', encoding = 'UTF-8')
dat01.head()

# %%
dat01 = pd.read_csv('Seoul_Hangang_Tourist_2009_2013.csv', header =0)
dat01.head()

# %%
# %ls "서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv"

# %%
#dat02 = pd.read_csv('서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv')
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb4 in position 1: invalid start byte
dat02 = pd.read_csv('서울특별시 공공자전거 대여소별 이용정보(월간)_2017_1_12.csv', encoding='CP949')
#https://m.blog.naver.com/PostView.nhn?blogId=youji4ever&logNo=221592440302&proxyReferer=https:%2F%2Fwww.google.com%2F

# %%
dat02.head(n=3)

# %% [raw]
# dat03 = pd.read_csv("http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.csv")
# ## codec 오류 발생 : 위에서와 동일하게 처리

# %% [raw]
# ---------------------------------------------------------------------------
# UnicodeDecodeError                        Traceback (most recent call last)
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_tokens()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_with_dtype()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._string_convert()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers._string_box_utf8()
#
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xaa in position 1: invalid start byte
#
# During handling of the above exception, another exception occurred:
#
# UnicodeDecodeError                        Traceback (most recent call last)
# <ipython-input-60-7b098b49c174> in <module>
# ----> 1 dat03 = pd.read_csv("http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.csv")
#       2 ## codec 오류 발생 : 위에서와 동일하게 처리
#
# ~/anaconda3/envs/rtopython2/lib/python3.6/site-packages/pandas/io/parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision)
#     674         )
#     675 
# --> 676         return _read(filepath_or_buffer, kwds)
#     677 
#     678     parser_f.__name__ = name
#
# ~/anaconda3/envs/rtopython2/lib/python3.6/site-packages/pandas/io/parsers.py in _read(filepath_or_buffer, kwds)
#     452 
#     453     try:
# --> 454         data = parser.read(nrows)
#     455     finally:
#     456         parser.close()
#
# ~/anaconda3/envs/rtopython2/lib/python3.6/site-packages/pandas/io/parsers.py in read(self, nrows)
#    1131     def read(self, nrows=None):
#    1132         nrows = _validate_integer("nrows", nrows)
# -> 1133         ret = self._engine.read(nrows)
#    1134 
#    1135         # May alter columns / col_dict
#
# ~/anaconda3/envs/rtopython2/lib/python3.6/site-packages/pandas/io/parsers.py in read(self, nrows)
#    2035     def read(self, nrows=None):
#    2036         try:
# -> 2037             data = self._reader.read(nrows)
#    2038         except StopIteration:
#    2039             if self._first_chunk:
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader.read()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._read_low_memory()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._read_rows()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_column_data()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_tokens()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_with_dtype()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._string_convert()
#
# pandas/_libs/parsers.pyx in pandas._libs.parsers._string_box_utf8()
#
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xaa in position 1: invalid start byte
#

# %%
guess_encoding01("JoEG_BP_diversity_data.csv"), \
guess_encoding02("JoEG_BP_diversity_data.csv"), \
guess_encoding03("JoEG_BP_diversity_data.csv")

# %%
import pandas as pd

# %%
dat03 = pd.read_csv("http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.csv", \
                   encoding='ISO-8859-1')

# %%
dat03 = pd.read_csv("http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.csv", \
                   encoding='CP949')

# %%
dat03.head(n=3)

# %%
dat03 = pd.read_csv("http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.csv", \
                    sep=';', \
                   encoding='CP949')
dat03.head()

# %% [markdown]
# ## 8.3.4

# %% [raw]
# readr::read_delim(file = , delim =  ,col_names = )

# %% [raw]
# data.table::fread(file=, sep=, header = )

# %%
import datatable as dt

# %%
dt.fread("http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.csv")

# %% [markdown]
# 데이터테이블이 출력되는 형식도 눈여겨보자. 문자열 컬럼은 빨간색, 정수 컬럼은 녹색, 실수 컬럼은 파란색이다.

# %% [markdown]
# # 8.3.5

# %%
# dat1 <- read.table('UTF-8test.txt', 
#                    sep=',', 
#                    fileEncoding='UTF-8',
#                    stringsAsFactors=FALSE);
# dat1

dat1 = pd.read_csv('UTF-8test.txt',
                   encoding='UTF-8'
                   );
dat1


# %%
dat1 = pd.read_csv('UTF-8test2.txt',
                   encoding='UTF-8'
                   );
dat1

# %%
dat1 = pd.read_csv('UTF-8test.txt',
                   encoding='UTF-8',
                   quotechar='"',
                   doublequote=True
                   );
dat1

# %%
# ?pd.read_csv

# %%
import csv

# %%
## csv quoting constants
# csv.QUOTE_ALL, QUOTE_MINIMAL, QUOTE_NONNUMERIC, QUOTE_NONE

# %%
dat1 = pd.read_csv('UTF-8test.txt',
                   encoding='UTF-8',
                   quotechar='"',
                   doublequote=True,
                   header=None,
                   quoting=csv.QUOTE_ALL
                   );
dat1

# %%
# dat2 <- readr::read_delim('UTF-8test.txt',
#                           delim=',',
#                           col_names=FALSE);
        
# dat2

dat2 = pd.read_table('UTF-8test.txt', 
                   sep=',', 
                   encoding='UTF-8',
                   header=None
                   );
dat2


# %%
dat = pdDataFrame(col1=["création d'un rôle","初演","초연"],
                 col2=['""ÿ""', "重役",'"중역"이라고'])

# %%
dat.to_csv("dat.csv")
dat2 = pd.read_csv("dat.csv", index_col=0)
dat.equals(dat2)

# %%
with open("dat.csv", "rt", encoding='UTF-8') as f:
    print(f.readlines())

# %%
# dat3 <- data.table::fread('UTF-8test.txt', 
#                           sep=',', 
#                           header=FALSE, 
#                           encoding='UTF-8'); 
# dat3

dat3 = dt.fread('UTF-8test.txt')
dat3

# %% [markdown]
# 위에서 보면 정확하게 읽은 것은 `dt.fread()` 뿐이다. 어떻게 `pd.read_table()`로도 정확하게 읽을 수 있을까?

# %%
dat3.to_pandas().to_csv('UTF-8test.csv')

# %%
pd.read_csv('UTF-8test.csv', index_col=0)

# %%
pd.read_table('UTF-8test.csv', index_col=0, quotechar='"', doublequote=True, sep=',')

# %% [markdown]
# 이번에는 정확하게 읽었다. 그렇다면 화일내용을 확인해보자.

# %%
with open('UTF-8test.csv', encoding='UTF-8') as f:
# 윈도우에서는 open(encoding = '')의 기본값은 cp949인 듯
    lns = f.readlines()
    for l in lns:
        print(l)

# %%
## Window error
# ---------------------------------------------------------------------------
# UnicodeDecodeError                        Traceback (most recent call last)
# <ipython-input-64-2688d787a9f5> in <module>
#       1 with open('UTF-8test.csv') as f:
# ----> 2     lns = f.readlines()
#       3     for l in lns:
#       4         print(l)

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xe5 in position 34: illegal multibyte sequence

# %% [markdown]
# ## 8.3.5.1

# %%
# dat1$V1
# dat3$V1


# dat3df <- as.data.frame(dat3); dat3tb <- tibble::as_tibble(dat3)
# print(dat3df); print(dat3df$V1)

# print(dat3tb); print(dat3tb$V1)

# %% [markdown]
# ## 8.4

# %% [raw]
# excel_sheets(path= )
# read_excel(path= , sheet= )

# %%
pd.read_excel('서울시 한강공원 이용객 현황 (2009_2013년).xls')
#install xlrd
#ValueError: Your version of xlrd is 2.0.1. In xlrd >= 2.0, only the xls format is supported. Install openpyxl instead.
#openpyxl

# %% [markdown]
# ## 8.4.1

# %%
#rm(list=ls())

# %%
fn = "excel_example.xls"
vSh = pd.read_excel(fn)

# %%
vSh

# %% [raw]
# %conda install xmltodict

# %% [raw]
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
#
#
# ==> WARNING: A newer version of conda exists. <==
#   current version: 4.7.10
#   latest version: 4.8.4
#
# Please update conda by running
#
#     $ conda update -n base -c defaults conda
#
#
#
# ## Package Plan ##
#
#   environment location: /home/publishingkwon/anaconda3/envs/rtopython2
#
#   added / updated specs:
#     - xmltodict
#
#
# The following packages will be downloaded:
#
#     package                    |            build
#     ---------------------------|-----------------
#     xmltodict-0.12.0           |             py_0          14 KB
#     ------------------------------------------------------------
#                                            Total:          14 KB
#
# The following NEW packages will be INSTALLED:
#
#   xmltodict          pkgs/main/noarch::xmltodict-0.12.0-py_0
#
#
#
# Downloading and Extracting Packages
# xmltodict-0.12.0     | 14 KB     | ##################################### | 100% 
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
#
# Note: you may need to restart the kernel to use updated packages.

# %%


def get_sheet_details(filename):
    sheets = []
    # Make a temporary directory with the file name
    directory_to_extract_to = (filename.with_suffix(''))
    directory_to_extract_to.mkdir(parents=True, exist_ok=True)
    # Extract the xlsx file as it is just a zip file
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()
    # Open the workbook.xml which is very light and only has meta data, get sheets from it
    path_to_workbook = directory_to_extract_to / 'xl' / 'workbook.xml'
    with open(path_to_workbook, 'r') as f:
        xml = f.read()
        dictionary = xmltodict.parse(xml)
        for sheet in dictionary['workbook']['sheets']['sheet']:
            sheet_details = {
                'id': sheet['@sheetId'],  # can be sheetId for some versions
                'name': sheet['@name']  # can be name
            }
            sheets.append(sheet_details)
    # Delete the extracted files directory
    shutil.rmtree(directory_to_extract_to)
    return sheets


# %%

# %%
pd.read_excel('excel_example.xls', sheet_name=0)

# %%

# %% [markdown]
# ### excel 화일(`.xlsx')에서 sheet name 확인하기 : `get_sheet_details()`
#
# 아래 참조 사이트에서 조금 수정하였다.
#
# * 참조 : [STACKOVERFLOW](https://stackoverflow.com/questions/12250024/how-to-obtain-sheet-names-from-xls-files-without-loading-the-whole-file)

# %%
import xmltodict
import shutil
import zipfile

def get_sheet_details(file_path, tempname = '.temp_get_sheet_details'):
    sheets = []
    file_name = os.path.splitext(os.path.split(file_path)[-1])[0]
    # Make a temporary directory with the file name
    #directory_to_extract_to = os.path.join(settings.MEDIA_ROOT, file_name)
    directory_to_extract_to = os.path.join('.', tempname, file_name)
    directory_temp = os.path.join('.', tempname)
    if not os.path.isdir(directory_temp):
        os.mkdir(directory_temp)
    
    if not os.path.isdir(directory_to_extract_to):
        os.mkdir(directory_to_extract_to)
    

    # Extract the xlsx file as it is just a zip file
    zip_ref = zipfile.ZipFile(file_path, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()

    # Open the workbook.xml which is very light and only has meta data, get sheets from it
    path_to_workbook = os.path.join(directory_to_extract_to, 'xl', 'workbook.xml')
    with open(path_to_workbook, 'r') as f:
        xml = f.read()
        dictionary = xmltodict.parse(xml)
        sheets1 = dictionary['workbook']['sheets']['sheet'] 
        if not(isinstance(sheets1, list)): sheets1 =[sheets1]
        #for sheet in dictionary['workbook']['sheets']['sheet']:
        #    sheet_details = {
        #        'id': sheet['sheetId'], # can be @sheetId for some versions
        #        'name': sheet['name'] # can be @name
        #    }
        #    sheets.append(sheet_details)

    # Delete the extracted files directory
    
    shutil.rmtree(directory_to_extract_to)
    shutil.rmtree(os.path.join('.', tempname))
    return sheets1

# %%
get_sheet_details('excel_example.xlsx')

# %% [markdown]
# 반면 아래와 같이 `pd.read_excel`은 제대로 작동되지 않는 듯 하다.

# %%
# 제대로 작동하지 않는 듯...
file = 'excel_example.xlsx'
xl = pd.ExcelFile(file, engine='openpyxl')
# engine = 
# 'xlrd' supports most old/new Excel file formats.
# 'openpyxl' supports newer Excel file formats
print(xl.sheet_names)

import xlrd
xls = xlrd.open_workbook(r'excel_example.xlsx', on_demand=True)
print(xls.sheet_names())

# %% [markdown]
# 반면 `.xls`의 경우 `pd.ExcelFile()`과 `pd.read_excel`은 제대로 작동한다. 

# %%
xls = pd.ExcelFile('excel_example.xls')
sheets = xls.sheet_names
sheets

# %%
vSh = pd.read_excel('./excel_example.xls', sheet_name = sheets)
vSh

# %%

# %%
#del FirstSheet
#del Tomato
#del Ketchup

# %%
fn = "excel_example.xls"

xls = pd.ExcelFile(fn)
lSh = xls.sheet_names
#vSh = excel_sheets(fn)

dat = pd.read_excel(fn, sheet_name = sheets)

for sh in lSh:
    if sh in globals().keys() or sh in locals().keys():
        print('변수 '+sh+ ' 가 이미 존재합니다.')
        break
    else:
        exec(sh+"=dat['"+sh+"']")

# %%

# %% [markdown]
# ## 8.5

# %% [raw]
# #install.packages('foreign')
# #install.packages('haven')
#
# # 기본값이 없는 인수에 대한 오류
#
# #library(foreign)
# #read.spss() # SPSS
# pd.read_spss('___.sav')
# #read.dta() # Stata
# pd.read_stata('___.dta')
# #read.ssd() # SAS
# pd.read_sas('___.xpt')
# ###??? ssd?
# ???
#
#
# read.octave() # Octave
#
# ## matlab .mat files
# from scipy.io import loadmat
# annots = loadmat('cars_train_annos.mat')
#
#
# read.mtp() # Minitab
# read.systat() # Systat
#
#
# library(haven)
# read_dta() # Stata
# read_por() # SPSS .por
# read_sas() # SAS
# read_sav() # SPSS .sav, .zsav
# read_stata() # Stata
# read_xpt() # SAS transport files
#
#
# url = 'http://www.nber.org/data/population-birthplace-diversity/JoEG_BP_diversity_data.dta'

# %% [markdown]
# ## PDF 화일 읽기

# %%
# pip install pdfplumber
# [installation](https://github.com/jsvine/pdfplumber#installation)

import pdfplumber

def pdf2txt(fn_pdf, fn_txt, progress=False):
    res = []
    #with pdfplumber.open(r'D:\Books\python\DS\Applied Data Science with Python and Jupyter by Alex Galea (z-lib.org).pdf') as pdf:
    with pdfplumber.open(fn_pdf) as pdf:
        for ipage in range(len(pdf.pages)):
            print(ipage, end='\r')
            page = pdf.pages[ipage]
            #res[ipage] = page.extract_text()
            res.append(page.extract_text())
            if ipage % 10 == 0:
                print('reading page {:3d}'.format(ipage))

    res2 = [x if isinstance(x, str) else '' for x in res]   # for Nonetype
    res3 = ''.join(res2)

    #with open(r'D:\Books\python\DS\Applied Data Science with Python and Jupyter by Alex Galea (z-lib.org).txt', 'wt', encoding = 'UTF-8') as f:
    with open(fn_txt, 'wt', encoding = 'UTF-8') as f:
        f.write(res3)
    
    return fn_txt


# %%
# %ls *.pdf  # 국가법령정보센터(law.go.kr)에서 다운로드함

# %%
pdf2txt('민법(법률)(제17905호)(20210126).pdf', '민법.txt')

# %% [markdown]
# # 8.5.1

# %% [markdown]
# # 8.5.2

# %%

# %%
FirstSheet

# %% [raw]
#
# install.packages('htmltab')
# library(htmltab)
#
# url <-
#   "https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Europe"
# surnames <- htmltab(doc = url, which = 13)
# head(surnames, n=10)
#
# #install.packages("RCurl")
# #install.packages("rlist")
#
# library(XML)
# library(RCurl) 
# library(rlist)
#
# # error:1407742E:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert protocol version
#
# url <- "https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Europe"
# theurl <- getURL(url, .opts = list(ssl.verifypeer = FALSE) )
# df <- readHTMLTable(theurl, header = TRUE, which = 13,
#                     stringsAsFactors = FALSE, encoding = "UTF-8")
# head(df, n=10)

# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup

# %%
url = "https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Europe"

# %%
req = requests.get(url)

# %%
html = req.text

# %%
soup = BeautifulSoup(html, 'html.parser')

# %% [markdown]
# https://blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221811618848&categoryNo=45&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
# 참조

# %%
tables = soup.select('table')
table = tables[12]
table_html = str(table)

# %%
table_html = str(table)
table_df_list = pd.read_html(table_html)

# %%
table_df_list[0]

# %%
htmltabs =  pd.read_html(html) # html에 있는 테이블을 모두 읽어옴. 

# %%
htmltabs[12]

# %%
