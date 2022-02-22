# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.5.1
#   kernelspec:
#     display_name: rtopython2-pip
#     language: python
#     name: rtopython2-pip
# ---

# %%
# %load_ext rpy2.ipython


# %% language="R"
# sessionInfo()


# %% language="R"
# .libPaths("/home/publishingkwon/R/x86_64-pc-linux-gnu-library/3.6")

# %% language="R"
# #install.packages('AER')

# %% [markdown]
# ## 제 15장. 간편 시각화

# %% [markdown]
# ## 15.1 간편 시각화의 예

# %% [markdown]
# ## 15.1.1 일변수 분포

# %% magic_args="-o BankWages -o mtcars -o BankWages" language="R"
# #제 15장. 간편 시각화
# #15.1 간편 시각화의 예
# #15.1.1 일변수 분포
# library(dplyr)
# library(ggplot2)
# library(lattice)
# data('BankWages', package='AER')
# data(mtcars)
# head(BankWages)

# %%

# %% language="R"
# hist(BankWages$education) # 연속형 변수


# %% language="R"
# plot( ~ gender, data=BankWages) # 이산형 변수


# %%
from pydataset import data
mtcars = data('mtcars')
mtcars.to_csv('mtcars.csv')


# %%
from plotnine import *
import pandas as pd
mtcars = pd.read_csv('mtcars.csv', sep=',')
BankWages = pd.read_csv('BankWages.csv', sep=',')

# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from plotnine import *
#from dfply import *


# %%
plt.hist(BankWages['education'])
# (array([ 53., ...]), <a list of 10 Patch objects>) 등을 생략하려면 plt.hit() 끝에 ;를 붙인다


# %%
BankWages['education'].hist();


# %%
plt.hist(BankWages['education'])
BankWages['education'].hist()  # 여기서 색은 왜 바뀌는 것인가?

# %%
# #BankWages.plot?
# plot은 numerica data만 가능?
# > BankWages['gender'].plot()
# TypeError: no numeric data to plot

# %%

# %%
BankWages['gender'].value_counts().plot(kind='bar')
#BankWages.groupby('gender').size().plot(kind='bar')  # 위의 그래프와 동일한 결과


# %%
BankWages

# %% [markdown]
# ## 15.1.2 이변수 플롯

# %% [markdown]
# ## 데이터 준비 : 범주 비율이 차이를 두기 위해서

# %% language="R"
#
# Bank1 <- BankWages %>% slice(1:200) %>% filter(gender == 'male')
# Bank2 <- BankWages %>% slice(-(1:200))
# Bank <- rbind(Bank1, Bank2)

# %%
BankWages_head=BankWages[1:200]
BankWages_head[BankWages_head['gender']=='male'];
# 일반적으로 ;을 붙이면 결과가 출력되지 않음

# %%
Bank1 = BankWages.iloc[:200]
Bank1 = Bank1.loc[Bank1['gender'] == 'male']
Bank2 = BankWages.iloc[200:]
Bank = pd.concat([Bank1, Bank2], axis=0) # index에 상관없이!

# 신기한 것은 column 이름이 동일할 수도 있다!!!
Bank = pd.concat([Bank1.iloc[:10], Bank2.iloc[:10]], axis=1) 
Bank.loc[:, 'job']
# 따라서 Bank['job']은 pd.Series일 수도 있고, pd.DataFrame일 수도 있다.

# Bank1 = BankWages.iloc[:200] >> filter_by(X.gender == 'male')
# Bank2 = BankWages.iloc[201:]
# Bank = pd.concat([Bank1, Bank2])

# %% language="R"
# #이변수 그림 : x=이산형, y=이산형
# plot(job ~ gender, data=Bank)

# %%
Bank = pd.concat([Bank1, Bank2], axis=0) # index에 상관없이!

state_bank = Bank.groupby(['gender','job']).agg({'gender':'count'})
state_bank.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))  # 여기서 float의 이유?
state_bank.groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).plot(kind='bar')

