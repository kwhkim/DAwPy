# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: rtopython2-pip
#     language: python
#     name: rtopython2-pip
# ---

# %% [markdown]
#
# # 파이썬의 패키지

# %% [markdown]
# > R 사용자를 위한 안내: 파이썬의 **패키지**는 R의 **패키지**와 거의 동일한 역할을 한다. 다른 점은 파이썬이 통계 분석 외에도 여러 가지 다방면의 목적을 위해 사용되는 범용 언어라서 패키지 역시 엄청나게 다양한 목적을 위해 만들어진다. 그리고 한 패키지가 다른 패키지를 사용하기도 하는데 이때 파이썬에서는 패키지 사이의 버전이 중요하다. 왜냐하면 한 패키지 버전이 달라지면 이를 사용하는 다른 패키지가 작동하지 않기도 하기 때문이다. 파이썬 버전 자체도 문제가 되기도 한다. 그렇기 때문에 파이썬에서는 파이썬의 버전과 패키지의 버전, 그리고 패키지들 사이의 버전이 중요하다. 그런데 운영체제에 파이썬을 설치할 경우 하나의 버전만을 사용할 수 있다. 그래서 사람들은 **가상환경**을 사용하여 여러 버전의 파이썬을 사용하거나, 여러 버전의 패키지를 사용한다. 
#
# > R 사용자는 대부분 최신의 R, 그리고 최신의 패키지를 사용하지만, 파이썬 사용자는 필요에 따라 구 버전의 파이썬을 사용하기도 하고, 구 버전의 패키지를 사용하기도 한다. 그리고 이렇게 다양한 버전의 파이썬, 패키지를 한 컴퓨터에서 사용 가능하게 하기 위해 **가상환경**을 사용한다. 
#
# > R의 스크립트에 해당하는 파일을 파이썬에서는 모듈(module)이라고 부른다.

# %% [markdown]
# 보통 확장자 `.py` 파일에는 파이썬 명령문들이 들어간다. 특정한 목적을 위해 파이썬 언어로 작성된 `.py` 파일을 모듈(Module)이라고 한다(좀더 정확히는 순수모듈이라고 한다. 자세한 설명은 아래 용어 설명 참조). 그리고 특정한 목적을 위해 만들어진 여러 모듈을 모아 패키지를 만든다.

# %% [markdown]
# #### 용어 설명
#
# * 모듈 : 파이썬에서 재사용 가능한 최소 단위로 순수 모듈과 확장 모듈이 있다
#   - 순수 모듈(pure module) : 파이썬으로 쓰여진 .py 파일
#   - 확장 모듈(extension module) : C, C++, Java 등의 다른 컴파일 언어로 쓰여졌다.  
#
# * 배포 패키지와 임포트 패키지 : 둘다 보통 패키지로도 불린다. 파이썬 공식 사이트의 용어 구분에 따르면, 배포 패키지란 배포를 목적으로 여러 파일을 압출한 **파일**이다. 임포트 패키지란 파이썬에 `import`로 불러들일 수 있는 모듈이다. 보통 패키지는 여러 모듈로 구성된다. 

# %%

# %%

# %%
#https://www.it4nextgen.com/purpose-of-channels-in-anaconda/
#**Conda Channels** are basically the locations where **packages are stored**. 
#If there is a need of a **package that is other than the defaults**, 
#the developers can also create their own channels as there is a method available in the Anaconda. 
#The channels Anaconda Channel and the R channel are two of the 10 official repositories present in Anaconda. 
#10 official repositories???
#You can understand its purpose with the fact that conda channels serve as the base for hosting and managing packages. 
#Anaconda Navigator is a phenomenal platform for developers to launch multiple applications and manage them with ease.

# %%
# conda cheat sheet
# https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf

# %% [markdown]
# ## 2.1 패키지 설치

# %% [markdown]
# 파이썬에서 패키지 설치는 보통 운영체제의 커맨드 라인(유닉스의 쉘 또는 윈도우의 명령 프롬프트)에서 진행된다. 파이썬에서 패키지를 설치하는 방법은 여러 가지이지만, 가장 기본적인 방법은 `pip`이라는 패키지를 사용하는 것이다. PiP은 **P**iP **i**nstalls **P**ackages의 약자로 패키지를 설치하는 무엇이라는 의미이다. 그런데 `pip` 역시 패키지이다. 그렇다면 `pip`은 어떻게 설치하는가? 그렇기 때문에 보통 패키지 `pip`은 파이썬과 함께 배포된다. 

