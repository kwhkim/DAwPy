# -*- coding: utf-8 -*-
# %% [markdown]
# 일단 뭘 하려는 건지 전체적인 그림이 그려져야 함
# 그냥 practice 형식으로 나아가도 괜찮을 듯.

# %% [markdown]
# # 범주형 데이터

# %% [markdown]
# ## 파이썬 범주형 데이터(`pd.Categorical`과 `pd.Series([...], dtype='category'))`

# %% [markdown]
# 파이썬의 **내장 클래스** 또는 **표준 모듈**에는 범주형 데이터를 위한 클래스가 없다. **넘파이** 배열에서도 범주형을 위한 dtype(데이터타입)을 지원하지 않는다. 하지만 데이터 분석에서 범주형 자료는 자주 쓰인다. 판다스에서는 범주형 데이터를 위해 `pd.Categorical()`과 `pd.Series([], dtype='category')`를 지원한다.

# %%
import numpy as np
import pandas as pd

# %%
pd.Categorical(['North', 'East', 'West', 'East', 'West'])

# %%
pd.Series(['North', 'East', 'West', 'East', 'West'],
          dtype='category')

# %% [markdown]
# 일단 `pd.Categorical()`과 `pd.Series([], dtype='category')`의 차이에 알아보자.
#
# `type()`으로 둘을 비교해보면 다음과 같다.

# %%
import numpy as np
import pandas as pd
x = pd.Categorical([])
type(x)
#<class 'pandas.core.arrays.categorical.Categorical'>
x.dtype
y = pd.Series([], dtype='category')
type(y)
#<class 'pandas.core.series.Series'>
y.dtype
#CategoricalDtype(categories=)
type(x), x.dtype, type(y), y.dtype

# %% [markdown]
# ```
# x = pd.Categorical([])
# type(x)
# # <class 'pandas.core.arrays.categorical.Categorical'>
# x.dtype
# # CategoricalDtype(categories=[], ordered=False)
# y = pd.Series([], dtype='cateogry')
# type(y)
# # <class 'pandas.core.series.Series'>
# y.dtype
# # CategoricalDtype(categories=)
# ```

# %% [markdown]
# 이 둘의 관계는 마치 `np.array()`와 `pd.Series()`의 관계와 비슷하다. 먼저 `.dtype`은 동일하다.
#
# 넘파이 배열은 범주형 자료를 지원하지 않기 때문에 판다스에서 새롭게 범주형을 지원하는 새로운 클래스를 만들었다.
# 위의 결과를 보면 클래스는 `pandas.core.arrays.categorical.Categorical`이다. 중간의 `arrays`에서 넘파이 배열(`array`)와의 유사성을 유추해 볼 수 있다. 둘의 차이는 넘파이 배열은 인덱스를 지원하지 않고, `pd.Series()`는 인덱스가 있다는 점이다.
#
# `pd.Categorical()`에는 범주형 데이터를 다루는 여러 가지 메쏘드가 존재한다. 예를 들어 새로운 범주를 추가할 때에는 `.add_categories()` 메쏘드를 사용한다. 이런 메쏘드는 `pd.Series()`에서는 `.cat` accesor로 접근할 수 있다.  예를 들어, `x=pd.Categorical()`, `y=pd.Series([], dtype='category')`일 때, `x.add_categories([])`, `y.cat.add_cateogries([])`으로 쓴다.

# %%
from mypack.utils import c, seq

# %%
type(c(1,3,2))

# %% [markdown]
# ## `pd.Categorical()`

# %% [markdown]
# `pd.Categorical` 객체를 생성하는 방법은 다음과 같다.

# %%
#x <- factor(c('A', 'B', 'A', 'A', 'C', 'B'))
import pandas as pd
x = pd.Categorical(['Alpha', 'Beta', 'Alpha', 'Charley', 'Beta'])
x


# %% [markdown]
# 위에서 생성한 `x`와 동일한 내용을 담고 있는 넘파이 배열 `y`를 다음과 같이 생성했다.

# %%
y = np.array(['Alpha', 'Beta', 'Alpha', 'Charley', 'Beta'])
type(y), y.dtype

# %% [markdown]
# 문자열을 담고 있는 배열은 `dtype='O'` 또는 `dtype='U'`로 생성할 수 있다. `pd.array([], dtype='O')` 또는 `pd.array([], dtype='U')`과 같은 문자열 넘파이 배열과 `pd.Categorical()`의 차이는 데이터를 저장하는 방식에 있다. `pd.Categorical()`은 먼저 범주를 확인한다. `y`를 보면 총 자료는 5개이지만, `Alpha`와 `Beta`과 반복되고 있다. 그래서 총 범주는 3개로 리스트로 나타내면 `['Alpha', 'Beta', 'Charley']`이다. 그리고 이들에 코드를 배정한다. `Alpha`는 0, `Beta`는 1, `Charley`는 2로 코드를 배정한 후, 실제 데이터는 배정된 코드를 사용하여 표현한다. `['Alpha', 'Beta', 'Alpha', 'Charley', 'Beta']`는 코드로 나타내면 `[0,1,0,2,1]`이 된다. 
#
# `pd.Categorical()`은 이렇게 데이터는 범주(category)와 코드로 분리해 저장하게 된다. 범주와 코드는 `.categories`와 `.codes`로 확인할 수 있다.

# %%
x.categories, x.codes

# %% [markdown]
# 만약 결측값(`None` 또는 `np.nan`)이 있다면 코드 `-1`로 저장된다.

# %%
x = pd.Categorical(['Alpha', 'Beta', 'Alpha', np.nan, None])
x.codes, x

# %% [markdown]
# 위에서 자료에 `'Charley'`가 포함되어 있지 않기 때문에 결과에 `Categories`를 보면 `'Alpha'`와 `'Beta'`만 있다. 만약 범주를 이미 알고 있다면 `categories=`를 통해 알려줄 수 있다.

# %%
x = pd.Categorical(['Alpha', 'Beta', 'Alpha', np.nan, None],
                  categories=['Alpha', 'Beta', 'Charley'])
x

# %% [markdown]
# 범주형 데이터는 크게 **명목형**과 **순위형**이 있다. 명목형은 서로 독립된 범주형이고, 순위형은 범주 사이에 순위 관계가 존재하는 경우이다. 명목형의 예로 서울, 부산, 대구 등과 같이 범주 사이에 innate한 대소, 우열이 없는 경우이다. 그와 반대로 리커트 응답 항목의 "매우 그렇지 **않다**", "그렇다", "매우 그렇다"는 긍정의 강도에서 "매우 그렇지 **않다**" < "그렇다" < "매우 그렇다"임을 누구나 알 수 있다. 이때 순위형의 문제는 각 범주 사이의 크기를 정확하게 결정할 수 없다는 점에 있다. "매우 그렇지 **않다**", "그렇다", "매우 그렇다"를 0,1,2로 코딩할 수 있지만, 이 코딩값의 의미가 "그렇다"와 "매우 그렇지 않다"의 차이가 1이고, "매우 그렇다"와 "그렇다"의 차이가 정확하게 1이라는 것을 의미하지 않는다. (사람이 "매우 그렇다", "그렇다", "그렇지 않다"라고 대답하는 경우에 그 차이가 정확히 같다고 말하기 힘들다.)

