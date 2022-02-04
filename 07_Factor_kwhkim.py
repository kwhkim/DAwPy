# -*- coding: utf-8 -*-
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
# 참고로 이렇게 `x.categories`와 `x.codes`로 분리 저장된 내용을 다시 합치고 싶다면 `np.asarray(x)`를 한다.

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
# `x.as_ordered()`를 하면 새로운 객체가 생성되고, `x.as_ordered(inplace=True)`를 하면 `x`가 바로 변환된다. (결과만 보면 `x=x.as_ordered()`와 같다.) # 바로 반환된다는 것은 새로운 객체를 생성하지 않고 x 자체를 변환시킨다는 것.

# %% [markdown]
# 이때 범주 순위를 결정하기 위해서는 `.reorder_categories()`를 사용할 필요가 있다.

# %%
x.as_ordered().reorder_categories(['Charley', 'Beta', 'Alpha'])

# %% [markdown]
# 만약 `.as_ordered(inplace=True)`를 했다면, 마찬가지로 `.reorder_categories([], inplace=True)`를 해준다. 하지만 `.reorder_categories()`에서 `inplace=True`는 판다스 미래 버전에서 허용되지 않는다고 한다. 그러니 미래 판다스 버전까지 염두해 둔다면 `x=x.reorder_categories([])`가 나을 것이다.

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
# (예상했겠지만) 데이터 타입이 범주형(명목형 또는 순위형)인 판다스 시리즈는 여러 가지 방식으로 생성할 수 있다.

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
x1.dtype == 'cat' # 'category'로 적어줄 경우만 True로 출력된다. 

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

x = np.random.random_integers(1,3,n) # 현재는 다음과 같은 메세지가 출력된다: DeprecationWarning: This function is deprecated. Please call randint(1, 3 + 1) instead
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
dat.plot(x='x', y='y', kind='scatter') # 
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
# 범주가 많건 적던 dtype이 다르다면 dtype은 `object`로 변경된다. 물론 `.astype('category')`로 다시 범주형으로 변환하거나 다음과 같이 `union_categorical()` 함수를 사용할 수 있다(순위형인 경우, 범주는 같은데 순위가 다르다면 에러가 발생한다. 만약 순위를 무시하고 싶다면 `ignore_order=True`로 설정한다.)

# %%
from pandas.api.types import union_categoricals
union_categoricals([s, pd.Series(['b'], dtype=unordered(['b']))])
s
# %% [markdown]
# 한 가지 아쉬운 점은 판다스 시리즈의 경우 인덱스가 보존되지 않는다는 점이다. 결과로 시리즈가 필요하다면 다음과 같이 인덱스를 보존할 수 있다.
# s2 = pd.Series(['b'], dtype=unordered(['b']))
# pd.Series(union_categoricals([s, s2]),
#           index = s.index.union(s2))


# %% [markdown]
# ## 범주형 다루기

# %% [markdown]
# 위에서 확인했듯이 범주형 dtype은 다른 dtype과 조금 다른 부분이 있다. 일단 가능한 범주가 다른 범주형은 다른 dtype으로 취급된다. 여기서는 범주형 dtype을 관리하는 여러 방법을 안내한다. 주요 내용은 다음과 같다.
#
# 1. 범주 추가하기 : `.add_categories()`
# 2. 범주 삭제하기 : `.remove_categories()`, `.remove_unused_categories()`
# 3. 범주 이름 바꾸기 : `.rename_categories()`
# 4. 범주 순서 바꾸기 : `.reorder_categories()`, `.set_categories()`
# 5. 범주 합치기 : `from mypack.utils`, `cat_combine()`, `cat_collapse()`, `cat_collapse_cum()`
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
# 모든 범주 이름을 바꾸려면 다음과 같이 새로운 범주 이름만 리스트로 제공해도 된다.

# %%
x.rename_categories(['Alpha', 'Beta', 'Charley']), \
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

# %% [markdown]
# 범주를 합치는 방법은 판다스에서 지원하지 않는 것으로 보인다. (!!! 혹시 제3자 패키지라도 발견하게 되면 알려주세요) 다음에서 저자가 만든 함수를 소개한다.

# %%
from mypack.utils import cat_combine, cat_collapse, cat_collapse_cum

# %% [markdown]
# `cat_combine()` 함수는 범주형 데이터에서 2개 이상의 범주를 하나로 합친다. `pd.Categorical()`과 dtype이 `category`인 판다스 시리즈 모두 사용 가능하다.

# %%
import numpy as np
import pandas as pd

# %%
x0 = np.random.choice(list('abcdefg'), size=100, p=[0.6, 0.18, 0.07, 0.05, 0.05, 0.03, 0.02])

# %%
x = pd.Categorical(x0)
y = pd.Series(x0, dtype='category')

# %%
y.value_counts()

# %%
cat_combine(x, ['a', 'b'], 'c')

# %%
cat_combine(y, ['a', 'b'], 'c')

# %% [markdown]
# `cat_collapse(x, min_freq)`와 `cat_collapse(x, min_pct)`은 모두 빈도 또는 비율이 작은 범주를 하나(예. `others`)로 묶어준다.

# %%
cat_collapse

# %%
res1 = cat_collapse(x, min_pct=0.1, others='insignificant') 
# 0.1보다 작은 비율의 범주는 모두 'insignificant'로 묶는다.
res1

# %%
res2 = cat_collapse_cum(x, min_pct=0.1, others='<0.1') 
# 합쳐서 0.1보다 작은 비율의 범주는 모두 '<0.1'로 묶는다.
res2

# %% [markdown]
# 둘의 차이는 다음의 결과에서 확인할 수 있다. 아쉽게도 위의 함수들은 순위형 자료형을 적절하게 처리하지 못한다. 순위형도 명목형으로 취급한다.

# %%
x.value_counts()

# %%
res1.value_counts()/len(res1)

# %%
res2.value_counts()/len(res1)

# %%

# %%

# %%

# %%

# %% [markdown]
# #### 참고자료
#
# * https://stackoverflow.com/questions/63067496/how-do-i-assign-other-to-low-frequency-categories-pandas
# * https://stackoverflow.com/questions/39099217/pandas-reduce-number-of-categorical-variables-in-value-counts-tabulation

# %%

# %%
## 07_Factor_kwhkim.py 정리
#일단 생성
pd.Categorical()  # ordered = True, False

#먼저 R의 factor를 잘 알아야?
#아니면 일부 기능만 python으로 구현해도...


factor(c('a', 'b', 'c'), levels=c('a', 'b')) # 어떤 값을 범주에 포함시키는가?
factor(c('a', 'b', 'c'), levels = c('a', 'b', 'c'), labels = c('a', 'b', 'a'))  # 그 값들에 대해 범주명을 뭘로 할 것인가?
