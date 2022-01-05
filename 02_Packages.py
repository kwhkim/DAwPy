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
# > R 사용자를 위한 안내: 파이썬의 **패키지**는 R의 **패키지**와 거의 동일한 역할을 한다. 다른 점은 파이썬이 통계 분석 외에도 여러 가지 다방면의 목적을 위해 사용되는 범용 언어라서 패키지 역시 엄청나게 다양한 목적을 위해 만들어진다. 그리고 한 패키지가 다른 패키지를 사용하기도 하는데 이때 파이썬에서는 패키지 사이의 버전이 중요하다. 왜냐하면 한 패키지 버전이 달라지면 이를 사용하는 다른 패키지가 작동하지 않기도 하기 때문이다. 그리고 파이썬 버전 자체도 문제가 되기도 한다. 그렇기 때문에 파이썬에서는 파이썬의 버전과 여러 패키지의 버전이 모두 중요하다. 그런데 R과 달리 파이썬은 보통 하나의 컴퓨터에 하나의 버전만 설치할 수 있다. 그래서 사람들은 **가상환경**을 구성하여 서로 다른 버전의 파이썬을 하나의 컴퓨터에서 사용할 수 있도록 하였다. 가상환경(virtual environment)란 운영체제의 환경을 가상으로 구성한 것으므로, 기존의 환경과 구별되는 가상 환경을 여럿 만들 수 있다. 가상 환경을 사용하면 각 가상 환경마다 별도의 파이썬, 패키지 등을 설치할 수 있다. 
#
# > R 사용자는 대부분 최신의 R, 그리고 최신의 패키지를 사용하지만, 파이썬 사용자는 필요에 따라 구 버전의 파이썬을 사용하기도 하고, 구 버전의 패키지를 사용하기도 한다. 그리고 이렇게 다양한 버전의 파이썬, 패키지를 한 컴퓨터에서 사용 가능하게 하기 위해 **가상환경**을 사용한다. 
#
# > R의 스크립트에 해당하는 파일(*.R)을 파이썬에서는 모듈(module)(*.py)이라고 부른다.

# %% [markdown]
# ## 전체 구성
#
# * 모듈/패키지/라이브러리
#   - `import`로 모듈 불러들이기
#   - 불러들인 모듈 확인하기
#   - 모듈 정보 확인
#   - 모듈 제거
#   
# * 가상환경의 구성
#   - 가상환경 구성 패키지 종류
#   - conda
#

# %% [markdown]
# 보통 확장자 `.py` 파일에는 파이썬 명령문들이 들어간다. 특정한 목적을 위해 파이썬 언어로 작성된 `.py` 파일을 모듈(Module)이라고 한다(좀더 정확히는 순수모듈이라고 한다. 자세한 설명은 아래 용어 설명 참조). 그리고 특정한 목적을 위해 만들어진 여러 모듈을 모아 패키지를 만든다.

