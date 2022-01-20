# -*- coding: utf-8 -*-
# %%
## 사전 지식
## 정규표현식 re
## 
# %% [markdown]
# ## 날짜 시간 데이터에 대한 개괄
#
# ###  사전 지식 
#
# 1. 날짜를 표기하는 방법은 나라마다 다르다.
#     - 예. 2022-04-10(한국) vs. 04-10-2022(미국) vs. 10-04-2022(유럽)
# 2. 시간은 시간대(timezone)과 DST(Daylight Saving Time; 서머타임 실시 여부)에 따라 다르게 표기된다.
#     - 시간대는 생각보다 자주 변한다(예. 평양시간)
#     - 역사적으로도 역법이 바뀌었다.
#     - 미래에는 어떻게 바뀔지 예상할 수 없다.
# 3. 우리가 사용하는 날짜와 시간은 불규칙적으로 흐른다.
#     - 하루는 항상 $86400 = 60 \times 60 \times 24$ 초인가? -> 윤초(leap second)
#     - 1달은 항상 동일한 날로 구성되는가? -> 윤달(2번째 달은 28일 또는 29일)
#
# ## 참고 동영상 
#
# * [The Complexity of Time Data Programming](https://www.mojotech.com/blog/the-complexity-of-time-data-programming/)
# * [North Korea changes its time zone to match South](https://www.bbc.com/news/world-asia-44010705)
#
#     
# ###  주요 내용(자료형)
#
# 1. 표기 방법이 다른 날짜(/시간) 문자열과 날짜(시간) 타입의 상호 변환
# 2. 주요 성분을 구하거나, 수정하기(예. 년,월,일,시,분,초,시간대,dst?)
# 3. 시간 차이를 구하거나, 시간에 시간 차이를 더하거나 빼기
# 4. 객체 타입에 따라 저장 가능한 날짜의 최소/최대값과 정밀도가 다르다.
#
# ### 파이썬/Computer
#
# 1. class 구조
# 2. naive/aware
# 3. unix timestamp : seconds since unix epoch(1970-01-01 00:00:00)
# 3. locale : 시스템 로케일에 대한 설명?
# 4. platform-independent?
# 5. standard modules(time, datetime, calendar), numpy & pandas dtype
#
# ### 최상의 전략과 이유?
#
# 1. 과거 시간은 UTC를 사용한다.
# 2. 미래 시간은 날짜시간과 시간대를 함께 저장한다.
#

# %%
# 음력
# https://pypi.org/project/korean-lunar-calendar/
# https://pypi.org/project/LunarCalendar/

# %% [markdown]
# # 날짜시간

# %% [markdown]
# 파이썬에서 날짜시간을 다루는 모듈은 `datetime`, `time`, 그리고 `calendar`가 있다. 날짜시간을 다루는 경우 대부분은 `datetime`을 활용하여 처리할 수 있다. 여기서는 `datetime` 모듈을 활용하는 방법을 설명하고, 추가로 `time`, `calendar`을 사용하는 법을 소개하여 `time`, `calendar`를 사용하는 예전 코드들도 읽고, 수정할 수도 있도록 하였다.

# %% [markdown]
# `datetime` 모듈에서 정의하는 클래스의 상속 관계는 다음과 같다.
#
# ```
# object
#     time
#     date
#         datetime
#     timedelta
#     tzinfo
#         timezone
# ```

# %% [markdown]
# `time`은 시간, `date`는 날짜, `datetime`은 날짜시간 자료(값 1개, 스칼라)를 저장한다. `timedelta`는 시간 차이, `timezone`은 시간대(timezone)을 저장하고, 관련 연산을 수행할 수 있다.

# %% [markdown]
# 2023년 한글날(10.9) 오후 2시 20분을 생각해보자. 이 시각은 날짜와 시간으로 구성된다. 

# %%
import datetime
date1 = datetime.date(2023,10,9)
time1 = datetime.time(14,20)
date1, time1

# %%
datetime1 = datetime.datetime(2023, 7, 17, 14, 20)
# datetime1 = datetime.datetime.combine(date1, time1)

# %% [markdown]
# 파이썬의 표준 모듈 `datetime`의 날짜형(`date`), 시간형(`time`), 날짜시간형(`datetime`) 객체를 생성하는 방법은 위와 같다. `date`, `time`, `datetime`은 모두 클래스 이름이다. 변수 `date1`, `time1`을 합쳐 날짜시간형 객체를 만들어내고 싶다면 `datetime.datetime` 클래스의 클래스 메쏘드는 `.combine()`을 사용할 수 있다.

# %% [markdown]
# 이렇게 날짜형, 시간형, 날짜시간형 객체를 만들면 날짜시간이 명확히 정의되고, 날짜시간과 관련된 여러 가지 연산을 쉽게 할 수 있다는 장점이 있다. 만약 문자열 `"2023-10-09"` 또는 `"14:20"`을 사용한다면 어떨까? 날짜가 10월 9일인지, 9월 10일인지 헷갈릴 수 있다. 그리고 날짜시간 사이의 차이를 구하기도 힘들다.

# %% [markdown]
# 예를 들어 2023년 한글날에서 2024년 한글날까지 몇 일이 지나야 하는가?

# %%
date2 = datetime.date(2024, 10, 9)
date2 - date1

# %% [markdown]
# 결과는 366일이다. 2024년은 윤년이라고 추측할 수 있다(윤년은 2월 29일로 구성된다).

# %% [markdown]
# 이를 문자열에서 실행하려고 하면 오류가 발생한다.

# %%
"2024-10-09" - "2023-10-09"

# %% [markdown]
# 시간의 차이를 나타내는 `datetime.timedelta` 클래스는 직접 생성하기 보다는 주어진 날짜, 시간, 날짜시간에서 얻는 경우가 더 많을 것이다. 그래도 생성하는 방법을 보인다면 다음과 같다.

# %%
datetime.timedelta(days=2, seconds = 70, microseconds = 100.50, milliseconds = -20.5, minutes = -70.43, hours=1, weeks=3)


# %% [markdown]
# 일, 초, 밀리초(1/1000초), 마이크로초(1/1000밀리초), 분, 시간, 주를 입력하면 알아서 계산해준다. 이때 음수도 가능하고, 실수도 가능하다. 하지만 달(month)과 년(year)은 사용할 수 없다. 왜냐하면 달과 년의 길이는 고정되어 있지 않기 때문이다. (달의 길이는 28,29,30,31일 중 하나이고, 년의 길이는 365일, 366일 중의 하나이다.)

# %% [markdown]
# `timedelta` 클래스는 전체 시간을 **일**, **초**, **마이크로초**로 저장하기 때문에 시간, 분을 확인하기 어렵다. 다음의 함수 `d_h_m_s()`는 `timedelta` 인스턴스에서 **시간**, **분**을 계산해준다.