# %% [markdown]
# 순위형 데이터를 생성하는 방법은 다음과 같다.

# %%
y = pd.Categorical(['매우 그렇다', '그렇다', '그렇지 않다', '그렇지 않다', '그렇다'],
                  categories=['그렇지 않다', '그렇다', '매우 그렇다'],
                  ordered = True)
y

# %%
y.categories, y.ordered, y.codes

# %% [markdown]
# 순위형에서는 자료에서 범주의 순위를 확인하기 힘들기 때문에 범주의 순위대로 `categories=`를 설정하고, `ordered=True`로 지정한다. 순위형에서는 자료 사이의 대소를 확인할 수 있고, 대소를 통해 계산할 수 있는 메쏘드(`.min()`, `.max()`)를 지원한다.

# %%
y.min(), y.max()

# %%
x.min(), x.max()

# %% [markdown]
# 만약 명목형 자료를 순위형으로 변환하고자 한다면, `.as_ordered()` 메쏘드를 사용할 수 있다.

# %%
x.as_ordered()

# %% [markdown]
# `.as_ordered()`를 하면 새로운 객체가 생성되고, `.as_ordered(inplace=True)`를 하면 `x`가 바로 변환된다. (결과만 보면 `x=x.as_ordered()`와 같다.)  

# %% [markdown]
# 이때 범주 순위를 결정하기 위해서는 `.reorder_categories()`를 사용할 필요가 있다.

# %%
x.as_ordered().reorder_categories(['Charley', 'Beta', 'Alpha'])

# %% [markdown]
# 만약 `.as_ordered(inplace=True)`를 했다면, 마찬가지로 `.reorder_categories([], inplace=True)`를 해준다. 하지만 `.reorder_categories()`에서 `inplace=True`는 판다스 미래 버전에서 허용되지 않는다고 한다. 그러니 미래 판다스 버전까지 염두해 둔다면 `x=x.reorder_categories([], inplace=True)`가 나을 것이다.

# %%
x.as_ordered(inplace=True)
x = x.reorder_categories(['Charley', 'Beta', 'Alpha'])
x

# %% [markdown]
# 만약 순위형을 범주형으로 변환하고자 한다면 `.as_unordered()`를 사용한다.

# %%
x.as_unordered()

# %% [markdown]
# ### 범주형(`pd.Categorical`) 생성/확인/변환

# %% [markdown]
# 변수가 `x`일 때, 
#
# |         | 범주형  | 순위형  |
# |:--------|:------|:------|
# |  생성    | `pd.Categorical([...], categories=[...])`| `pd.Categorical([...], categories=[...], ordered=True)` |
# |  확인    | `isinstance(x, pd.Categorical) and not x.ordered`    | `isinstance(x, pd.Categorical) and x.ordered` |
# |  변환(~으로)    | `x.as_unordered()` | `x.as_ordered().reorder_categories([...])`|

# %% [markdown]
# ## `pd.Series([...], dtype='category')`

# %% [markdown]
# 판다스 시리즈는 넘파이 배열과 인덱스를 합쳐 놓은 데이터 형태이다. 

# %%
s = pd.Series(x, index = ['a', 'b', 'c', 'd', 'e'])
s

# %% [markdown]
# 위의 출력을 보자. 위의 `a`, `b`, `c` 등은 인덱스를 나타내고, 오른쪽은 값(`Alpha`, `Beta` 등)을 나타낸다. `dtype:`은 자료형을 나타낸다. 그 아래 `Categories`는 범주 목록과 순위 관계를 보여준다. 

# %% [markdown]
# (예상했겠지만) 데이터 타입이 범주형(명목형 또는 순위형)인 판단스 시리즈는 여러 가지 방식으로 생성할 수 있다.

# %%
pd.Series(['Alpha', 'Beta', 'Alpha', np.nan, None], dtype='category', index=list('abcde'))

# %% [markdown]
# 만약 순위형을 생성하고자 한다면 3장에서 소개했던 방법을 사용하자.

# %%
# 3장에서 정의된 ordered()
#def ordered(categories):
#    #print(categories)
#    from pandas.api.types import CategoricalDtype
#    return CategoricalDtype(categories=categories, ordered=True)
from mypack.utils import ordered
pd.Series(['Alpha', 'Beta', 'Alpha', np.nan, None], 
          dtype=ordered(['Charley', 'Beta', 'Alpha']), 
          index=list('abcde'))

# %% [markdown]
# `pandas` 공식 문서에서는 다음과 같은 방법을 제시한다.

# %%
from pandas.api.types import CategoricalDtype
x = pd.Series(['Alpha', 'Beta', 'Alpha', np.nan, None], 
            dtype=CategoricalDtype(
                categories = ['Charley', 'Beta', 'Alpha'],
                ordered = True), 
            index=list('abcde'))
x

# %% [markdown]
# 다른 사람의 소스코드를 읽을 때에는 기억해 둘 필요가 있다. 

# %%
x.dtype

# %% [markdown]
# 범주형의 `dtype`은 다른 `dtype`(예. `dtype('int8')`, `dtype('float')` 등)과 달리 상당히 길다.

# %%
y = np.array([1,2,3])
y.dtype

# %% [markdown]
# 두 범주형 데이터의 `dtype`이 같으려면, 범주가 같아야 하고, 그리고 순위형이라면 순위도 같아야 한다. 다음을 보자. 

# %%
from mypack.utils import ordered, unordered

# %%
import numpy as np
import pandas as pd

# %%
u1 = pd.Series(['c', 'b', 'b', 'a'], dtype=ordered(['a', 'b', 'c']))
u2 = pd.Series(['c', 'b', 'b', 'a', 'c', 'a'], dtype=ordered(['a', 'b', 'c']))
u3 = pd.Series(['c', 'b', 'b', 'a'], dtype=ordered(['c', 'b', 'a'])) 
u4 = pd.Series(['c', 'b', 'b', 'a'], dtype=ordered(['a', 'b']))
x1 = pd.Series(['c', 'b', 'b', 'a'], dtype=unordered(['a', 'b', 'c']))
x2 = pd.Series(['c', 'b', 'b', 'a', 'c', 'a'], dtype=unordered(['a', 'b', 'c']))
x3 = pd.Series(['c', 'b', 'b', 'a'], dtype=unordered(['c', 'b', 'a']))
x4 = pd.Series(['c', 'b', 'b', 'a'], dtype=unordered(['a', 'b']))

# %%
u1.dtype, u2.dtype, u3.dtype, u4.dtype

# %%
x1.dtype, x2.dtype, x3.dtype, x4.dtype

# %%
u1.dtype == u2.dtype, u1.dtype == u3.dtype, u1.dtype == u4.dtype, \
u2.dtype == u3.dtype, u2.dtype == u4.dtype, u3.dtype == u4.dtype

