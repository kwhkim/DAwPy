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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# `ax` 또는 `axes`는 `axesSubplot`의 약어

# %%

# %% [markdown]
# ## package `seaborn`
#
# * 패키지 `seaborn`은 `matplotlib` 패키지를 기반으로 만들어진 파이썬의 시각화 패키지이다.
# * `matplotlib`가 저수순의 그래픽 인터페이스라면, `seaborn`은 고수준의 그래픽 인터페이스이다.
# * 데이터를 위치, 크기, 색, 모양 등으로 변환하는 과정이 `matplotlib`보다 편리하다.
#
# !!!TO-DO: `matplotlib`으로 색, 모양 대응시키는 법과 `seaborn`을 활용하는 법 비교

# %%
import seaborn as sns

# %% [markdown]
# * 여기서 sns은 seaborn의 축약형 같아 보이지 않는다.
# * sns은 Seaborn Newell Samuel의 약자이다.(참고문헌???) 
# * Seaborn Newell Samuel이란 The West Wing이란 미국 드라마 시즌 1-4의 주인공이다.
# * 어디서 웃어야할지 모르겠지만, inner(inside???) joke라고 한다.[^snsname]
#
# [^snsname]: 저자는 The West Wing 시즌 1의 첫 에피소드를 감상했다. 여전히 모르겠다.

# %% [markdown]
# ### package `matplotlib`
#
# * seaborn은 matplotlib를 기반으로 만들어졌다. 
# * 그래서 seaborn을 사용할 때 matplotlib의 함수 또는 객체가 필요한 경우가 생긴다.
# * 보통 matplotlib.pyplot도 함께 import 한다.

# %%
import matplotlib.pyplot as plt


# %% [markdown]
# ### `sns.load_dataset()`
#
# * seaborn에는 예제 데이터가 있다
# * 데이터는 `sns.load_dataset()`으로 불러올 수 있다.
# * 대표적으로 가용한 데이터는 `anscombe`, `diamonds`, `flights`, `iris`, `mpg`, `tips` 등이 있다. 
# * 가용한 데이터의 전체 리스트는 `https://github.com/mwaskom/seaborn-data`에서 확인할 수 있다.

# %%
tips = sns.load_dataset('tips')


# %%
print(tips.shape)
tips.head()

# %% [markdown]
# ## `tips` 데이터
#
# * `tips` 데이터는 어떤 웨이터가 어떤 식당에서 일하면서 자신이 받은 팁을 기록한 자료이다.
# * 전체 식사비(달러; `total_bill`), 받은 팁(달러; `tip`), 팁을 준 사람의 성별(Male/Female; `sex`), 식사모임에 흡연자가 포함되어 있는지(Yes/No; `smoker`), 요일(`day`), 시간(`time`), 식사모임의 인원(`size`)이 기록되어 있다.
# * 사례의 갯수는 244이다.

# %%
tips.head()

# %% [markdown]
# ## 대담한 시도
#
# `tips` 데이터를 단 하나의 `seaborn` 함수로 시각화해보자.

# %%
sns.set_theme(context="poster")
sns.relplot(kind='scatter',
            x='total_bill', y='tip', 
            hue='sex', size='size', 
            col='day', row='time', 
            style='smoker',
            alpha=0.7,
            data=tips)

# %% [markdown]
# 먼저 그래프의 배치를 확인할 필요가 있다. 2행 4열로 8개의 그래프가 배치되어 있으며, 첫 번째 행은 모두 Lunch, 두 번째 행은 모두 Dinner인  데이터를 시각화하고 있다. 각 열은 목, 금, 토, 일요일의 데이터를 시각화한다. 남자는 파란색, 여자는 주황색으로, 흡연자는 동그라미, 비흡연자는 엑스(x)자로 시각화되어 있다. 그리고 각 집단의 크기(집단을 구성하는 사람 수)에 비례하여 동그라미 또는 엑스(x)자의 크기가 크다. 이렇게 데이터의 모든 열(`total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size`)은 그래프의 각 시각적 특질(x-좌표, y-좌표, 색, 모양, 열, 행, 점의 크기)에 대응하여 시각화되어 있다! 시각화 결과를 얼마나 쉽게 이해할 수 있는가와 별개로 데이터의 모든 정보를 하나의 화면에 시각화한 것이다.
#
# 위의 그래프에서 무엇을 확인할 수 있는가?
#
# * 그래프를 보면 목요일은 점심시간에 그리고 토요일과 일요일에는 저녁시간에 팁을 받는다는 것을 알 수 있다. 팁이 0인 경우는 없으므로 팁을 안 주는 사람이 없거나 팁을 안 받은 경우는 자료에 포함되지 않은 듯 하다. (데이터가 어떤 나라에서 생산되었는지는 알 수 없지만, 미국의 경우 팁은 명목상으로 자율이고 대부분은 팁을 주는 것이 불문율이라고 한다.)
# * 식사 비용이 증가할 수록 팁이 증가하는 경향을 뚜렷이 확인할 수 있다(미국에서 팁은 보통 식사비의 15-25%를 낸다고 한다).