# %%

# %%
import sys
sys.path

# %%

# %% [markdown]
# * 복잡한 파이썬
#
# 프로그래밍을 하다 보면 자주 적용되는 패턴이 있고, 보통은 새로운 언어를 배울 때에도 당연히 적용될 것이라 가정하기 싶다. 하지만 새로운 언어를 배울 때 조심해야 하는 부분도 바로 그 지점이다. 새로운 언어에 대한 좀더 포괄적인 이해가 없다면 제대로 작동하는 소스 코드를 되도록 수정하지 말고 실행하는 것이 좋다.
#
# 예를 들어, 대부분의 컴퓨터 없는 `a=3` 또는 `a = 3` 또는 `a= 3`이 모두 같은 의미를 나타낸다. 하지만 linux bash shell에서 `b=3`은 작동하지만 `b = 3`, `b= 3`은 모두 `command not found` 오류를 발생할 것이다. 대부분의 언어에서 `a="str"`과 `a='str'`는 동일한 결과를 산출한다. 하지만 SQL에서는 문자열을 나타내기 위해서 반드시 `'`를 써야 하며, `"`를 쓸 수 없다. 

# %%

# %% [markdown]
# * [두 가지 의미의 패키지](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
#     - 배포 패키지
#     - 임포트 패키지
#
# * 모듈 : basic unit of **code reusability** in Python, existing in one of two types
#     - 순수 모듈(pure module) : 파이썬으로 쓰여졌으면 하나의 .py 파일에 담겨 있다.
#     - 확장 모듈(extension module) : 파이썬의 저수준 언어(예. C/C++)로 쓰여졌으며 하나의 dynamically loadable pre-compiled file에 담겨 있다. (예. e.g. a shared object (.so) file for Python extensions on Unix, a DLL (given the .pyd extension) for Python extensions on Windows, or a Java class file for Jython extensions.)
#
# * 패키지 설치 방법
#     - 전역적으로 vs 지역적으로?
#     - 패키지 격리
#
# * [venv](https://docs.python.org/3/library/venv.html)


# %%
## 파이썬에서 가상 환경(Virtual Environment) 
## R의 환경(Environment)

## 파이썬에서 가상 환경이 필요한 이유 : 
##  패키지들의 상호 의존성 : 어떤 패키지는 다른 패키지의 특정한 버전을 필요로 한다.
##                     버전 하위 호환성이 깨지는 경우
##  
##  R의 경우 CRAN에 등록된 패키지들은 이런 패키지 사이의 호환성을 계속 테스트하기 때문에
##   패키지의 버전이 문제가 되는 경우가 거의 없다. 대부분 최신의 버전을 사용하면 된다.

## python -m mod : run library module as a script (terminates option list)
## conda base에서 venv test를 실행하면? source test/bin/activate
## (test) (base) kwhkim@...

# %% [markdown]
# ### conda channels(with `-c` or `--channel`)
#
# ```
# conda install -c conda-forge matplotlib
# ```
#
# * defaults
# * conda-forge
# * r
# * 

# %% [raw]
# source ~/.bashrc  # conda에 필요한 설정이 포함되어 있기 때문??? 구체적으로 어떤 것들???
# conda activate
# source activate
# conda env list
# conda install [PACKAGE-NAME]
# pip install [PACKAGE-NAME]
#
# conda config --append channels conda-forge
# -> condarc
#    order of channels matter
#
# conda env export --file environment.yml
# conda env create -n conda-env -f /path/to/environment.yml # duplicate
# conda env update -n conda-env -f /path/to/environment.yml # update
#
# R environment
# conda create -n r-env r-base
# Conda’s R packages are available from the R channel of Anaconda Cloud, which is included by default in Conda’s default_channels
#
# Revisions track changes to your environment over time, allowing you to easily remove packages and all of their dependencies
# conda list --revisions
#
# As you build more projects, each with their own environment, you’ll begin to quickly accumulate tarballs from packages you’ve installed.
# To get rid of them and free up some disc space, run:
# % conda clean --all                     # no active env needed 
#
# defusedxml-0.7.1-pyhd8ed1ab_0.tar.bz2         23 KB
# backports.functools_lru_cache-1.6.4-pyhd8ed1ab_0.tar.bz2       9 KB
# libtiff-4.3.0-h1167814_1.tar.bz2             621 KB
# testpath-0.5.0-pyhd8ed1ab_0.tar.bz2           86 KB
#
# ---------------------------------------------------
# Total:                                     433.8 MB
#
# Proceed ([y]/n)? 