# %% [markdown]
# 순위형 데이터타입(`dtype`)의 경우는 **범주와 순위**가 모두 같아야 데이터 타입이 같다. 

# %%
u1.dtype == ordered(['a', 'b', 'c'])

# %%
x1.dtype == x2.dtype, x1.dtype == x3.dtype, x1.dtype == x4.dtype, \
x2.dtype == x3.dtype, x2.dtype == x4.dtype, x3.dtype == x4.dtype

# %% [markdown]
# 위의 결과를 보면 범주형의 경우 **범주의 순서는 상관없다**는 것을 확인할 수 있다.[^cat]
#
# [^cat]: 예외적으로 모든 범주형 dtype은 "category" 또는 `CategoricalDtype(None, ordered=False)`와 `==`이다.

# %%
x1.dtype

# %%
x1.dtype == "category", x2.dtype == "category", x3.dtype == "category", x4.dtype == "category"

# %%
x1.dtype == 'cat'

# %%
from pandas.api.types import CategoricalDtype

# 판다스 공식 문서에 따르면 다음의 등호도 모두 True라고 하지만,
x1.dtype == CategoricalDtype(None, ordered = False), \
x2.dtype == CategoricalDtype(None, ordered = False), \
x3.dtype == CategoricalDtype(None, ordered = False), \
x4.dtype == CategoricalDtype(None, ordered = False)


# %%
x1.dtype

# %%
pd.__version__

# %% [markdown]
# ## 범주형의 중요성

# %% [markdown]
# 범주형은 데이터 분석에서 중요한 역할을 한다. 특히 어떤 변수가 범주형이냐 연속형이냐에 따라 분석 결과가 판이하게 달라질 수도 있다. 다음의 데이터에서 변수 `x`에는 `1`,`2`,`3` 중 하나의 값이 들어있다. 변수 `x`를 연속형으로 취급할 때와 범주형으로 놓고 분석할 때의 분석 결과를 비교해보자. 

# %%
n = 30
#x <- sample(1:3, n, replace=TRUE); x
import numpy as np
import pandas as pd

x = np.random.random_integers(1,3,n)
x # 1부터 3까지의 정수 중 하나를 무작위로 추출한다(총 30개).
# x = np.random.choice([1,2,3], n) 로도 가능하다.


# %%
#y <- ifelse(x>2, x + rnorm(n), rnorm(n)-x)
y = np.where(x > 2, x + np.random.normal(0,1,n), np.random.normal(n)-x)
# y를 생성한다.


# %%
y

# %%
dat = pd.DataFrame({'x':x, 'y':y}) 
# x, y로 구성된 데이터프레임을 만든다.

# %% [markdown]
# 우선 데이터를 시각화 보면 다음과 같다.

# %%
dat.plot(x='x', y='y', kind='scatter')
# * matplotlib.pyplot을 사용한다면 다음과 같다.
# import matplotlib.pyplot as plt
# plt.scatter(x, y)
# * 다음과 같이 상자 그림도 그려보자.
# dat.boxplot(by='x', column='y', grid=False)
# import seaborn as sns
# sns.boxplot(x="x", y="y", data=dat, width=0.5)
# plt.show()

# %% [markdown]
# 이제 변수 `x`를 연속형으로 취급하면서 회귀분석을 해보자.

# %%
from statsmodels.formula.api import ols

# %%
mod = ols("y ~ x", data = dat)
res = mod.fit()
print(res.summary())

# %% [markdown]
# 분석결과에 따르면 `x`가 1 증가할 때, y의 평균은 11.6 감소하는 것으로 나온다.

# %% [markdown]
# 만약 변수 `x`를 범주형으로 취급한다면(아래 `C(x)`는 **C**ategorical의 **C**인 듯 하다) 분석 결과는 다음과 같다.

# %%
mod = ols("y ~ C(x)", data = dat)
res = mod.fit()
print(res.summary())

# %% [markdown]
# 범주 `1`에서 범주 `2`로 바뀔 때 예상되는 `y` 평균의 감소는 1, 범주 `1`에서 범주 `3`으로 바뀔 때 예상되는 `y`의 평균 감소 25.65로 추정되었다. 위의 분석결과와 어떻게 다른지 생각해보자. 만약 `x`가 이미 범주형이라면면 `C(x)`로 쓰지 않아도 된다.

# %%
#dat = pd.DataFrame({'x2':pd.Categorical(x), 'y':y})
dat['x2'] = pd.Categorical(dat['x'])

# %%
mod = ols("y ~ x2", data = dat)
res = mod.fit()
print(res.summary())

# %% [markdown]
# ## 데이터 전처리에 있어 범주형

# %% [markdown]
# 판다스 시리즈를 조작할 때 `dtype`이 범주형이라면 좀더 유의해야 한다. 다음의 예를 보자. 

# %%
x = pd.Series([1,2,3,2])
x[4] = 5 # dtype('int64')에서는 추가가 어렵지 않다
x

# %% [markdown]
# 만약 범주형이라면?

# %%
s = pd.Series(['a', 'b', 'b', 'a'], dtype='category')
s[4] = 'b' # 하지만 dtype이 object로 바뀜
s

# %% [markdown]
# 범주형(`dtype='category'`)에서 새로운 범주를 추가하자 `dtype`이 `object`으로 바뀌었다. 원한다면 `s.astype('category')`로 다시 범주형으로 돌려 놓을 수 있지만, 왜 그럴까?

# %%
s = s.astype('category')
s

# %% [markdown]
# 추가되는 원소의 타입을 확인해 볼 필요가 있다.

# %%
type('b')

# %% [markdown]
# 위의 dtype `int64`에서도 마찬가지 현상을 확인할 수 있다.

# %%
x[5] = 1.2
x

# %% [markdown]
# 역시 dtype이 `float64`로 변경되었다.

# %% [markdown]
# 그렇다면 이제 dtype을 보존하면서 새로운 원소를 추가하려면 어떻게 해야 할까? 복잡해보이지만 `pd.concat()`을 활용하면 다음과 같다.

# %%
pd.concat([s, pd.Series(['b'], dtype=unordered(['a', 'b']))])

# %% [markdown]
# 이때 추가하는 시리즈의 dtype에 유의해야 한다. 동일한 dtype끼리 합칠 때에는 dtype에 변화가 없다. 하지만 그렇지 않다면?

# %%
pd.concat([s, pd.Series(['b'], dtype=unordered(['b']))])

# %% [markdown]
# 범주가 많건 적던 dtype이 다르다면 dtype은 `object`로 변경된다. 물론 `.astype('category')`로 다시 범주형으로 변환할 수 있다.

# %% [markdown]
# ## 범주형 다루기

# %% [markdown]
# 위에서 확인했듯이 범주형 dtype은 다른 dtype과 조금 다른 부분이 있다. 일단 가능한 범주가 다른 범주형은 다른 dtype으로 취급된다. 여기서는 범주형 dtype을 관리하는 여러 방법을 안내한다. 주요 내용은 다음과 같다.
#
# 1. 범주 추가하기 : `.add_categories()`
# 2. 범주 삭제하기 : `.remove_categories()`, `.remove_unused_categories()`
# 3. 범주 이름 바꾸기 : `.rename_categories()`
# 4. 범주 순서 바꾸기 : `.reorder_categories()`, `.set_categories()`
# 5. 범주 합치기
#

