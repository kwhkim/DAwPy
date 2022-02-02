# -*- coding: utf-8 -*-


# +
# https://ellun.tistory.com/320
# -

# 소인 : 소인이라 함은 일반적으로 우체국에서 사용했다는 표시로 엽서나 우표 따위에 찍는 도장이나 찍는 일을 의미
# 통신우편 날짜 도장이란 우표를 다시 사용할 수 없도록 하면서 우편물 접수일자를 증명하기 위해 우체국에서 우표 위에 찍는 도장을 말하며, 통신우편 날짜 도장을 찍는 것을 일반적으로 소인이라고 합니다.
# timestamp : 


# Y2K, 밀레니엄 버그
# 
# 컴퓨터 200년 인식 오류 대란
#
# 2038 bug
# 날짜를 어떻게 저장할 것인가?
# 

# `datetime`, `numpy`, `pandas` 모듈

import pandas as pd
import numpy as np

pd.Timestamp # 약칭인 듯?`
# pandas._libs.tslibs.timestamps.Timestamp

pd.Timestamp is pd._libs.tslibs.timestamps.Timestamp

#help(pd.Timestamp) # class
help(pd.to_datetime) # function

a = np.datetime64('2012-10-14')
b = np.datetime64('2011-10-14')

a-b

a2 = pd.Series(a)
b2 = pd.Series(b)

(a2-b2)

(a2-b2)[0].to_pytimedelta()

dir(a2-b2)

dir((a2-b2)[0])

x=1; y=2; z=3; print(f"{x}, {y}, {z}")

print("{} {} {}".format(*(x,y,z)))


def tup_to_datetime(*args):
    if len(args) == 6:
        return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*args)
    elif len(args) == 5:
        return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}".format(*args)        
    elif len(args) == 4:
        return "{:04d}-{:02d}-{:02d} {:02d}".format(*args)        
    elif len(args) == 3:
        return "{:04d}-{:02d}-{:02d}".format(*args)                
    elif len(args) == 2:
        return "{:04d}-{:02d}".format(*args)
    elif len(args) == 1:
        return "{:04d}".format(*args)
    else:
        raise ValueError("! NOT supported format. Supported format is YYYY-mm-dd HH:MM:SS")
    


tup_to_datetime(2022,1,4), tup_to_datetime(2014,5,8,14,3), tup_to_datetime(2019,8)


def np_datetime(x):
    res = []
    if isinstance(x, list):
        for y in x:
            res.append(tup_to_datetime(*y))
    else:
        res.append(tup_to_datetime(*x))
    print(res)
    return np.array(res, dtype='datetime64')


np_datetime((2014,5,8,14,3))

np_datetime([(2014,5,8,14,3), 
             (2012,6,4),
             (2014,3,2)])

pd.Timestamp(2014,5,8,14,3)


def pdTimestamp(*args):
    res = []
    if len(args) == 1:
        if isinstance(args[0], list):
            for y in args[0]:
                res.append(pd.Timestamp(*y))
            return pd.Series(res)
        elif isinstance(args[0], tuple):
            return pd.Timestamp(*args[0])
    else:
        return pd.Timestamp(*args)
            


pdTimestamp([(2014,5,8,14,3), (2012,6,4)])

pdTimestamp([(2014,5,8,14,3)])

pdTimestamp((2014,5,8,14))

pdTimestamp(2014,5,8,14,3)

# ## 생성 
#
# !!! meta package?!!!
# ### 년,월,일,시,분,초
# * `datetime.datetime` : `datetime.datetime(2022, 1, 14, 13, 15, 18)`
# * `numpy` : 없음
#     - `np_datetime([])`
# * `pd.to_Timestamp()`




## Epoch : 시간 기원
## http://www.ktword.co.kr/test/view/view.php?m_temp1=2706
## 여러 epoch:  https://en.wikipedia.org/wiki/Epoch_(computing)
## 뉴럴 넷 훈련에서 epochs?
## . a period of time marked by distinctive features, noteworthy events, changed conditions, etc.: an epoch of peace.
## 2. the beginning of a distinctive period in the history of anything.

## 매우 긴 시간...
## Geological Time?(지질학적 시간)

## Unix Epoch?

# Unix Epoch(aka POSIX Time), C, C++, ... : 1970-01-01
# MATLAB : BC 0000-01-01
# 

# 지질학적 시간, billions of years
# 천문단위(Astrological Unit)
# astrolomical time, geological time?