# %%
# PiP : PiP installs Packages의 약자!

# What is conda channels?
# https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html

# cf. PyPI : Python Package Index
# https://pypi.org

# Installing Packages in Python : https://packaging.python.org/en/latest/tutorials/installing-packages/

# !!!

# %% [markdown]
# ### Python과 R 비교
#
# * 패키지/모듈/스크립트 불러오기(Python : packname, filename.py, R: packname, filename.R)
#
# |대상    |  상황   | Python | R    |
# |:------|:-------|:-------|:-----|
# |패키지 실행    |R/Python 콘솔/스크립트 내에서 |`import packname` | `library(packname)` |
# |패키지 실행   | 운영체제 명령프롬프트/쉘       |`python -m packname` |    |
# |패키지 삭제   | 운영체제 명령프롬프트/쉘       |`del sys.modules["packname"]; del packname` | `detach("package:packname")`|
# |모듈/스크립트 실행| R/Python 콘솔/스크립트 내에서 |`import filename` | `source('filename.R')` |
# |모듈/스크립트 실행| 운영체제 명령프롬프트/쉘       |`python filename.py` | `Rscript filename.R` |

# %% [markdown]
# 파이썬의 경우 패키지를 실행하는 것과 모듈을 실행하는 것이 모두 `import` 문(statement)로 구현된다. 그리고 패키지를 운영체제 커맨드 라인에서 실행할 수 있다. 그런데 패키지를 `import`할 때는 보통 패키지의 함수나 객체를 활용하려는 것이지 패키지가 무엇인가를 주도적으로 실행하길 바라지 않는다. 그럼에도 파이썬은 운영체제 커맨트 라인에서 패키지를 실행할 수 있다. 이 경우에는 단순히 함수나 객체를 **정의**하는 것을 바라는 것이 아닐 것이다. 왜냐하면 그 경우에는 어떤 패키지를 실행해도 아무 결과없이 종료될 것이기 때문이다.
#
# 그래서 파이썬에서는 `import`로 다른 모듈 또는 콘솔에서 수입(import)되는 경우와 커맨드 라인에서 직접 실행되는 경우를 구분할 수 있는 방법이 있다. 자동으로 생성되는 `__name__`이라는 전역 변수는 `import`되는 경우에는 해당 모듈의 이름이 저장되지만, 운영체제 커맨드 라인에서 실행될 때에는 `__main__`이라는 문자열이 저장된다. 그래서 많은 파이썬 모듈에서 다음과 같은 부분을 확인할 수 있다.
#
# ```
# if __name__ == "__main__":
#     main()
# ```
#
# 만약에 모듈이 운영체제 커맨드 라인에서 실행이 된다면, `main`이라는 함수를 실행한다.

# %% [markdown]
# <예제>
# 다음의 모듈 `check_happy.py`는 함수 `question1`, `question2`를 정의한다.
#
# ```
# def question1():
#     return input("Are you happy today?")
#  
# def question2():
#     return input("Are you happy yesterday?")
#     
# a1 = question1()
#     
# if __name__ == "__main__":    
#     a2 = question2()
#     
#     if a1=='Y' and a2=='Y':
#         print('Good. You seems to be happy all the time')
#     else:
#         print("It's okay. keep it up.")
# ```

# %% [markdown]
# 파이썬 콘솔에서 `import check_happy.py`를 해보자. 그리고 운영체제 커맨드 라인에서 `python check_happy.py`(또는 `python3 check_happy.py`)를 해보자. 결과가 어떻게 다른가?

# %% [markdown]
# 계속 해서 파이썬 콘솔에서 `check_happy.question2()`를 해보자.