# %% [markdown]
# 먼저 메쏘드 이름에서 그 기능을 충분히 유추할 수 있는 경우부터 살펴보자. 범주를 추가하거나(`.add_categories()`), 범주를 삭제하고(`.remove_categories()`), 사용되지 않는 범주를 삭제하는(`.remove_unused_categories()`)는 메쏘드를 사용해보자.

# %%
# x = pd.Categorical(['b', 'a', 'b', 'b'], dtype=CategoricalDtype(['a', 'b', 'c'], False))
x = pd.Categorical(['b', 'a', 'b', 'b'], dtype=unordered(['a', 'b', 'c']))
# y = pd.Series(['b', 'a', 'b', 'b'], dtype=CategoricalDtype(['a', 'b', 'c'], False))
y = pd.Series(['b', 'a', 'b', 'b'], dtype=unordered(['a', 'b', 'c']))
x, y

# %%
x2 = x.add_categories(['d', 'e'])
x2

# %%
y.add_categories(['d', 'e'])

# %% [markdown]
# `pd.Categorical()`에도 사용 가능하고 `pd.Series()`에 대해서도 dtype이 범주형이라면 `.cat`을 통해 사용가능하다.

# %%
y2 = y.cat.add_categories(['d', 'e'])
y2

# %% [markdown]
# 추가를 했으니 다시 삭제해보자.

# %%
x2.remove_categories(['d', 'e']), y2.cat.remove_categories(['d', 'e'])

# %% [markdown]
# 사용되지 않는(데이터에 존재하지 않는) 범주를 삭제하려면 다음과 같다.

# %%
x.remove_unused_categories(), \
y.cat.remove_unused_categories()

# %% [markdown]
# 범주 이름을 바꿀 때는 딕을 사용해서 바꾸기 전 이름과 바뀐 후 이름을 대응해 준다. 'a'를 'Alpha', 'b'를 'Big'으로 바꿔보자.

# %%
x.rename_categories({'a':'Alpha', 'b':'Beta'}), \
y.cat.rename_categories({'a':'Alpha', 'b':'Beta'})

# %% [markdown]
# 범주의 순서를 바꾸기 위해서는 `.reorder_categories()`와 `.set_categories()`를 사용할 수 있다. `.reorder_categories()`의 경우 기존의 범주를 재배치(`reorder`)하여 순서를 결정한다. 기존의 범주가 빠지거나, 새로운 범주가 추가될 수 없다. 반면 `.set_categories()`는 범주를 새롭게 지정하면서 순서까지 바꾼다. 기존의 범주가 빠지거나 새로운 범주가 추가될 수도 있다.

# %%
x.reorder_categories(['c', 'b', 'a']) # 원래 순서는 ['a', 'b', 'c']
y.cat.reorder_categories(['c', 'b', 'a'])

# %%
x.set_categories(['c', 'b', 'a']),
y.cat.set_categories(['c', 'b', 'a'])

# %% [markdown]
# 이제 범주 `a`를 빼고, `d`를 추가해보자.

# %%
x.set_categories(['b', 'c', 'd']), \
y.cat.set_categories(['b', 'c', 'd'])

# %% [markdown]
# 삭제된 범주였던 곳은 `np.nan`이 되었음을 확인하자.

# %% [markdown]
# ### 범주 합치기
#
# * https://stackoverflow.com/questions/63067496/how-do-i-assign-other-to-low-frequency-categories-pandas
# * https://stackoverflow.com/questions/39099217/pandas-reduce-number-of-categorical-variables-in-value-counts-tabulation

# %%

# %%
s

# %%
# #차선책?
fac2 = pd.Categorical(['b'])
pd.concat([pd.Series(fac1), pd.Series(fac2)]) # 그냥 [fac1, fac2] 해도 안 된다.
# pd.concat은 pd.Series나 pd.DataFrame만 concat한다.
# 역시 dtype = object

# %%
# pandas doc에서 추천하는 방법
pd.concat([pd.Series(fac1), pd.Series(fac2)]).astype('category')

# %%
# 다른 방법
pd.Series(fac1.tolist() + ['b'], dtype='category')

# 이상적인 방법? category를 합치고, codes도 합치고

# %%
type(fac1)

# %%
isinstance(type(fac1), pd.Categorical)

# %%
fac1 = pd.Series(fac1) # 이건 Series의 경우
# type이 Series이고 dtype이 category인 경우와,
# type이 pandas.core.arrays.categorical.Categorical인 경우가 있다!
# 결국은 array?

# %%
type(fac1)

# %%
fac1

# %%
fac1[4] = 'b' # 데이터가 추가되거나,

# %%
fac1

# %%
fac1 = pd.Series(pd.Categorical(['a', 'b', 'b', 'a']))

# %%
fac1[5] = 'c' # 새로운 category가 추가되면 dtype이 object로 바뀐다.

# %%
fac1

# %%
np.array(fac1) # array로 변환하면, dtype이 object로 변환되는 듯이 아니라, levels(categories)에 따라 적절히 변환되는 듯

# %%
np.array(pd.Categorical([1,2,1,1,3,5]))

# %%
from mypack.utils import c

# %%
c(pd.Categorical([1,2,1,1,3,5])) # 흠...

# %%
# pd.Series의 경우, categorical한 dtype이 있으므로,
# dtype만 보존해준다면?

# %%
fac1 = pd.Categorical(['a', 'b', 'b', 'a'])
type(fac1), fac1.dtype
# array와 array의 dtype?

# %%
s1 = pd.Series(fac1)
type(s1), s1.dtype  # dtype은 array와 Series가 같다

# %%
fac1.categories.dtype

# %%
type(fac1.categories), fac1.categories.dtype  # index로 하면 array로 할 때보다 장점이???

# %%
pd.Series(fac1, dtype=fac1.categories.dtype)

# %%
fac_num = pd.Categorical([1,2,1,1,3,5])

pd.Series(fac_num, dtype=fac_num.categories.dtype) # R의 경우 levels는 모두 character인데 반해, python은 다르다!

# %%
# All instances of CategoricalDtype compare equal to the string 'category'
# 자기 마음대로 '==' 연산을 정의할 수 있는 듯. ???? 무슨 말?

# %%
fac1 = pd.Series(fac1)

# %%
fac1.append('a')

# %%
fac1.append(pd.Series('a'))

# %%
fac_num = pd.Categorical([1,2,1,1,3,5])
fac2 = np.concatenate([fac1, pd.Categorical(['a'])])
fac2 # 결과가 pd.Categorical이 아니라 np.array임을 유의하자

# %%
fac2 = pd.Categorical(np.concatenate([fac1, pd.Categorical(['a'])]))
fac2

# %%
type(fac2), fac2.dtype