# %% [markdown]
# ### 용어 설명
#
# * 모듈 : 파이썬에서 재사용 가능한 최소 단위로 순수 모듈과 확장 모듈이 있다
#   - 순수 모듈(pure module) : 파이썬으로 쓰여진 .py 파일
#   - 확장 모듈(extension module) : C, C++, Java 등의 다른 컴파일 언어로 쓰여졌다.  
#
# * 배포 패키지와 임포트 패키지 : 둘다 보통 패키지로도 불린다. 파이썬 공식 사이트의 용어 구분에 따르면, 배포 패키지란 배포를 목적으로 여러 파일을 압출한 **파일**이다. 임포트 패키지란 파이썬에 `import`로 불러들일 수 있는 모듈이다. 보통 패키지는 여러 모듈로 구성된다. 
#
# #### **모듈**, **패키지**, **라이브러리(Library)**
#
# **모듈**이란 코드 재사용의 최소 단위로 순수 모듈의 경우 `.py`로 끝나는 파일 하나를 생각하면 된다. 모듈의 길이가 길어지면 필요에 따라 모듈 파일을 두 개 이상으로 나누기도 하고, 복잡한 기능을 조직화하기 위해 디렉토리를 나눠 모듈을 저장하기도 한다. 이렇게 여러 모듈을 모아놓은 것을 **패키지**라고 한다.[^module] 보통 하나의 패키지는 하나의 주제로 통합할 수 있는 여러 기능들이 여러 모듈에 나눠 담겨 있다. **라이브러리**는 여러 패키지들을 모아 부르는 말이다. 예를 들어 파이썬 표준 라이브러리(The Python Standard Library; https://docs.python.org/3.8/library/index.html)에는 보통 파이썬과 함께 배포되는 자주 쓰이는 패키지 또는 모듈을 담고 있다. 파이썬 표준 라이브러리에 속하지 않는 패키지를 보통 제3자 패키지(third-party package)라고 부른다. 파이썬(제1자)이 만들지 않았고, 내(제2자)가 만들지도 않았다는 의미이다.
#
# * 내장 모듈 
#   - 내장(built-in) 모듈은 다른 모듈과 달리 파일로 존재하지 않고, Python 안에 존재하는 C로 쓰여진 모듈이다.
#   - 내장 모듈을 불러들이기 위해서는 다른 모듈과 마찬가지로 `import` 문을 쓴다.
#   - 하지만 그렇게 불러들인 모듈의 `.__file__`은 존재하지 않는다(예. `import sys; sys.__file__`)
#   - 내장 모듈 리스트는 `sys.builtin_module_names`로 확인할 수 있다. 
#   
# [^module]: 하지만 파이썬 내에서는 이런 구분 없이 import의 결과는 모두 module이라고 표시하는 듯 하다. `import`한 결과를 출력해보면 `<module '...' from 'C:\\Users\\Home\\...\\__init__.py'>`와 같이 모두 `module`로 표시된다. 만약 패키지로 디렉토리를 구성한다면 파일 이름은 모두 `__init__.py`가 된다.
#
#

# %%
import psutil
psutil

# %%
from matplotlib import pyplot

# %%
import matplotlib.pyplot

# %%

# %% [markdown]
# ### 파이썬의 `import` 문
#
# `import`는 필요한 패키지, 모듈을 불러올 때 쓴다. 예를 들어 `math` 모듈을 불러오려면 `import math`라고 쓴다. `import`의 대상은 다음과 같이 나눠볼 수 있다.
#
# * 내장 모듈 : C로 작성된 모듈. Python 인터프리터에 결합되어 있다.
# * 파이썬 표준 라이브러리의 패키지와 모듈 
#   - 파이썬 표준 라이브러리에 포함된 패키지와 모듈 리스트는  https://docs.python.org/3.8/library/index.html 에서 확인할 수 있다.
#   - 내장 모듈을 포함한다
#   - 외장 모듈은 보통 파이썬 폴더 안의 `Lib` 폴더에서 찾을 수 있다.
#   - 내장 모듈 빌트인즈(`builtins`)에는 내장 함수(built-in function)들이 정의되어 있다. `__builtin__`, `__builtins__`은 모두 내장 모듈 `builtins`를 가리킨다. 내장 모듈의 함수는 `builtins.print`로 쓸 필요없이 그냥 `print`로 쓸 수 있다.
# * 직접 만든 모듈 : 자신이 만든 모듈도 `import` 문으로 불러들일 수 있다. 이때 모듈 파일의 위치가 중요하다. 
# * 제3자 패키지
#   - 파이썬 설치 후 `pip install` 등을 통해 설치된 제3자 패키지는 보통 파이썬 폴더의 안의 `Lib/site-packages/`에서 찾을 수 있다.
#   
# 해당 파일의 위치는 `import json`과 같이 패키지를 불러들인 후, `json.__file__`과 같이 `.__file__` 속성을 통해 확인할 수 있다(하지만 항상 정확하지 않기 때문에 https://docs.python.org/3.8/library/index.html 에서 확인할 필요가 있다. 예. zipimport)
# `print(json.__doc__)`으로 패키지 설명도 확인할 수 있다. `import`된 모듈은 `sys.modules`에 사전 형식으로 기록된다.
#
# #### `import` 사용법
#
# 1. 패키지/모듈 불러들이기 `import numpy`
# 2. 패키지에서 서브패키지 불러들이기 `import matplotlib.pyplot`, `from matplotlib import pyplot`
# 3. 패키지/모듈에서 함수 불러들이기 `from numpy import abs`
# 4. 서브패키지에서 함수 불러들이기 `from matplotlib.pyplot import scatter`
#
# ##### `as`로 별칭 만들기
#
# 1. `import numpy as np`
# 2. `import matplotlib.pyplot as plt`, `from matplotlib import pyplt as plt`
# 3. `from numpy import abs as ab`
# 4. `from matplotlib.pyplot import scatter as sct`