# %%
# R에서는 x <- fct_infreq(x)을 하겠지만,
# * python에서 x <- fct_infreq(x)는 다음과 같이 쓸 수 있다.
#   x = x.reorder_categories(s.value_counts().index.values.to_list())
# index가 category라면, 그냥 .sort_values()로 가능하다.

# %%
dat2 = state_bank.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
dat2.sort_values(ascending = False).plot(kind = 'bar')

# %%
state_bank2 = Bank.groupby(['gender', 'job']).agg({'gender':'count', 'education':'mean'})
state_bank2
#state_bank2.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
# TypeError: cannot convert the series to <class 'float'>
# Series를 float을 변환하는 방법? x.sum().float()

# %%
#state_bank2.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
state_bank2.groupby(level=0).apply(lambda x: 100 * x / x.sum().astype(float))

# %%
state_bank2.groupby(level=0).apply(lambda x: 100 * x / x.sum())
state_bank2.index  # category 정렬하는 방법? 위에서 봤듯이 .sort_values로 가능...

# %%
state_bank = Bank.groupby(['gender','job']).size()
state_bank.unstack(level=0)

# %%
state_bank.unstack(level=0).plot.bar()
#state_bank.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
#state_bank.groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).plot(kind='bar')

# %%
dat2.sum(axis=1)

# %%
dat2 = state_bank.unstack(level=0)  
# R에서와 같이 (dat2 = state_bank.unstack(level=0))로
# 할당과 출력을 동시에 하기 어려운 듯.

# %%
index = dat2.sum(axis=1).sort_values(ascending = False).index # 정렬한 인덱스
# Python vs R:
# * Python: sum의 기본 옵션이 NA 무시
# * R     : NA가 포함되면 NA

# %%
# 여기서 female + male을 기준으로 plot을 정렬하고자 한다면,
dat2.loc[index].plot.bar()

# %%
from statsmodels.graphics.mosaicplot import mosaic
mosaic(Bank, ['gender', 'job']);


# %% language="R"
# #이변수 그림 : x=이산형, y=연속형
# plot(education ~ gender, data=Bank)

# %%
import seaborn as sns

# %%
Bank.head()

# %%
sns.boxplot(x='gender', y='education', data=Bank, order=['male', 'female'])

# %%
Bank.head()

# %%

# %%
pd.pivot_table(data=Bank, index=Bank.index, values='education', columns=['gender'])

pd.pivot_table(data=Bank, index=Bank.index, values='education', columns=['gender'])

pd.pivot_table(data=Bank, index=Bank.job, values='education', columns=['gender'])
# aggfunc = 'mean'

def tr_mean(x, tr1, tr2):
    n = len(x)
    n1 = int(n*tr1)
    n2 = int(n*(1-tr2))

    return np.mean(np.sort(x)[n1:n2])

aggfunc = lambda x: tr_mean(x, tr1=0.1, tr2=0.2)

pd.pivot_table(data = Bank, index=Bank.job, 
                            columns = ['gender'], values='education', 
                            aggfunc = aggfunc)

# %%
Bank2 = Bank.copy()
Bank2['dum'] = 1

# %%
pd.pivot_table(data = Bank2, index=Bank.job, 
                            columns = ['gender'], values=['education', 'dum'], 
                            aggfunc = aggfunc)

# %%
Bank.pivot( columns='gender', values='education').boxplot(column=['male', 'female'])

# %%
Bank.boxplot(by='gender', column='education')

# %%
# 추후에 생각해볼 방법
# https://stackoverflow.com/questions/21912634/how-can-i-sort-a-boxplot-in-pandas-by-the-median-values
grouped = Bank.groupby('gender')

# 이건 어떤 상황에서 쓰지???
df2 = pd.DataFrame({col:vals['education'] for col,vals in grouped})
df2

# %% language="R"
# #이변수 그림 : x=연속형, y=연속형
# plot(qsec ~ hp, mtcars)

# %%
mtcars.plot(x='hp', y='qsec', kind='scatter')

# %%
mtcars.plot.scatter(x='hp', y='qsec')

