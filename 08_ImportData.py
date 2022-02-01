# -*- coding: utf-8 -*-
# ## 데이터 종류
# * 패키지 속 데이터
# * 텍스트 데이터 파일 읽기
#     - csv, tsv, txt
#     - json
#     - 빅데이터
#     - 압축파일
# * 바이너리 데이터 파일 읽기
#     - 엑셀
#     - SPSS
#     - SAS
#     - Stata
# * 웹에서 파일 읽어오기
#     - html
#     - json
# * pdf에서 읽어오기
# * 

import statsmodels.api as sm
from tabulate import tabulate
ces11 = sm.datasets.get_rdataset('CES11', 'carData')
# CES11, carData = data name, package
# 

dir(sm.datasets)

dir(ces11.data)

type(ces11.data)

print(ces11.__doc__)

# +
## Comparison
## https://towardsdatascience.com/comparing-the-speed-and-filesize-of-to-csv-np-save-to-hdf-to-pickle-functions-6c53a6a3fc82

# +
#numpy : 
#	Efficient, fast, and clean

# +
#matrix = rows and columns
#data.frame = observations and variables

# +
#Wes McKinney and Hadley Hackham
#	feather

# +
#LIGO researchers use hdf5
# -



# +
#Pickle: native python file type
#	dict -> how to store this???

#	-> human readable -> json
# -

Serialize : convert object to bytestream

computer readable/human readable

# +
## What can we save with pickle?
# -

import pickle
with open('data/excel_example.xls', 'rb') as f:
    data = pickle.load(f)
# 근데 왜 f.pickle_load()하지 않고???
print(data)


# +
# Excel spreadsheets
## There are many ways to import Excel file

import pandas as pd
file = 'data/excel_example.xls'
data = pd.ExcelFile(file)
print(data.sheet_names) # 
# -

df1 = data.parse('FirstSheet')
df2 = data.parse(1)

df1, df2

# #### SAS(**S**tatistical **A**nalysis **S**ystem) : 비즈니스과 생물학계에서 많이 쓰이는 통계 프로그램
# * 파일 확장자 : `.sas7bdat`(데이터 파일), `.sas7bcat`(카테고리 파일)
#
# #### Stata(**St**atistics + d**ata**) : 사회과학분야에서 자주 쓰이는 통계 프로그램

# sas data source : https://github.com/xiaodaigh/sas7bdat-resources
import pandas as pd
#from sas7bdat import SAS7BDAT
#with SAS7BDAT('data/korea.sas7bdat') as file:
#    df_sas = file.to_data_frame()
dat = pd.read_sas('data/korea.sas7bdat')
#dat = pd.read_sas('data/gdp.sas7bdat')

dat

# context manager란!???

# +
#importing stata files
# stata data set: https://www.stata.com/links/examples-and-datasets/


# http://gss.norc.org/get-the-data/stata
# About the GSS
# For more than four decades, the General Social Survey (GSS) has studied the growing complexity of American society. It is the only full-probability, personal-interview survey designed to monitor changes in both social characteristics and attitudes currently being conducted in the United States.
import pandas as pd
dat= pd.read_stata('data/gss2021.dta')

# -

dat

Hdf5:
	standard for storing large quantities of numerical data
	x00g, xT
	can scale to exabytes

import h5py
filename = " "
data = h5py.File(filename,  "r")
print(type(data))

for key in data.keys():
    print(key) # each is an HDF group


# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = group['Strain'].value




# #### MATLAB(**MAT**rix **LAB**oratory)
# * 공학과 과학에서 많이 쓰임
# * 파일 확장자 : `.mat`
#     - 여러 객체를 함께 저장할 수 있음







import scipy.io

import numpy as np
x = np.random.normal(0,1,(100,100))
scipy.io.savemat("dat.mat", {"x":x, "y":x-1})

dat = scipy.io.loadmat("dat.mat")
dat

print(type(dat))