# %%
# 만약 python 설치 후 python 또는 pip이 실행되지 않는다면
# PATH에 Python의 folder와 Python/Scripts를 포함시킨다.
# # echo %PATH%
# # echo $PATH

# %%
# 만약 python 설치 후 python 또는 pip이 실행되지 않는다면
# PATH에 Python의 folder와 Python/Scripts를 포함시킨다.
# # echo %PATH%
# # echo $PATH

# %%
import itertools

# %%
count = itertools.count

itertools.count = 10

# then later
itertools.count = count

# %%
itertools.count

# %%
import itertools
count = itertools.count

itertools.count = 10


import sys

del sys.modules['itertools']
del itertools

import itertools

itertools.count

# %% [markdown]
# ## 패키지 관리 관련
#
# reference 
#   - ref/A Guide to Python’s Virtual Environments | by Matthew Sarmiento | Towards Data Science.pdf
#
# * `venv` : 
#
# * `pipenv` : https://www.daleseo.com/python-pipenv/
#
#    - Install on mac M1
#      - `brew install pipenv`(-> `02_Packages_pipenv_m1.md`)
#      - `arch -arm64 brew install pipenv`(-> `02_Packages_pipenv_m1.md`)
#          - but this is discouraged!(https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
# * `conda`
#
# * `venv`와 `conda`의 가장 큰 차이
#   - conda는 language-agnostic! (python이 아니라 다른 언어로 씌여진 package도 관리할 수 있고, 
#
# * pip : pip is a python package manager
# * venv : environment manager for Python
# * conda : language-agnostic package & environment manager
#   - ensure dependecies are satisfied
#   위의 세 개 비교 : https://conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands
#
#

# %% [raw]
# D:\pipenv\test>pipenv --python 3.8
# Creating a virtualenv for this project...
# Pipfile: D:\pipenv\test\Pipfile
# Using C:/Users/Home/AppData/Local/Programs/Python/Python38/python.exe (3.8.10) to create virtualenv...
# [====] Creating virtual environment...created virtual environment CPython3.8.10.final.0-64 in 5627ms
#   creator CPython3Windows(dest=C:\Users\Home\.virtualenvs\test-SXprqnij, clear=False, no_vcs_ignore=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Home\AppData\Local\pypa\virtualenv)
#     added seed packages: pip==21.1.2, setuptools==57.0.0, wheel==0.36.2
#   activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
#
# Successfully created virtual environment!
# Virtualenv location: C:\Users\Home\.virtualenvs\test-SXprqnij
# Creating a Pipfile for this project...

# %%

# %% [markdown]
# 파이썬은 R과 다르게 여러 버전의 파이썬과 패키지를 쓰는 경우가 많기 때문에 현재 사용하고 있는 파이썬의 버전과 패키지의 버전을 확인해야 하는 경우가 생기곤 한다. 

# %%
import sys
sys.version

# %%

# %%
import sys
sys.executable

# %%

# %%

# %% [markdown]
# ## 2.2 패키지 관련 정보

# %%
# #%pip show numpy

# %%
#쥬피터 노트북 안에서 !pip를 쓰지 않도록 주의한다. 왜냐하면 서로 다른 정보가 나타날 수도 있기 때문이다.
# #!pip show numpy

# %%
import numpy
print(numpy.__version__)

import numpy as np
print(np.__name__) # 임포트된 모듈의 이름
# .py 화일을 스크립트로 실행할 때,
#if __name__=="__main__":
#    main()
# import 할 때는 실행되지 않는 이유? 
# import 할 때는 __name__이 "numpy"이기 때문에...

# import 모듈명이 될 수 없는 것은?
# import 모듈명은 어떤 것이 되어도 상관 없다고 생각하지만,
#   꼭 그런 것은 아니다.

# import 할 모듈을 어디서 찾는가?
# 첫 번째는 프로그램이 실행된 디렉토리내에서 모듈을 찾는다.
# 두 번째는 PYTHONPATH 라는 환경변수에 지정된 디렉토리에서 찾습니다.
# 세 번째는 파이썬 라이브러리 디렉토리에서 찾습니다. 이곳은 파이썬을 설치한곳 아래 Lib 디렉토리 입니다.

# https://offbyone.tistory.com/106
# 패키지는 모듈을 디렉토리형식으로 구조화한 것이다.
#