# %%
plt.scatter(x=mtcars.hp, y=mtcars.qsec)

# %% language="R"
# # 15.1.3 조건부 일변수 분포
# histogram( ~ job | gender, BankWages)

# %% language="R"
# histogram( ~ job | gender * minority, BankWages)

# %%
# 일변수 분포
BankWages['job'].value_counts().plot(kind='bar')
# 빈도수로 자동 정렬?

# %%
#BankWages[['job', 'gender']].groupby('job').value_counts('gender') ->  'DataFrameGroupBy' object has no attribute 'value_counts'

# %%
# 조건부 일변수 분포 : gender에 따른 job의 분포
BankWages.groupby(['job', 'gender']).size().unstack(level=0).plot.bar()

# %%
# gender에 따른 job의 분포
ax = sns.countplot(x="gender", hue="job", data=BankWages) 
# ?? 그런데 두 plot에서 범주가 정렬되는 방법? 범주의 순서?

# %%
# gender, minority에 따른 job의 분포
sns.catplot(x="gender", hue="job", row="minority",
                data=BankWages, kind="count",
                height=2.6, aspect=1.5);

# %%
BankWages.groupby(['job', 'gender', 'minority']).size().unstack(level=0)

# %%
# 이게 필요해?
# 위의 sns.catplot()과 같이 함수 자체에서 지원하는 않는 경우에
#
fig, axes = plt.subplots(nrows=2, ncols=1, sharex = True, sharey=True)
#fig, axes = plt.subplots(nrows=2, ncols=1, sharey=True)
#plt.subplots_adjust(hspace = 1)
i = 1

for i, dfs in enumerate(BankWages.groupby('minority')):    
    title, df = dfs
#     if i > 0:
#         ax = plt.subplot(2,1,i+1, sharex=ax0)
#     else:
#         ax0 = plt.subplot(2,1,i+1)
#         ax = ax0
#     df.groupby(['job', 'gender']).size().unstack().plot.bar(ax=ax)
    
    df.groupby(['job', 'gender']).size().unstack().plot.bar(ax=axes[i])
    axes[i].set_title('minority='+title, loc='left', x=0.05, y=0.8)  # location of title -> loc='left'/'right', x, y

# %% language="R"
# # 15.1.4 조건부 이변수 플롯
# # 조건부 이변수 그림 : x=범주형, y=연속형
# xyplot(education ~ job | gender, BankWages)
# xyplot(education ~ job | gender, BankWages, jitter.x=TRUE)

# %%
BankWages.groupby('gender').plot.scatter(x='job', y='education')

# %%
BankWages.shape

# %%
plt.scatter(x='job', y=np.repeat(1,474), data=BankWages) # ERROR 확인하기?

# %%
# plt.scatter?

# %%
np.number

# %%
np.random.uniform(0,1,10)

# %%
np.issubdtype(BankWages['education'].dtype, np.number)

# %%
pd.Series(np.array([1,3,2.,np.nan])).std()


# %%
def jitter(x, y,
    jitter_x = 0.1,
    jitter_y = 0.1,
    s=None,
    c=None,
    marker=None,
    cmap=None,
    norm=None,
    vmin=None,
    vmax=None,
    alpha=None,
    linewidths=None,
    edgecolors=None,
    *,
    plotnonfinite=False,
    data=None,
    **kwargs):
    
    if data is None:
        raise ValueError('None data is not supported yet')
    if np.issubdtype(data[x].dtype, np.number):
        data[x+'(jittered)'] = data[x] + jitter_x * np.random.uniform(0, 1, data.shape[0]) * data[x].std()
        x = x + '(jittered)'
    if np.issubdtype(data[y].dtype, np.number):
        data[y+'(jittered)'] = data[y] + jitter_y * np.random.uniform(0, 1, data.shape[0]) * data[y].std()
        y = y + '(jittered)'
    
    plt.scatter(x=x, y=y, s=s, c=c, marker=marker,cmap=cmap, norm=norm, 
                vmin=vmin, vmax=vmax, alpha=alpha, linewidths=linewidths, edgecolors=edgecolors,
                plotnonfinite=plotnonfinite, data=data,
                **kwargs)
                

    