# %%
import numpy as np 
# import numpy를 하면 numpy의 모든 subpackage를 활용할 수 있다. 
# 예. np.random 등

# %%
import matplotlib.pyplot as plt

# %%
from matplotlib import pyplot as plt

# %%
from numpy import abs as ab

# %%
from matplotlib.pyplot import scatter as sct

# %% [markdown]
# ### import된 모듈 정보 확인

# %%
np.__file__  # 패키지를 저장하고 있는 파일

# %%
print(np.__doc__)  # 패키지 안내 documentation

# %%
# 그 밖에 거의 모든 패키지가 가지고 있는 속성(정보)
np.__loader__

# %%
np.__name__  # 별칭 말고 원래 이름

# %%
plt.__package__  # 서브패키지의 경우 패키지 이름

# %%
np.__spec__

# %%
plt.__spec__

# %%
np.math.__spec__

# %%
np.__version__

# %%
plt.__version__


# %% [markdown]
# ### import된 모듈/패키지 리스트

# %%
def imported():
    import sys
    import types
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
        
    # module object name(alias), 파일, 빌트인 모듈 여부
    return aliasnames, filenames, b_builtins 


# %%
imported()

# %%
import pandas as pd

# %%
imported()

# %% [markdown]
# ### import된 모듈/패키지 제거

# %%
import sys

del sys.modules['pandas']  # sys.module에 해당하는 패키지와
del pd                     # 해당 패키지를 가리키는 모든 변수(별칭 포함)

# %%
imported()

# %% [markdown]
# ### import된 모듈이 수정된 경우 다시 불러오기
#
# * 내장 모듈이 아니라면 `importlib.reload()`로 가능하다
# * 만약 내장 모듈이라면 모듈을 제거한 후 다시 불러와야 한다.

# %%
import os

# %%
imported()

# %%
import importlib
importlib.reload(os) 

# %% [markdown]
# ### 오류를 사전에 방지하는 법
#
# 모듈(스크립트)을 만들 때 파이썬 표준 모듈(내장 모듈 포함)과 PyPI에 등록된 제 3자 모듈 이름을 사용하지 말자. 

# %% [markdown]
# #### 파이썬 내장 모듈 리스트

# %%
import sys
" ".join(sys.builtin_module_names)

# %% [markdown]
# #### 파이썬 표준 라이브러리
#
# * 리스트 : [https://docs.python.org/3.8/py-modindex.html](https://docs.python.org/3.8/py-modindex.html)

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

df_func = pd.read_html('https://docs.python.org/3.8/py-modindex.html')[0]

df_func.columns = ['_', 'function', 'description']

#df_func['description'].str.len()
#df_func['function']st.len() > 1

#pysl = df_func[df_func['function'].str.len() > 1].function.str.replace("\\s*[(](Unix|Windows|Tk|Linux|Linux, FreeBSD)[)]", "", regex=True).tolist()
pysl = df_func[df_func['function'].str.len() > 1].function.str.\
           replace("\\s*[(](Unix|Windows|Tk|Linux|FreeBSD)(, (Unix|Windows|Tk|Linux|FreeBSD))*[)]", "", regex=True).tolist()

# %%
" ".join(pysl) # https://stackoverflow.com/questions/6463918/how-can-i-get-a-list-of-all-the-python-standard-library-modules

# %% [markdown]
# ### PyPI(Python Package Index; )에 등록된 패키지
#
# 파이파이(PyPI; Python Package Index; https://pypi.org)는 온라인 코드 저장소로 누구나 패키지를 올릴 수 있다. 
#
# 두 가지 종류의 배포가 있다.
#  
# * 소스 배포 : 소스
# * 휠(wheel) 배포 : 소스가 처리되어 작고 빠르게 설치 가능한 배포
#
# 전체 리스트는 https:/pypi.org/simple/ 또는 https://www.kaggle.com/rtatman/list-of-pypi-packages 에서 확인할 수 있다. 