# %%
def d_h_m_s(td):
    
    if not isinstance(td, (datetime.timedelta)):
        raise ValueError('td should be datetime.timedelta class')
    tot_sec = td.total_seconds()
    if tot_sec > 0:
        sign = +1
    else:
        sign = -1
        tot_sec = - tot_sec
        
    days, remainder = divmod(tot_sec, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, secs = divmod(remainder, 60)
    
    return sign*days, sign*hours, sign*minutes, sign*secs


# %%
d_h_m_s(datetime.timedelta(1,83200, 10))

# %%
d_h_m_s(datetime.timedelta(0,-90*60-1,-10))

# %% [markdown]
# 2024년 1월 1일에서 2024년 12월 25일까지 시간(일수)을 구해보자. 

# %%
datetime.date(2024, 12, 25) - datetime.date(2024, 1, 1)

# %% [markdown]
# 오전 9시에서 오후 6시까지의 시간(근무시간?)을 구하려면 어떻게 해야 할까? `datetime.time(16,0)-datetime.time(9,0)`은 TypeError를 발생시킨다. 일단 날짜 없이 정확한 시간 차이를 구할 수 없다(왜냐하면 드물게 윤초가 존재하기 때문이다.)
#
# 만약 이런 차이를 무시하고 시간 차이를 구하고 싶다면, 임의의 날짜를 지정해서 시간 차이를 구하면 된다. 
#

# %%
datetime.datetime.combine(datetime.date(2024,1,1), datetime.time(18,0)) - \
  datetime.datetime.combine(datetime.date(2024,1,1), datetime.time(9,0)) # 임의의 날짜 입력
# 이때 0을 00으로 쓰지 않도록 유의하자.

# %% [raw]
# dateNow <- Sys.Date()
# print(dateNow)
# class(dateNow)

# %%
import datetime
import sys
# sys — System-specific parameters and functions

# %% [markdown]
# 현재 날짜와 시간을 얻는 방법은 다음과 같다. 

# %%
dateNow = datetime.date.today()
print(dateNow)
type(dateNow)

# %%
datetimeNow = datetime.datetime.now()
print(datetimeNow)
type(datetimeNow)

# %% [markdown]
# ### 클래스 `date`, `time`, `datetime` 사이 변환
#
# 클래스 `date`, 클래스 `time`, 클래스 `datetime` 사이의 변환은 다음과 같다.

# %%
datetimeNow.date()

# %%
datetimeNow.time()

# %%
dateNow = datetimeNow.date()
dateNow

# %%
timeNow = datetimeNow.time()
timeNow

# %%
datetimeNow = datetime.datetime.combine(dateNow, timeNow)
datetimeNow

# %% [markdown]
# ### 문자열과 `datetime` 사이 변환

# %%
datetimeNow.strftime('%Y-%m-%d %H:%M:%S')
dateNow.strftime('%Y-%m-%d')
timeNow.strftime('%H:%M:%S')

# %%
print(datetime.datetime.strptime('2022-10-09 11:30:00', '%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.strptime('2022-10-09', '%Y-%m-%d')) # %H:%M:%S의 기본값은 00:00:00
print(datetime.datetime.strptime('11:30:00', '%H:%M:%S'))   # %Y-%m-%d의 기본값은 1900-01-01

# %% [markdown]
# ### 시간대

# %% [markdown]
# `datetime` 인스턴스의 속성 `.tzinfo`는 날짜시간의 시간대를 저장한다. `datetimeNow.tzinfo`는 `None`이다.

# %%
datetimeNow.tzinfo

# %% [markdown]
# 우리가 `datetime.datetime.now()`로 얻은 날짜시간은 시간대에 대한 정보가 없다. 이렇게 시간대 정보가 얻는 날짜시간형을 naive(offset)라고 하고 시간대 정보가 있는 날짜시간형을 aware(offset)라고 한다. naive 날짜시간형은 본인의 컴퓨터가 다른 시간대로 옮겨간다던지 다른 시간대의 컴퓨터로 정보를 옮기면 그 정확한 의미를 확인할 수 없기 때문에 시간대 정보를 추가해주는 것이 좋다.

# %% [markdown]
# `datetime` 모듈에는 지역시간과 UTC와의 차이를 나타내기 위해 `timezone` 클래스가 있습니다만, 이는 **고정된 시간차이**만 나타낼 수 있습니다. 시간대는 역사적으로 UTC와의 시간차이가 변해왔습니다.

# %%
from datetime import timezone
tzSeoul = timezone(offset = datetime.timedelta(hours = 9), name = 'Seoul')
tzSeoul = timezone(offset = datetime.timedelta(hours = 9))
# UTC와 시간차이를 datetime.timedelta로 나타냅니다.

# %%
tzSeoul

# %% [markdown]
# 이렇게 정의된 `tzSeoul`은 UTC와 9시간 앞서는 시간대를 나타냅니다. 

# %%
datetimeNow

# %% [markdown]
# naive한 날짜시간형 `datetimeNow`에 시간대 정보를 추가하려면 `.replace(tzinfo=)`와 `.astimezone(tz=)` 메쏘드를 활용합니다. `.replace(tzinfo=)`는 주어진 날짜시간은 그대로 두고 시간대만 수정합니다(날짜시간을 그대로 두고 시간대를 변경하면 의미하는 시각이 변하기 마련입니다). `.astimezone(tz=)`는 주어진 시각은 바꾸지 않으므녀 시간대를 포함한 날짜시간을 다른 시간대의 날짜 시간으로 변환합니다. 
#
# 보통 naive 날짜시간은 현재 컴퓨터가 사용하는 시간대를 가정하기 때문에 `tzSeoul`을 사용하면 둘의 차이를 확인하기 힘들 수 있습니다. UTC+0800(예. 홍콩) 시간대를 사용해봅니다. 

# %%
tzHongkong = timezone(datetime.timedelta(hours= 8))

# %%
datetimeNow.replace(tzinfo=tzHongkong)

# %%
datetimeNow.astimezone(tz=tzHongkong)

# %%
datetimeNow = datetime.datetime.now()

# %%
dt1 = datetimeNow.astimezone(tzSeoul)
dt1

# %%
tzHongkong = timezone(offset = datetime.timedelta(hours = 8), name = 'Hongkong')

# %%
dt1.replace(tzinfo= tzHongkong)

# %% [markdown]
# 그런데 1988년 5월 10일 오전 9시라면 어떨까? 위와 마찬가지로 다음과 같이 써도 될까?

# %%
dt1 = datetime.datetime(1988,5,10,9).replace(tzinfo = tzSeoul)
dt1

# %%

# %% [markdown]
# 우리나라는 1988년 5월 8일부터 써머타임을 실시했다. 그래서 1988년 5월 10일에는 UTC와 시간차이가 10시간이었다! `datetime.timezone()`으로 생성된 시간대 정보는 고정된 시간차이를 저장하기 때문에 역사적으로 변해간 시간차이를 나타내기에는 적절하지 않다. 이럴 경우 보통 `pytz`라는 패키지를 사용한다.
#
#

# %%
import pytz
pytzSeoul = pytz.timezone('Asia/Seoul')
pytzSeoul

# %% [markdown]
# 위의 출력 결과를 보면 `LMT+8:28:00 STD`로 다소 생소한 수가 나타난다. 이는 `datetime.datetime.strptime('11:30:00', '%H:%M:%S')`에서 나타난 기본 날짜 1900년 1월 1일의 시간차이를 나타낸다. `pytzSeoul`은 서울의 시간대를 나타내고 날짜에 따라 UTC와의 시간차이가 달라진다. `pytzSeoul.localize()`로 naive 날짜 시간을 aware하게 만들 수 있다.

# %%
datetimeNow =datetime.datetime.now()
dtNowSeoul = pytzSeoul.localize(datetimeNow)
dtNowSeoul

# %% [markdown]
# `tzinfo=` 이하의 정보를 보면 `KST+9:00:00`로 현재 시간차이를 정확하게 나타내고 있다. 이번에 1988년 5월 10일 시간을 aware하게 만들어 보자.

# %%
dt2 = pytzSeoul.localize(datetime.datetime(1988,5,10,9,0)) 
# 이때 datetime.datetime(1988,5,10,10, tzinfo=pytzSeoul)는 부정확하다.
dt2

# %% [markdown]
# `tzinfo=` 이후의 `KDT+10:00:00`을 주목하자. K**D**T는 Korea **D**aylight-saving Time, KST는 Korea **S**tandard Time을 의미한다. DST는 Daylight Saving Time, STD는 STAndard의 약자인 듯 하다.
#
#

# %%
dt1

# %%
dt1 - dt2

# %%
dt1, dt2, dt1.utcoffset(), dt2.utcoffset()

# %% [markdown]
# `dt1`과 `dt2`를 살펴보면 둘 다 1988년 5월 10일 9시로 되어 있지만, 시간대(`tzinfo=`)가 다르다. 특히 `.utcoffset()`으로 UTC와의 시간차이를 확인해보면 `dt1`은 UTC보다 9시간(32400초) 빠르고, `dt2`는 UTC보다 10시간(36000초) 빠르다는 것을 알 수 있다.

# %% [markdown]
# 이처럼 시간대를 잘못 설정하면 시간이 부정확하게 입력되므로 유의해야 한다.

# %% [markdown]
# #### 그 밖에


# %% [markdown]
# 년, 월, 일, 시, 분, 초, 마이크로초, 시간대 참조하기

# %%
dt2.year, dt2.month,dt2.day, \
dt2.hour, dt2.minute, dt2.second, dt2.microsecond, \
dt2.tzinfo


# %% [markdown]
# 년, 월, 일, 시, 분, 초, 마이크로초 덮어쓰기

# %%
dt2.replace(year = 1989), dt2.replace(month=6), dt2.replace(day=11), \
dt2.replace(hour = 10),   dt2.replace(minute = 1), dt2.replace(second = 30), dt2.replace(microsecond = 55000), \
dt2.replace(tzinfo=tzSeoul)

# %% [markdown]
# 시간은 그대로 시간대만 변경하기(동일한 시각이 시간대가 다른 시간으로 변환된다)

# %%
dt1.astimezone(pytzSeoul) # dt1을 1988년 DST가 적용된 시간으로 표기하면 오전 10시가 된다.

# %% [markdown]
# # 넘파이 행렬

# %%
import numpy as np

# %% [markdown]
# ### 생성
#
# 평소와 마찬가지로 리스트를 통해 원소를 입력할 수 있다. 이때 `dtype="datetime64"`를 잊지 말자. `datetime.datetime`, `datetime.date` 또는 날짜시간 형식을 갖춘 문자열은 모두 넘파이의 `datetime64` 타입으로 변형된다. 이때 `datetime64`에서 `64`는 `datetime.datetime`과 구분하기 위해 추가했다고 한다. 물론 `np.datetime`으로 써도 `datetime.datetime`과 구별된다(Namespace가 다르다!). 어쨋든 좀더 명시적으로 구분하기 위해 `datetime64`로 명명했다고 한다. 

# %%
sDate = np.array([datetime.datetime(2021,10,4,10),
                  datetime.datetime(2022,3,1,9,11),
                  datetime.datetime(2023,10,9,7,10)])
sDate

# %% [markdown]
# `dtype="datetime64"` 또는 `dtype=np.datetime64`를 하지 않으면 dtype은 object로 저장된다.

# %%
sDate = np.array([datetime.date(2021,10,4),
                  datetime.date(2022,3,1),
                  datetime.date(2023,10,9)], 
                 dtype='datetime64')
sDate

# %%
sDate = np.array([datetime.datetime(2021,10,4,10),
                  datetime.datetime(2022,3,1,9,11),
                  datetime.datetime(2023,10,9,7,10)],
                dtype='datetime64')
sDate

# %% [markdown]
# dtype의 마지막에 `[D]`(일) 또는 `[us]`(마이크로초)는 시간단위를 나타낸다. `np.datetime64`는 내부적으로 특정한 시점(예. 1970-01-01 00:00)에서 지나간 시간으로 시각을 저장한다. 시간단위가 일(`[D]`)이라면 시각은 특정한 시점(예. 1970-01-01 00:00)에서 몇 일이 지났는지를 정수로 저장하게 된다. 

# %% [markdown]
# 문자열 리스트를 입력해도 날짜시간형으로 인식한다.

# %%
sDate = np.array(['2021-10-04 10:00', 
                  '2022-03-01 11:00', 
                  '2023-10-09 09:07:10'], dtype='datetime64')
sDate

# %% [markdown]
# 만약 날짜시간을 표기하는 형식이 다르다면 다음과 같이 `pd.to_datetime()`을 사용할 수 있다. `pd.to_datetime()`의 결과 type은 `DatetimeIndex`라는 인덱스 타입이기 때문에 판다스 시리즈로 변환하기 위해서 `.to_numpy()` 메쏘드를 사용했다.

# %%
import pandas as pd
sDate = pd.to_datetime(['10:00 04-10-2021',
                        '11:00 01-03-2022',
                        '09:07 09-10-2023'], 
                       format = "%H:%M %d-%m-%Y").to_numpy()
sDate

# %%
sDate.itemsize, sDate.size
# dtype="datetime64"에서 64는 64 비트(8 바이트)를 의미함을 확인할 수 있다.

# %% [markdown]
# ### 시간대

# %% [markdown]
# 넘파이 배열은 시간대를 저장할 수 없다. 모든 시간은 UTC로 저장된다.

# %% [markdown]
# ## 문자열 변환

# %% [markdown]
# `np.datetimea_as_string()`을 사용하면 날짜시간형 넘파이 배열을 문자열로 변환한다. 형식은 `%Y-%m-%dT%H:%M:%S`로 고정되어 있으며 `unit=`을 통해 최소 시간 단위를 결정할 수 있다. `unit='D'`(**D**ay)로 하면 년-월-일까지만 출력한다. 이때 주어진 날짜시간 데이터에서 생략되는 정보가 있다면 `casting = 'unsafe'`로 놓아야 한다. 

# %%
np.datetime_as_string(sDate, unit='h')

# %%
np.datetime_as_string(sDate, unit='D', casting = 'unsafe') 
# timezone = 'naive', 'UTC', 'local'
# casting = 'no', 'equiv', 'safe', 'same_kind', 'unsafe'

# %% [markdown]
# 넘파이 배열은 모든 시각을 UTC로 저장하므로 출력시 필요한 시간대로 출력할 수 있다면 좋을 것이다. `timezone=`을 통해 출력 시간대를 설정할 수 있다. `naive`는 시간대 표시없이, `UTC`는 UTC를 의미하는 `Z`, 그리고 `local`은 현재 시간대의 UTC와 시간 차이를 시간 뒤에 붙인다. 

# %%
aDate1 = sDate[0]

print(np.datetime_as_string(aDate1, unit='m', timezone='naive'))
print(np.datetime_as_string(aDate1, unit='m', timezone='UTC'))
print(np.datetime_as_string(aDate1, unit='m', timezone='local'))

# %%
pytzHongkong = pytz.timezone('Asia/Hong_Kong')

# %%
np.datetime_as_string(sDate, unit='m', timezone=pytzHongkong) 

# %% [markdown]
# 만약 특정한 날짜시간 형식의 문자열로 변환하고 싶다면 판다스 시리즈로 변환한 후에 `.dt.strftime()` 메쏘드를 사용할 수 있다.

# %%
pd.Series(sDate).dt.strftime("%H:%M:%S %d-%m-%Y")


# %% [markdown]
# # 판다스 시리즈

# %%
import pandas as pd

# %%
s = pd.Series(['2022-05-14 08:15:10', '1988-05-10 09:11:20', '2024-10-09 15:14:05.99'],
              dtype='datetime64[ns]')
s # naive

# %%
# to timezone aware
tzSeoul = timezone(offset = datetime.timedelta(hours = 9), name='Seoul')
s.dt.tz_localize(tzSeoul) 
# 위에서 name='Seoul'을 생략하면
# dtype: datetime64[ns, UTC+09:00]

# %%
s2 = s.dt.tz_localize(pytzSeoul)
s2

# %%
# timezone conversion

# %%
s2.dt.tz_convert(tzHongkong) # UTC+0800으로 시간대 변환(고정된 시각)

# %% [markdown]
# ### 년, 월, 일, 시, 분, 초, 마이크로초, 나노초

# %%
s.dt.year, s.dt.month, s.dt.day, \
s.dt.hour, s.dt.minute, s.dt.second, \
s.dt.microsecond, s.dt.nanosecond

# %%
s.dt.isocalendar().week, \
s.dt.day_of_year, s.dt.dayofyear, \
s.dt.days_in_month, s.dt.daysinmonth, \
s.dt.day_of_week, s.dt.dayofweek, s.dt.weekday, \
s.dt.month_name(), s.dt.day_name()

# %%

# %% [markdown]
# ### 문자열 변환

# %% [markdown]
# dtype이 `datetime64`인 판다스 시리즈를 문자열 타입(`dtype="O"`)로 변환하거나, 문자열 타입을 `datetime64` 타입으로 변환하기 위해서는 `.dt.strftime()`과 `pd.to_datetime()`을 사용한다.

# %%
s_str_datetime = s.dt.strftime("%Y-%m-%d %H:%M:%S")
s_str_datetime # dtype을 확인하자

# %% [markdown]
# 날짜시간 형식을 통제하지 않는다면 .astype('O')로도 충분하다.

# %%
s_str2_datetime = s.astype('O')
s_str2_datetime

# %%
pd.to_datetime(s_str_datetime, format = '%Y-%m-%d %H:%M:%S')

# %% [markdown]
# 만약 `pd.to_datetime()`의 경우 문자열 리스트를 사용할 경우에는 결과가 `DatetimeIndex`가 되므로, `pd.Series()`를 통해 판다스 시리즈로 변환한다. (`.to_series()`를 사용할 수도 있다. 이때 결과 인덱스를 비교해보자.)

# %%
pd.to_datetime(['2022-05-14 08:15:10', 
                '1988-05-10 09:11:20',
                '2024-10-09 15:14:05'], format = '%Y-%m-%d %H:%M:%S').to_series()

# %% [markdown]
# 다음의 두 결과를 확인해 보자.

# %%
pd.Series(pd.to_datetime(['1300-01-01', '1310-12-25'], 
                         format='%Y-%m-%d', errors='ignore'))
# dtype이 datetime64[ns]가 아니라 object임

# %%
pd.Series(pd.to_datetime(['1990-01-01', '1991-12-25'], 
                         format='%Y-%m-%d', errors='ignore'))

# %% [markdown]
# `['1300-01-01', '1310-12-25']`은 dtype `datetime64[ns]`로 저장되지 않았다. 왜 그럴까?

# %% [markdown]
# 꼭 dtype `datetime64[ns]`이 필요하다면 `errors='coerce'`로 해보자. 

# %%
pd.Series(pd.to_datetime(['1300-01-01', '1310-12-25'], 
                         format='%Y-%m-%d', errors='coerce'))

# %% [markdown]
# 모두 실수의 `np.nan`에 해당하는 `np.datetime64('NaT')`가 되었다.

# %% [markdown]
# 넘파이 배열과 비교를 해보자. 

# %%
np.array(['1300-01-01', '1301-12-25'], dtype='datetime64')

# %% [markdown]
# dtype이 `datetime64[D]`로 시간 간격이 `D`(**D**ay)가 되었다. 판다스의 날짜시간형 데이터타입은 모두 시간간격이 `ns`(**n**ano**s**econd)이다. 이에 따라 판다스 날짜시간형이 저장할 수 있는 기간은 1678년에서 2262년까지이다. 따라서 1300년대의 날짜는 저장이 불가능한 것이다!

# %% [markdown]
# 혼동하지 말자. `pd.to_datetime(..., unit='D')`이나 `astype('datetime64[D]')`처럼 시간간격을 일로 설정할 수 있는 함수가 있지만, 판다스 시리즈에서 저장되는 형식은 언제나 `datetime64[ns]`이다.

# %%
pd.to_datetime([100,200], unit='D')

# %%
pd.Series(pd.to_datetime(['2022-01-20 19:04', '2023-11-03 02:10'])).astype('datetime64[D]')

# %%

# %%
s.dt.year, s.dt.month, s.dt.day, \
s.dt.hour, s.dt.minute, s.dt.second, \
s.dt.microsecond, s.dt.nanosecond, \
s.dt.month_name(), s.dt.day_name()

# %%
type(s2)

# %%
dir(s)

# %% [markdown]
# #### 시간대

# %%
s = pd.Series(pd.to_datetime(['2022-05-14 08:15', '2023-03-01 09:11', '2024-10-09 15:14']))
s

# %% [markdown]
# 시간대를 설정하려면 `.dt.tz_localize()`를 사용하고, 시간대를 변경하려면 `dt.tz_convert()`를 사용한다.

# %%
s2 = s.dt.tz_localize(pytzSeoul)
s2

# %%
s2.dt.tz_convert(tzHongkong)

# %% [markdown]
# ### 연산

# %% [markdown]
# #### 하루 후

# %%
datetime.datetime.now() + pd.Timedelta('1 day') # pd.Timedelta()에 문자열을 사용 가능

# %%
datetime.datetime.now() + pd.offsets.BDay() # 1 영업일

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# # 6.1

# %%

# %% [markdown]
# ## 6.1.1

# %% [markdown]
# ### ISO 8601

# %%
# !!! 역사적인 날을 여러 가지 형식으로 바꿔 본다면?

# 동일본 대지진 : 2011. 3. 11
# 리만 브라더스 파산 : 2008. 9. 15
# 

# %% [raw]
# # 스타일   표기            의미                     예
# # 기본형 (+-)YYYYMMDD    년월일                  20200103
# # 확장형 (+-)YYYY-MM-DD  년-월-일                2020-01-03
# # 기본형 (+-)YYYYDDD     년일(1년의 몇번째 일)   2020003
# # 확장형 (+-)YYYY-DDD    년-일(1년의 몇번째 일)  2020-003
# # 기본형 (+-)YYYYWwwD    년주일                  2020W013
# # 확장형 (+-)YYYY-Www-D  년-W주-일               2020-W01-3


# %% [markdown]
# ## 6.1.2

# %% [markdown]
# ### ISO 8601 시간

# %% [raw]
# # 스타일     표기                      의미
# # 기본형  hhmmss(,ss)(Z)(+-hh(:)mm)    시분초(,100분의 1초)(Z)(타임존)
# # 확장형  hh:mm:ss(,ss)(Z)(+-hh(:)mm)  년-월-일(,100분의 1초)(Z)(타임존)

# %% [markdown]
# ## 6.2

# %% [raw]
# x <- Sys.time()
#
# format(x, '%Y-%m-%d %H:%M:%S')
# format(x, '%Y-%jT%H:%M:%S')
# format(x, '%G-W%V-%u %H:%M:%S')

# %%
x = datetime.datetime.now()
print(x.strftime('%Y-%m-%d %H:%M:%S'))
print(x.strftime('%Y-%jT%H:%M:%S'))
x.strftime('%G-W%V-%u %H:%M:%S')


# %% [markdown]
# ### 기호   의미

# %% [raw]
# %Y     4자리 년
# %m     2자리 월
# %d     2자리 (월 중) 일(01-31)
# %H     2자리 시간(00-23)
# %M     2자리 분(00-59)
# %S     2자리 초(00-59)
# %j     3자리 (년 중) 일(001-366)
# # 출처 : https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes

# %% [raw]
# %G     4자리 ISO 8601 년 
# %V     2자리 (년 중) ISO 8601 주(01-53)
# %u     1자리 (주 중) ISO 8601 일(1-7, 1=월요일)

# %%
#for (y in 2020:2023) 
#  print(format(as.Date(paste0(y, '-01-01', sep='')), '%Y/%m/%d, V=%V U=%U u=%u w=%w A=%A a=%a'))
#from Ax_rutils import lc, lseq

# mypack.utils를 import하려면 먼저 dateparser 패키지를 설치해야
from mypack.utils import lc, lseq

seq = lseq
from datetime import date
for im, y in enumerate(seq(2022,2025)):
    #print(f'{y:04d}')
    #print(f'{y:04d}-01-01')
    #print(datetime.datetime.strptime(f'{y:04d}-01-01', '%Y-%m-%d'))
    #print(datetime.strptime(f'{y:04d}-01-01', '%Y-%m-%d'))
    #print(datetime.datetime.strptime(f'{y:04d}-01-01', '%Y-%m-%d').
    # strftime('%Y/%m/%d, V=%V U=%U u=%u w=%w A=%A a=%a'))
    print(datetime.datetime.strptime(f'{y:04d}-{im+1:02d}-01', '%Y-%m-%d').
    strftime('%Y/%m/%d, V=%V U=%U u=%u w=%w A=%A a=%a B=%B b=%b'))

# %%
# https://docs.python.org/3/library/locale.html#background-details-hints-tips-and-caveats
import locale
locale.setlocale(locale.LC_ALL, '') 
for im, y in enumerate(seq(2022,2025)):
    print(datetime.datetime.strptime(f'{y:04d}-{im+1:02d}-01', '%Y-%m-%d').
    strftime('%Y/%m/%d, V=%V U=%U u=%u w=%w A=%A a=%a B=%B b=%b'))
## locale은 pip install에서 문제를 일으키기도 한다.
## https://m.blog.naver.com/chandong83/221298511028
## 다음과 같은 에러
## locale.setlocale(locale.LC_ALL, '')
##   File "/usr/lib/python2.7/locale.py", line 581, in setlocale
##     return _setlocale(category, locale)
## locale.Error: unsupported locale setting

# %% [raw]
# # docker 설정에서 문제가 발생할 수도 있다
# # https://www.44bits.io/ko/post/setup_linux_locale_on_ubuntu_and_debian_container
#


# %% [markdown]
# ## 6.3

# %% [markdown]
# ### 6.3.1


# %% [markdown]
# #### ISO 8601 

# %%
# !!! 실제 이런 형식이 어디서 사용되고 있는지 확인 또는 예시가 있으면 좋을 듯.

# %% [raw]
# #   표기            의미                     예           날짜로 변환
# #  (+-)YYYYMMDD    년월일                  20200103     format='%Y%m%d'
# #  (+-)YYYY-MM-DD  년-월-일                2020-01-03   format='%Y-%m-%d'
# #  (+-)YYYYDDD     년일(1년의 몇번째 일)      2020003      format='%Y%j'
# #  (+-)YYYY-DDD    년-일(1년의 몇번째 일)     2020-003     format='%Y-%j'
# #  (+-)YYYYWwwD    년주일                  2020W013     format='%GW%V%u'
# #  (+-)YYYY-Www-D  년-W주-일               2020-W01-3   format='%G-W%V-%u'

# %% [raw]
# install.packages("parsedate")
# library(parsedate)
# as.Date('20210102', format='%Y%m%d'); as.Date(parse_iso_8601('20210102'))
# as.Date('2021-01-02', format='%Y-%m-%d'); as.Date(parse_iso_8601('2021-01-02'))

# %%
#??? https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object
from dateutil import parser
datetime.datetime.strptime('20220102', '%Y%m%d')
parser.parse('20220102') # subpackage parser
datetime.datetime.strptime('2022-01-02', '%Y-%m-%d')
parser.parse('2022-01-02')

# %%
from mypack.utils import lsf, lsf_doc
### ??? package의 모든 subpackage와 module 나열하기???
### https://www.google.com/search?q=python+listing+all+subpackages&client=safari&rls=en&sxsrf=AOaemvKWU59ayc3ntrOhR9iEJmJ3Ef02Mg%3A1642213240292&ei=eC_iYYKdEYaEr7wPufWO2Ak&ved=0ahUKEwiCudSG2bL1AhUGwosBHbm6A5sQ4dUDCA0&uact=5&oq=python+listing+all+subpackages&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BwgjELACECdKBAhBGABKBAhGGABQ-BNYhhpgtBtoAXACeACAAZ0BiAHpB5IBAzAuN5gBAKABAcgBCsABAQ&sclient=gws-wiz


# %%
import dateutil

# %%
lsf(dateutil) # 굳이 dateutil 아래 parser에 함수를 넣은 이유가?

# %%
lsf_doc(dateutil)

# %%
datetime.datetime.fromisoformat('2022-01-02')
# ISO 8601 형식 중 YYYY-MM-DD만 지원. 
# date.isoformat()는 date.strftime('%Y-%m-%d')와 동일하다.   

# %%
import aniso8601
# https://aniso8601.readthedocs.io/en/v1.0.0/
aniso8601.parse_date('20220102')
aniso8601.parse_date('2022-01-02')
aniso8601.parse_date('2022-W14-1') # ISO 8601 week date format
aniso8601.parse_date('2022-144')   # ISO 8601 ordinal date

# %% [raw]
# as.Date('2021002', format='%Y%j'); as.Date(parse_iso_8601('2021002'))
# as.Date('2021-002', format='%Y-%j'); as.Date(parse_iso_8601('2021-002'))

# %%
parser.parse('2022002') # ParseError: year 2022002 is out of range
# 2022년 00월은 존재하지 않으니까?

# %%
datetime.datetime.strptime('2022002', '%Y%j')
datetime.datetime.strptime('2022-002', '%Y-%j')
aniso8601.parse_date('2022002')   
aniso8601.parse_date('2022-002')   

# %% [raw]
# as.Date(parse_iso_8601('2020W536'))
# as.Date(parse_iso_8601('2020-W53-6'))

# %%
# https://stackoverflow.com/questions/304256/whats-the-best-way-to-find-the-inverse-of-datetime-isocalendar
datetime.datetime.strptime('2020W536', '%GW%V%u')
datetime.datetime.strptime('2020-W53-6', '%G-W%V-%u')
aniso8601.parse_date('2020W536')
aniso8601.parse_date('2020-W53-6')

# %%
#datetime.datetime.fromisocalendar() 를 사용하기
import regex
patt = regex.compile('(W|(?<=W\\d)(?=\\d{2}\\b))')
patt = regex.compile('W')
patt = regex.compile(r'(?<=\b\d{4})W(?=\d{3}\b)|(?<=\b\d{4}W\d{2})(?=\d{1}\b)')
patt = regex.compile(r'(?<=\D{0,1}\d{4})W(?=\d{3}\D{0,1})|(?<=\D{0,1}\d{4}W\d{2})(?=\d{1}\D{0,1})')
#                       ??? 이렇게 만들어 놓으니 읽기 엄청 불편...
[int(x) for x in patt.split('2020W536')]
lst = ['2020W536', ' 2020W536', '2020W536 ', '그 날은 2020W536', '2020W536에',
          '12020W555', '2020W5366', '2020W536-', '#2020W536@']
for y in lst:
    print([int(x) for x in patt.split(y)])

# %%
patt1 = regex.compile(r'(?<=^|\D)\d{4}W\d{3}(?=\D|$)')
#                        앞쪽이 처음이거나 숫자
#                        
#patt1.findall('12020W555')
patt2 = regex.compile(r'(?<=\d{4})W(?=\d{3})|(?<=\d{4}W\d{2})(?=\d{1})')
for x in lst:
    found = patt1.findall(x)
    if found:
        for y in found:
            print(x, found, [int(z) for z in patt.split(y)])
    else:
        print(x)

# %%
datetime.datetime.fromisocalendar(*[int(x) for x in patt.split('2020W536')])
datetime.date.fromisocalendar(*[int(x) for x in patt.split('2020W536')])
patt = regex.compile(r'(?<=\b\d{4})-W(?=\d{2}-\d{1}\b)|(?<=\b\d{4}-W\d{2})-(?=\d{1}\b)')
[int(x) for x in patt.split('2020-W53-6')]
datetime.date.fromisocalendar(*[int(x) for x in patt.split('2020-W53-6')])

# %%
patt1 = regex.compile(r'\d{4}-W\d{2}-\d{1}')
patt2 = regex.compile(r'(?<=\d{4})-W(?=\d{3})|(?<=\d{4}-W\d{2}-)(?=\d{1})')
lst = ['2020-W53-6', ' 2020-W53-6', '2020-W53-6 ', '그 날은 2020-W53-6', '2020-W53-6에',
          '12020-W55-5', '2020-W53-66', '2020-W53-6-', '#2020-W53-6@']
for x in lst:
    for y in patt1.findall(x):
        print([int(z) for z in patt.split(y)])

# %% [raw]
# ???

# %% [raw]
# library(magrittr)
# as.Date('Jan 01 2020', format='%b %d %Y')
# as.Date('January 01 2020', format='%B %d %Y')
# Sys.getlocale("LC_ALL") %>% strsplit(";")

# %%
import datetime
import locale
#??? locale setting
#!!! locale을 변경하는 데에 따르는 문제점?
datetime.datetime.strptime('Jan 01 2020', '%b %d %Y')

# %%
datetime.datetime.strptime('January 01 2020', '%B %d %Y')

# %%
#locale.setlocale('')
from dateutil import parser 
parser.parse('Jan 01 2020')
parser.parse('January 01 2020')
locale.getlocale(locale.LC_ALL)
# initial setting : ('C/ko_KR', 'UTF-8/C/C/C/C')

# %% [raw]
# Sys.setlocale("LC_ALL", "English") %>% strsplit(";")
# as.Date('Jan 01 2020', format='%b %d %Y')
# as.Date('January 01 2020', format='%B %d %Y')

# %%
#locale.setlocale(locale.LC_ALL, 'English') # mac: unsupported locale setting
# for windows?
#locale.setlocale(locale.LC_ALL, 'EN') # mac: unsupported locale setting

# %%
# locale -a 로 나오는 code
# ex. fr_FR.UTF-8
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
datetime.datetime.strptime('Jan 01 2020', '%b %d %Y')
datetime.datetime.strptime('January 01 2020', '%B %d %Y')

# %%
datetime.date(2020,3,1).strftime("%Y %b %d")

# %%
#Sys.setlocale("LC_ALL", "Korean") %>% strsplit(";")
#as.Date('March 01 2020', format='%B %d %Y')
#as.Date('Mars 01 2020', format='%B %d %Y') 

locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')



datetime.datetime.strptime('2020년 3월 1일', '%Y년 %B %d일')
#datetime.datetime.strptime('2020년 3월 1일', '%Y년 %b월 %d일')
# ValueError: time data '2020년 3월 1일' does not match format '%Y년 %b 월 %d일'

# # %B = 3월
# # %b = 3
# !!!주의 : 아래와 같이 쓰면 안된다 
# datetime.datetime.strptime('2020년 3월 1일', '%Y년 %b월 %d일')
# parser.parse('2020년 3월 1일')
# parser.parse('2020 3월 1')

# %%
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
datetime.datetime.strptime('March 01 2020', '%B %d %Y')
# ValueError: time data 'March 01 2020' does not match format '%B %d %Y'
datetime.datetime.strptime('Mars 01 2020', '%B %d %Y')
# ValueError: time data 'Mars 01 2020' does not match format '%B %d %Y'

# %%
parser.parse('March 01 2020')
parser.parse('Mars 01 2020', fuzzy = True) # WRONG

# %%
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
parser.parse('March 01 2020')
locale.setlocale(locale.LC_ALL, '') # back to default

# %%
import icu  # PyICU

# %% [raw]
# # icu 설치 방법(mac)
# arch -arm64 brew install icu4c
#
# echo 'export PATH="/opt/homebrew/opt/icu4c/bin:$PATH"' >> ~/.zshrc
# echo 'export PATH="/opt/homebrew/opt/icu4c/sbin:$PATH"' >> ~/.zshrc
# # or compilers to find icu4c you may need to set:
# export LDFLAGS="-L/opt/homebrew/opt/icu4c/lib"
# export CPPFLAGS="-I/opt/homebrew/opt/icu4c/include"
#
# # https://pypi.org/project/PyICU/
# arch -arm64 brew install icu4c
# arch -arm64 brew install pkg-config
# export PATH="/usr/local/opt/icu4c/bin:/usr/local/opt/icu4c/sbin:$PATH"
# #export PKG_CONFIG_PATH="$PKG_CONFIG_PATH:/usr/local/opt/icu4c/lib/pkgconfig"
# export PKG_CONFIG_PATH="/opt/homebrew/opt/icu4c/lib/pkgconfig"
#
# export CC="$(which gcc)" CXX="$(which g++)"
#
# export PYICU_CFLAGS=-std=c++11
# pip install --no-binary=:pyicu: pyicu # Success

# %%
df = icu.SimpleDateFormat(
               'MMM dd yyyy', icu.Locale('fr_FR'))
ts = df.parse(u'Mars 01 2020')
print(datetime.datetime.utcfromtimestamp(ts))

# %%
df = icu.SimpleDateFormat(
               'EEE, dd MMM yyyy HH:mm:ss zzz', icu.Locale('pt_BR'))
ts = df.parse(u'Ter, 01 Out 2013 14:26:00 -0300')
print(datetime.datetime.utcfromtimestamp(ts))

# %%
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
datetime.datetime.strptime('Mars 01 2020', '%B %d %Y')

# %% [markdown]
# ### 참고  

# %% [markdown]
# * https://stackoverflow.com/questions/55532672/python-how-to-set-french-locale
# * https://stackoverflow.com/questions/955986/what-is-the-correct-way-to-set-pythons-locale-on-windows/956084#956084
# * https://docs.microsoft.com/en-us/cpp/c-runtime-library/locale-names-languages-and-country-region-strings?view=msvc-160&viewFallbackFrom=vs-2019
# * https://www.rfc-editor.org/info/bcp47

# %% [raw]
# install.packages("lubridate")
# ??? import Babel
#
# %conda install Babel
# Babel is an integrated collection of utilities that assist in internationalizing and localizing Python applications, with an emphasis on web-based applications.
# #http://babel.pocoo.org/en/latest/dates.html
# 날짜 문자열을 변환하는 함수는 없나?
#

# %% [raw]
# library(lubridate)

# %% [raw]
# mdy('March 01 2020')
# mdy('Mars 01 2020', locale='French') # locale을 설정하지 않고도! 
# Sys.setlocale("LC_ALL", "French") %>% strsplit(";")

# %%
import dateparser # $ pip install dateparser
dateparser.parse('March 01 2022').date()
dateparser.parse('Mars 01 2022').date()

# %%
dateparser.parse('2022년 3월 1일').date() # ERROR
# https://github.com/scrapinghub/dateparser/blob/8e91eb1a6d161a50b1869408c559dc605ef3583f/data/languages.yaml#L207

# %%
# 한글 지원이 되지 않는 듯
# 하지만 한글은 크게 쓸모가 없음
dateparser.parse('2020년 3월 2일', 
date_formats=['%Y년 %m월 %d일'], languages=['ko'])#, locales=['ko-KR'])
dateparser.parse('Mars 01 2020', 
date_formats=['%A %m %Y'], languages=['fr'])#, locales=['ko-KR'])

# %%
import parsedatetime as pdt # $ pip install parsedatetime pyicu
# pyicu 설치가 쉽지 않음

# %%
calendar = pdt.Calendar(pdt.Constants(localeID='fr', usePyICU=True))
for date_string in [u"Aujourd'hui", "3 juillet", u"4 Août", u"Hier"]:
    dt, success = calendar.parseDT(date_string)
    if success:
       print(date_string, dt.date())

# %%
# https://stackoverflow.com/questions/26294333/parse-french-date-in-python
for date_string in [u"Aujourd'hui", "3 juillet", u"4 Août", u"Hier"]:
    print(dateparser.parse(date_string).date())

# %% [raw]
# as.Date('Mars 01 2020', format='%B %d %Y')
# as.Date('March 01 2020', format='%B %d %Y')
# mdy('March 01 2020')
# mdy('Mars 01 2020')

# %%
locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
#locale.setlocale(locale.LC_ALL, "")
datetime.datetime(2022, 3,1).strftime('%Y-%B(%b)-%d %A %a')
datetime.datetime.strptime('mars 01 2022', '%B %d %Y')
dateparser.parse('Mars 01 2020', languages=['fr'])
# https://dateparser.readthedocs.io/en/latest/

# %%
# timezone도 가능
dateparser.parse('March 01 2020 EST', languages=['en'])
dateparser.parse('March 01 2020 KST', languages=['en'])
dateparser.parse('March 01 2020 17:00:00+09:00', languages=['en'])

# %%
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
datetime.datetime(2022, 3,1).strftime('%Y-%B(%b)-%d %A %a')
datetime.datetime.strptime('March 01 2022', '%B %d %Y')
dateparser.parse('March 01 2020')

# %%
locale.setlocale(locale.LC_ALL, "ko_KR.UTF-8")
datetime.datetime(2022, 3,1).strftime('%Y-%B(%b)-%d %A %a')
datetime.datetime.strptime('3월 01 2022', '%B %d %Y')
dateparser.parse('2020년 3월 01일') # None!
dateparser.parse('2020 3월 01')

# %% [raw]
# Sys.setlocale("LC_ALL", "Korean") %>% strsplit(";")
# mdy('Mars 01 2020', locale='French_France.1252')

# %%
#wday(today(), label = TRUE, abbr = FALSE, locale = "German")
#wday(today(), label = TRUE, abbr = FALSE, locale = "French")
#month(today(), label = TRUE, abbr = FALSE, locale = "German")
#month(today(), label = TRUE, abbr = FALSE, locale = "French")
locale.setlocale(locale.LC_ALL, "") # default
locale.getlocale()
today = datetime.datetime.today()
today.weekday() # 1


# %% [raw]
# %U : Week number of the year(Sunday as the first day, w00 for the days before the first Sunday)
# %W : Week number(Monday as the first day)
# %w : Week day(0-6, 0=Sunday)
# %u : Week day(1-7, 1=Monday)
# %w와 %u는 일요일이 0이냐, 7이냐만 다르다.

# %%
import pandas as pd

# %%
for x in pd.date_range('2021-12-25', '2022-01-05'):
    #print(x)
    #print(type(x))
    #print(x.to_pydatetime())
    x2 = x.to_pydatetime()
    print(x2.strftime('%Y-%m-%d %Y %B %d(%A) %Y-%U-%w %Y-%W-%u %G-W%V-%u(ISO 8601)'))

# %% [raw]
# today.strftime('%Y-%U-%w %Y-%W-%u %G-W%V-%u(ISO 8601)')

# %%
today.strftime('%A')
today.month

# %%
from babel.dates import format_date

# %%
format_date(today, locale = 'ko')
format_date(today, locale = 'en')
format_date(today, locale = 'ja')
format_date(today, locale = 'zh')
format_date(today, locale = 'es')
format_date(today, locale = 'fr')
format_date(today, locale = 'de')

# %%
format_date(today, format = 'E EE EEE EEEE EEEE', locale='en')
# format = 'E' 
#  weekday : Day of week. 
# Use one through three letters for the short day, 
# or four for the full name, 
# or five for the narrow name.
format_date(today, format = 'E EE EEE EEEE EEEE', locale='ko')
format_date(today, format = 'E EE EEE EEEE EEEE', locale='ja')
format_date(today, format = 'E EE EEE EEEE EEEE', locale='zh')
format_date(today, format = 'E EE EEE EEEE EEEE', locale='es')
format_date(today, format = 'E EE EEE EEEE EEEE', locale='fr')
format_date(today, format = 'E EE EEE EEEE EEEE', locale='de')
# https://www.science.co.il/language/Locale-codes.php
# ko = korean, ja = japanese, zh = chinese
# es = spanish(Espanol), fr = french, de = deutch(Germany)

# %%
format_date(today, format = 'M MM MMM MMMM MMMMM', locale='ko')
format_date(today, format = 'M MM MMM MMMM MMMMM', locale='ja')
format_date(today, format = 'M MM MMM MMMM MMMMM', locale='zh')
format_date(today, format = 'M MM MMM MMMM MMMMM', locale='en')
format_date(today, format = 'M MM MMM MMMM MMMMM', locale='es')
format_date(today, format = 'M MM MMM MMMM MMMMM', locale='fr')
format_date(today, format = 'M MM MMM MMMM MMMMM', locale='de')
# M or MM : numerical form, 
# MMM : abbreviation, MMMM : full name,
# MMMMM : narrow name


# %%
format_date(today, format = 'LLL LLLL LLLLL', locale='ko')
format_date(today, format = 'LLL LLLL LLLLL', locale='ja')
format_date(today, format = 'LLL LLLL LLLLL', locale='zh')
format_date(today, format = 'LLL LLLL LLLLL', locale='en')
format_date(today, format = 'LLL LLLL LLLLL', locale='es')
format_date(today, format = 'LLL LLLL LLLLL', locale='fr')
format_date(today, format = 'LLL LLLL LLLLL', locale='de')

# %%
import pytz

# %%
#Sys.setlocale("LC_ALL", "English") %>% strsplit(";")
#as.POSIXct('March 01 2020 11:13:22', format='%B %d %Y %H:%M:%S')
#strptime('March 01 2020 11:13:22', format='%B %d %Y %H:%M:%S')
#mdy_hms('March 01 2020 11:13:22')
#mdy_hms('March 01 2020 11:13:22', tz='Asia/Seoul')
locale.setlocale(locale.LC_ALL, 'en_US')
datetime.datetime.strptime('March 01 2022 11:14:44', '%B %d %Y %H:%M:%S')
pytz.timezone('Asia/Seoul').localize(
    datetime.datetime.strptime('March 01 2022 11:14:44', '%B %d %Y %H:%M:%S'))

# %% [raw]
# Sys.setlocale("LC_ALL", "French") %>% strsplit(";")
# as.POSIXct('Mars 01 2020 11:13:22', format='%B %d %Y %H:%M:%S')
# strptime('Mars 01 2020 11:13:22', format='%B %d %Y %H:%M:%S')
# mdy_hms('Mars 01 2020 11:13:22')
# mdy_hms('Mars 01 2020 11:13:22', tz='Asia/Seoul')

# %% [raw]
# Sys.setlocale("LC_ALL", "Korean") %>% strsplit(";")

# %% [markdown]
# # 6.4

# %% [raw]
# t0 <- Sys.time()
# t1 <- as.POSIXct("2030-01-01 00:00:00")
# t1-t0
# difftime(t1, t0, units='weeks')
# difftime(t1, t0, units='hours')

# %%
t0 = datetime.datetime.now()
t1 = datetime.datetime(2030,1,1)
t1-t0
(t1-t0).days % 7
(t1-t0).total_seconds() / (60*60)  # 60*60 seconds = 1 hour

# %% [raw]
# ???
# t0s <- format(t0, format="%Y-%m-%d %H:%S:%M")
# t1s <- format(t1, format="%Y-%m-%d %H:%S:%M")
# t1s-t0s
# difftime(t1s, t0s, units='weeks')
# difftime(t1s, t0s, units='hours')


# %% [markdown]
# # 6.5

# %% [raw]
# # 함수                       의미                              지역설정
# # julian(x)                1970년 1월 1일 이후 몇번째의 일     "Korean"
# # julian(x, origin = )     origin 이후 몇번째 일               "Korean"
# # quartes(x)               분기(Q1, Q2, Q3, Q4)                "Korean"
# # months(x)                월(1월, 2월, 3월, ...)              "Korean"
# # months(x)                월(January, Februrary, March, ...)  "English"
# # months(x, abbr = TRUE)   월(1, 2, 3, ...)                    "Korean"
# # months(x, abbr = TRUE)```월(Jan, Feb, Mar, ...)              "English"
# # weekdays(x)              요일(월요일, 화요일, 수요일,..)     "Korean"
# # weekdays(x)              요일(Monday, Tuesday, Wednesday, ...)"English"
# # weekdays(x, abbr =TRUE)  요일(월, 화, 수, ...)               "Korean"
# # weekdays(x, abbr =TRUE)  요일(Mon, Tue, Wed,...)             "English"


# %% [markdown]
# # 6.6

# %% [raw]
# # 함수     의미              
# # year()   년
# # month()  월
# # week()   주
# # yday()   (년 중) 일(1-366)
# # mday()   (월 중) 일(1-31)
# # day()    (월 중) 일
# # yday()   (주 중) 일(1-7, 1:일)
# # hour()   시
# # minute() 분
# # second() 초
# # tz()     타임존
# # dst()    써머타임(Daylight Saving Time)의 여부

# %% [raw]
# # Daylight-Saving Time?
# # https://stackoverflow.com/questions/12203676/daylight-savings-time-in-python
# %%


# %% [raw]
# t <- Sys.time()
# t
# year(t); year(t) <- 2030; t
# month(t); month(t) <- 1; t
# week(t); week(t) <- 2; t
# day(t); day(t) <- 2; t

# %%
import datetime
t = datetime.datetime.now()
t.year
t = t.replace(year = 2030) # ??? inplace???
t.month
t = t.replace(month = 1)
#t.week # NOT working
#t.isocalendar() # year, weeknumber, weekday
t.isocalendar()[1] # weeknumber
#t.isocalender().week
t.strftime('%W') 
t.strftime('%U') 
t.strftime('%V')


# %% [raw]
# %U : Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
# %W : Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
# %V : ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4.

# %%
t.day
t = t.replace(day=2)

# %% [raw]
# yday(t); yday(t) <- 1; t
# yday(t); yday(t) <- 366; t
# mday(t); mday(t) <- 2; t # same as day(t)
# wday(t); wday(t) <- 3; t
# wday(t, label=TRUE); wday(t); 
# wday(t) <- 1; t 

# %%
t.strftime('%j')

# %% [raw]
# hour(t); hour(t) <- 12; t
# minute(t); minute(t) <- 41; t
# second(t); second(t) <- 12; t
# tz(t) ; tz(t) <- "GMT"; t
# dst(t)
# dst(t) <- TRUE
# t

# %%
t = t.astimezone(pytz.timezone('Asia/Seoul'))
t.hour; t2 = t.replace(hour=12); t2
t.minute; t2 = t.replace(minute=41); t2
t.second; t2 = t.replace(second = 12); t2
t.tzinfo; t2 = t.replace(tzinfo=None).astimezone(pytz.timezone('GMT')); t2
#pytz.timezone('GMT').localize(t.replace(tzinfo=None))
t.dst() # ??? dst는 시간과 timezone에 의해 결정되므로 바꿀 수 없을 듯??? 

# %% [raw]
# format(as.Date(parse_iso_8601('2020-W53-6')), "%A")
# options('lubridate.week.start'=1) 
# wday(as.Date(parse_iso_8601('2020-W53-6'))) 
# options('lubridate.week.start'=2) 
# wday(as.Date(parse_iso_8601('2020-W53-6')))


# %% [raw]
# t <- Sys.time()
# t
# tz(t) <- "GMT" # 또는 force_tz(t, tzone="GMT")
# t
# with_tz(t, "Asia/Seoul")

# %%
import datetime
t = datetime.datetime.now()
t
import pytz
pytz.all_timezones
pytz.timezone('GMT').localize(t)
datetime.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second, t.microsecond, 
                  tzinfo = datetime.timezone(datetime.timedelta(hours=0)))
pytz.timezone('GMT').localize(t) == \
    datetime.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second, t.microsecond, 
                  tzinfo = datetime.timezone(datetime.timedelta(hours=0)))

# %%
tzKST = pytz.timezone('Asia/Seoul')  # Korea Standard Time
tzKST.localize(t) == \
    datetime.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second, t.microsecond, 
                  tzinfo = datetime.timezone(datetime.timedelta(hours=9)))

