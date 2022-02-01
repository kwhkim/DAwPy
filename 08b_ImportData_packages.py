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

# %%
dat.data.head()

# %%
dat.title

# %%
## print(dat.__doc__)
print(dat.__doc__[:300])

# %%

# %%