# %%
### PyPI의 패키지 리스트 다운로드

# Download from https://www.kaggle.com/rtatman/list-of-pypi-packages/version/479
import zipfile
zip = zipfile.ZipFile(r'C:\Users\Home\Downloads\simple.zip', mode='r')
dat = zip.read('simple')
text_html = dat.decode('utf8')

# Url : https://pypi.org/simple/
import requests 
text_html = requests.get("https://pypi.org/simple/").text



import html

from bs4 import BeautifulSoup 
soup = BeautifulSoup(text_html)  # 'html5lib'

found = soup.findAll('a')

package_names = [x.text for x in found]

package_names

# %%
import requests
import json
import re       
import pandas as pd

patt1 = re.compile('from\\s+([A-Za-z_][A-Za-z0-9_.]*)\\s+import\\s+([A-Za-z_][A-Za-z0-9_]*)\\s*$', re.MULTILINE)
patt2 = re.compile('(?<!from)\\s+[^\\s]+\\s+import\\s+([A-Za-z_][A-Za-z0-9_.]*)\\s*$', re.MULTILINE)

res = []

#npack = 200; mpack = 100

npack = len(package_names)
mpack = 1000

for ipack, package in enumerate(package_names[:npack]):
    if ipack % mpack == 0 and ipack != 0:
        dat = pd.DataFrame(res)
        dat.to_csv('dat_pypi/dat_pypi_'+"{:06d}".format(ipack)+'.csv')
        print('* SAVED to '+'dat_pypi_'+"{:06d}".format(ipack)+'.csv')
        res = []
    try:
        url = requests.get('https://pypi.org/pypi/'+package+'/json')
        text = url.text
        #print(type(text))
        dat_pack = json.loads(text)
    except Exception as e:
        print(package, str(e))
        continue    
    desc = dat_pack['info']['description']
    f1 = patt1.findall(desc)
    f2 = patt2.findall(desc)    
    name_import = ''
    if len(f1) > 0:
        name_import = f1[0][0].split('.')[0]
    elif len(f2) > 0:
        name_import = f2[0].split('.')[0]    
    if len(f1) or len(f2):
        print(package, name_import)
        res.append((package, name_import))

dat = pd.DataFrame(res)
dat.to_csv('dat_pypi/dat_pypi_'+"{:06d}".format(ipack)+'.csv')
print('* SAVED to '+'dat_pypi_'+"{:06d}".format(ipack)+'.csv')


# %%
# stdlib-list란 패키지도 있지만 버전 3.5까지만 업데이트 되었다.

# %%
# #%pip install stdlib-list

# %%
import stdlib_list

# %%
stdlib_list.stdlib_list(version="3.8")

# %%
# stdlib_list.fetch.fetch_list(version="3.8")

# %% [markdown]
# ### 사용 가능한 모듈/패키지 확인

# %% [markdown]
# #### pip 또는 conda로 설치한 패키지 확인

# %%
# %conda list
# %pip list

# %% [markdown]
# #### import 가능한 모든 모듈/패키지 확인 
# 1. `help('modules')` : jupyter notebook에서는 다운됨

# %%
help('modules')  # import 가능한 모든 모듈

# %% [markdown]
# 2. 패키지 `pkgutil` 활용 

# %%
import pkgutil

def show_acceptable_modules():
    line = '-' * 100
    print('{}\n{:^30}|{:^20}\n{}'.format(line, 'Module', 'Location', line))
    for entry in pkgutil.iter_modules():
        print('{:30}| {}'.format(entry[1], entry[0].path))
        
show_acceptable_modules()

# %%
set(remains) - set(remains2)

# %%