# %%
t.replace(tzinfo = tzKST)
t.replace(tzinfo = datetime.timezone(datetime.timedelta(hours=9)))
t.replace(tzinfo = tzKST) == \
    t.replace(tzinfo = datetime.timezone(datetime.timedelta(hours=9)))
# !!! False 
# !!! Bug?  LMT+8:28:00

# %% [markdown]
# * https://stackoverflow.com/questions/11473721/weird-timezone-issue-with-pytz?noredirect=1&lq=1
# * https://en.wikipedia.org/wiki/Tz_database#Example_zone_and_rule_lines

# %%
t.astimezone(tzKST)
t.astimezone(datetime.timezone(datetime.timedelta(hours=9)))

# %%
t2a = t.astimezone(tzKST)
t2b = t.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
t2a == t2b
# !!! True

# %%
t2a.astimezone(pytz.timezone('UTC'))
t2b.astimezone(datetime.timezone(datetime.timedelta(hours=0)))
t2b.astimezone(datetime.timezone.utc)
# 참고 : https://brownbears.tistory.com/356

# %% [raw]
# strftime.org 

# %%
# source의 확장성
datetime.datetime.now() # 그 지역의 날짜로 표시
datetime.datetime.utcnow().astimezone(tzKST) # 어디에서도 한국 시간

