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
# ## 바이너리 파일 읽기
#
# ### 피클(pickle)

# %% [markdown]
# 바이너리 파일은 데이터를 이진수를 저장한다. 파이썬에서 기본적으로 지원하는 파일은 피클 파일 형식이다. 피클 파일은 판다스 데이터 프레임뿐 아니라 파이썬의 여러 가지 데이터(예. 리스트, 딕셔너리, 셋 등)을 모두 저장할 수 있는 바이너리 파일이다.

# %%
import numpy as np
import pandas as pd

# %%
x = ['a', 'b', 32, ['a', 'b', 64], 128]

# %%
import pickle
with open('data/x.pkl', 'wb') as f:
     pickle.dump(x, f)        

# %% [markdown]
# `x.pkl` 파일을 확인해보면 앞서와 마찬가지로 사람이 그 내용을 읽고 이해하기 힘들다. 피클 파일을 읽으려면 다음과 같이 한다.

# %%
with open('data/x.pkl', 'rb') as f:
    y = pickle.load(f)

# %%
x, y

# %% [markdown]
# 이렇게 다양한 타입을 저장할 수 있는 피클이지만 여기서는 데이터 프레임을 저장하는 경우로 한정시켜보자. 데이터 프레임을 저장하고 읽는 방법은 판다스를 쓰면 좀더 간단하다. 간단하게 저장하고자 하는 데이터 프레임에 `.to_pickle()` 메쏘드를 쓰거나, `pd.read_pickle()` 함수를 사용하면 된다.

# %%
import statsmodels.api as sm
dat = sm.datasets.get_rdataset('diamonds', package='ggplot2').data

# %%
dat.to_pickle('data/diamonds.pkl')

# %%
dat2 = pd.read_pickle('data/diamonds.pkl')
dat.equals(dat2)

# %% [markdown]
# ### 엑셀 파일 읽기

# %%
import numpy as np
import pandas as pd

# %%
pd.read_excel('data/excel_example.xls')

# %%
dat = pd.read_excel('data/excel_example.xls')

# %%
dat.head()

# %%
pd.read_excel('data/excel_example.xls', sheet_name=1) 
# sheet_name = 1 : 2번째 시트(sheet)

# %%
# 모든 sheet 읽기
pd.read_excel('data/excel_example.xls', sheet_name=None) 

# %%
pd.read_excel('data/excel_example.xlsx')
# 에러나는 이유???

# %% [markdown]
# ### hdf5

# %% [markdown]
# HDF5는 **H**ierarchical **D**ata **F**ormat의 약자로 여러 빅 데이터를 계층적으로 구성할 수 있는 형식이다. 

# %%
import numpy as np
import pandas as pd

# %%
import statsmodels.api as sm
diamonds = sm.datasets.get_rdataset('diamonds', package='ggplot2').data
#flights = sm.datasets.get_rdataset('flights', package='nycflights13').data
fertility = sm.datasets.get_rdataset('Fertility', package='AER').data
#AER	Fertility

# %%
diamonds.head()

# %%
fertility.head()

# %% [markdown]
# 위에서 읽은 데이터 프레임 `diamonds`와 `fertility`를 저장하기 위해서 앞에서 배운 `.to_csv()` 함수를 사용한다면 두 파일로 나눠 저장해야 하겠지만, hdf5 파일 형식을 사용한다면 다음과 같이 할 수 있다. 

# %%
diamonds.to_hdf('data/dat.h5',
               key='diamonds',
               mode='w') # 처음 파일을 생성할 때에는 mode='w'

# %%
fertility.to_hdf('data/dat.h5',
                 key='fertility',
                 mode='a') # 데이터를 추가할 때에는 mode='a'

# %% [markdown]
# 결과로 생성된 `dat.h5`는 두 프레임을 모두 저장하고 있다. 이제 `dat.h5`를 읽어보자. 앞에서 저장할 때 지정한 `key=`를 알고 있다면 다음과 같이 할 수 있다.

# %%
diamonds2 = pd.read_hdf('data/dat.h5', key='diamonds')

# %%
fertility2 = pd.read_hdf('data/dat.h5', key='fertility')

# %%
diamonds.equals(diamonds2), fertility.equals(fertility2)

# %% [markdown]
# ### 그 밖의 통계 프로그램 데이터 파일

# %% [markdown]
# SAS는 **S**tatistical **A**nalysis **S**ystem의 약자로 비즈니스과 생물학계에서 많이 쓰이는 통계 프로그램이다. 파일 확장자는 `.sas7bdat`(데이터 파일)와 `.sas7bcat`(카테고리 파일)를 사용한다. SAS의 데이터 파일인 `.sas7bdat` 파일을 읽기 위해서는 다음과 같이 진행한다.

