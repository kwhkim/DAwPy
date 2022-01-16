# -*- coding: utf-8 -*-
# + active=""
# install.packages("ggplot2")
# install.packages("dplyr")
# -

# # 5.1

# # 5.1.1

#data(diamonds , package='ggplot2')
from codecs import xmlcharrefreplace_errors # !!!???
# https://www.cmi.ac.in/~madhavan/courses/prog2-2015/docs/python-3.4.2-docs-html/library/codecs.html
#from pydataset import data
#diamonds = data('diamonds')

# +
#import pandas as pd
#diamonds.to_csv('pydataset_diamonds.csv')
# -

diamonds = pd.read_csv('pydataset_diamonds.csv', index_col=0)

#dim(head(diamonds , n=4)) 
diamonds.head(n=4)
diamonds.head(n=4).shape

# + active=""
# library(magrittr) 
# diamonds %>% head(., n=4) %>% dim(.) 
# diamonds %>% head(n=4) %>% dim() 

# + active=""
# diamonds %>% head(n=4) %>% dim 
# -

#diamonds %>% .$price %>% .[1:10]
diamonds.price[1:10]

#diamonds %>% .[["price"]] %>% .[1:10]
diamonds['price'][1:10]

# + active=""
# options(tibble.print_max = 5, tibble.print_min = 5)
# ???
# -

#class(diamonds) 
type(diamonds)

# + active=""
# library(dplyr) 
# diamonds 
# -

#diaTB <- as_tibble(diamonds[1:10, ]) 
#diaDF <- as.data.frame(diamonds[1:10, ])
diaDF = diamonds.iloc[:10, :]

# + active=""
# #diaDF$pri      # partial matching
# diaDF.pri      #AttributeError: 'DataFrame' object has no attribute 'pri'
# #diaDF[, 'pri'] # ERROR
# diaDF.loc[:, 'pri'] # KeyError: 'pri'
# #diaTB$pri      # NULL
# #diaTB[, 'pri'] # ERROR


# + active=""
# ## 책과 다른 부분 1: data.frame() 의 stringAsFactors 옵션이 원래는 true였는데 지금은 false로 바뀐것 같음
# df <- data.frame(a = c('Kim','Lee','Park'))
# tb <- tibble(a = c('Kim','Lee','Park'))
# ## 그래서 여기서 df의 클래스가 factor 가 아닌 character 로 뜬다.
# class(df$a)
# class(tb$a)
# -

df = pd.DataFrame({'a':['Kim', 'Lee', 'Park']})
type(df)

# # 5.2

# # 5.2.1

#library(dplyr)
#data(mtcars) 
mtcars = data('mtcars')
df = mtcars

# + active=""
# tb = as_tibble(mtcars) 
# -

# # 5.2.2

#tb[2:5, ]
#slice(tb, 2:5)
df.iloc[1:5]  # 2-1 = 1, 5 = 5

# + active=""
# tb %>% .[2:5, ]
# tb %>% slice(., 2:5)
# -


#tb %>% slice(2:5)
#tb %>% slice(c(2:3, 4, 5))
#from Ax_rutils import ac, aseq, lc, lseq
from mypack.utils import ac, aseq, lc, lseq

# + active=""
# import Ax_rutils
# from Ax_rutils import ac as c
# from Ax_rutils import aseq as seq
# -

# 결과를 lseq, aseq로 구분하는게 나을 듯?(list or array)
df.iloc[lc(lseq(1,2),3,4), :]

##5.2.3
#tb[tb$mpg>30, ]
df[df.mpg > 30]
#filter(tb, mpg>30)
#tb %>% filter(., mpg>30)
#tb %>% filter(mpg>30)
df.query("mpg > 30")

# 만약 &가 필요하다면,
df[(df.mpg > 30) & (df.cyl == 4)] # &의 연산 순서가 <,>,==보다 낮기 때문에!
df.query("mpg>30 & cyl==4") # .query()의 경우는 괜찮음
# 연산 순서에 주의할 필요가 있다.

# query의 경우 column 이름에 공백이나 기호가 들어갈 경우 다음과 같이 backtik을 사용한다
df['horse power'] = df.hp
df[df['horse power'] > 250]
df.query('`horse power` > 250')

# # 5.2.4

#tb <- tb %>% slice(3:5)
df = df.iloc[2:5]

# + active=""
# tb[, c(1,3)]
# select(tb, c(1,3))
# tb %>% select(c(1,3))
# -

#tb <- tb %>% slice(3:5)
#tb[, c(1,3)]
df.iloc[:, [1,3]]
df.filter(items = df.columns[[0,2]])