# %% [markdown]
# 그래프는 목적에 맞춰 수정될 수 있다. 예를 들어 남자와 여자의 개별 패턴을 확인하고 싶다면 남자와 여자를 나눠서 산점도를 그릴 수 있다. 그리고 `total_bill`과 `tip`이 모두 0인 점과 수직, 수평선, 그리고 통상적인 팁의 범위인 15-25%를 확인하기 위해 기울기 0.15와 0.25의 (원점을 지나가는) 직선을 그려줄 수 있다.

# %%
sns.set_theme(context="notebook")
g = sns.relplot(kind='scatter',
            x='total_bill', y='tip', 
            hue='time',     # R의 ggplot2에서는 col
            size='size',
            style = 'day',  # R의 ggplot2에서는 shape
            col='sex',      # R의 ggplot2에서는 + facet_grid()
            alpha=0.9,      # 진한 정도
            data=tips)

# %%
sns.set_theme(context="notebook")
g = sns.relplot(kind='scatter',
            x='total_bill', y='tip', 
            hue='time',     # R의 ggplot2에서는 col
            size='size',
            style = 'day',  # R의 ggplot2에서는 shape
            col='sex',      # R의 ggplot2에서는 + facet_grid()
            alpha=0.9,      # 진한 정도
            data=tips)

#g.axes[0,0].axhline(y=0)
#g.axes[0,0].axvline(x=0)
for ax in g.axes.flatten():#g.axes.flatten()??
    ax.axhline(y=0)
    ax.axvline(x=0)
    ax.axline((0,0), slope = 0.15, linestyle = 'dotted', color = 'grey') 
    # (0,0)을 지나는 기울기 0.15 직선
    ax.axline((0,0), slope = 0.25, linestyle = 'dotted', color = 'grey')  
    # cf) ax.hline, ax.vline



# %%

# %% [markdown]
# * 점의 모양으로 요일을 구분할 수는 있지만 쉽게 들어오지 않는다(위에서는 너무도 쉽게 목요일은 점심 손님이 많고 토/일요일은 저녁 손님이 대부분이라는 것을 파악할 수 있다).
#
# * 보통 여러 값의 구분이 가장 쉬운 순서는 위치(x-좌표, y-좌표), 크기, 색의 순서이며, 모양은 범주를 구분할 수는 있지만 양을 나타내기에 부적합하다. 
#
# `seaborn` 패키지를 쓰면 데이터 프레임의 변수를 다양한 시각적 특질과 손쉽게 대응시킬 수 있다. 이렇게 자료의 변수와 시각적 특질(aesthetic)을 연결시켜 자료를 시각화하는 방식을 **G**rammar of **G**raphics라고 부르기도 한다. `seaborn` 저자는 `seaborn`이 **G**rammar of **G**raphics를 완전히 구현하는 것은 아니라고 했지만[^seabornpaper]이라고 하지만 위의 예를 통해 비슷한 방식으로 활용할 수 있다는 사실을 확인할 수 있다. 그리고`seaborn`의 시각화 결과에 세부적인 사향은 `matplotlib`를 활용하여 수정할 수 있다(위에서 `g.axes`은 두 플롯을 모두 담고 있는 배열이며 `g.axes[0,0]`은 0-번째 행, 0-번째 열의 플롯을 의미한다).
#
# [^seabornpaper]: 저자 논문(TO-DO)

# %% [markdown]
# 위의 그림에서 `seaborn` 함수만을 실행해보자. 주요 내용이 `sns.relplot()`을 통해 출력되었음을 확인할 수 있다. 이렇게 `sns.relplot()`으로 데이터에서 시각화하고자 하는 내용과 방법을 결정해줄 수 있다. 그 이후에는 보조선, 레이블, 팔레트 등의 부수적인 내용을 원하는 방식으로 추가하거나 조정하는 정도의 일만 남는다.

# %% [markdown]
# ### `sns.relplot(kind=)`

# %% [markdown]
# `sns.relplot()`은 두 변수의 관계를 x-좌표, y-좌표로 시각화한다. x-좌표, y-좌표에 출력되는 모양은 `kind=`가 결정한다. 다음의 두 플롯을 비교해보자.

# %%
sns.relplot(kind='scatter', x='total_bill', y='tip', data=tips)

# %%
sns.relplot(kind='line', x='total_bill', y='tip', data=tips)

# %% [markdown]
# #### `sns.replot(kind='line',)`

