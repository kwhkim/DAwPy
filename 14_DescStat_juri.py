# -*- coding: utf-8 -*-
import rpy2.rinterface


# %load_ext rpy2.ipython

# + language="R"
# sessionInfo()

# + language="R"
# .libPaths()

# + language="R"
# .libPaths('usr/bin/R')
# .libPaths('/home/publishingkwon/R/x86_64-pc-linux-gnu-library/3.6')

# + language="R"
# .libPaths()

# + language="R"
# Mode <- function(x) {
#   ux <- unique(x)
#   ux[which.max(tabulate(match(x, ux)))]
# }
#
# set.seed(0); x <- rnorm(10); x


# + language="R"
# mean(x)
# median(x)
# Mode(x) # table을 통해 빈도수를 확인할 수 있다. 
# mean(x, trim = 0.2)
# -


import numpy as np
np.random.seed(0)
x = np.random.normal(0,1,10)
x

np.mean(x)

np.median(x)

# numpy에는 mode 없음.
from scipy.stats import mode
mode(x) # count까지 알 수 있다

xmode = mode(x)

xmode.mode, xmode.count

### mean(x, trim = 0.2) 절사평균
from scipy.stats import trim_mean
m = trim_mean(x, 0.2)
m

# + magic_args="-o x" language="R"
# max(x)-min(x)
# -


# %R IQR(x)


# %R var(x)


# %R sd(x)


max(x)-min(x)

np.max(x) - np.min(x)
# max와 np.max의 차이??


np.quantile(x, q=0.75) - np.quantile(x, q=0.25)

np.var(x, ddof=1)  # sample variance
# for population variance(or MLE), ddof = 0
# The average squared deviation is normally calculated as x.sum() / N, where N = len(x). If, however, ddof is specified, the divisor N - ddof is used instead.

np.std(x, ddof=1)

# +
import pandas as pd
x = pd.Series(data=x)

x.describe()

# + language="R"
# gini = function(x, ...) { #useNA = 'always', 'no', 'ifany'
#     1-sum(prop.table(table(x, ...))^2)
# }
# print(x); gini(x)
# -
xSer = pd.Series(x)


def gini(x, **kwargs):
    xSer = pd.Series(x)
    return 1-(xSer.value_counts(normalize=True, **kwargs) ** 2).sum()


gini(x)

# + language="R"
# x = c(1,3,2,2,4,NA,5,NA)
# gini(x)
# -

x = [1,3,2,2,4,np.nan, 5, np.nan]
gini(x)

# + language="R"
# gini(x, useNA = 'no')
# -

gini(x, dropna = True)

# + language="R"
# gini(x, useNA = 'ifany')
# -

gini(x, dropna = False)

# + language="R"
# gini(x, useNA = 'always')
# -

gini(x, dropna = False)

# + language="R"
# data(mpg, package='ggplot2'); require(dplyr)


# + language="R"
# table(x)

# + language="R"
# prop.table(table(x))
# -

pd.Series(x).value_counts()

pd.Series(x).value_counts(normalize=True)

pd.Series(x).value_counts(normalize=True, dropna=False)

# 파이썬 ggplot 사용할 수 있는 라이브러리 plotnine
from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
#from plotnine.data import mpg
import plotnine as p9

import pydataset

mpg = pydataset.data('mpg')

# levels 지정 미입력
mpg.sort_values(by=['drv'])

# + language="R"
# library(ggplot2)
# library(dplyr)
#
# mpg$drv <- ordered(mpg$drv, levels=c("f", "r", "4"))
# mpg
# + language="R"
# mpg$fl <- factor(mpg$fl)


# + magic_args="-o mpg2" language="R"
# mpg2 <- mpg %>% select(class, drv, fl, hwy)


# + language="R"
# summary(mpg2)
# -


mpg2.describe()

mpg2.describe(include='all') 
# include ='all'을 쓰면 categorical variable에 대해서도 
# 정보를 확인할 수 있다. 

# + language="R"
# install.packages('prettyR')

# + magic_args="-o mpg2" language="R"
# mpg2[c(1,4,5,16),1] = NA
# mpg2[c(1,4,5,16),2] = NA
# prettyR::freq(mpg2)
# -