# + active=""
# tb[, c("cyl", "hp")]
# select(tb, c("cyl", "hp"))
# select(tb, c(cyl, hp))

# + active=""
# tb %>% select(c("cyl", "hp"))
# tb %>% select(c(cyl, hp))
# -

#tb %>% select("cyl", "hp")
#tb %>% select(cyl, hp)
df.loc[:, ['cyl', 'hp']]
df.filter(['cyl', 'hp'])
#df.filter(items = ['cyl', 'hp'])

import numpy as np

#which(colnames(tb)=='hp')
np.where(df.columns == 'hp')[0]

#which(colnames(tb)=='qsec') 
np.where(df.columns == 'qsec')[0]

#tb[, which(colnames(tb)=='hp'):which(colnames(tb)=='qsec')] 
df.iloc[:, lseq(np.where(df.columns == 'hp')[0],
                np.where(df.columns == 'qsec')[0])]

#tb %>% select(hp:qsec)
df.loc[:, 'hp':'qsec'] # Slice는 가능하지만
#df.loc[:, lseq('hp', 'qsec')]

# + active=""
# slice(tb, c(1, 2))
# #책과 다른 부분 2 : slice 가 벡터를 받지 않아도 실행이 된다.
# slice(tb, 1, 2)
# -

# # 5.2.4.1

# + active=""
# #  구문                  의미
# # starts_with('ab')   ab로 시작하는
# # ends_with('yz')     yz로 끝나는
# # contains_with('ef)  ef를 포함하는
# # one_of(coln)        문자열 벡터 coln의 각 원소와 일치하는
# # matches('..[cd]')   정규표현식 ..[cd]와 대응하는
# -

#tb3 <- tb %>% slice(1:3) 
#tb3 
#tb3 %>% select(starts_with('c')) 
#tb3 %>% select(starts_with('ca')) 
#tb3 %>% select(ends_with('p')) 
#tb3 %>% select(contains('c'))
df.filter(regex = '^c', axis=1) 
df.filter(regex = '^c')
df.filter(regex = '^ca')
df.filter(regex = 'p$')
df.filter(like = 'c')
df.filter(regex = '.*c.*')

#coln <- c('drat', 'qsec') 
#tb3 %>% select(one_of(coln)) 
colmn = ['drat', 'qsec']
df.filter(items = colmn)

#tb3 %>% select(matches('^(.s|.{4})')) 
df.filter(regex = '^(.s|.{4})')

# # 위아래 한쌍으로 dplyr 함수와 동일한 정규 표현식

# + active=""
# tb %>% select(starts_with('c'))
# tb[, grep('^c', colnames(tb))]

# + active=""
# tb %>% select(ends_with('p'))
# tb[, grep('p$', colnames(tb))]

# + active=""
# tb %>% select(contains('c'))
# tb[, grep('c', colnames(tb))]
# -

# # 5.2.5

#tb %>% select(-cyl, -qsec)
#tb %>% select(-c(cyl, qsec))
#https://stackoverflow.com/questions/406230/regular-expression-to-match-a-line-that-doesnt-contain-a-word
# does NOT contain
df = df.iloc[:5, :]
df.filter(regex = '^((?!m).)*$') # m을 포함하지 않는
df.filter(regex = '^((?!cyl|qsec).)*$') # cyl 또는 qsec을 포함하지 않는
df.filter(regex = '^((?!(cyl|qsec|m)).)*$')

# NOT one of
df.filter(regex = '^(?!m$)')
# look ahead or look behind
# positive/negative look ahead q(?=u), q(?!u)
# positive/negative look behind (?<=u)q, (?<!u)q 
df.filter(regex = '^(?!(m$|cyl$|qse$))')  # m, cyl, qse를 제외
df.filter(items = df.columns.difference(['m', 'cyl', 'qse']))
# 컴럼 내용은 같지만 순서가 다르다?
# df.filter(regex = '^(?!(m$|cyl$|qse$))').sort_values() #
# TypeError: sort_values() missing 1 required positional argument: 'by'
df.filter(items = df.columns.difference(['m', 'cyl', 'qse'])).sort_values()


df.filter(regex = '^(?<!(m|cyl|qsec))$')  
# re.error: look-behind requires fixed-width pattern
df.filter(regex = '^.{3}(?<!(cyl|qse))') # seems impossible
# cyl, qse로 시작하지 않는...

#tb %>% select(-starts_with('c'))
#tb %>% select(-contains('c'))
df.filter(regex = '^(?!c)')
df.filter(regex = '^((?!c).)*$')

# # 5.3

# # 5.3.1