# 패키지내 각 디렉토리에는 __init__.py 가 반드시 존재해야 합니다. __init__.py 파일은 비어있을수도 있고, 패키지내에 포함된 모듈들의 정보를 제공하기도 합니다.

# !!!TODO https://realpython.com/python-modules-packages/
#         https://wikidocs.net/1418
#         https://docs.python.org/3.8/tutorial/modules.html#id2
# 

# https://realpython.com/lessons/python-modules-packages-overview/
# modular programming
#   - simplicity, maintainablitiy, reusability, scoping
# 
#   - module search path `sys.path` <- PYTHONPATH or builtin defaults
#     
#     1. builtins(import builtins) : 
#        The compiled-in module names are in sys.builtin_module_names. 
#        For all importable modules, see pkgutil.iter_modules

# Variables :
#   Where does it come from?
#   1. builtins
#   2. third-party package?
#   3. user-defined


# The search path can be manipulated from within a Python program 
# as the variable sys.path.

# Environment Variables
# - PYTHONHOME, PYTHONPATH, ...
# - 만약 conda라면 달라지는 듯. CONDA_EXE, CONDA_PYTHON, CONDA_SHLVL
# 
# The directory containing the script being run is 
# placed at the beginning of the search path, 
# ahead of the standard library path.

# Standard Library(표준 모듈?)
# 



__builtins__
dir(__builtins__)

import sys
sys.builtin_module_names
# 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype')
# %%
import itertools # itertools can not be imported
#from itertools import test
# itertools has
#   def test(a):
# %%
itertools.test()

# %%
from itertools import test

# %%

# %%
# list all importable modules
import pkgutil
for x in pkgutil.iter_modules():
    #print(dir(x))
    #break
    print(x.name, end=', ')

# !!!Python Module Index ???
# https://docs.python.org/3.8/py-modindex.html

# os and collections are part of the standard library, not builtins

#   - `from mod import abst as a, bbst as b`
#   - scope and namespaces : `dir()`
#   - dundar attribute of name
#      - Double underscores are referred to as dunders because they appear quite often in the Python code and it's easier to use the shorten “dunder” instead of “double underscore”.
#      이중밑줄(?)
#      - https://wiki.python.org/moin/DunderAlias
#   - importlib.reload ( library for import )
#   - how to organize packages
# %%
itertools.count

# %%
for x in itertools.count(3,2):
    if x > 30: 
        break
    print(x, end = ' ')

# %%
itertools.count = 10;
print(itertools.count)

# %%
import itertools
itertools.count

# %%
# ?importlib.reload

# %%
from itertools import count

# %%
del sys.modules['itertools']; del itertools

# %%
itertools

# %%
count

# %%
import importlib
importlib.reload(itertools)
itertools.count

# %%
import numpy as np

# %%
np.any([True, False])

# %%
np.any = None

# %%
a = np.any

# %%
a

# %%

# %%
np.any([True, False])

# %%
importlib.reload(np)

# %%
np.any([True, False])

# %%
dir(np)

# %%
dir(itertools)

# %% [markdown]
# ## 2.3 패키지 불러오기/확인하기/제거하기

# %% [markdown]
# ### 임포트 된 모듈 확인

# %%
import numpy as np

# %%
'np' in set(globals())

# %%
'numpy' in set(globals())

# %%
np.__name__ # alias(별칭)이 아니라 원래 이름

# %%
'np' in sys.modules.keys()

# %%
'numpy' in sys.modules.keys()

# %%



# %%
import Ax_rutils
import sys

# listing all packages imported
modulenames = set(sys.modules) & set(globals())
allmodules = [sys.modules[name] for name in modulenames]
print(allmodules)

d_allmodules = {name:sys.modules[name] for name in modulenames}
print(d_allmodules)
d_allmodules.keys()
# %%
import numpy as np

# %%
np

# %%
numpy

# %%
import pandas as pd

# %%
set([1,2,3])

# %%
pandas

# %%
pd

# %%
type(globals())

# %%

# %%
import re
re.match('^_\\d{1,}$', '_80')

# %%

# %%
from pprint import pprint

# %%
from np import any # import numpy as np 와 같은 alias를 쓸 수 없음
# 그래서 이건 어디서 알 수 있다?
# sys.modules.keys()