# %% [markdown]
# `kind='line'`은 사실 시계열 자료에 적합한 방식이다. `seaborn` 내장 시계열 데이터 `flights`를 시각화해보자.

# %%
flights = sns.load_dataset('flights')

# %%
import pandas as pd

# %% [markdown]
# 먼저 `date` 컬럼을 만들어 분리되어 있는 `year`와 `month`를 합쳐 날짜로 만든다.

# %%
flights['date'] = pd.to_datetime(flights['year'].astype('str') + '-' + flights['month'].astype('str'))

# %% [markdown]
# 그리고 `sns.replot()`에 `x='date'`(x축에 `date` 컬럼), `y='passengers'`(y축에 `passengers` 컬럼)을 입력하면 `flights` 데이터가 다음과 같이 시각화된다.

# %%
sns.relplot(kind='line', x='date', y='passengers', data=flights)

# %% [markdown]
# 사실 이 정도의 플롯은 `sns.replot()`을 쓰지 않고도 다음과 같이 그릴 수 있다. 

# %%
# 그림 크기 작게
flights[['date', 'passengers']].plot(x='date', y='passengers')
flights[['date', 'passengers']].set_index('date').plot()

# %% [markdown]
# 하지만 `sns.relplot(kind='line', )`만큼 `hue=`, `size=`, `style=`, `col=`, `alpha=`등의 여러 특질을 손쉽게 데이터의 변수와 대응시킬 수는 없다.

# %% [markdown]
# `sns.relplot()`의 `x=`와 `y=`는 반드시 연속형일 필요는 없지만, `x=`와 `y=` 중 하나가 범주형일 경우에는 `sns.catplot()`이 좀더 효과적이다. 비교해보자.

# %%
sns.relplot(kind='scatter',
            x='day', y='tip',
            alpha=0.5,
            data=tips)

# %%
sns.catplot(kind='strip', 
            # default kind for catplot
            y='tip', x='day',
            alpha=0.5,
            data=tips)

# %% [markdown]
# ### `sns.catplot()` : x 또는 y 좌표에 범주형

# %% [markdown]
# `sns.catplot()`은 x 또는 y 좌표에 범주형 변수를 시각화할 때 쓰인다. `sns.catplot()`의 `kind=`는 다음과 같다. 

# %% [markdown]
# # kind = 'xx' :  뒷 부분의 'sns.xxplot()'은 삭제하는 것이 이해에 도움이 될 것 같습니다 
# - 사례 플롯
#     - `kind='strip'` : `sns.stripplot()`
#     - `kind='swarm'` : `sns.swarmplot()`
# - 분포 플롯
#     - `kind='box'` : `sns.boxplot()`
#     - `kind='violin'` : `sns.violinplot()`
#     - `kind='boxen'` : `sns.boxenplot()`  # Final removal of the lvplot function (the previously-deprecated name for boxenplot()).
# - 요약 통계량 플롯
#     - `kind='point'` : `sns.pointplot()`
#     - `kind='bar'` : `sns.barplot()`
# - 빈도 플롯
#     - `kind='count'` : `sns.countplot()`

# %% [markdown]
# `sns.catplot()`이 범주형 자료를 시각화하는 방식은 크게 4가지 방법으로 생각할 수 있다. 모든 사례(instance)를 시각화하는 경우(사례 플롯), 범주별로 연속형 자료의 분포를 몇 가지 간단한 그림(예. 상자 그림, 바이올린 그림, 박슨 그림)으로 시각화하는 경우, 범주별로 요약통계량을 그리는 경우, 그리고 다른 연속형 변수 없이 범주형의 빈도를 그리는 방법이 있다. 이들은 아래에 직접 시연으로 확인하자.

# %% [markdown]
# #### 모든 사례를 시각화

# %%
sns.catplot(kind='swarm',
            y='tip', x='day',
            #alpha=0.8,
            #size = 9, # 여기 size는 point의 size가 아닌 듯... size -> height
            s = 3, # marker의 크기
            data=tips)

# %% [markdown]
# #### 분포를 시각화

# %%
sns.catplot(kind='box',
            y='tip', x='day',
            width=0.2,
            #alpha=0.8,
            #height = 9, # 여기 size는 point의 size가 아닌 듯... size -> height
            data=tips)

# %%
sns.catplot(kind='violin',
            y='tip', x='day', col='time',
            #alpha=0.8,
            #height = 9, # 여기 size는 point의 size가 아닌 듯... size -> height
            data=tips)

# %%
sns.catplot(kind='boxen',
            y='tip', x='day', col='time',
            #alpha=0.8,
            #height = 9, # 여기 size는 point의 size가 아닌 듯... size -> height
            data=tips)

# %% [markdown]
# #### 요약 통계량 시각화