# %%
#??? 정말 이게 최선?

# %%
#원소 하나가 되었던, 여럿이 되었던 문제는,
#코딩이 다를 수 있다는 것. 
#따라서 먼저 코딩을 맞춰줘야 한다?

# %%

# %%
# #?fac1.add_categories
# remove_categories, remove_unused_categories, rename_categories, reorder_categories

# %%
#dir(fac1)

# %%
pd.Categorical(fac2)

# %%
fac2 = np.pad(fac1, (0,1), mode='constant', constant_values='a')
# fac1에서 왼쪽에 0개, 오른쪽에 1개의 constant(상수) 'a'를 덧붙여라!
fac2

# %%
#https://stackoverflow.com/questions/12668027/good-ways-to-expand-a-numpy-ndarray
#에 따르면, np.concatenate이 np.pad보다 훨씬 빠르다.


# %%
#fac1[6] <- 'c'
#fac1
fac2 = np.concatenate([fac2, pd.Categorical(['c'])])
fac2 


# %%
pd.Categorical(fac2)

# %%
#fac1
#fac2 <- factor(c('a', 'b', 'c', 'c', 'b'))
#c(fac1, fac2)
fac1

# %%
fac2 = pd.Categorical(['a', 'b', 'c', 'c', 'b'])
pd.Categorical(np.concatenate([fac1, fac2]))

# %%
help(pd.Categorical)

# %%
fac1 = pd.Categorical(['a', 'b', 'c', 'b', 'a'])
fac2 = pd.Categorical(['b', 'a', 'b', 'c', 'c'], categories=['c', 'b', 'a'])
pd.Categorical(np.concatenate([fac1, fac2]))

# %%
fac1 = factor(c('a', 'b', 'c', 'b', 'a'))
fac2 = factor(c('b', 'a', 'b', 'c', 'c'), levels = c('c', 'b', 'a'))



# %%
#str1 <- c('a', 'b', 'b', 'a')
#str1[5] <- 'c'
#str1
#str2 <- c('a', 'd', 'd', 'c')
#c(str1, str2)
str1 = pd.Series(['a', 'b', 'b', 'a'])
str1[5] = 'c'
# pd.Series는 np.array나 pd.Categorical과 달리 원소를 바로 추가할 수 있다!

# %%
#str1
#str2 <- c('a', 'd', 'd', 'c')
#c(str1, str2)
str2 = pd.Series(['a', 'd', 'd', 'c'])


# %%
str2 = str1.append(str2)
str2

# %%
x = pd.Categorical(['a', 'b', 'c', 'c'])
y = pd.Categorical(['b', 'c', 'd', 'd', 'a'])
pd.Categorical(x.to_list()+ y.to_list())

# %%
pd.Series(x) # dtype: category

# %%
pd.Series(x).append(pd.Series(y))  # 결과는 dtype:object

# %%
## 어떻게 합칠 것인가?
# https://stackoverflow.com/questions/45639350/retaining-categorical-dtype-upon-dataframe-concatenation

# %%
pd.Categorical(np.concatenate([x.to_numpy(), y.to_numpy()]))

# %% [markdown]
# # 7.3 `forcats` 패키지


# %%

# %%
#install.packages("forcats")

# %%
#library(forcats)
#x
#fct_relevel(x, '3', '2', '1')
x = np.random.choice([1,2,3], n)

# %%
x = pd.Categorical(x, categories=[1,2,3], ordered=True)
x

# %%

# %%
dir(x)
# .rename_categories()
# .as_ordered(), as_unordered()
# .reorder_categories(), .add_categories(), remove_categories(), remove_unused_categories()


# %%
s = pd.Series(x)

# %%
s

# %%
dir(s)
# .astype, .reorder_levels, swaplevel

# %%
# 헷갈릴만한 attribute?
set(dir(s)).intersection(set(dir(x)))

# %%
# s.swaplevel() # for multi-index

# %%
s

# %%
help(s.values.as_ordered)  

# %%
type(s), s.dtype

# %%
s.values.as_ordered(inplace=True)  # category의 순서를 지정하려면?

# %%
s.values.categories # 여기에는 ordered 정보가 나와 있지 않다.

# %%
s.values.ordered # 

# %%
# Series의 경우 one layer를 까야?
# Series의 경우, .values와 .cat

# %%
s.cat.ordered

# %%
s.cat.as_unordered().cat.as_ordered().head()

# %%
s.cat.reorder_categories([2,3,1]).cat.as_unordered().cat.as_ordered().head() 
# !!! unordered 되기 전의 order을 보존하고 있음!

# %%
# 뭔가 그림 하나로 정리를 해야 할 듯...


# %%
help(s.cat) 
# s.cat.categories, 
# s.cat.rename_categories(),
# s.cat.reorder_categories(),
# s.cat.add_categories(),
# s.cat.remove_categories(),
# s.cat.set_categories(),
# s.cat.as_ordered(),
# s.cat.as_unordered(),


# %%
s.head()

# %%
c2 = pd.Categorical(['a', 'c', 'd', 'c', 0, 'd', 0], categories = ['a', 'c', 'd', 0], ordered = True)

# %%
s2 = pd.Series(c2)

# %%
s2.astype('category') # ordered는 보존됨!

# %%

# %%
from pandas.api.types import CategoricalDtype # CategoricalDtype은 뭐 하는 놈?
s2.astype(CategoricalDtype(ordered = False)) # 이것도 가능!!!
# https://opensource.com/article/18/4/python-datetime-libraries
# 

# %%
s2.cat.as_ordered() 
# 그냥 이렇게 해도 되는데 왜 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#sorting-and-order
# 에서는 어렵게 풀었을까?

# 참고 문헌 : https://stackoverflow.com/questions/45639350/retaining-categorical-dtype-upon-dataframe-concatenation

# 그 밖에 : https://realpython.com/python-time-module/
# https://stackabuse.com/converting-strings-to-datetime-in-python/
# https://docs.astropy.org/en/stable/time/index.html

# %%
s2.cat.as_unordered()

# %%

# %%
# How about ??? categories가 보존되는가?
ordered = CategoricalDtype(ordered = True)
unordered = CategoricalDtype(ordered = False)
s2.astype(unordered)



# %%
x = pd.Categorical([1,2,3])

# %%
x.astype()


# %%
def as_unordered(x):
    return 


# %%
dir(s2)

# %%
s2

# %%
s.astype('category')

# %%
s.dtype

# %%

# %%
x.reorder_categories([3,2,1])

# %%
fac2

# %%
fac2.categories

# %%

# %%
# ?fac2.reorder_categories
# `new_categories` need to include all old categories and no new category items.

# %%
#fct_relevel(fac2, "b", "a")
fac2.reorder_categories(['b','a'] + list(set(fac2.categories) - set(['b', 'a']))) 
# 하지만 set으로 하면 순서가 바뀔 텐데?
#???!!!
# 참고자료? https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html