# %%
pprint()

# %%
# ?pprint

# %%
pprint(sorted(list(sys.modules.keys()))) # importable modules???

# %%
import pprint
import sys

# %%
pprint.pprint(sorted(list(sys.modules.keys())))

# %%
import types
import sys
def imports():
    modules = list(sys.modules.keys())    
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            if val.__name__ in modules: # 이건 불필요한가???
            #if True:
            #if not re.match('^_\\d{1,}$', name): # and not re.match('^__.*__$', name):
            # jupyter notebook의 output _1, _2, ...와
            # __builtins__, __builtins__는 제외
                yield (name, val.__name__)
                
{x for x in imports()}

# %%
import math
import check_happy

# %%

# %%
sys.builtin_module_names

# %%
import sys

sys.a = 3

import importlib
importlib.reload(sys)

print(sys.a)

sys.builtin_module_names

del sys.modules['sys']
del sys

# Hmmm... There no way to import sys again?

import sys # works fine here
print(sys.a)

# %%
sys.builtin_module_names = None
sys.a = 3
import sys
print(sys.a)

# %%
del sys.modules['sys']
del sys
import sys

# %%
sys.builtin_module_names

# %%
import sys
import types
def imports():
    modules = list(sys.modules.keys())
    aliasnames = {}
    filenames = {}
    b_builtins = {}
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            if val.__name__ not in aliasnames:
                aliasnames[val.__name__] = [name]                
                filenames[val.__name__] = getattr(val, '__file__', None)
                b_builtins[val.__name__] = val.__name__ in sys.builtin_module_names
                if hasattr(val, '__file__'):
                    #filenames[val.__name__] = val.__file__
                    pass
                #else:
                #    filenames[val.__name__] = val.__file__
            else:
                aliasnames[val.__name__].append(name)                
        
    return aliasnames, filenames, b_builtins



# %%
import csv

# %%
import numpy

# %%
imports()

# %%
sys.builtin_module_names

# %%
# Python Module Index
# https://docs.python.org/3.8/py-modindex.html

# %%

# %%

# %%

# %%

# %%
__builtins__.print == print

# %%
with open("C:\\Users\\Home\\miniconda3\\envs\\rtopython2-pip\\lib\\csv.py", 'rt') as f:
    for x in f.readlines():
        print(x, end='')

# %%
[(name, val.__name__) for name, val in globals().items() if isinstance(val, types.ModuleType)]

# %%

# %%
sys.modules

# %%
dir(sys.modules['builtins'])

# %%
sys.modules.keys()


# %%
def search(original=True):
    import Ax_rutils
    import sys

    # listing all packages imported
    modulenames = set(sys.modules) & set(globals())
    if original:
        return set([sys.modules[name].__name__ for name in modulenames])
    else:
        return modulenames
    
search()

# %%
search(original=False)

# %%
[x for x in globals().keys() if x.startswith('p')]

# %%
x = globals()
x.keys()


# %%
def f():
    return globals()


# %%
f().keys()

# %%
type(allmodules[0])

# %%
funcs = dir(allmodules[0])

# %% [markdown]
# * 0-번째 모듈의 모든 함수를 첫 글자를 기준으로 나눠 보았다.

# %%
dict_funcs = {}
for x in funcs:
    if x[0] in dict_funcs.keys():
        dict_funcs[x[0]].append(x)
    else:
        dict_funcs[x[0]] = [x]

# %%
import pprint # dictionary를 좀 더 보기 쉽게 보여준다.
pprint.pprint(dict_funcs)

#funcs.sort()
pprint.pprint(sorted(funcs))

# %%
import re

# %%
re.findall('a', 'abc')

# %%
re.findall('a\w', 'All mighty! I saw a bus, an apple and a house. An')
# !!! \w meaning... 

# %%
del re

# %%
re.findall('a', 'abc')
# NameError: name 're' is not defined

# %%
sys.modules['re']

# %%
sys.modules['re'].findall('a', 'abc')

# %%
re = sys.modules['re']

# %%
# re를 다시 import하려면?(re가 upgrade 되었을 수도???)
# re-import
import importlib
importlib.reload(re)

# import meaning
# !!!load if not loaded yet and then import into namespace