# %% [markdown]
# 평균과 표준오차(standard error)를 시각화하기 위해 `sns.catplot()`에서 `kind='point'` 또는 `kind='bar'`를 사용할 수 있다. `kind='point'`는 평균을 점으로, 표준오차를 바(bar)로 시각화하며, `kind='bar'`는 평균을 막대그림으로 시각화한다. 
#
# 관련된 설정사항은 `join=False`(점을 선으로 연결하지 않음), `dodge=True`(점이 겹칠 경우 위치를 살짝 이동) 등이 있다.
#
# https://seaborn.pydata.org/generated/seaborn.pointplot.html 

# %%
sns.catplot(kind='point',
            y='tip', x='day', col='time',
            #alpha=0.8,
            #height = 9, # 여기 size는 point의 size가 아닌 듯... size -> height
            data=tips)

# %%
sns.catplot(kind='bar',
            y='tip', x='day', col='time',
            #alpha=0.8,
            #height = 9, # 여기 size는 point의 size가 아닌 듯... size -> height
            data=tips)

# %% [markdown]
# #### 빈도 플롯

# %% [markdown]
# 마지막으로 `sns.catplot(kind='count')`는 `x=`의 변수에 대해 빈도를 시각화한다.

# %%
sns.catplot(kind='count',
            x='day', col='time',
            #alpha=0.8,
            #height = 9, # 여기 size는 point의 size가 아닌 듯... size -> height
            data=tips)

# %% [markdown]
# #### 선형회귀분석 : `sns.lmplot()`  
#
# 위에서 `sns.relplot()`으로 두 연속형 변수 사이의 모든 점을 시각화할 수 있었다. 이런 시각화는 보통 두 변수 사이에 존재하는 관계(**rel**ation)을 시각화하기 위해 사용한다. 두 변수 사이에 존재하는 관계는 선형 회귀 등의 통계 분석 방법으로 요약될 수 있다. `sns.lmplot()`은 선형모형(**l**inear **m**odel)을 시각화하기 위해 사용된다.
#
# * `sns.lmplot(x=, y=, col=, row=, data=)`

# %%
sns.lmplot(x='total_bill', y='tip', col='day',
           data=tips)

# %% [markdown]
# #### 분포 시각화 : `sns.displot()`
#
# `sns.catplot()`의 `kind='box'`, `'violin'`, `'boxen'`은 모두 범주에 따른 연속형 변수의 분포를 시각화했다. `sns.displot()`은 좀더 전문적으로 **분포**(**dist**ribution)를 시각화한다.

# %% [markdown]
# `sns.displot(kind='hist', )`는 주어진 자료에 대해 히스토그램을 그린다. 만약 `x=`만 주어진다면 우리가 익히 아는 히스토그램이 그려지고, `x=`, `y=`를 모두 입력하면 2차원 상에서 색으로 빈도를 표시한다.

# %%
sns.displot(kind='hist', 
            x='total_bill', col='day',
            data = tips)

# %%
sns.displot(kind='hist', 
            x='total_bill', y='tip', col='day',
           data = tips)

# %% [markdown]
# 히스토그램은 막대의 너비(또는 범위)를 설정하는 것을 제외하고는 자료를 있는 그대로 시각화한다. 
# `sns.displot(kind='kde', )`의 `kde`는 **k**ernel **d**ensity **e**stimation을 의미한다. **kde**는 분포를 추정할 때 특정한 커널(kernel)을 사용한다. 커널 추정에 필요한 설정 사항은 `kde_kws=`에 인자로 입력할 수 있다.

# %%
sns.displot(kind='kde', 
            x='total_bill', col='day',
            hue='time',
            fill = True,
            data = tips)
# 자세한 설정 사항은 다음을 참조하라
# https://seaborn.pydata.org/generated/seaborn.kdeplot.html

# %% [markdown]
# `sns.distplot(kind='ecdf',)`은 **e**mpirical **c**umulative **d**istribution **f**unction을 시각화한다. ecdf는 경험적 누적 분포 함수(**e**mpirical **c**umulative **d**istribution **f**unction)의 약어(acronym)으로 이 함수는 어떤 값이 주어졌을 때, 전체 자료에서 이 값과 같거나 작은 값의 비율을 출력한다. 만약 입력 x에 대한 함수값이 0이라면 x보다 작은 값이 관찰되지 않았음을 의미하고, 입력 x에 대한 함수값이 1이라면 x보다 큰 값이 관찰되지 않았음을 의미한다. 

# %%
sns.displot(kind='ecdf', 
            x='total_bill', col='day',
            hue='time',
            data = tips)
# 자세한 설정 사항은 다음을 참조하라
# https://seaborn.pydata.org/generated/seaborn.kdeplot.html