#library(dplyr)
#data(mtcars) 
#tb = as_tibble(mtcars) 
#tb2 <- tb %>% select(hp, cyl, qsec) %>% slice(1:3)
df = data('mtcars')
df2 = df.loc[:, ['hp', 'cyl', 'qsec']].iloc[:3, :]

#tb2 %>% mutate(hp/cyl)
#tb2 %>% mutate(hpPerCyl = hp/cyl)
#tb2 %>% mutate(hpPerCyl = hp/cyl, V2 = hp*qsec)
df2.assign(hpPerCyl = df2.hp/df2.cyl)
df3 = df2.assign(hpPerCyl = df2.hp/df2.cyl, V2=df2.hp*df2.qsec)

# + active=""
# tb2$`hp/cyl` 
# tb3 <- tb2 %>% mutate(hp/cyl) 
# tb3$`hp/cyl` 

# + active=""
# tb$V2 = with(tb, hp*qsec)
# tb[c('V1', 'V2')] = data.frame(tb$hp/tb$cyl, tb$hp*tb$qsec)
# -

# # 5.3.2

# # dplyr 함수와 기존의 방법 비교

#tb %>% arrange(cyl)
#tb[order(tb$cyl), ]
df.sort_values("cyl")

#tb %>% arrange(desc(cyl))
#tb[order(tb$cyl, decreasing = T), ]
df.sort_values('cyl', ascending = False)

#tb3 %>% arrange(cyl, desc(qsec))
df.sort_values(['cyl', 'qsec'], ascending = [True, False])

# # 5.3.3

#tb %>% summarise(mean(hp)) 
#tb %>% summarize(V1 = mean(hp))
#tb %>% summarise(hpMean = mean(hp), qsecMedian =median(qsec))
df[['hp']].agg('mean')
df[['hp']].agg(np.mean)
df.agg(V1 = ('hp', np.mean)) # V1은 'hp' 컬럼에 np.mean을 적용하라
df.agg(hpMean = ('hp', np.mean), qsecMedian = ('qsec', 'median'))
df.groupby([0]*len(df)).\
    apply(lambda x: 
      pd.Series([np.mean(x.hp), np.median(x.qsec)],
                index = ['hpMean', 'qsecMedian']))
df.groupby([0]*len(df)).\
    apply(lambda x: 
      pd.Series(
          {'hpMean':np.mean(x.hp), 
           'qsecMedian':np.median(x.qsec)}))
df.pipe(lambda x: 
      pd.Series([np.mean(x.hp), np.median(x.qsec)],
                index = ['hpMean', 'qsecMedian']))