# %%
re.findall('a', 'abc')

# %%
import re

# %%
del sys.modules['re']

# %%
# del sys.modules를 해도 import된 module이 사라지지 않는다?
# binding이 모두 없어졌다면? del sys.modules['re']; del re
#
# sys.modules.pop('re'); 하면 cache가 사라진다?
# 하지만 다른 모듈에서 이미 import한 경우에는 영향을 미치지 않는다.
# 하지만 reload는 모두 바꾼다????
# !!! 생각보다 까다로운 문제!!!

# https://stackoverflow.com/questions/32234156/how-to-unimport-a-python-module-which-is-already-imported
# https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module/61617169#61617169
#   - Memo tip: "import" doesn't mean "load", it means "load if not loaded yet and then import into namespace"
#   - import_file module?

# %%
re.findall('a', 'abc')

# %%
#https://mail.python.org/pipermail/tutor/2006-August/048596.html

# %%
sorted(sys.modules.keys())

# %%
m = sys.modules.pop('re')

# %%
sys.modules['re']

# %%

# %%
# #?alias 
#alias?  #
__builtins__
sys.modules['builtins']


# %%

# %% [markdown]
# ## 2.4 패키지 관리하기

# %%
### 설치된 패키지 목록을 확인하고 싶다면 다음과 같다.
### 하지만 어디에? (conda installed? pip installed? ...)

# %%
# listing available packages
# from https://stackoverflow.com/questions/5632980/list-of-all-imports-in-python-3
import shutil
import pkgutil

def show_acceptable_modules():
    line = '-' * 100
    print('{}\n{:^30}|{:^20}\n{}'.format(line, 'Module', 'Location', line))
    for entry in pkgutil.iter_modules():
        print('{:30}| {}'.format(entry[1], entry[0].path))

show_acceptable_modules()

## conda를 쓴다면, conda list
##               conda list --revisions


# !!! modules created by modifying the PYTHONPATH (e.g. local project imports)

# built-in modules, available modules, loaded modules
sys.builtin_module_names
show_acceptable_modules() # load 가능한 packages... conda list?
sys.modules  # list of imported modules

# %%
# pip freeze
# pip freeze | grep xxx   # xxx를 포함한 패키지만
# conda list
#
# conda env export --file environment.yml
# conda env create -n conda-env -f /path/to/environment.yml # duplicate
# conda env update -n conda-env -f /path/to/environment.yml # update


# 

# help('modules')
## Please wait a moment while I gather a list of all available modules...
## ... 
# %%
help('modules') # 시간이 오래 걸린다.

# %%
### 패키지를 갱신(update)하고 싶다면,

# %%
# pip install xxx --upgrade

# conda update xxx

# %%
### 현재 import한 패키지를 확인하고 싶다면,

# %%
import re

# %%
## dir() 활용하기

# %%
# 실행 환경이 어디인가요?
# - jupyter notebook?
print([x for x in dir() if (not x.startswith('_') and not x in ['In', 'Out', 'exit', 'get_ipython', 'quit'])])

# %%
#'xxx'.startswith('xxx')

# %%
## locals() 활용하기
## !!! locals(), globals(), vars()의 차이?
# https://stackoverflow.com/questions/7969949/whats-the-difference-between-globals-locals-and-vars
# https://stackoverflow.com/questions/32003472/difference-between-locals-and-globals-and-dir-in-python
## 

# %%
l = locals(); 
[key for key in l.keys() 
  if isinstance(l[key], type(__builtins__)) and not key.startswith('_')]
  #if isinstance(l[key], type(re)) and not key.startswith('_')]
# %%

# %% [markdown]
# ## 2.6 재현성을 위해 python 정보 남기기

# %%
import sys
sys.platform

# %%
print(sys.version)


# %% [markdown]
# ## 그밖에

# %%
import sys
import socket
import random
import pwd  # works only on mac and linux?
import os
hostname = socket.gethostname()

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]    

un = get_username()

print('hostname = {}, user_name = {}'.format(hostname, un))
pcIdentity = un+'@'+hostname

# %% [markdown]
# * windows에서는 pwd 모듈이 없음
# * `sys.platform`이 `win`으로 시작하면 다른 방법을 강구해야?
# !!! windows에서 pwd 모듈을 대체하는 방법???
# %% [markdown]
#
# # conda installable 
#   - matplotlib, plotnine, pandas, statsmodel, seaborn
#   - 
#
# # pip installable
#   - dfply, pydatasets