# %%
sns.displot(kind='hist',
           x='total_bill', col='day',
           hue='time', data=tips)

# %% [markdown]
# kde로 추정된 분포에서 cdf(**c**umulative **d**ensity **f**unction)을 시각화라면 다음과 같이 `sns.displot(kind='kde', cumulative = True, )`를 사용한다. 다음의 예를 보자. 

# %%
sns.displot(kind='kde', 
            x='total_bill', col='day',
            hue='time',
            fill = True,
            cumulative = True,
            common_norm=False, 
            common_grid=True,
            data = tips)

# %%
# relplot, catplot, displot의 차이와 각각에서 사용가능한 plot을 표나 그림으로 마지막에 정리해주면 훨씬 좋을 것 같습니다!
# 참고: https://www.inflearn.com/questions/98630

# %% [markdown]
# ## Figure 수준의 결과와 Axes 수준의 결과
#
# `seaborn`의 결과는 크게 figure(그림) 수준의 결과와 **axes(축) 수준**의 결과로 나눠 볼 수 있다. 그림(figure) 수준의 결과는 하나 또는 그 이상의 **축(ax) 수준** 결과가 모여 만들어진다. 그림 수준의 함수와 축 수준의 함수는 매개변수 `col=` 또는 `row=`의 존재여부로 판정이 가능하다. `col=`과 `row=`는 하나의 그림에 행 또는 열을 따라 여러 플롯을 생성하기 위해 사용하기 때문에 그림(figure) 수준의 함수라고 볼 수 있다.
#
# 앞에서 소개한 함수 `relplot()`, `catplot()`, `lmplot()`, `distplot()`은 모두 그림 수준의 함수이다. 다음의 표는 그림 수준의 함수와 대응하는 축 수준의 함수를 보여준다.
#
#
#
#

# %% [markdown]
# | 그림 수준의 함수 | 축 수준의 함수 |
# |:-------------|:------------|
# |`relplot(kind='scatter')` | `scatterplot()`|
# |`                'line')` | `lineplot()`|
# |`catplot(kind='strip')` | `stripplot()`|
# |`             'swarm')` | `swarmplot()`|
# |`               'box')` | `boxpplot()`|
# |`            'violin')` | `violinplot()`|
# |`             'boxen')` | `boxenplot()`|
# |`             'point')` | `pointplot()`|
# |`               'bar')` | `barplot()`|
# |`             'count')` | `countplot()`|
# |`distplot(kind='ecdf')` | `pointplot()`|
# |`              'hist')` | `barplot()`|
# |`               'kde')` | `countplot()`|
# |`lmplot()`              | `regplot()` |
#
#

# %% [markdown]
# 예를 들어 `relplot(kind='scatter',)`와 `scatterplot()`을 비교 실행해보면 다음과 같다.

# %%
sns.relplot(kind='scatter',
            x='total_bill', y='tip', 
            alpha=0.7,
            data=tips)

# %%
sns.scatterplot(x='total_bill', y='tip', 
                alpha=0.7,
                data=tips)

# %% [markdown]
# `sns.replot(kind='scatter',)`와 거의 동일한 방식으로 `sns.scatterplot()`을 사용할 수 있음을 확인할 수 없다. 하지만 위에 말했듯이 `col=`을 설정할 수는 없다. 그리고 여러 가지 부가 설정 방법이 다르다. 아래에는 그림의 크기를 높이 2, 너비 6으로 설정하고 있다.

# %%
g = sns.relplot(kind='scatter',
            x='total_bill', y='tip', 
            alpha=0.7,
            data=tips)
g.fig.set_figheight(2)
g.fig.set_figwidth(6)

# %%
plt.figure(figsize = (6,2)) # width, height
sns.scatterplot(x='total_bill', y='tip', 
                alpha=0.7,
                data=tips)

# %% [markdown]
# 참고로 위에서 소개한 함수를 제외한 나머지 시각화 함수는 다음과 같다.

# %% [markdown]
# * `pairplot()` : 변수 쌍 그림
# * `residplot()` : 회귀 분석 잔차 그림
# * `rugplot()` : 러그 그림
# * `dogplot()` : 그냥 개 사진(필자가 이해하지 못하는 농담)

# %% [markdown]
# 이들 중 `pairplot()`은 산점도 행렬(scatterplot matrix)을 출력하며, 탐색적 데이터 분석을 위해 요긴하게 사용할 수 있다. 

# %%
g = sns.pairplot(tips, hue='time')
g.fig.set_figheight(4)
g.fig.set_figwidth(6)

# %% [markdown]
# 다음은 그림 수준의 `seaborn` 함수를 사용하여 시각화를 한 후, 각 축에 대해 `matplotlib` 또는 `seaborn`의 축 수준 함수를 사용하여 수정하는 예를 보여준다. 