# %%
def swap_cate_order(fac, level1, level2, inplace=False):
    lst = fac.categories.to_list()

    #index1 = lst.index("a")
    index1 = lst.index(level1)
    #index2 = lst.index("b")
    index2 = lst.index(level2)

    lst[index1], lst[index2] = lst[index2], lst[index1]
    
    if inplace:
        fac.categories = lst
    else:
        fac2 = fac.copy()
        fac2.categories = lst
        return fac2



# %%
fac2.categories

# %%
swap_cate_order(fac2, 'c', 'a') # category order만 바꾼다는 뜻


# %%
#x <- factor(unlist(strsplit(
#  'wzwzzwzwzcczwzdzczwzwzdzdddzdyydddddwzwwwdddzzddddzdzzd',''
#)))
x = pd.Categorical(list('wzwzzwzwzcczwzdzczwzwzdzdddzdyydddddwzwwwdddzzddddzdzzd'))

# %%
#table(x)
pd.crosstab(1, x)

# %%
s = pd.Series(x)
s.value_counts()

# %%
s.value_counts().index.values

# %%
#x <- fct_infreq(x)
x = x.reorder_categories(s.value_counts().index.values.to_list())
#s.value_counts().index.values까지만 하면 s categories의 순서가 그대로 지정된다

# %%
#table(x)
x.categories

# %%
pd.crosstab(1, x)

# %% [markdown]
# # 7.3.2

# %%
# dog=개, zebra=얼룩말, whimbrel=중부리도요, catfish = 메기, yak=야크
#x2 <- fct_recode(x, 
#                 "dog"="d", "zebra"="z", "whimbrel"="w",
#                 "catfish"="c", "yak"="y")
x2 = x.rename_categories({'d':'dog', 'z':'zebra', 'w':'whimbrel', 'c':'catfish', 'y':'yak'}) # '옛 이름':'새 이름'
x2
# ???python이 argument를 받는 방식에 대한 이해?

# %%

# %%
#x3 <- fct_collapse(x2, 
#                   "mammals"=c("dog", "zebra", "yak"),
#                   "birds"="whimbrel",
#                   "fish"="catfish")
#x3 = x2.rename_categories({'dog':'mammals', 'zebra':'mammals', 'yak':'mammals', 'whimbrel':'birds', 'catfish':'fish'})
# ERROR : categories must be unique

x2.categories


# %%

# %%
x2.codes

# %%
typ = type(cat_lump(y))

# %%
typ(['a'])

# %%
dtyp = cat_lump(y).dtype

# %%
dtyp

# %%
dtyp.categories

# %%
dtyp.categories=['a', 'b', 'c']


# %%
# https://towardsdatascience.com/staying-sane-while-adopting-pandas-categorical-datatypes-78dbd19dcd8a

# %%
# 하지만 아래 코드가 데이터에 존재하지 않는 categories도 합치는가?
# 합쳐지겠군. 어짜피 데이터에 없으니, 이 데이터로 pd.Categorical를 한다면,

def condense_category(col, min_freq=0.01, new_name='other'):
    series = pd.value_counts(col)
    mask = (series/series.sum()).lt(min_freq)
    return pd.Series(np.where(col.isin(series[mask].index), new_name, col))

def cat_lump(col, min_freq=0.1, new_name='other'):
    typ = type(col)
    
    ###???!!! 아마 codes와 categories를 따로 활용해야???!!!
    ### 이게 제대로 작동하는가? 아닌가?
    series = pd.value_counts(col)
    mask = (series/series.sum()).lt(min_freq)
    #return pd.Categorical(np.where(col.isin(series[mask].index), new_name, col))
    x = np.where(col.isin(series[mask].index), new_name, col)
    return typ(x, dtype=dtyp)

# 그런데, 기존의 category와 새로운 category를 연결하는 정보를 생산해야 할 듯
# 만약 min_freq보다 빈도가 작은 범주가 단 하나라면? 굳이 others라고 할 필요가 없지 않나?

# others의 범주를 모두 합해서 특정한 비율 아래로 맞추려면???
def cat_lump2(col, min_freq=0.1, new_name='other'):
    ###???!!! 아마 codes와 categories를 따로 활용해야???!!!
    ### 이게 제대로 작동하는가? 아닌가?
    
    ### 만약 new_name이 기존의 categories 이름에 속한다면?
    cat1 = col.categories
    series = pd.value_counts(col)
    
    r = series/series.sum()
    if (r < min_freq).sum() <2:
        return col, {x:x for x in cat1}
    else:

        mask = (r).lt(min_freq)
        y = pd.Categorical(np.where(col.isin(series[mask].index), new_name, col))
        cat2 = y.categories

        lumped_cat = set(cat1) - set(cat2)
        dic_categories = {}
        for cat in set(cat1)-set([new_name]):
            dic_categories[cat] = cat
        for cat in lumped_cat:
            dic_categories[cat] = new_name

        return y, dic_categories


# %%
cat_lump(y)

# %%
np.random.randint(1,3,10)

# %%
cat_lump(pd.Categorical(np.random.randint(1,10,100)))

# %%
cat_lump(pd.Categorical(np.random.randint(1,10,100))).value_counts()

# %%
condense_category(y)

# %%
condense_category(x)

# %%
x2.value_counts()/len(x2)

# %%
cat_lump2(x2, min_freq=0.05)[0].value_counts()

# %%
cat_lump2(x2, min_freq=0.06)[0].value_counts()

# %%
type(x2)

# %%

# %%
pd.Categorical(condense_category(x2, min_freq=0.))

# %%
pd.Categorical(condense_category(x2, min_freq=0.1))

# %%
x4 = cat_lump(x2, min_freq=0.1)
x4 

# %%
cat_lump2(x2, min_freq=0.1)

# %%
x5 = pd.Series([1,3,2,4,4,5,0,0,1,1,1,0,0,0,0,0])
x6 = condense_category(x5, min_freq=0.1, new_name = -99) # 
# 여기서 그냥 category라면 
# 굳이 condense_category를 쓸 필요가 있나? 이런 기능을 하는 함수가 있을 듯
x6

# %%
x = pd.Series(pd.Categorical(['a', 'b']))
x

# %%
pd.Series(['a', 'b'], dtype='category')

# %%
type(x)  

# %% [markdown]
# # 7.3.3

# %%
fac1

# %%
fac2

# %%
fac1
fac2
c(fac1, fac2) # R처럼 np.array로 바뀜.


# %%
pd.concat([pd.Series(fac1), pd.Series(fac2)]) # pd.concat은 categories를 보존한다


# %%
type(pd.concat([pd.Series(fac1), pd.Series(fac2)]))

# %%
#fct_c(fac1, fac2)
# #??????


# %%
def fct_c(fac1, fac2):
    return pd.Categorical(pd.concat([pd.Series(fac1), pd.Series(fac2)]))


# %%
pd.Categorical(pd.concat([pd.Series(fac1), pd.Series(fac2)]))

# %%
type(pd.Categorical(pd.concat([pd.Series(fac1), pd.Series(fac2)])))

# %%
fac1 = pd.Categorical(['a', 'b', 'c'])
fac2 = pd.Categorical(['a', 'b'])