df.pipe(lambda x: 
      pd.DataFrame(
          {'hpMean': [np.mean(x.hp)], 
           'qsecMedian' : [np.median(x.qsec)]})

#tb %>% summarise(newVar1 = mean(hp) + median(qsec))
#tb %>% summarise(newVar1 = mean(hp), newVar2 = median(qsec))
df.pipe(lambda x:
  pd.DataFrame({'newVar1':[np.mean(x.hp) + np.median(x.qsec)]}))
df.pipe(lambda x:
  pd.Series({'newVar1':np.mean(x.hp),
             'newVar2':np.median(x.qsec)}))

#tb %>% summarise(v1 = mean(hp), v2 = median(qsec), v3 = v1 + v2)
#data.frame(v1 = mean(tb$hp), v2 = median(tb$qsec), v3 = v1 + v2)
df2 = df.agg(v1 = ('hp', np.mean),
             v2 = ('qsec', np.median)).T
df2['v3'] = df2.v1 + df2.v2
df2.agg('mean', axis=0)


# #5.3.4

#tb3 %>% group_by(cyl) 
#tb3_grp <- tb3 %>% group_by(cyl) 
#class(tb3_grp)
df3.groupby('cyl') # pandas.core.groupby.generic.DataFrameGroupBy

##5.3.5
#tb %>% group_by(am) %>% summarise(mean(qsec))
df.groupby('am').agg({'qsec':'mean'})
df.groupby('am').apply(lambda x: 
  pd.Series({'mQsec':np.mean(x.qsec)}))

# # 5.3.6

# # 책과 다른 부분 3 : summarise 에 벡터가 아니라 range 를 넣은 경우 오류가 나온다고 적혀있지만 실제로 결과값이 나옴

#tb %>% summarise(range(hp))
def peak_to_peak(x):
    return x.max() - x.min()
df.groupby([0]*len(df)).apply(lambda x: peak_to_peak(x.hp))
#tb %>% group_by(am) %>% do(head(., n=2))
df.groupby('am').apply(lambda x: x.head(n=2))

#tb %>% group_by(am) %>% do(summary(.))
df.groupby('am').apply(lambda x: x.describe())

#tb %>% group_by(am) %>% 
#  do(as.data.frame(summary(.))) %>% 
#  slice(1:3)
df.groupby('am').apply(lambda x: pd.DataFrame(x.describe())).iloc[:3, :]

# # 5.3.7

# # 선별 및 가공 절차
# #tb %>% select() %>% filter() %>% group_by() %>%
# #summarise(), do(), arrange(, .by_group=T)



# # 5.4
# # 5.4.1


#library(dplyr)
#mtcars %>% mutate(exp(qsec)) %>% head(3)
mtcars.assign(q = np.exp(mtcars.qsec)).head(3)

#mtcars %>% 
#  mutate(expMpg=exp(mpg), expCyl=exp(cyl), expDisp=exp(disp), 
#         expHp=exp(hp), expDrat=exp(drat), expWt=exp(wt), 
#         expQsec=exp(qsec), expVs=exp(vs), expAm=exp(am), 
#         expGear=exp(gear), expCarb=exp(carb)) %>% 
#  head(n=3)
mtcars.assign(expMpg = np.exp(mtcars.mpg),
              expCyl = np.exp(mtcars.cyl))

#mtcars %>% mutate_all(exp) %>% head(n=3) 
mtcars.transform(np.exp) 

# #5.4.2


# #                  _all         _at      _if
# # select       select_all  select_at   select_if
# # mutate       mutate_all  mutate_at   mutate_if
# # transmute    transmute_all transmute_at  transmute_if
# # group_by     group_by_all  group_by_at group_by_if
# # summarise    summarise_all summarise_at summarise_if 

# options(digits=4)

# coln = c('cyl', 'disp', 'drat', 'carb') 
# mtcars %>% mutate_at(coln, exp) %>% head(n=3) 

colmn = ['cyl', 'disp', 'drat', 'carb']
mtcars.loc[:, colmn].transform(np.exp).head(3)

#mtcars %>% 
#  select(starts_with('c'), starts_with('d')) %>% 
#  mutate_all(exp) %>% 
#  head(n=3)
mtcars.filter(regex=('(^c|^d)')).transform(np.exp).head(3)

# mtcars %>% 
#  mutate_at(vars(starts_with('c'), starts_with('d')), 
#            exp) %>% 
#  head(n=3)

#mtcars %>% 
#  mutate_if(function(x) { sum(x)<100 }, exp ) %>% 
#  head(n=3)
colmn = mtcars.apply(lambda x: x.sum() < 100, axis=0) # axis=0을 모두 모아...
mtcars.loc[:, colmn].transform(np.exp).head(3)


# mtcars %>% 
#  transmute(expCarb = exp(carb)) %>% head(n=3) 

mtcars.assign(expCarb = np.exp(mtcars.carb)).head(3)
mtcars.pipe(lambda x:
    pd.DataFrame({'expCarb':
        np.exp(mtcars.carb)})).head(3)
pd.DataFrame({'expCarb': np.exp(mtcars.carb)}).head(3)

# mtcars %>% transmute_if(function(x) sum(x)<100, exp) %>% head(n=3)
# #`funs()` is deprecated as of dplyr 0.8.0
# mtcars %>% transmute_if(funs(sum(.) <100), exp) %>% head(n=3)


# mtcars %>% 
#  mutate_if(funs(sum(.) >= 100), 
#            funs(paste(.,"+",sep=""))) %>% head(n=3)
# mtcars %>% transmute_at(vars(starts_with('d')), exp) %>% head(n=3)

# Ref : https://towardsdatascience.com/python-pandas-vs-r-dplyr-5b5081945ccb
# To add
#   renaming axis
#   
df2.rename(columns = {'hp':'horse power', 
                      'cyl':'cylinder(2/4/6)',
                      'qsec':3.14159})
df2.rename({'hp':'horse power', 
                      'cyl':'cylinder(2/4/6)',
                      'qsec':3.14159}, axis=1)
df2.rename(lambda x: x.upper(), axis=1)                     
df2.rename(len, axis=1) # 입력은 str?
def renamer(x):
  if len(x) < 4:
    return x.upper()
  else:
    return x
    # return None  # name will be NaN
df2.rename(renamer, axis=1)
df2.rename(columns = renamer)

# distinct values?
import pandas as pd
df2.apply(lambda x: x.unique(), axis=0)
df2.apply(lambda x: pd.Series(x.unique()), axis=0)

df.value_counts('cyl')
df.groupby('cyl').size()

# Delete Column
df.drop("mpg", axis=1, inplace=True)
'mpg' in df.columns
'hp' in df.columns

# Reordering columns
df.reindex(df.columns.sort_values(), axis=1).head()