# %%
g = sns.relplot(kind='scatter',
            x='total_bill', y='tip', 
            style= 'sex', data=tips, 
            col='sex', row='time')
g.fig.set_figheight(4)
g.fig.set_figwidth(6)

# matplotlib 함수
g.axes[0,1].scatter(x=tips['total_bill'], 
                    y=tips['tip'],
                    color='black', 
                    # col이 아니라 color임을 유의하자.
                    # seaborn의 figure 수준의 함수에서는 
                    # column을 의미하는 col을 쓰기 때문에 
                    # hue를 쓴다는 점도 유의하자.
                    alpha=0.1)
# sns의 ax 수준 함수
sns.rugplot(x='total_bill',
            y='tip',
            data=tips,
            ax = g.axes[1,0])

plt.show()

# %%
g = sns.relplot(kind='scatter',
            x='total_bill', y='tip', 
            style= 'sex', data=tips, 
            col='sex', row='time')
g.fig.set_figheight(4)
g.fig.set_figwidth(6)

# %%

# %%

# %% [markdown]
# ### === END OF DOCUMENT

# %%

# %%

# %%

# %%
## figure-수준 함수와 대응하는 ax-수준 함수

* catplot
  - barplot, boxenplot, boxplot, countplot, pointplot, stripplot, swarmplot, violinplot
* relplot
  - scatterplot, lineplot
* displot
  - ecdfplot, histplot, kdeplot  
* lmplot
  - regplot
* 기타
  - pairplot : 변수쌍 그림(?)
  - displot : histplot, kdeplot, rugplot을 모두 합친 그래프
  - residplot : 회귀 분석 잔차 그림
  - rugplot
  - dogplot : 그냥 개 사진

## 참고?
* https://dining-developer.tistory.com/30sca

# %%

# %%
g = sns.catplot(kind='count',
            x='day', col='time',
            #alpha=0.8,
            #height = 9, # 여기 size는 point의 size가 아닌 듯... size -> height
            data=tips)

g.fig.set_figheight(4.8)
g.fig.set_figwidth(6.4)

# %%
#plt.figure(figsize = (6.4, 4.8))
#plt.figure(figsize = (12.8, 9.6)) # 만약 sns.replot 후 plt...으로 덧붙인다면?


# %%
# ?sns.catplot

# %%
sns.catplot(kind='strip', # default kind
            x='day', y='tip',
            alpha=0.5,
            data=tips)

# %%

# %%

# %%

# %%
g = sns.relplot(kind='line',
            x='date', y='ratio_tip', 
            hue='time',     # R의 ggplot2에서는 col
            #size='size',
            style = 'day',  # R의 ggplot2에서는 shape
            col='sex',      # R의 ggplot2에서는 + facet_grid()
            alpha=0.9,      # 진한 정도
            data=tips)

# %%
g = sns.relplot(kind='line',
            x='date', y='day', 
            hue='time',     # R의 ggplot2에서는 col
            #size='size',
            #style = 'day',  # R의 ggplot2에서는 shape
            col='sex',      # R의 ggplot2에서는 + facet_grid()
            alpha=0.9,      # 진한 정도
            data=tips)

# %%

# %%

# %% [markdown]
# * 1범주형+1연속형 변수 : `sns.catplot(kind=)`
#     - 사례 플롯
#         - `kind='strip'` : `sns.stripplot()`
#         - `kind='swarm'` : `sns.swarmplot()`
#     - 분포 플롯
#         - `kind='box'` : `sns.boxplot()`
#         - `kind='violin'` : `sns.violinplot()`
#         - `kind='boxen'` : `sns.boxenplot()`  # Final removal of the lvplot function (the previously-deprecated name for boxenplot()).
#     - 요약 통계량 플롯
#         - `kind='point'` : `sns.pointplot()`
#         - `kind='bar'` : `sns.barplot()`
#     - 빈도 플롯
#         - `kind='count'` : `sns.countplot()`
#        

# %%

# %%

# %% [markdown]
# 하지만 `sns.relplot(kind='line', 
#
#
# 하지만 `sns.relplot(kind='line', 

# %%
flights['date'] = pd.to_datetime(flights['year'], flights['month'])

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# ## Figure 수준의 결과와 Axes 수준의 결과
#
# * `seaborn`의 결과는 크게 figure(그림) 수준의 결과와 **axes(축) 수준**의 결과로 나눠 볼 수 있다.
# * figure 수준의 결과는 하나 또는 그 이상의 **축 수준** 결과가 모여 만들어진다.

# %%
cm = 1/2.54 

# %%
6.4/cm, 4.8/cm

# %%
# https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/figure_size_units.html

cm = 1/2.54  # centimeters in inches