# %%

# %%

# %%

# %%

# %%
sys.byteorder

# %%
sys.builtin_module_names[0:5]
#A tuple of strings giving the names of all modules that are compiled into this Python interpreter. 
# (This information is not available in any other way — modules.keys() only lists the imported modules.)

# %%
sys.modules.keys() # import numpy 를 하면 numpy.random도 사용할 수 있다 # imported modules

# %%

# %%
__name__

# %%
from __future__ import print_function
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
try:
    from reprlib import repr
except ImportError:
    pass

def total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                   }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


##### Example call #####

if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, d=[4,5,6,7], e='a string of chars')
    print(total_size(d, verbose=True))

# %%
a = [1]*100
b = [2]*100
c = [a,b]

# %%
sys.getsizeof(c)

# %%
total_size(c)

# %%

# %%
import sys

# %%
sys.stdout

# %%
sys.getwindowsversion()

# %%
sys.int_info

# %%
sys.int_info=None

# %%
sys.int_info

# %%
import sys

# %%
sys.int_info

# %%
# Did not reload

# %%
del sys.modules['sys']

# %%
del sys

# %%
import sys

# %%
sys.int_info

# %%
sys.stdout

# %%
sys.modules['numpy']

# %%
import numpy

# %%
sys.stdout

# %%
sys.modules['numpy']

# %%
del sys.modules['numpy']

# %%
import numpy

# %%
dir(site)

# %%
import site

# %% [markdown]
# Importing this module will append site-specific paths to the module search path and add a few builtins, unless -S was used. In that case, this module can be safely imported with no automatic modifications to the module search path or additions to the builtins. To explicitly trigger the usual site-specific additions, call the site.main() function.

# %%
import sys
sys.path

# %%
import site
sys.path
# '' meaning???

# %%
site.PREFIXES

# %%
site.PREFIXES[0] == site.PREFIXES[1]

# %%
site.USER_SITE

# %%

# %%

# %%
# 파이썬 모듈 Index : https://docs.python.org/3.8/py-modindex.html


# %%
sys.modules

# %%
# # 지워버리기?

# %%
m = sys.modules.pop('re')

# %%
import sys
import types
def imports():
    modules = list(sys.modules.keys())
    aliasnames = {}
    filenames = {}
    b_builtins = {}
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            if val.__name__ not in aliasnames:
                aliasnames[val.__name__] = [name]                
                filenames[val.__name__] = getattr(val, '__file__', None)
                b_builtins[val.__name__] = val.__name__ in sys.builtin_module_names
                if hasattr(val, '__file__'):
                    #filenames[val.__name__] = val.__file__
                    pass
                #else:
                #    filenames[val.__name__] = val.__file__
            else:
                aliasnames[val.__name__].append(name)                
        
    return aliasnames, filenames, b_builtins


# %%
imports()

# %%
m

# %%
dir(m)

# %% [markdown]
# 특정 패키지의 특정 버전 함수를 사용하고 싶다면?
# 패키지 소스의 setup.py를 보면 `python_requires='>=3.5, !=3.9.*'` 와 같은 버전을 특정하는 부분을 볼 수 있다. 
#
# 패키지 히스토리 또는 릴리즈 노트를 확인하자.

# %%
# !pip freeze > requirements.txt 

# %%
# #!pip install -r requirements

# %%

# %% [markdown]
# PyPI(Python Package Index): online code repository, anyone anywhere can upload packages
#
# https://pypi.org
#
# * distribution package - a bundled version of your package which is ready to install
#   - source distribution : source 
#   - wheel distribution : slightly processed, smaller, faster, ...
#   
#

# %%
#you can build source and wheel distributions from the terminal using this command
#python setup.py sdist bdist_wheel #source distribution, wheel distribution
# dist/*.whl, dist/*.tar.gz, /build, /...egg-info

# %%
# upload
# twine upload dist/*
# twine upload -r testpypi dist/*

# %%
# install
# pip install ...
# pip install --index-url https://test/pypi.orgsimple --extra-index-url https://pypi.org/simple ...