# %% [raw]
# last friday?
# iso format에서 다시 iso format으로???

# %%
#t0 <- as.POSIXct("2021-01-01 13:00:00", tz='Europe/Paris'); t0
#t1 <- t0; tz(t1) <- "Asia/Seoul"; t1
#t2 <- with_tz(t1, tzone='Europe/Paris'); t2
#t3 <- t2; hour(t3) <- hour(t3) + 7; t3
#t4 <- with_tz(t3, tzone='Asia/Seoul'); t4
tzParis = pytz.timezone('Europe/Paris')
t0 = tzParis.localize(datetime.datetime(2021,1,1,5,54,0))
datetime.datetime(2021,1,1,23,54,0, tzinfo=tzParis) # logical ERROR
datetime.datetime(2021,1,1,23,54,0).replace(tzinfo=tzParis) # logical ERROR
t1 = t0.replace(tzinfo=None).astimezone(pytz.timezone('Asia/Seoul'))
t1
t2 = t1.astimezone(pytz.timezone('Europe/Paris'))
t2
t3 = t2; 
t3
#t3.hour = t3.hour + 7 # ERROR
#t3.replace(hour = t3.hour + 7) # possibly ERROR
# hour must be in 0..23
t3 = t3 + datetime.timedelta(hours = 7)
t3
t4 = t3.astimezone(pytz.timezone('Asia/Seoul'))
t4