# %%
BankWages.head()

# %%
jitter(x='job', y='education',data=BankWages)

# %%
np.array([1,32,1]).dtype

# %%
jitter(x='x', y='y', data = pd.DataFrame({'x':[3,2,1],'y':[2,4,3]}))

# %%
conditional_plot = sns.FacetGrid(BankWages, col='gender', col_wrap=2)
conditional_plot.map(plt.scatter, 'job', 'education')

# ?? 솔직히 너무 복잡해 보임. 좀더 간단하게 풀어가는 방법?
# 아니면 함수를 만들거나...

# %%
# BankWages.plot?

# %%
#BankWages.groupby('gender').plot(jitter_x=0.1)
#손 쉽게 jitter를 넣는 방법이 없어 보임...

# %%
conditional_plot = sns.FacetGrid(BankWages, col='gender', col_wrap=2)
conditional_plot.map(plt.scatter, 'job', 'education' )
# conditional_plot.map(plt.scatter, 'job')

# %%
sns.stripplot('job', 'education', data=BankWages, jitter=0.2)

# %%
conditional_plot = sns.FacetGrid(BankWages, col='gender', col_wrap=2)
conditional_plot.map(sns.stripplot , 'job', 'education', alpha=0.3)
# conditional_plot.map(sns.stripplot, 'job', 'education')

# %%

# %% language="R"
# # 15.1.5 조건부 이변수 플롯
# # 조건부 이변수 그림 : x=연속형, y=연속형
# xyplot(qsec ~ hp | mpg, mtcars)
# mpgequal <- equal.count(mtcars$mpg, number=3, overlap=0)
# xyplot(qsec ~ hp | mpgequal, mtcars)

# %%
import seaborn as sns

# %%
# pd.qcut?

# %%
# sns.stripplot?


# %%
# equal.count 구현? 먼저 전체 갯수를 파악한 후, 하나의 구간에 몇 %가 들어가야 할 지 확인

# %%
# ?np.arange

# %%
n=len(mtcars)
m=3 # 3개씩 들어가야 한다면
qbin = m/n
qs = np.arange(0,1,qbin)
if qs[-1] != 1:
    qs = np.concatenate([qs, [1]], axis=0)

# %%
mtcars['mpg_qcut'] = pd.qcut(mtcars['mpg'], q=qs)
conditional_plot = sns.FacetGrid(mtcars, col='mpg_qcut', col_wrap=4)
conditional_plot.map(plt.scatter, 'hp', 'qsec' )

# %% language="R"
# mpgequal <- equal.count(mtcars$mpg, number=5, overlap=0)
# xyplot(qsec ~ hp | mpgequal, mtcars)

# %%
n=len(mtcars)
m=5 # 3개씩 들어가야 한다면
qbin = m/n
qs = np.arange(0,1,qbin)
if qs[-1] != 1:
    qs = np.concatenate([qs, [1]], axis=0)
mtcars['mpg_qcut'] = pd.qcut(mtcars['mpg'], q=qs)
conditional_plot = sns.FacetGrid(mtcars, col='mpg_qcut', col_wrap=4)
conditional_plot.map(plt.scatter, 'hp', 'qsec' )

# %%



# %%
import math
n=len(mtcars)
m=5 # 3개씩 들어가야 한다면
nq = math.ceil(n/m)
qs = np.arange(0,1,1/nq)
if qs[-1] != 1:
    qs = np.concatenate([qs, [1]], axis=0)
mtcars['mpg_qcut'] = pd.qcut(mtcars['mpg'], q=qs)
conditional_plot = sns.FacetGrid(mtcars, col='mpg_qcut', col_wrap=4)
conditional_plot.map(plt.scatter, 'hp', 'qsec' )

# %% language="R"
# mpgequal <- equal.count(mtcars$mpg, number=5, overlap=0.2)
# xyplot(qsec ~ hp | mpgequal, mtcars)


# %%