# %%
fct_c(fac1, fac2)

# %%




# %%

# %%

# %% [markdown]
# ## 추가할 내용?

# %%
x.value_counts()

y = pd.Categorical([2,1,1,0,2,1,2,1])
y.value_counts()

isinstance(y, pd.Series)

pd.Series.__mro__
# 이것들이 어떤 의미를 갖는가? 
# 중요한 부분은?

pd.Categorical.__mro__

set(pd.Series.__mro__).intersection(set(pd.Categorical.__mro__))

set(pd.Series.__mro__).difference(set(pd.Categorical.__mro__))

set(set(pd.Categorical.__mro__)).difference(pd.Series.__mro__)

# %%
# ### 읽어들이기

#df.to_csv('data/07_factor_00.txt', index = False)

with open('data/07_factor_00.txt', 'rt') as f:
    lns = f.readlines()
    for ln in lns:
        print(ln, end='') 

dfIn = pd.read_csv('data/07_factor_00.txt')

dfIn.info()

df.info()

dfIn2 = pd.read_csv('data/07_factor_00.txt', 
                    dtype={'커피':'category',
                           '코드':'category',
                           '숫자':int})

dfIn2.info()

# ### 변환하기

dfIn

dfIn.커피 = pd.Categorical(dfIn.커피)
#dfIn.코드 = pd.Categorical(dfIn.코드)
dfIn.코드 = dfIn.코드.astype('category')
## !!!! assingning에서 dfIn.코드 와 df['코드']가 다른 의미가 있었던 걸로?

type(dfIn.커피) # 분명 dfIn.커피 = pd.Categorical()로 했지만, type은 pd.Series로 나옴
# 데이터프레임의 한 컬럼을 categorical로 변환하면 그 컬럼은 결국 pd.Series가 된다.

# %%
df = dfIn

# %%
dfIn.info()

x0 = np.array(['까페라떼', '아메리카노', '아메리카노', '에스프레소', '까페라떼', '아메리카노', '까페라떼', '아메리카노'])
x = pd.Categorical(x0)
x

# ## 작업
# * 일반적인 작업 : CREAD
# * 새로운 작업 : 범주에 대한 작업
#     - CREAD?
#     - 모든 범주(level) 읽기
#     - 새로운 범주 생성
#     - 기존의 범주 합치기
#     - 범주 수정
#     - 기존의 범주 삭제
#     

# ## 읽기(Read)
# * `x.loc`
# * `x.iloc`

x[:-1:2]

# %%
x.loc[x == '까페라떼' | x == '에스프레소'] # AttributeError: 'Categorical' object has no attribute 'loc'

# %%
y = pd.Series(x)

y.loc[y != '까페라떼']

# ## 수정(Edit)
#

x[1] = '까페라떼'; x

y[1] = '까페라떼'; y

x[1:3] = ['아메리카노', '까페라떼']; x

y[1:3] = ['아메리카노', '까페라떼']; x

# +
# 하지만 y[1:3]은 index를 의미하는지, 아니면 순서를 의미하는지 모호하다
# y.iloc[1:3] 순번, y.loc[1:3] 인덱스
# -

y2 = y[-1::-1]

y2

y2.iloc[1:3]

y2.loc[1:3]

y2.loc[3:1] # 인덱스의 슬라이싱은 마지막을 포함한다!

# ### 일반적인 작업에서 주의할 사항?
#
# > Be aware that assigning new categories is an inplace operation, while most other operations under Series.cat per default return a new Series of dtype category. /pandas-categorical data-documentation

# ### 범주와 관련된 작업

# 모든 범주 나열
x.categories # Index가 가지는 특징???

# 새로운 범주 생성
dir(x)
x.add_categories(['카푸치노'])

x.add_categories(['카푸치노'], inplace=True)

x.add_categories(['까페모카', '플랫화이트'], inplace = True)

# 기존의 범주 합치기
rename = pd.DataFrame([('에스프레소', '커피'), 
                       ('아메리카노', '커피'),
                       ('까페라떼', '커피+우유'),
                       ('카푸치노', '커피+우유'),
                       ('까페모카', '커피+우유+초콜릿'),
                       ('플랫화이트', '커피+우유')],
                     columns = ['커피종류', '구성성분'])

# %%
import numpy as np
import pandas as pd

# %%
x

# %%
rename

# %%


pd.merge(pd.DataFrame({'커피종류':x}),
         rename, on='커피종류') # 하지만, 한번도 나타나지 않는 범주는 포함시키지 못한다

# %%
# +
# 그래서 범주가 데이터에 존재하는 경우와 그렇지 않은 경우로 나눠야 할 듯...
# 그런데 합쳐야 할 범주가 데이터에 있기도 하고, 없기도 하다면???
# https://stackoverflow.com/questions/38516664/anti-join-pandas
# anti_join같은 함수를 새로 만들어준다면?

# +
# 근데 그냥 문자열이라고 생각해보면,
# 문자열에는 나타나지 않은 문자열을 저장할 순 없다!

# 어쨋든 존재하는 문자열이라면, 이들 중 몇 개를 하나로 합치는 방법을 생각해보자.
# -

# %%
import numpy as np
import pandas as pd

ser = pd.Series(['까페라떼', '아메리카노', '아메리카노', '에스프레소', '까페라떼', '아메리카노', '까페라떼', '아메리카노'])

df = pd.DataFrame({'커피종류':ser})
df

pd.merge(df, rename, on='커피종류')

df.merge(rename, on='커피종류')

# %%
# +
#df.reset_index().merge(rename, how='left', on='커피종류', sort=False).sort('index') # 만약 컬럼 이름이 index라면?
# AttributeError: 'DataFrame' object has no attribute 'sort'
# # # ???
# https://stackoverflow.com/questions/20206615/how-can-a-pandas-merge-preserve-order
# 그런 문제로...
df.reset_index().merge(rename, how='left', on='커피종류', sort=False).sort_index().drop('index', axis=1)
# -

# %%
help(df.join)

# %%
df.join(rename, on='커피종류', how='left', sort=False)
# ValueError: You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat
df.join(rename.set_index('커피종류'), on='커피종류', how='left', sort=False)
# df.join(B)는 기본적으로 index-on-index merge
# 만약 다른 컬럼을 기준으로하려면 on이나 .reset_index()를 활용하자.

# %%
help(df.update)
# Modify in place using non-NA values 

# %%
df

# %%
df2 = df.copy()

# %%
rename

rename.rename({'커피종류':'커피종류0', '구성성분':'커피종류'}, axis=1)
# rename의 경우 해당하는 index 이름이 없어도 별다른 error 또는 warning이 발생하지 않으므로 주의해야 한다.

# %%
df2.update(rename.rename({'커피종류':'커피종류0', '구성성분':'커피종류'}, axis=1), 
           join = 'left', 
           overwrite = True)
# 그런데 이건 join과 다른 개념인 듯...
# 그런데 그냥 overwrite한다면, 굳이? 그냥 concat을 하는게???