# Unix Tick Tocks to a Billion
# https://www.wired.com/2001/09/unix-tick-tocks-to-a-billion/

#







# 시간을 결정하는 요소들.
# 문화적 요소. 물리학적 요소.
# 동시성이란 개념도.
# 관찰자의 운동 속도에 따라 달라진다.
# 역사학자들의 농간.
# 갈릴레오와 뉴턴의 생일과 사망일
# 지구는 태양 주위를 돌고 있으며,
# 태양은 은하의 중심을 돌고 있다.
#

# 주로 연결되는 부분.
#   file modified, created, ...
#   

# timeanddate.com : 각국의 공휴일
#   2000년 이후 가능

# modules
#  datetime, date, time, dateutil, calendar

# These tzinfo objects capture information 
#  about the offset from UTC time, 
#  the time zone name, 
#  and whether daylight saving time is in effect.

# 북한의 시간대 변경: https://www.bbc.com/korean/news-43945658
# datetime.tzinfo와 datetime.timezone의 차이는?

# d.tzinfo
# d.tzinfo.utcoffset(None)

import datetime
dtdelta = datetime.datetime(2021,8,8,15,9) - datetime.datetime(2021,8,8,12,10)
# class attributes
dir(dtdelta)
dtdelta.min, dtdelta.max # class attributes

# 현재 시간을 확인하는 방법
import datetime, time
datetime.datetime.now()
# datetime.datetime(2021, 8, 8, 15, 23, 46, 263619)
datetime.datetime.utcnow()
# This is like now(), 
# but returns the current UTC date and time, as a naive datetime object.
# the same as datetime.now(timezone.utc), but this is aware
datetime.datetime.now(datetime.timezone.utc)
datetime.datetime.today()
# datetime.datetime.fromtimestamp(time.time()) 과 동일
datetime.datetime.fromtimestamp(time.time())
time.time() # POSIX timestamp
# 1628403834.236213

td = datetime.datetime.now()
td.replace(year=2010)
td.replace(month=3)
td.replace(day=3)
td.replace(hour = 3)
td.replace(minute=20)
td.replace(second = 10)

td.replace(year = -1)
# ValueError: year -1 is out of range
td.replace(second = -10)
# ValueError: second must be in 0..59
help(td.replace)

# locale
# 로케일의 핵심은 나라마다 표기가 다른 
# 인코딩(?), 문자의 순서(collate), 
# 날짜, 요일, 시간, 통화, 숫자 등을
# 그 나라의 표기법에 맞춰 표기하거나, 인식하는 것 

# locale
import locale
for x in locale.windows_locale.values():
    print(x.replace('_','-'))

locale.getlocale() # 'ko_KR', 'UTF-8'

# locale이 영향을 미치는 부분
import locale
import datetime
td = datetime.datetime.now()
td.strftime('%B %b %A %a')  # Month, Month(abbr), Weekday, Weekday(abbr)
#https://bugs.python.org/issue29457
locale.setlocale(locale.LC_ALL, '') # ko_KR.UTF-8
# get the locale setting from the environment
# https://docs.python.org/3/library/locale.html#background-details-hints-tips-and-caveats

td.strftime('%B %b %A %a')  
# now this produces "8월 8 월요일 월"
td.strftime('%x')  
td.strftime('%c')
# Have you tried enabling the locale with locale.setlocale()? I believe Python only enables LC_CTYPE by default, 
# so other locale aspects like LC_TIME won’t work until they are enabled.
# As Martin said, you need to set the LC_TIME category using an empty string to use the locale LC_* environment variables. Python 3 sets LC_CTYPE at startup (on Unix platforms only), 
# but LC_TIME is left in the initial C locale:

import pandas as pd
days = pd.date_range(start='2021-08-09', end='2021-08-15')
for day in days:
    print(day)
    print(type(day))
    td = datetime.datetime(day.year, day.month, day.day)
    td.strftime('%Y-%m-%d %H:%M:%S ')

# 2009 World Championships in Berlin
# 1	9.58	Usain Bolt	JAM	+0.9	WR
# 2	9.71	Tyson Gay	USA	+0.9	P2WR
# 3	9.84	Asafa Powell	JAM	+0.9	
# 4	9.93	Daniel Bailey	ANT	+0.9	
# 5	9.93	Richard Thompson	TTO	+0.9	
# 6	10.00	Dwain Chambers	GBR	+0.9	
# 7	10.00	Marc Burns	TTO	+0.9	P7WR