# %%
# sas data source : https://github.com/xiaodaigh/sas7bdat-resources
import pandas as pd
#from sas7bdat import SAS7BDAT
#with SAS7BDAT('data/korea.sas7bdat') as file:
#    df_sas = file.to_data_frame()
dat_korea = pd.read_sas('data/korea.sas7bdat')
#dat = pd.read_sas('data/gdp.sas7bdat')
dat_korea.head()

# %% [markdown]
# Stata는 **St**atistics과 d**ata**를 합친 말로 사회과학분야에서 자주 쓰이는 통계 프로그램이다. 스테이타(또는 스타타로도 읽는다, stata)는 `.dta`를 확장자로 사용한다. 읽는 방법은 다음과 같다.

# %%
#importing stata files
# stata data set: https://www.stata.com/links/examples-and-datasets/


# http://gss.norc.org/get-the-data/stata
# About the GSS
# For more than four decades, the General Social Survey (GSS) has studied the growing complexity of American society. It is the only full-probability, personal-interview survey designed to monitor changes in both social characteristics and attitudes currently being conducted in the United States.
import pandas as pd
dat_gss= pd.read_stata('data/gss2021.dta')
dat_gss.head()

# %% [markdown]
# MATLAB은 **MAT**rix **LAB**oratory(행렬 연구실)의 약자로 행렬 계산에 특화된 프로그램으로 개발되어 공학과 과학자들이 많이 사용하는 프로그램이다. 이 프로그램은 `.mat` 확장자를 사용하며 여러 객체를 함께 저장할 수 있다는 특징이 있다. 하지만 데이터프레임보다는 넘파이 행렬을 저장하는데 적합하다. 파일을 쓰고 읽는 방법은 다음과 같다.

# %%
import scipy.io

# %%
num_korea = dat_korea.to_numpy()
num_gss = dat_gss.select_dtypes('number').to_numpy() # 수치형 데이터만 골라서 넘파이 배열로 변환

# %%
scipy.io.savemat("data/dat.mat", {'korea':num_korea, "gss":num_gss})
# 딕셔너리도 저장 할 수 있다. 

# %%
dat = scipy.io.loadmat('data/dat.mat')
# dat['korea']와 dat['gss']

# %%
np.abs(dat['korea'] - num_korea).sum()

# %%
np.nansum(np.abs(dat['gss'] - num_gss)) # np.nansum()은 nan를 제외한 원소를 합한다.

# %% [markdown]
# 아래와 같이 넘파이 배열을 바로 저장할 수 없으므로 원소 하나의 딕셔너리를 구성한 후 저장한다.

# %%
scipy.io.savemat('data/korea.mat', num_korea)

# %%
scipy.io.savemat('data/korea.mat', {'korea':num_korea})

# %%
scipy.io.loadmat('data/korea.mat')['korea']

# %% [markdown]
# ### === END OF DOCUMENT

# %% [markdown]
# In general it is not a very good idea to use pickle to transmit a dictionary over a network (json could be better here). Though in rare cases it might be useful e.g., multiprocessing module. – 
# jfs
#  Jan 23 '12 at 9:42 
# @Tim Pietzcker: protocol=0 (default on Python2.x) can be used with files opened in text mode. – 
# jfs
#  Jan 23 '12 at 9:43 
# @J.F.Sebastian: OK, but he opened the file for reading, not for writing. – 
# Tim Pietzcker
#  Jan 23 '12 at 10:10
# Geez, this is what happens when you write the code here absentmindedly and don't actually debu
#
#
# Pickling is absolutely necessary for distributed and parallel computing.
#
# Say you wanted to do a parallel map-reduce with multiprocessing (or across cluster nodes with pyina), then you need to make sure the function you want to have mapped across the parallel resources will pickle. If it doesn't pickle, you can't send it to the other resources on another process, computer, etc. Also see here for a good example.
#
# To do this, I use dill, which can serialize almost anything in python. Dill also has some good tools for helping you understand what is causing your pickling to fail when your code fails.
#
# And, yes, people use picking to save the state of a calculation, or your ipython session, or whatever. You can also extend pickle's Pickler and UnPickler to do compression with bz2 or gzip if you'd like.
#
#
#
# ### pickle과 관련
#
# * https://en.wikipedia.org/wiki/Serialization
# * https://docs.python.org/3/library/pickle.html#restricting-globals
# * https://stackoverflow.com/questions/25353753/python-can-i-safely-unpickle-untrusted-data
# * https://nbviewer.org/gist/minrk/5241793

# %%