# %%
# +
# 그런데 비슷비슷한 함수들이 많음
# pd.merge, join, merge_ordered, update, pandas DataFrame documentation을 보는 게 나을 수도...?
# -

# %%

# %%

# %%

# %%
# error message에서 traceback을 생략하는 방법?
import sys

sys.tracebacklimit = 0

# %%

# %% [markdown]
# ## R과의 차이점

# %%

# %%
# pandas.core.series.Series

df[['group']] # R에서는 [[]]를 쓰면 내부로 들어가는데...
# python에서는 df[[]]는 DataFrame


# %%

# %%

# %%

# %% [markdown]
# # @@@@@@@@@@@@@@@@@@@
#
# !! levels -> categories로 변경

# %%
def factor(values, categories=None, ordered=None, dtype=None, fastpath=False, copy=True, **kwargs):
    if 'levels' in kwargs:
        if categories is not None:
            raise ValueError("use either levels or categories")
        else:
            return pd.Categorical(values, categories=kwargs['levels'], ordered=ordered, dtype=dtype, fastpath=fastpath, copy=copy)
    else:
        return pd.Categorical(values, categories=categories, ordered=ordered, dtype=dtype, fastpath=fastpath, copy=copy)
    


# %%
factor(c('High', 'Medium', 'Low', 'Medium', 'Low'), levels = c('Low', 'Medium', 'High'), ordered = True)

# %%
# 
#factor(c('High', 'Medium', 'Low', 'Medium', 'Low'), levels = c('Low', 'Medium', 'High'), ordered = True)
factor(c('High', 'Medium', 'Low', 'Medium', 'Low'), categories = c('Low', 'Medium', 'High'), ordered = True)

# %%
factor(c('High', 'Medium', 'Low', 'Medium', 'Low'), categories = c('Low', 'Medium'))


# %%

# %%
# R
#factor(x = character(), levels, labels = levels,
#            exclude = NA, ordered = is.ordered(x), nmax = NA)
# R에서는 levels를 labels로 바꾼다.

def factor(values, categories=None, ordered=None, dtype=None, fastpath=False, copy=True, **kwargs):
    if 'levels' in kwargs:
        if categories is not None:
            raise ValueError("use either levels or categories")
        else:
            x = pd.Categorical(values, categories=kwargs['levels'], ordered=ordered, dtype=dtype, fastpath=fastpath, copy=copy)
    else:
        x = pd.Categorical(values, categories=categories, ordered=ordered, dtype=dtype, fastpath=fastpath, copy=copy)
    if 'labels' in kwargs:
        map_labels = {x:y for x,y in zip(kwargs['levels'], kwargs['labels'])}
        return x.map(map_labels).astype('category')
    else:
        return x



# %%
def factor(x, levels = None, ordered = None):
    return pd.Categorical(x, categories=levels, ordered = ordered)


# %%
factor(c('High', 'Medium', 'Low', 'Medium', 'Low'), levels = c('Low', 'Medium', 'High'), ordered = True)


# %%
#class(x)
type(x)
# pd.Categorical(..., ordered = True)도 type은 같다.

# %%
# ordered인지 확인하기
x.ordered

# %%
x.categories  # categories만 가지고는 순위형 자료인지에 대한 확인은 불가하다.

# %%
pd.core.arrays.categorical.Categorical.levels = pd.core.arrays.categorical.Categorical.categories

# %%
x.levels


# %%
def levels(x):
    if isinstance(x, pd.Series):
        print('* For python way: use x.cat.categories')
        return x.cat.categories
    elif isinstance(x, pd.Categorical):
        print('* For python way: use x.categories')
        return x.categories


# %%
x

# %%
levels(x)

# %%
# how to find inner structure of an instance x
set(dir(pd.Categorical)) - set(dir(x))

# %%
x.to_list()

# %%
x.tolist() # 차이???

# %%
x.to_list

# %%
x.tolist

# %%
x.to_list is x.tolist

# %%
x.to_list == x.tolist

# %%
set(dir(x)) - set(dir(pd.Categorical))
# 이들 중 뭐가 inherit된 것인가?

# %%
pd.Categorical.levels   # https://www.daleseo.com/python-property/

# %%

# %%
pd.Categorical.levels # 지금 Class 이름을 써서 <property ... >로 나옴

# %%
x = pd.Categorical(['a', 'b', 'a', 'a', 'c'])
x.levels  # 구체적인 instance에서는 

# %%
# What is python class property
# https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute/7377013
for x in dir(pd.Categorical):
    if isinstance(getattr(pd.Categorical, x), property):
        print(x)


# %%
import inspect
## _codes, _constructor, categories, codes, dtype, levels, nbytes, ordered

## source of property getter
print(inspect.getsource(pd.Categorical.categories.fget))
# return self.dtype.categories

print(inspect.getsource(pd.Categorical.codes.fget))
        # v = self._codes.view()
        # v.flags.writeable = False
        # return v




x= factor(c('High', 'Medium', 'Low', 'Medium', 'Low'), levels = c('Low', 'Medium', 'High'), ordered = True)
x.dtype
x.dtype.categories


# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
import pandas as pd
factor = pd.Categorical
x = factor(c('A', 'B', 'A', 'C', 'B'))
x


# %%

# data structure : categories, codes(-1(missing), 0, 1, 2, ...)

# 어떤 연산이 가능한가?
# * .as_ordered() : .min(), .max()
#                   근데 .sort() 안 됨...
#
df = pd.DataFrame({"value": np.random.randint(0, 100, 20)})
labels = ["{0} - {1}".format(i, i + 9) for i in range(0, 100, 10)]
df["group"] = pd.cut(df.value, range(0, 105, 10), right=False, labels=labels)
df.head(10)


# %%
df['group'].cat.categories


# %%
df['group'].cat.codes


# %%
pd.cut(df.value, range(0,100,10))


# %%
#class(x)
type(x)


# %%
#x <- ordered(c('High', 'Medium', 'Low', 'Medium', 'Low'), 
#             levels=c('Low', 'Medium', 'High'))
x = pd.Categorical(['High', 'Medium', 'Low', 'Medium', 'Low'], \
                   categories = ['Low', 'Medium', 'High'], \
                   ordered=True)
x

# %%

# %%

# %% [markdown]
# ## 회귀분석 : `sklearn.linear_model` 사용

# %%
#lm(y ~ x)
# #%conda install scikit-learn -c conda-forge

import sklearn


# %%
from sklearn import linear_model 

# %%
regr = linear_model.LinearRegression()

# %%
regr.fit(x.reshape(-1,1), y.reshape(-1,1))
regr.coef_, regr.intercept_

# %%
regr.get_params()

# %%
x = pd.Categorical(x)

# %%
x

# %%
#x <- as.factor(x)
# pd.get_dummies() = sklearn.preprocessing.OneHotEncoder
x_dummies = pd.get_dummies(x, prefix='x', drop_first=True)

# %%
x_dummies.head()

# %%
regr.fit(x_dummies, y.reshape(-1,1))
regr.intercept_, regr.coef_