# 2021년 8월 9일 월요일은
# 2021년의 몇 번째 날이고
# 첫 번째 일요일을 첫 번째의 주의 시작이라고 했을 때, 2021년의 몇 번째 주이며,
# https://docs.python.org/3.6/library/datetime.html#strftime-strptime-behavior

# get locale은 'ko_KR', 'UTF-8'임에도
# 결과는 August Aug Monday Mon?
# macos의 terminal에서 locale -a
#        ls /usr/share/locale -lha
# 한국어의 경우 /usr/share/locale/ko_KR.UTF-8/LC_COLLATE, LC_CTYPE
#                                          LC_MESSAGES, LC_MONETARY
#                                          LC_NUMERIC, LC_TIME
#
#
# module babel?
#    The functionality Babel provides for internationalization (I18n) and 
#      localization (L10N) can be separated into two different aspects:


#https://minwook-shin.github.io/python-internationalization-library-using-babel/
from babel import Locale

locale = Locale('en', 'US')
print(locale.territories['US'])

locale = Locale('ko', 'KR')
print(locale.territories['US'])

# 각 나라의 이름을 특정 로케일에 맞춰 출력할 수 있다
# 일종의 번역
lang = Locale.parse('ko_KR')
print(lang.display_name)
print(lang.english_name)
print(lang.language)
print(lang.language_name)

locale = Locale('ko')
month_names = locale.months['format']['wide'].items()
for _, name in sorted(month_names):
    print(name)

month_names = locale.days['format']['wide'].items()
for _, name in sorted(month_names):
    print(name)


# module dateparser : https://dateparser.readthedocs.io/en/latest/
#  
import dateparser
dateparser.parse('2019년 2월 3일') # not working!
dateparser.parse('2019-09-02')
# supported locale? ko-KP?

# http://cldr.unicode.org



# key reference
# 1. python date/time : https://docs.python.org/3.8/library/datetime.html
# 2. python calendar : 
# 3. pandas datetime : https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html?highlight=holiday#time-zone-handling


# 수출입 물류 정보 커뮤니티 : https://www.forwarder.kr/curr/holiday.php?s=2019-03-06&continent=
#
#
# https://hwangheek.github.io/2020/pandas-custom-businessday-from-krx/
#     거래소의 휴장일?
#
# 구글 calender api : https://gipyeonglee.tistory.com/209
# 네이버 api? : 
# 특일 정보 제공 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221341051478
# http://astro.kasi.re.kr/information/pageView/31
# https://www.kotra.or.kr/kh/about/KHKINY150M.do?&MENU_CD=T0506&TOP_MENU_CD=T0500&LEFT_MENU_CD=T0506

# 휴일 캘린더 : https://kr.investing.com/holiday-calendar/
#              어제, 오늘, 내일, 이번 주, 다음 주
# 문화권마다 다른 새해 : https://www.hani.co.kr/arti/science/future/982752.html

# 국경일 : https://www.mois.go.kr/frt/sub/a06/b08/nationalHoliday/screen.do
# Resources : https://www.bydewey.com/time.html
# Britannica : Time & Calendar
#              https://www.britannica.com/science/calendar/Time-determination-by-stars-Sun-and-Moon
#              https://www.britannica.com/science/time/Lengths-of-years-and-months
#

# Working on time with python
# https://wiki.python.org/moin/WorkingWithTime

# Short history of measuring time
#     https://www.bsswebsite.me.uk/A%20Short%20History%20of/time.html
#
# https://www.nist.gov/pml/time-and-frequency-division/popular-links/walk-through-time/walk-through-time-ancient-calendars
# https://webspace.science.uu.nl/~gent0113/calendar/isocalendar.htm
# https://biega.com/time.shtml
# https://nrich.maths.org/6070
#
# https://www.nist.gov/si-redefinition/second-introduction
# http://www.exactlywhatistime.com/measurement-of-time/time-standards/

# Lanugage Identificaton
# https://datatracker.ietf.org/doc/html/rfc1766.html

# Related modules
# https://opensource.com/article/18/4/python-datetime-libraries

# https://docs.python.org/3/library/time.html
# https://docs.python.org/3.8/library/datetime.html
# https://www.tutorialspoint.com/python/python_date_time.htm
# https://realpython.com/python-datetime/
# https://www.geeksforgeeks.org/python-datetime-module/
# https://www.dataquest.io/blog/python-datetime-tutorial/