# inches
plt.rcParams["figure.figsize"] = (6.4, 4.8)  # width, height
plt.rcParams['figure.figsize'] = (16.256*cm, 12.192*cm)
fig, axes = plt.subplots(3,2)
# 크기 변경 : 아래 모두 안 됨
#fig, axes = plt.subplots(3,2, figsize=(6.4, 4.8))
#fig, axes = plt.subplots(3,2, figsize=(12.8, 9.6))
#plt.figure(figsize = (6.4, 4.8))
#plt.figure(figsize = (12.8, 9.6))
plt.show()
print(axes.shape)
type(axes)

# %% [markdown]
# * `matplotlib`의 결과는 여러 개의 축(`axes`)가 모여 하나의 그림(`fig`)이 만들어진다.
# * 그리고 각 축을 지정해서 그래프를 그린 후, 화면에 표시한다.

# %%
fig, axes = plt.subplots(3,2)
axes[1,0].scatter(x = tips['total_bill'],
                  y = tips['tip']); # 1-번째 행, 0-번째 열에 해당하는 축
plt.show()

# %% [markdown]
# * `seaborn` 패키지를 사용하는 경우, 각 축에 들어갈 그래프를 각자 그릴 수도 있고, 전체 그림을 한 번에 생성할 수도 있다.

# %%
fig, axes = plt.subplots(3,2)
sns.scatterplot(x='total_bill', y='tip', 
                style= 'sex', data=tips, ax= axes[1,0])
plt.show()

# %%
# ?sns.relplot

# %%
dir(g.figure)

# %%
type(g.figure)

# %%
type(g.fig)

# %%
help(g.set)

# %%
# jupyter notebook에서 seaborn plot 크기 정하기
# 아래 모두 작동하지 않음
# sns.replot( , height = h, aspect = h/w) # 로 height/width

#sns.set(rc = {'figure.figsize':(15,8)})
#sns.set(rc = {'figure.figsize':(6.4, 4.8)})
#plt.figure(figsize = (6.4, 4.8))
#plt.figure(figsize = (12.8, 9.6))


g = sns.relplot(kind='scatter',
             x='total_bill', y='tip', 
             style= 'sex', data=tips, 
             col='sex', row='time',
             height = 4.8/2, 
             #aspect = 4.8/6.4)
             aspect = 6.4/4.8)

# 아래 : 크기에 변화 없음
#plt.figure(figsize = (6.4, 4.8))
#plt.figure(figsize = (12.8, 9.6)) # 만약 sns.replot 후 plt...으로 덧붙인다면?

g.fig.set_figheight(4.8)
g.fig.set_figwidth(6.4)


# height : height of each facet(in inches)
# height = h, aspect = h/v에서 
# 각 facet의 수만큼 나누면 될 듯...
# 위에서와 같이 h,w = 4.8, 6.4로 하면 legend(범례)때문에 plot이 좁아짐?
# 범례는 포함시키지 않는 듯

dir(g)


# %%
g = sns.relplot(kind='scatter',
             x='total_bill', y='tip', 
             style= 'sex', data=tips, 
             col='sex', row='time',
             #height = 4.8/2, 
             #aspect = 4.8/6.4)
             #aspect = 6.4/4.8)
               )
g.fig.set_figheight(4.8)
g.fig.set_figwidth(6.4)
# 근데 여긴 왜 legend가...?

#g.fig.set_figheight(9.6)
#g.fig.set_figwidth(12.8)



# %% [markdown]
# * 전체 그림을 생성한 이후에도 `matplotlib` 또는 `sns`을 활용하여 각 축을 수정할 수 있다.

# %%

# %%
# https://medium.com/analytics-vidhya/5-lesser-known-seaborn-plots-most-people-dont-know-82e5a54baea8

# %%
dir(plt)

# %%

# %%
isinstance(g, plt.Axes)

# %%
g

# %%
### module object?
sns.miscplot
dir(sns.miscplot)

# %%
fn = 'barplot'
fns = [x for x in dir(sns) if x.endswith('plot')]

for fn in fns:
    print(fn)
    g = None
    f = getattr(sns, fn)
    try:
        g = f(x = 'total_bill', y='tip', data=tips)
        print(g)
    except Exception as e1:
        try:
            print("!   ", e1)
            g = f(x='day', y='tip', data=tips)
            print(g)
        except Exception as e2:
            try:
                print("!!  ", e2)
                g = f(x='day', data=tips)
                print(g)
            except Exception as e3:
                try:
                    print("!!! ", e3)
                    g = f(x='total_bill', data=tips)
                    print(g)
                except Exception as e4:
                    print("!!!!", e4)
    
    if g is not None:
        if isinstance(g, plt.Axes):
            g.set_title(fn)
        elif isinstance(g, sns.FacetGrid):
            g.fig.suptitle(fn)
        else:
            print('! g is neither Axes Nor Figure')
            
    plt.show()