# %%
print(t1)
print(t2)
t1 == t2
t1.strftime('%Y-%m-%d %H:%M:%S %Z')
t2.strftime('%Y-%m-%d %H:%M:%S %Z') # CET : Central Europe Time?

# %% [markdown]
# # pandas

# %%
t = pd.to_datetime(0, origin='2020/01/01', unit='D')
## type(t) == <class 'pandas._libs.tslibs.timestamps.Timestamp'>
t.isoweekday()
t.dayofweek

# %%
ser = pd.Series(t)
[x for x in set(dir(t)) - set(dir(ser)) if not x.startswith('_')]
# ['isoformat', 'dayofyear', 'year', 'to_julian_date', 'normalize', 'now', 'weekday', 'to_datetime64', 'value', 'daysinmonth', 'day', 'today', 'timestamp', 'timetuple', 'isocalendar', 'fromisoformat', 'day_of_week', 'tzinfo', 'month', 'strftime', 'day_name', 'resolution', 'microsecond', 'week', 'second', 'is_year_start', 'tz', 'strptime', 'asm8', 'utcoffset', 'days_in_month', 'timetz', 'astimezone', 'is_quarter_end', 'fromtimestamp', 'freq', 'weekofyear', 'is_quarter_start', 'dst', 'to_pydatetime', 'time', 'utcfromtimestamp', 'fromisocalendar', 'isoweekday', 'is_year_end', 'dayofweek', 'is_month_start', 'utctimetuple', 'toordinal', 'ctime', 'floor', 'month_name', 'fold', 'date', 'nanosecond', 'is_leap_year', 'fromordinal', 'utcnow', 'ceil', 'freqstr', 'tzname', 'quarter', 'hour', 'minute', 'day_of_year', 'is_month_end']
[x for x in set(dir(ser)) - set(dir(t)) if not x.startswith('_')]