# %% [markdown]
# #### `import` 순서
#
# 현재 디렉토리에 `time.py`라는 모듈을 만들었다고 해보자. 현재 디렉토리에 같은 이름의 파일을 생성할 수 없으므로 `import time`를 하면 `time.py`를 임포트하게 될 것이다. 정말 그럴까?
#
# 다른 디렉토리에도 `time.py`라는 파일이 존재할 수 있다. 그리고 내장 모듈 또는 파이썬 표준 라이브러리에 `time`이라는 이름의 모듈 또는 패키지가 존재할 수도 있다. 따라서 `import`가 모듈을 찾는 순서가 중요하다.
#
# `import`는 먼저 이미 임포트가 된 모듈/패키지를 사전 형식으로 저장하고 있는 `sys.modules`에서 `import` 대상을 찾는다. 만약 이미 임포트되어 있다면 이미 임포트되어 있는 대상을 사용한다[^already_import]. 두 번째로 `sys.builtin_module_names`에서 이름을 찾는다. 만약 내장 모듈이라면 내장 모듈을 임포트한다. 그리고 마지막으로 `sys.path`를 확인한다. `sys.path`에는 파이썬이 모듈 또는 라이브러리를 찾을 때 확인하는 폴더가 순서대로 저장되어 있다.[^syspath] 보통 `sys.path`의 가장 첫 번째 원소는 현재 실행하는 모듈이 존재하는 디렉토리[^currentwd]이고, `sys.path`에는 파이썬 표준 라이브러리의 내장 모듈을 저장하는 폴더(보통 `Lib`)도 포함된다.
#
# 그렇다면 `time.py`는 몇 번째 순서인가? 1. `sys.modules` 2. `sys.builtin_module_names` 3. `sys.path`
# `time.py`가 현재 디렉토리에 있으므로 3. `sys.path`의 첫 번째 원소에 해당한다. 하지만 `time`은 보통 1번과 2번에 모두 해당한다. 따라서 임포트가 되지 않는다.[^importtry]
#
# 같은 파이썬 표준 라이브러리에 속하지만 `os`는 내장 모듈이 아니다. 그래서 현재 디렉토리에 `os.py`가 있을 경우 1번에서 `os`를 삭제하면 현재 디렉토리의 `os.py`를 임포트할 수 있다. 이때 주의할 점은 이렇게 `os.py`를 임포트하면 파이썬이 내부적으로 쓰는 `os`와 현재 우리가 쓰는 `os`는 서로 다른 모듈이 된다.
#
# [^syspath]: `sys.path`의 디렉토리는 파이썬을 설치할 때 설정 사항이 반영되어 있거나 `PYTHONPATH`라는 운영체제 환경변수가 반영되어 결정된다.
#
# [^already_import]: `import numpy as np`와 같이 별칭(alias)을 사용할 때에도 마찬가지이다.
#
# [^currentwd]: 보통 현재 실행 중인 모듈을 포함하는 디렉토리는 현재 작업 디렉토리(`os.getcwd()`의 결과)가 된다. 하지만 `os.chdir()`로 현재 작업 폴더를 바꿔도 `sys.path[0]`은 변경되지 않는다. 만약 `python ../test.py`와 같이 모폴더의 모듈을 실행하면 현재 디렉토리(`os.getcwd()`)와 모듈을 포함하는 디렉토리(`sys.path[0]`)가 다르다.
#
# [^importtry]: 저자는 `sys.modules`와 `sys.builtin_module_names`에서 `time`을 삭제해보았지만 그래도 임포트할 수 없었다.

# %%
import sys
sys.path[0]

# %%
import os
os.getcwd() # get current working directory

# %%
os.chdir("R") # change directory

# %%
os.getcwd()

# %%
import sys
sys.path

# %% [markdown]
# #### 패키지냐? 모듈이냐?
#
# 패키지는 패키지 이름의 디렉토리를 구성하고 그 안에 `__init__.py`가 있어서 패키지를 `import` 하면 우선 `__init__.py`를 실행한다. 모듈은 모듈 이름의 `.py` 파일로 존재한다. 만약 같은 디렉토리 안에 동일한 이름의 모듈과 패키지가 동시 존재한다면 무엇이 `import` 될까? 저자의 실험 결과에 따르면 패키지가 `import`  된다.

# %%
import sillyenough

# %% [markdown]
# 만약 제3자 패키지와 같은 이름의 패키지가 실행 폴더에 있다면 어떨까? 저자는 현재 환경에 제3자 패키지 `numpy`를 설치하였다. 그리고 실행 폴더에 `numpy`라는 폴더를 만들었다. `import numpy` 결과를 보자.

# %%
import numpy

# %% [markdown]
# 저자가 만든 폴더가 임포트되었다. 문제는 여기에 그치지 않는다. 내부적으로 `numpy`를 임포트하는 `pandas`를 임포트 해보자.