mpg2.iloc[[0,3,4,15],[0,1]] = np.nan

mpg2

mpg2['class'].value_counts()

# pd.DataFrame({'class':mpg2['class'].value_counts()}).T
pd.DataFrame({'freq':mpg2['class'].value_counts()}).T

df = pd.DataFrame({'freq':mpg2['class'].value_counts()}).T
df.columns.name = 'class'
df

for col in mpg2.columns:
    print('Frequency for '+col)
    print(pd.DataFrame({col:mpg2[col].value_counts()}).T)
    print('')

col = 'class'

# +
# #?pd.Series.value_counts
# -

mpg2[col].value_counts(normalize=True, dropna=True)

pd.DataFrame({col:mpg2[col].value_counts(normalize=True, dropna=True)})

for col in mpg2.columns:
    print('Frequency for '+col)    
    row1= pd.DataFrame({col:mpg2[col].value_counts(dropna=False)}).T
    row2 = pd.DataFrame({col:mpg2[col].value_counts(normalize=True, dropna=False)}).T
    row3 = pd.DataFrame({col:mpg2[col].value_counts(normalize=True, dropna=True)}).T
    allrows = pd.concat([row1, row2, row3], axis=0)
    allrows.index = ['freq', '%', '%(!NA)']
    print(allrows)
    print('')

# ## 결측치 관련

mpg2.isnull().sum() # 각 컬럼의 결측치 갯수

mpg2.isnull().sum().sum()  # 전체 결측치 갯수

mpg2.isnull().any()  # 각 컬럼에 결측치가 존재하는가?

mpg2.isnull().any().any() # 전체에 결측치가 하나라도 존재하는가?

# ### 결측치 존재 여부 시각화

# + active=""
# %pip install missingno

# + active=""
# Collecting missingno
#   Downloading missingno-0.4.2-py3-none-any.whl (9.7 kB)
# Requirement already satisfied: seaborn in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno) (0.10.1)
# Requirement already satisfied: matplotlib in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno) (3.1.3)
# Requirement already satisfied: numpy in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno) (1.18.1)
# Requirement already satisfied: scipy in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno) (1.5.0)
# Requirement already satisfied: pandas>=0.22.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from seaborn->missingno) (1.0.5)
# Requirement already satisfied: cycler>=0.10 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib->missingno) (0.10.0)
# Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib->missingno) (2.4.6)
# Requirement already satisfied: kiwisolver>=1.0.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib->missingno) (1.1.0)
# Requirement already satisfied: python-dateutil>=2.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib->missingno) (2.8.1)
# Requirement already satisfied: pytz>=2017.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas>=0.22.0->seaborn->missingno) (2020.1)
# Requirement already satisfied: six in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from cycler>=0.10->matplotlib->missingno) (1.14.0)
# Requirement already satisfied: setuptools in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from kiwisolver>=1.0.1->matplotlib->missingno) (45.2.0.post20200210)
# Installing collected packages: missingno
# Successfully installed missingno-0.4.2
# Note: you may need to restart the kernel to use updated packages.

# +
import missingno as msno
import matplotlib.pyplot as plt

msno.matrix(mpg2)
plt.show()
# -

msno.bar(mpg2)
plt.show()

# +
# #%%R
#install.packages('psych', dependencies=TRUE)
#library(psych)
# psych 설치의 고질점 문제점. mnormt 패키지가 항상 최신의 R만 지원!
# -


mpg2

# + language="R" active=""
# install.packages('psych', dependencies=TRUE)

# + language="R"
# psych::describe(mpg2)
# #describe(mpg2)


# + language="R"
# install.packages('Hmisc')

# + language="R" active=""
# install.packages('cluster')

# + language="R"
# .libPaths()

# + language="R"
# Hmisc::describe(mpg2)
# # .libPaths()를 설정하지 않으면 install되는 곳과 library에서 찾는 장소가 달라지는 듯
# -




# + language="R"
# pastecs::stat.desc(mpg2)
#
# + active=""
# %pip install -U pandas_profiling