# %%
[x for x in set(dir(ser.dt)) - set(dir(t)) if not x.startswith('_')]
# []
[x for x in set(dir(t)) - set(dir(ser.dt)) if not x.startswith('_')]
# ['isoformat', 'max', 'to_julian_date', 'fold', 'now', 'resolution', 'fromordinal', 'to_datetime64', 'utcnow', 'combine', 'value', 'min', 'today', 'dst', 'freqstr', 'strptime', 'tzname', 'timestamp', 'timetuple', 'asm8', 'utcfromtimestamp', 'utcoffset', 'to_numpy', 'fromisocalendar', 'replace', 'isoweekday', 'fromisoformat', 'tzinfo', 'utctimetuple', 'toordinal', 'astimezone', 'ctime', 'fromtimestamp']
[x for x in set(dir(t)).intersection(set(dir(ser.dt))) if not x.startswith('_')]
# ['month_name', 'dayofyear', 'year', 'freq', 'normalize', 'date', 'nanosecond', 'weekday', 'day_name', 'is_leap_year', 'weekofyear', 'round', 'microsecond', 'daysinmonth', 'day', 'week', 'second', 'is_quarter_start', 'is_year_start', 'tz', 'ceil', 'to_pydatetime', 'time', 'isocalendar', 'tz_convert', 'to_period', 'quarter', 'is_year_end', 'dayofweek', 'tz_localize', 'day_of_week', 'is_month_start', 'month', 'days_in_month', 'hour', 'minute', 'timetz', 'strftime', 'day_of_year', 'is_month_end', 'is_quarter_end', 'floor']
[x for x in set(dir(t)).intersection(set(dir(ser.dt))) if x.startswith('day')]