# %%
import pandas


# %%

# %%

# %%

# %%

# %%

# %%
def source(path):
    if path[-1]=='/' or path[-1]=='\\': 
        path = path[:-1]
    path0, packagename = os.path.split(path)
    path0 = os.path.abspath(path0)
    print(f"path={path0}, module/package = {packagename}")
    if os.path.isfile(path):
        #print("This is file")
        if packagename[-3:] == ".py":
            filename = packagename
            packagename = packagename[:-3]
        print(packagename)
        
        if packagename in sys.builtin_module_names:
            print(f"!! PACKAGE {packagename} is one of builtin modules")
            print(f"!! Here is the list of builtin modules")
            print(" ".join(sys.builtin_module_names))
            raise ValueError("Use different filename")

        if packagename in sys.modules.keys():
            if hasattr(sys.modules[packagename], "__file__"):
                print(f"!  PACKAGE {packagename} is already imported from {sys.modules[packagename].__file__}")
            else:
                print(f"!  PACKAGE {packagename} is already imported")
            raise ValueError("Remove the package from sys.module or use different name")
        
        if sys.path[0] != path0 and os.path.isfile(os.path.join(sys.path[0], filename)):
            print(f'Filename {filename} Exist in the sys.path[0] = {sys.path[0]}')
            raise ValueError("Better use Different Name")
        
        sys.path.insert(1, path0)        
        module = __import__(packagename)
        sys.path.pop(1)
        return module
            
    elif os.path.isdir(path):
        pass
    else:
        raise OSError("Not Found")
    


# %%
hasattr(sys.modules["os"], "__file__")

# %%
"abcd.py"[:-3]

# %%
source("time.py")

# %%
source("time.py")

# %%
source("R/check_happy.py")

# %%
source("R/check_happy2.py")

# %%
import pandas

# %%
# 만약 패키지와 모듈이 같은 폴더 내에 있다면, 모듈 먼저

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
# 파이썬에서 패키지 설치는 보통 운영체제의 커맨드 라인(유닉스의 쉘 또는 윈도우의 명령 프롬프트)에서 진행된다. 파이썬에서 패키지를 설치하는 방법은 여러 가지이지만, 가장 기본적인 방법은 `pip`이라는 패키지를 사용하는 것이다. PiP은 **P**iP **i**nstalls **P**ackages의 약자로 패키지를 설치하는 무엇이라는 의미이다. 그런데 `pip` 역시 패키지이다. 그렇다면 `pip`은 어떻게 설치하는가? 그렇기 때문에 보통 패키지 `pip`은 파이썬과 함께 배포된다. 만약 `pip`이 없다면 https://bootstrap.pypa.io/get-pip.py에서 `pip`을 다운로드하는 모듈을 다운로드할 수 있다.
#
#

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
# 파이썬의 경우 패키지를 실행하는 것과 모듈을 실행하는 것이 모두 `import` 문(statement)로 구현된다. 그리고 패키지를 운영체제 커맨드 라인에서 실행할 수 있다. 그런데 파이썬 내에서 패키지를 `import`할 때는 보통 패키지의 함수나 객체를 활용하려는 것이지 패키지가 무엇인가를 주도적으로 실행하길 바라지 않는다. 그럼에도 파이썬은 운영체제 커맨트 라인에서 패키지를 실행할 수 있다. 이 경우에는 단순히 함수나 객체를 **정의**하는 것을 바라는 것이 아닐 것이다. 왜냐하면 그 경우에는 어떤 패키지를 실행해도 아무 결과없이 종료될 것이기 때문이다.
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

# %% [markdown]
# ## 사용 가능한 가상 환경
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
'np' in globals()

# %%
'numpy' in globals()

# %%
np.__name__ # alias(별칭)이 아니라 원래 이름

# %%
# sys.modules에는 이미 임포트된 모듈이
# 딕셔너리로 저장된다. 이때 키는 (별칭이 아니라) 원래 이름이다.

# %%
'np' in sys.modules.keys()

# %%
'numpy' in sys.modules.keys()


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
# %conda list --revisions

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

