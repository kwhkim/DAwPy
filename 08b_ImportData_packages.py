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
#     display_name: venv
#     language: python
#     name: venv
# ---

# %% [markdown]
# ## 패키지의 데이터

# %% [markdown]
# 파이썬에 데이터를 불러오는 방법은 크게 **텍스트** 데이터 파일을 읽어오는 것과 **바이너리** 데이터 파일을 읽어오는 것으로 나뉠 수 있다. 그 밖에도 파이썬 패키지를 활용할 수도 있다.

# %% [markdown]
# 가장 풍부한 데이터에 접근할 수 있는 패키지는 `statsmodels`이다. `statsmodels.api.datasets.get_rdataset()` 함수를 활용하면 R의 다양한 데이터를 불러올 수 있다. 예를 들어 R 패키지 `ggplot2`의 `diamonds`라는 데이터를 불러읽기 위해서는 다음과 같이 한다. 

# %%
import statsmodels.api as sm
dat = sm.datasets.get_rdataset('diamonds', package='ggplot2')

# %% [markdown]
# 데이터는 `.data`에 저장되며, `.title` 또는 `.doc`을 통해 데이터의 이름과 설명을 확인할 수 있다. 
#
# dd # class와 object가 있다. class는 범주고 object는 class의 instance. 가령 add라는 함수가 수치에서는 합산일 수 있지만, 텍스트에서는 연결(이어 쓰기) 일수도 있다. 그런데 class를 지정하면 각 class에서 add를 다르게 읽을 수 있다.
#
# dat는 변수. object. 여기서 dir(dat)를 하면 dat라는 object가 갖는 method를 열람할 수 있다. 그 중 하나의 method가 data. 그런데 dat의 method 중 values라는 method도 있다. type(dat.values())를 하면 dict_values()로 나오는데, print(dat.values())를 하면 출력되는 서로 다른 값들을 무엇으로 해석할지(ex.서로 다른 타입의 값들을 한꺼번에 묶을 수 있는 건 리스트니까, len을 해본다). 리스트는 아니지만, 리스트화 할 수 있는. (ex. 점화식)

# %%
dat.data.head()

# %%
dat.title

# %%
## print(dat.__doc__)
print(dat.__doc__[:300])

# %%

# %%