# + active=""
# Collecting pandas_profiling
#   Downloading pandas_profiling-2.8.0-py2.py3-none-any.whl (259 kB)
#      |████████████████████████████████| 259 kB 2.6 MB/s eta 0:00:01
# Collecting visions[type_image_path]==0.4.4
#   Downloading visions-0.4.4-py3-none-any.whl (59 kB)
#      |████████████████████████████████| 59 kB 1.8 MB/s  eta 0:00:01
# Collecting confuse>=1.0.0
#   Downloading confuse-1.3.0-py2.py3-none-any.whl (64 kB)
#      |████████████████████████████████| 64 kB 985 kB/s eta 0:00:011
# Collecting matplotlib>=3.2.0
#   Downloading matplotlib-3.3.0-1-cp36-cp36m-manylinux1_x86_64.whl (11.5 MB)
#      |████████████████████████████████| 11.5 MB 7.9 MB/s eta 0:00:01
# Collecting astropy>=4.0
#   Downloading astropy-4.0.1.post1-cp36-cp36m-manylinux1_x86_64.whl (6.5 MB)
#      |████████████████████████████████| 6.5 MB 28.9 MB/s eta 0:00:01
# Collecting htmlmin>=0.1.12
#   Downloading htmlmin-0.1.12.tar.gz (19 kB)
# Collecting tangled-up-in-unicode>=0.0.6
#   Downloading tangled_up_in_unicode-0.0.6-py3-none-any.whl (3.1 MB)
#      |████████████████████████████████| 3.1 MB 25.5 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: joblib in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (0.16.0)
# Collecting requests>=2.23.0
#   Downloading requests-2.24.0-py2.py3-none-any.whl (61 kB)
#      |████████████████████████████████| 61 kB 436 kB/s  eta 0:00:01
# Requirement already satisfied, skipping upgrade: ipywidgets>=7.5.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (7.5.1)
# Requirement already satisfied, skipping upgrade: numpy>=1.16.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (1.18.1)
# Requirement already satisfied, skipping upgrade: missingno>=0.4.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (0.4.2)
# Requirement already satisfied, skipping upgrade: scipy>=1.4.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (1.5.0)
# Requirement already satisfied, skipping upgrade: pandas!=1.0.0,!=1.0.1,!=1.0.2,>=0.25.3 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (1.0.5)
# Collecting phik>=0.9.10
#   Downloading phik-0.10.0-py3-none-any.whl (599 kB)
#      |████████████████████████████████| 599 kB 58.0 MB/s eta 0:00:01
# Collecting tqdm>=4.43.0
#   Downloading tqdm-4.48.2-py2.py3-none-any.whl (68 kB)
#      |████████████████████████████████| 68 kB 7.3 MB/s  eta 0:00:01
# Requirement already satisfied, skipping upgrade: jinja2>=2.11.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas_profiling) (2.11.1)
# Requirement already satisfied, skipping upgrade: attrs>=19.3.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from visions[type_image_path]==0.4.4->pandas_profiling) (19.3.0)
# Collecting networkx>=2.4
#   Downloading networkx-2.4-py3-none-any.whl (1.6 MB)
#      |████████████████████████████████| 1.6 MB 55.9 MB/s eta 0:00:01
# Collecting imagehash; extra == "type_image_path"
#   Downloading ImageHash-4.1.0.tar.gz (291 kB)
#      |████████████████████████████████| 291 kB 52.6 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: Pillow; extra == "type_image_path" in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from visions[type_image_path]==0.4.4->pandas_profiling) (7.0.0)
# Requirement already satisfied, skipping upgrade: pyyaml in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from confuse>=1.0.0->pandas_profiling) (5.3.1)
# Requirement already satisfied, skipping upgrade: cycler>=0.10 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib>=3.2.0->pandas_profiling) (0.10.0)
# Requirement already satisfied, skipping upgrade: kiwisolver>=1.0.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib>=3.2.0->pandas_profiling) (1.1.0)
# Requirement already satisfied, skipping upgrade: python-dateutil>=2.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib>=3.2.0->pandas_profiling) (2.8.1)
# Requirement already satisfied, skipping upgrade: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from matplotlib>=3.2.0->pandas_profiling) (2.4.6)
# Requirement already satisfied, skipping upgrade: chardet<4,>=3.0.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from requests>=2.23.0->pandas_profiling) (3.0.4)
# Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from requests>=2.23.0->pandas_profiling) (2020.6.20)
# Requirement already satisfied, skipping upgrade: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from requests>=2.23.0->pandas_profiling) (1.25.8)
# Requirement already satisfied, skipping upgrade: idna<3,>=2.5 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from requests>=2.23.0->pandas_profiling) (2.8)
# Requirement already satisfied, skipping upgrade: ipykernel>=4.5.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (5.1.4)
# Requirement already satisfied, skipping upgrade: ipython>=4.0.0; python_version >= "3.3" in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (7.12.0)
# Requirement already satisfied, skipping upgrade: nbformat>=4.2.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (5.0.4)
# Requirement already satisfied, skipping upgrade: widgetsnbextension~=3.5.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (3.5.1)
# Requirement already satisfied, skipping upgrade: traitlets>=4.3.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipywidgets>=7.5.1->pandas_profiling) (4.3.3)
# Requirement already satisfied, skipping upgrade: seaborn in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from missingno>=0.4.2->pandas_profiling) (0.10.1)
# Requirement already satisfied, skipping upgrade: pytz>=2017.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pandas!=1.0.0,!=1.0.1,!=1.0.2,>=0.25.3->pandas_profiling) (2020.1)
# Collecting numba>=0.38.1
#   Downloading numba-0.50.1-cp36-cp36m-manylinux2014_x86_64.whl (3.6 MB)
#      |████████████████████████████████| 3.6 MB 49.2 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: MarkupSafe>=0.23 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jinja2>=2.11.1->pandas_profiling) (1.1.1)
# Requirement already satisfied, skipping upgrade: decorator>=4.3.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from networkx>=2.4->visions[type_image_path]==0.4.4->pandas_profiling) (4.4.1)
# Requirement already satisfied, skipping upgrade: six in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from imagehash; extra == "type_image_path"->visions[type_image_path]==0.4.4->pandas_profiling) (1.14.0)
# Collecting PyWavelets
#   Downloading PyWavelets-1.1.1-cp36-cp36m-manylinux1_x86_64.whl (4.4 MB)
#      |████████████████████████████████| 4.4 MB 70.3 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: setuptools in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from kiwisolver>=1.0.1->matplotlib>=3.2.0->pandas_profiling) (45.2.0.post20200210)
# Requirement already satisfied, skipping upgrade: jupyter-client in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipykernel>=4.5.1->ipywidgets>=7.5.1->pandas_profiling) (5.3.4)
# Requirement already satisfied, skipping upgrade: tornado>=4.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipykernel>=4.5.1->ipywidgets>=7.5.1->pandas_profiling) (6.0.3)
# Requirement already satisfied, skipping upgrade: jedi>=0.10 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.16.0)
# Requirement already satisfied, skipping upgrade: backcall in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.1.0)
# Requirement already satisfied, skipping upgrade: pickleshare in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.7.5)
# Requirement already satisfied, skipping upgrade: pexpect; sys_platform != "win32" in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (4.8.0)
# Requirement already satisfied, skipping upgrade: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (3.0.3)
# Requirement already satisfied, skipping upgrade: pygments in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (2.5.2)
# Requirement already satisfied, skipping upgrade: jsonschema!=2.5.0,>=2.4 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (3.2.0)
# Requirement already satisfied, skipping upgrade: ipython-genutils in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (0.2.0)
# Requirement already satisfied, skipping upgrade: jupyter-core in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (4.6.1)
# Requirement already satisfied, skipping upgrade: notebook>=4.4.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (6.0.3)
# Collecting llvmlite<0.34,>=0.33.0.dev0
#   Downloading llvmlite-0.33.0-cp36-cp36m-manylinux1_x86_64.whl (18.3 MB)
#      |████████████████████████████████| 18.3 MB 31.4 MB/s eta 0:00:01
# Requirement already satisfied, skipping upgrade: pyzmq>=13 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jupyter-client->ipykernel>=4.5.1->ipywidgets>=7.5.1->pandas_profiling) (18.1.1)
# Requirement already satisfied, skipping upgrade: parso>=0.5.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jedi>=0.10->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.6.1)
# Requirement already satisfied, skipping upgrade: ptyprocess>=0.5 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from pexpect; sys_platform != "win32"->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.6.0)
# Requirement already satisfied, skipping upgrade: wcwidth in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=7.5.1->pandas_profiling) (0.1.8)
# Requirement already satisfied, skipping upgrade: pyrsistent>=0.14.0 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (0.15.7)
# Requirement already satisfied, skipping upgrade: importlib-metadata; python_version < "3.8" in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (1.5.0)
# Requirement already satisfied, skipping upgrade: nbconvert in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (5.6.1)
# Requirement already satisfied, skipping upgrade: terminado>=0.8.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.8.3)
# Requirement already satisfied, skipping upgrade: prometheus-client in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.7.1)
# Requirement already satisfied, skipping upgrade: Send2Trash in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (1.5.0)
# Requirement already satisfied, skipping upgrade: zipp>=0.5 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from importlib-metadata; python_version < "3.8"->jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets>=7.5.1->pandas_profiling) (2.2.0)
# Requirement already satisfied, skipping upgrade: bleach in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (3.1.0)
# Requirement already satisfied, skipping upgrade: testpath in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.4.4)
# Requirement already satisfied, skipping upgrade: defusedxml in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.6.0)
# Requirement already satisfied, skipping upgrade: mistune<2,>=0.8.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.8.4)
# Requirement already satisfied, skipping upgrade: entrypoints>=0.2.2 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.3)
# Requirement already satisfied, skipping upgrade: pandocfilters>=1.4.1 in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (1.4.2)
# Requirement already satisfied, skipping upgrade: webencodings in /home/publishingkwon/anaconda3/envs/rtopython2/lib/python3.6/site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.5.1->pandas_profiling) (0.5.1)
# Building wheels for collected packages: htmlmin, imagehash
#   Building wheel for htmlmin (setup.py) ... done
#   Created wheel for htmlmin: filename=htmlmin-0.1.12-py3-none-any.whl size=27084 sha256=8f3bf5cf671e4150123194abaebee1ae12202117e3cfe92b96bcacd310fd98c4
#   Stored in directory: /home/publishingkwon/.cache/pip/wheels/c3/fe/0b/4450b38bceb9ae43dd7d0f16e353566f30f5f4d59a58eca2ed
#   Building wheel for imagehash (setup.py) ... done
#   Created wheel for imagehash: filename=ImageHash-4.1.0-py2.py3-none-any.whl size=291990 sha256=249afeabccb08deb883bac4783e7a6088ecf8fe9676683e40281dd0751b37dcd
#   Stored in directory: /home/publishingkwon/.cache/pip/wheels/43/f6/25/a58e553441acfc5ad7782c545147759c94d0d95ea1c1edd4bf
# Successfully built htmlmin imagehash
# Installing collected packages: networkx, tangled-up-in-unicode, PyWavelets, imagehash, visions, confuse, matplotlib, astropy, htmlmin, requests, llvmlite, numba, phik, tqdm, pandas-profiling
#   Attempting uninstall: matplotlib
#     Found existing installation: matplotlib 3.1.3
#     Uninstalling matplotlib-3.1.3:
#       Successfully uninstalled matplotlib-3.1.3
#   Attempting uninstall: requests
#     Found existing installation: requests 2.22.0
#     Uninstalling requests-2.22.0:
#       Successfully uninstalled requests-2.22.0
# Successfully installed PyWavelets-1.1.1 astropy-4.0.1.post1 confuse-1.3.0 htmlmin-0.1.12 imagehash-4.1.0 llvmlite-0.33.0 matplotlib-3.3.0 networkx-2.4 numba-0.50.1 pandas-profiling-2.8.0 phik-0.10.0 requests-2.24.0 tangled-up-in-unicode-0.0.6 tqdm-4.48.2 visions-0.4.4
# Note: you may need to restart the kernel to use updated packages.
# -

import pandas_profiling


pr = mpg2.profile_report()

pr.to_file('./14_DescStat_report.html')

pr

# +
# https://dandyrilla.github.io/2017-08-12/pandas-10min/
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