# %%
ser = pd.Series(pd.date_range('2021-08-13', '2021-08-17'))
ser.dt.month_name()
t.month_name()
ser.dt.day_name()

# %%
ser.dt.dayofyear   # ser.dt.day_of_year
ser.dt.daysinmonth # ser.dt.days_in_month
ser.dt.dayofweek   # ser.dt.day_of_week
ser.dt.day         # day of month


# %% [raw]
# tz_localize('KST')가 아니라 tz_localize('Asia/Seoul')로 써야 함
# holiday 확인하기?
# gregorian and julian calendar : https://keisan.casio.com/exec/system/1227757509
#

# %%
def without_underbar(s):
    return [x for x in s if not x.startswith('_')]

# %% [markdown]
# # Reference
# * https://stackoverflow.com/questions/17976063/how-to-create-tzinfo-when-i-have-utc-offset
# * https://www.kite.com/python/docs/pytz.FixedOffset
# * https://www.programcreek.com/python/example/50095/pytz.FixedOffset
# * https://stackoverflow.com/questions/3305413/python-strptime-and-timezones
# * https://stackoverflow.com/questions/1703546/parsing-date-time-string-with-timezone-abbreviated-name-in-python
# * https://stackoverflow.com/questions/13707545/linux-convert-timefor-different-timezones-to-utc/13713813#13713813