# 어떤 주제에 대해 읽어보면 좋을 사이트
# tutorialspoint.com
# realpython.com
# geeksforgeeks.org

# holidays
# https://publicholidays.co.kr/ko/2021-dates/ # 2018년부터 가능!
# https://www.abstractapi.com/holidays-api

# 특일 정보 활용
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221341051478


#https://hwangheek.github.io/2020/pandas-custom-businessday-from-krx/
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday

class ExampleCalendar(AbstractHolidayCalendar):
    rules = [
      Holiday('Example Holiday', month=3, day=21),
      Holiday('Another Example Holiday', year=2018, month=8, day=14),
    ]

## KRX 휴장일 정보
import re
import requests
import urllib
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday

results = {}  # {year: holidays_of_the_year_in_csv_format}

for year in range(2009, 2024+1):
    res_otp = requests.get(
        'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx',
        params={
            'name': 'fileDown',
            'filetype': 'csv',
            'url': 'MKD/01/0110/01100305/mkd01100305_01',
            'search_bas_yy': year,
        },
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    otp = res_otp.text
    
    res_csv = requests.post(
        'http://file.krx.co.kr/download.jspx',
        headers={
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://marketdata.krx.co.kr/mdi',
        },
        data=urllib.parse.urlencode({'code':otp})
    )
    
    results[year] = res_csv.text


holidays = []
for year in results:
    holidays.extend(
        re.findall(
            r'.*?\,(\d+)-(\d+)-(\d+)(?:\s\(.*?\))?\,(.*?)\s*\,(.*)',
            results[year]
        )
    )

holidays


# # pandas timezone
# # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html?highlight=holiday#time-zone-handling

import dateutil
import pandas as pd
rng_pytz = pd.date_range('3/6/2012 00:00', periods=3, freq='D', tz='Europe/London')
rng_pytz.tz # <DstTzInfo 'Europe/London' LMT-1 day, ...>

rng_dateutil = pd.date_range('3/6/2012 00:00', periods=3, freq='D', tz='dateutil/Europe/London')
rng_dateutil.tz # tzfile('Europe/Belfast')
#rng_dateutil.tz_localize('datetutil/Europe/London')  # tz-aware, use tz_convert
rng_dateutil = rng_dateutil.tz_convert('dateutil/Europe/London') 
rng_dateutil.tz

rng_utc = pd.date_range('3/6/2012 00:00', periods=3, freq='D', tz=dateutil.tz.tzutc())


# 정확한 현재 시각 맞추기
### Time Server?
# https://www.windowscentral.com/how-manage-time-servers-windows-10
# Type the address of Network Time Protocol (NTP) server. For example, 
# # if you want to use the Google Public NTP server, you can enter time.google.com
# 
# https://www.kriss.re.kr/standard/view.do?pg=standard_set_02
#   time.kriss.re.kr??? - SNTP (Simple Network Time Protocol)
#
# https://www.groovypost.com/howto/synchronize-clock-windows-10-with-internet-atomic-time/
# 
# https://answers.microsoft.com/en-us/windows/forum/all/how-to-force-windows-10-time-to-synch-with-a-time/20f3b546-af38-42fb-a2d0-d4df13cc8f43
# https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings


# Whats wrong with storing datetime in UTC?
#  - https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/
#  - http://www.creativedeletion.com/2015/03/19/persisting_future_datetimes.html
# [stop using utcnow & utcfromtimestamp](https://blog.ganssle.io/articles/2019/11/utcnow.html)
# 


# Problems ... Timezone
# [The Problem with Time & Timezones - Computerphile](https://www.youtube.com/watch?v=-5wpm-gesOY&ab_channel=Computerphile)
# [Why Leap Seconds Cause Glitches](https://www.youtube.com/watch?v=Uqjg8Kk1HXo&ab_channel=TomScott)
# [2038 problem](https://www.youtube.com/watch?v=QOeWxA9sXFY)


# [The Complexity of Time Data Programming](https://www.mojotech.com/blog/the-complexity-of-time-data-programming/)
# [North Korea changes its time zone to match South](https://www.bbc.com/news/world-asia-44010705)
# 

# https://www.guru99.com/date-time-and-datetime-classes-in-python.html

# DST? Timezone?
# https://www.prokerala.com/travel/timezones/Asia/Seoul?mode=history