# %%
l = locals(); 
[key for key in l.keys() 
  if isinstance(l[key], type(__builtins__)) and not key.startswith('_')]
  #if isinstance(l[key], type(re)) and not key.startswith('_')]
# %%

# %% [markdown]
# ## 2.6 재현성을 위해 python 정보 남기기

# %%
# 파이썬 버전
print(sys.version)


# %% [markdown]
# ## 그밖에

# %%
import get_pcinfo

get_pcinfo.main()

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


# %%
# # 지워버리기?

# %%
m = sys.modules.pop('re')

# %%
import sys
import types
def imported():
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

# %%
import sys
sys.builtin_module_names

# %%
import builtins

# %%
eval("ArithmeticError")

# %%
dir(builtins)

# %%
for x in dir(builtins):
    if not getattr(sys.modules['builtins'], x) == eval(x):
        print(x, getattr(sys.modules['builtins'], x) == eval(x))
        
# __doc__, __loader__, __name__, __package__, __spec__ 은 모두 현재 모듈에 대한 것이다

# %%
builtins.__IPYTHON__

# %%
__IPYTHON__

# %%

# %% [markdown]
# # ===========

# %% [markdown]
# ## 참고 자료
#
# ### Reading list
#
# * https://realpython.com/python-modules-packages/
# * https://wikidocs.net/1418
# * https://docs.python.org/3.8/tutorial/modules.html#id2
#
#
#

# %% [markdown]
# ## locals() 활용하기
#
# ### locals(), globals(), vars()의 차이?
# * https://stackoverflow.com/questions/7969949/whats-the-difference-between-globals-locals-and-vars
# * https://stackoverflow.com/questions/32003472/difference-between-locals-and-globals-and-dir-in-python
#

# %%
for x in dir(sys.modules['builtins']):
    if not getattr(sys.modules['builtins'], x) == eval(x):
        print(x, getattr(sys.modules['builtins'], x) == eval(x))

# %%

# %%
### stdlib_list와 python module list 비교

m = ['_abc',
'_ast',
'_asyncio',
'_bisect',
'_blake2',
'_bootlocale',
'_bz2',
'_codecs',
'_codecs_cn',
'_codecs_hk',
'_codecs_iso2022',
'_codecs_jp',
'_codecs_kr',
'_codecs_tw',
'_collections',
'_collections_abc',
'_compat_pickle',
'_compression',
'_contextvars',
'_crypt',
'_csv',
'_ctypes',
'_ctypes_test',
'_curses',
'_curses_panel',
'_datetime',
'_dbm',
'_decimal',
'_elementtree',
'_frozen_importlib',
'_frozen_importlib_external',
'_functools',
'_gdbm',
'_hashlib',
'_heapq',
'_imp',
'_io',
'_json',
'_locale',
'_lsprof',
'_lzma',
'_markupbase',
'_md5',
'_multibytecodec',
'_multiprocessing',
'_opcode',
'_operator',
'_osx_support',
'_pickle',
'_posixshmem',
'_posixsubprocess',
'_py_abc',
'_pydecimal',
'_pyio',
'_queue',
'_random',
'_sha1',
'_sha256',
'_sha3',
'_sha512',
'_signal',
'_sitebuiltins',
'_socket',
'_sqlite3',
'_sre',
'_ssl',
'_stat',
'_statistics',
'_string',
'_strptime',
'_struct',
'_symtable',
'_testbuffer',
'_testcapi',
'_testimportmultiple',
'_testinternalcapi',
'_testmultiphase',
'_threading_local',
'_tkinter',
'_tracemalloc',
'_uuid',
'_warnings',
'_weakref',
'_weakrefset',
'_xxsubinterpreters',
'_xxtestfuzz',
'antigravity',
'genericpath',
'idlelib',
'ntpath',
'nturl2path',
'opcode',
'posixpath',
'pydoc_data',
'pyexpat',
'sre_compile',
'sre_constants',
'sre_parse',
'this',
'xxlimited',
'xxsubtype']
for i in range(0, len(m)):
    module = m[i]
    #print(i, module)
    try:
        __import__(module)
        print(module, module in sys.builtin_module_names)
    except Exception  as e:
        pass
        #print(e, i, module)
        #print(module in sys.builtin_module_names)
    
# 19  _crypt
# 23 _curses
#