# %%

# %%


# %% [markdown]
# ## Questions?
#
# timedelta에서 왜 days, seconds, microseconds밖에 없는가?
# 분, 시간은 항상 60seconds, 60*60seconds가 아니다?

# %%
for iyear in range(1990, 2030):
    delT = datetime.datetime(iyear+1, 1, 4, 14, 2,2, 142) - \
        datetime.datetime(iyear, 1, 4, 14, 2,2, 142)
    if delT != datetime.timedelta(days=365) and delT != datetime.timedelta(days=366):
        print(iyear)

# %%
delTs = []
iyear = 2015
for imonth in range(1,13):
    #datetime.datetime(iyear, imonth, 1).days_in_month
    ndays = pd.Series(datetime.datetime(iyear, imonth, 1)).dt.days_in_month.item()
    for iday in range(1, ndays):
        t = datetime.datetime(iyear, imonth, iday, 14, 2,2, 142)
        delT = t.replace(day=t.day+1) -t
        #print(delT)
        delTs.append(delT)
        #if delT != datetime.timedelta(days=365) and delT != datetime.timedelta(days=366):
        #    print(iyear)

# %%
ser = pd.Series(delTs)
ser.value_counts()

# %%
# leap second : 2015-06-30
# does not account for leap second!!!
# https://stackoverflow.com/questions/9306328/why-python-time-has-61-seconds
# https://stackoverflow.com/questions/21027639/python-datetime-not-accounting-for-leap-second-properly
datetime.datetime(2015, 7, 1, 0, 0)-datetime.datetime(2015, 6, 30, 23,0)
datetime.datetime(2015, 6, 30, 23, 0)-datetime.datetime(2015, 6, 30, 22,0)


# %% [markdown]
# # pandas datetime의 강점

# %%
import pandas as pd
d = pd.to_datetime(['2021-01-04', '2022-04-01'])
d >= '2022'  # 그냥 이렇게 쓸 수 있다! d가 datetime이고 '2022'이 문자열이지만!
d >= pd.to_datetime('2022-01-01')
# datetime이 index일 때도 비슷하게 사용 가능...
# slicing도 가능

# %% [raw]
# .resample
# .groupby 를 datetime에 특수한 방법으로 사용
#
# ex) df.resample('D').agg({'Close':'mean', 'High':'max', 'Low':'min', 'Volume':'sum'})


# %% [markdown]
# ### 부록

# %%
import time
time.localtime()

# %% [raw]
# timeNow <- Sys.time()
# print(timeNow)
# class(timeNow)

# %%
import datetime
timeNow = datetime.datetime.now()
# almost the same result
#  datetime.datetime.toda|y()
#  datetime.datetime.utcnow()
print(timeNow)
type(timeNow)
timeNow

# %% [raw]
# unclass(dateNow); print.default(dateNow)
# unclass(timeNow); print.default(timeNow)

# %%
print(timeNow.timestamp()) # POSIX timestamp
import time
time.time() #  timestamp of current time

# %%

# %%