# %%
help(sns.displot)

# %%
help(sns.lmplot)

# %%
help(sns.distplot)

# %%
tips['total_bill']

# %%
g = sns.distplot(a = tips['total_bill'], hist=True, kde=True, rug=True)
plt.show()
print(g)

# %%
sns.pairplot(data=tips, hue='sex')

# %%
help(sns.pairplot)

# %% [markdown]
# ## 결과에 따른 분류
#
# * FacetGrid : catplot(factorplot), displot, lmplot, relplot, 
# * AxesSubplot : barplot, boxenplot, boxplot, countplot, distplot, ecdfplot, histplot, kdeplot, lineplot, pointplot, regplot, residplot, rugplot, scatterplot, stripplot, swarmplot, violinplot
# * JointGrid : jointplot
# * PairGrid : pairplot
# * module : miscplot
# * None : dogplot
# * ??? : pairplot, palplot
#     
# ## figure-수준 함수와 대응하는 ax-수준 함수
#
# * catplot
#   - barplot, boxenplot, boxplot, countplot, pointplot, stripplot, swarmplot, violinplot
# * relplot
#   - scatterplot, lineplot
# * displot
#   - ecdfplot, histplot, kdeplot  
# * lmplot
#   - regplot
# * 기타
#   - pairplot : 변수쌍 그림(?)
#   - displot : histplot, kdeplot, rugplot을 모두 합친 그래프
#   - residplot : 회귀 분석 잔차 그림
#   - rugplot
#   - dogplot : 그냥 개 사진
#
# ## 참고?
# * https://dining-developer.tistory.com/30

# %%
help(sns.displot)

# %%
fn

# %%
x = 'barplot'
getattr(sns, x)

# %%
l = [x for x in dir(sns) if x.endswith('plot')]

', '.join(l)


# %% [markdown]
# ## Figure 수준의 함수와 ax 수준의 함수
#
# * 1연속형+1연속형 변수 : `sns.relplot(kind=)`
#     - `kind='scatter'`: `sns.scatterplot()`
#     - `kind='line'`: `sns.lineplot()`
#
# * 1범주형+1연속형 변수 : `sns.catplot(kind=)`
#     - 사례 플롯
#         - `kind='strip'` : `sns.stripplot()`
#         - `kind='swarm'` : `sns.swarmplot()`
#     - 분포 플롯
#         - `kind='box'` : `sns.boxplot()`
#         - `kind='violin'` : `sns.violinplot()`
#         - `kind='boxen'` : `sns.boxenplot()`  # Final removal of the lvplot function (the previously-deprecated name for boxenplot()).
#     - 요약 통계량 플롯
#         - `kind='point'` : `sns.pointplot()`
#         - `kind='bar'` : `sns.barplot()`
#     - 빈도 플롯
#         - `kind='count'` : `sns.countplot()`
#         
# * 회귀분석 : `sns.lmplot()`  
#     - `sns.regplot()`
#     - `sns.residplot()`
#     
# * 그 밖의 ax 수준 함수
#     - 
#     

# %%
tips.head()

# %%
sns.lmplot(kind='resid', x='total_bill', y='tip', data=tips)

# %%
#sns.lvplot # letter-value plot
sns.__version__

# %%
sns.boxenplot(x='total_bill', y='day', data=tips)

# %%
sns.lvplot(x='total_bill', y='tip', data=tips)

# %%

# %%

# %%
# ?sns.regplot

# %%
fig = sns.lmplot(
            x='total_bill', y='tip', 
            hue='sex',     # R의 ggplot2에서는 col
            #size='size',
            #style = 'day',  # R의 ggplot2에서는 shape
            #col='sex',      # R의 ggplot2에서는 + facet_grid()
            #alpha=0.7,
            data=tips)

fig.axes[0,0].axhline(y=0)
fig.axes[0,0].axvline(x=0)

# %%
sns.lmplot(
            x='total_bill', y='tip', 
            hue='sex',     # R의 ggplot2에서는 col
            #size='size',
            #style = 'day',  # R의 ggplot2에서는 shape
            col='time',      # R의 ggplot2에서는 + facet_grid()
            #alpha=0.7,
            data=tips)

# %%
# axes 수준 plot
fig = sns.regplot(
            x='total_bill', y='tip', 
            #hue='time',     # R의 ggplot2에서는 col
            #size='size',
            #style = 'day',  # R의 ggplot2에서는 shape
            #col='sex',      # R의 ggplot2에서는 + facet_grid()
            #alpha=0.7,
            data=tips)

# %%
type(fig)

# %%
dir(fig)

# %%

# %%
