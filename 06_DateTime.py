
## 6

#dateNow <- Sys.Date()
#print(dateNow)
#class(dateNow)

import datetime
import sys

dateNow = datetime.date.today()
print(dateNow)
type(dateNow)

#timeNow <- Sys.time()
#print(timeNow)
#class(timeNow)

import datetime
timeNow = datetime.datetime.now()
# almost the same result
#  datetime.datetime.today()
#  datetime.datetime.utcnow()
print(timeNow)
type(timeNow)

#unclass(dateNow); print.default(dateNow)
#unclass(timeNow); print.default(timeNow)

timeNow.timestamp() # POSIX timestamp
import time
time.time() #  

## 6.1

## 6.1.1

## ISO 8601

## 스타일   표기            의미                     예
## 기본형 (+-)YYYYMMDD    년월일                  20200103
## 확장형 (+-)YYYY-MM-DD  년-월-일                2020-01-03
## 기본형 (+-)YYYYDDD     년일(1년의 몇번째 일)   2020003
## 확장형 (+-)YYYY-DDD    년-일(1년의 몇번째 일)  2020-003
## 기본형 (+-)YYYYWwwD    년주일                  2020W013
## 확장형 (+-)YYYY-Www-D  년-W주-일               2020-W01-3


## 6.1.2

## ISO 8601 시간

## 스타일     표기                      의미
## 기본형  hhmmss(,ss)(Z)(+-hh(:)mm)    시분초(,100분의 1초)(Z)(타임존)
## 확장형  hh:mm:ss(,ss)(Z)(+-hh(:)mm)  년-월-일(,100분의 1초)(Z)(타임존)

##6.2

#x <- Sys.time()
#
#format(x, '%Y-%m-%d %H:%M:%S')
#format(x, '%Y-%jT%H:%M:%S')
#format(x, '%G-W%V-%u %H:%M:%S')

x = datetime.datetime.now()
x.strftime('%Y-%m-%d %H:%M:%S')
x.strftime('%Y-%jT%H:%M:%S')
x.strftime('%G-W%V-%u %H:%M:%S')


## 기호   의미
## %Y     4자리 년
## %m     2자리 월
## %d     2자리 (월 중) 일(01-31)
## %H     2자리 시간(00-23)
## %M     2자리 분(00-59)
## %S     2자리 초(00-59)

## %j     3자리 (년 중) 일(001-366)
## 출처 : https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes

## %G     4자리 ISO 8601 년 
## %V     2자리 (년 중) ISO 8601 주(01-53)
## %u     1자리 (주 중) ISO 8601 일(1-7, 1=월요일)

#for (y in 2020:2023) 
#  print(format(as.Date(paste0(y, '-01-01', sep='')), '%Y/%m/%d, V=%V U=%U u=%u w=%w A=%A a=%a'))
from Ax_rutils import lc, lseq
seq = lseq
import date
for im, y in enumerate(seq(2022,2025)):
    #print(f'{y:04d}')
    #print(f'{y:04d}-01-01')
    #print(datetime.datetime.strptime(f'{y:04d}-01-01', '%Y-%m-%d'))
    #print(datetime.strptime(f'{y:04d}-01-01', '%Y-%m-%d'))
    #print(datetime.datetime.strptime(f'{y:04d}-01-01', '%Y-%m-%d').
    # strftime('%Y/%m/%d, V=%V U=%U u=%u w=%w A=%A a=%a'))
    print(datetime.datetime.strptime(f'{y:04d}-{im+1:02d}-01', '%Y-%m-%d').
    strftime('%Y/%m/%d, V=%V U=%U u=%u w=%w A=%A a=%a B=%B b=%b'))

# https://docs.python.org/3/library/locale.html#background-details-hints-tips-and-caveats
import locale
locale.setlocale(locale.LC_ALL, '') 
for im, y in enumerate(seq(2022,2025)):
    print(datetime.datetime.strptime(f'{y:04d}-{im+1:02d}-01', '%Y-%m-%d').
    strftime('%Y/%m/%d, V=%V U=%U u=%u w=%w A=%A a=%a B=%B b=%b'))
## locale은 pip install에서 문제를 일으키기도 한다.
## https://m.blog.naver.com/chandong83/221298511028

## docker 설정에서 문제가 발생할 수도 있다
## https://www.44bits.io/ko/post/setup_linux_locale_on_ubuntu_and_debian_container
# 


## datetime을 date으로 바꾸는 방법 : .date() 메쏘드

## 6.3

## 6.3.1


## ISO 8601 

##   표기            의미                     예           날짜로 변환
##  (+-)YYYYMMDD    년월일                  20200103     format='%Y%m%d'
##  (+-)YYYY-MM-DD  년-월-일                2020-01-03   format='%Y-%m-%d'
##  (+-)YYYYDDD     년일(1년의 몇번째 일)      2020003      format='%Y%j'
##  (+-)YYYY-DDD    년-일(1년의 몇번째 일)     2020-003     format='%Y-%j'
##  (+-)YYYYWwwD    년주일                  2020W013     format='%GW%V%u'
##  (+-)YYYY-Www-D  년-W주-일               2020-W01-3   format='%G-W%V-%u'

#install.packages("parsedate")
#library(parsedate)
#as.Date('20210102', format='%Y%m%d'); as.Date(parse_iso_8601('20210102'))
#as.Date('2021-01-02', format='%Y-%m-%d'); as.Date(parse_iso_8601('2021-01-02'))

#??? https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object
from dateutil import parser
datetime.datetime.strptime('20220102', '%Y%m%d')
parser.parse('20220102')
datetime.datetime.strptime('2022-01-02', '%Y-%m-%d')
parser.parse('2022-01-02')

datetime.datetime.fromisoformat('2022-01-02')
# ISO 8601 형식 중 YYYY-MM-DD만 지원. 
# date.isoformat()는 date.strftime('%Y-%m-%d')와 동일하다.   

import aniso8601
# https://aniso8601.readthedocs.io/en/v1.0.0/
aniso8601.parse_date('20220102')
aniso8601.parse_date('2022-01-02')
aniso8601.parse_date('2022-W14-1') # ISO 8601 week date format
aniso8601.parse_date('2022-144')   # ISO 8601 ordinal date

#as.Date('2021002', format='%Y%j'); as.Date(parse_iso_8601('2021002'))
#as.Date('2021-002', format='%Y-%j'); as.Date(parse_iso_8601('2021-002'))

parser.parse('2022002') # ParseError: year 2022002 is out of range
datetime.datetime.strptime('2022002', '%Y%j')
datetime.datetime.strptime('2022-002', '%Y-%j')
aniso8601.parse_date('2022002')   
aniso8601.parse_date('2022-002')   

#as.Date(parse_iso_8601('2020W536'))
#as.Date(parse_iso_8601('2020-W53-6'))

# https://stackoverflow.com/questions/304256/whats-the-best-way-to-find-the-inverse-of-datetime-isocalendar
datetime.datetime.strptime('2020W536', '%GW%V%u')
datetime.datetime.strptime('2020-W53-6', '%G-W%V-%u')
aniso8601.parse_date('2020W536')
aniso8601.parse_date('2020-W53-6')

#datetime.datetime.fromisocalendar() 를 사용하기
import regex
patt = regex.compile('(W|(?<=W\\d)(?=\\d{2}\\b))')
patt = regex.compile('W')
patt = regex.compile(r'(?<=\b\d{4})W(?=\d{3}\b)|(?<=\b\d{4}W\d{2})(?=\d{1}\b)')
patt = regex.compile(r'(?<=\D{0,1}\d{4})W(?=\d{3}\D{0,1})|(?<=\D{0,1}\d{4}W\d{2})(?=\d{1}\D{0,1})')
[int(x) for x in patt.split('2020W536')]
lst = ['2020W536', ' 2020W536', '2020W536 ', '그 날은 2020W536', '2020W536에',
          '12020W555', '2020W5366', '2020W536-', '#2020W536@']
for y in lst:
    print([int(x) for x in patt.split(y)])

patt1 = regex.compile(r'(?<=^|\D)\d{4}W\d{3}(?=\D|$)')
#patt1.findall('12020W555')
patt2 = regex.compile(r'(?<=\d{4})W(?=\d{3})|(?<=\d{4}W\d{2})(?=\d{1})')
for x in lst:
    found = patt1.findall(x)
    if found:
        for y in found:
            print(x, found, [int(z) for z in patt.split(y)])
    else:
        print(x)

datetime.datetime.fromisocalendar(*[int(x) for x in patt.split('2020W536')])
datetime.date.fromisocalendar(*[int(x) for x in patt.split('2020W536')])
patt = regex.compile(r'(?<=\b\d{4})-W(?=\d{2}-\d{1}\b)|(?<=\b\d{4}-W\d{2})-(?=\d{1}\b)')
[int(x) for x in patt.split('2020-W53-6')]
datetime.date.fromisocalendar(*[int(x) for x in patt.split('2020-W53-6')])

patt1 = regex.compile(r'\d{4}-W\d{2}-\d{1}')
patt2 = regex.compile(r'(?<=\d{4})-W(?=\d{3})|(?<=\d{4}-W\d{2}-)(?=\d{1})')
lst = ['2020-W53-6', ' 2020-W53-6', '2020-W53-6 ', '그 날은 2020-W53-6', '2020-W53-6에',
          '12020-W55-5', '2020-W53-66', '2020-W53-6-', '#2020-W53-6@']
for x in lst:
    for y in patt1.findall(x):
        print([int(z) for z in patt.split(y)])

# ???

#library(magrittr)
#as.Date('Jan 01 2020', format='%b %d %Y')
#as.Date('January 01 2020', format='%B %d %Y')
#Sys.getlocale("LC_ALL") %>% strsplit(";")

import datetime
import locale
#??? locale setting
#!!! locale을 변경하는 데에 따르는 문제점?
datetime.datetime.strptime('Jan 01 2020', '%b %d %Y')
datetime.datetime.strptime('January 01 2020', '%B %d %Y')
#locale.setlocale('')
from dateutil import parser 
parser.parse('Jan 01 2020')
parser.parse('January 01 2020')
locale.getlocale(locale.LC_ALL)
# initial setting : ('C/ko_KR', 'UTF-8/C/C/C/C')

#Sys.setlocale("LC_ALL", "English") %>% strsplit(";")
#as.Date('Jan 01 2020', format='%b %d %Y')
#as.Date('January 01 2020', format='%B %d %Y')

locale.setlocale(locale.LC_ALL, 'English') # mac: unsupported locale setting
# for windows?
locale.setlocale(locale.LC_ALL, 'EN') # mac: unsupported locale setting

# locale -a 로 나오는 code
# ex. fr_FR.UTF-8
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
datetime.datetime.strptime('Jan 01 2020', '%b %d %Y')
datetime.datetime.strptime('January 01 2020', '%B %d %Y')

#Sys.setlocale("LC_ALL", "Korean") %>% strsplit(";")
#as.Date('March 01 2020', format='%B %d %Y')
#as.Date('Mars 01 2020', format='%B %d %Y') 
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
datetime.datetime.strptime('2020년 3월 1일', '%Y년 %B %d일')
datetime.datetime.strptime('2020년 3월 1일', '%Y년%b월 %d일')
# !!!주의 : 아래와 같이 쓰면 안된다 
# datetime.datetime.strptime('2020년 3월 1일', '%Y년 %b월 %d일')
# parser.parse('2020년 3월 1일')
# parser.parse('2020 3월 1')

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
datetime.datetime.strptime('March 01 2020', '%B %d %Y')
# ValueError: time data 'March 01 2020' does not match format '%B %d %Y'
datetime.datetime.strptime('Mars 01 2020', '%B %d %Y')
# ValueError: time data 'Mars 01 2020' does not match format '%B %d %Y'
parser.parse('March 01 2020')
parser.parse('Mars 01 2020', fuzzy = True) # WRONG

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
parser.parse('March 01 2020')
locale.setlocale(locale.LC_ALL, '') # back to default

import icu  # PyICU

df = icu.SimpleDateFormat(
               'MMM dd yyyy', icu.Locale('fr_FR'))
ts = df.parse(u'Mars 01 2020')
print(datetime.datetime.utcfromtimestamp(ts))

df = icu.SimpleDateFormat(
               'EEE, dd MMM yyyy HH:mm:ss zzz', icu.Locale('pt_BR'))
ts = df.parse(u'Ter, 01 Out 2013 14:26:00 -0300')
print(datetime.datetime.utcfromtimestamp(ts))

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
datetime.datetime.strptime('Mars 01 2020', '%B %d %Y')

# 참고 : https://stackoverflow.com/questions/55532672/python-how-to-set-french-locale
# https://stackoverflow.com/questions/955986/what-is-the-correct-way-to-set-pythons-locale-on-windows/956084#956084
# https://docs.microsoft.com/en-us/cpp/c-runtime-library/locale-names-languages-and-country-region-strings?view=msvc-160&viewFallbackFrom=vs-2019
# https://www.rfc-editor.org/info/bcp47

#install.packages("lubridate")
#??? import Babel
#
# #%conda install Babel
#Babel is an integrated collection of utilities that assist in internationalizing and localizing Python applications, with an emphasis on web-based applications.
# #http://babel.pocoo.org/en/latest/dates.html
# 날짜 문자열을 변환하는 함수는 없나?
# 

#library(lubridate)

#mdy('March 01 2020')
#mdy('Mars 01 2020', locale='French') # locale을 설정하지 않고도! 
#Sys.setlocale("LC_ALL", "French") %>% strsplit(";")

import dateparser # $ pip install dateparser
dateparser.parse('March 01 2022').date()
dateparser.parse('Mars 01 2022').date()
dateparser.parse('2022년 3월 1일').date() # ERROR
# https://github.com/scrapinghub/dateparser/blob/8e91eb1a6d161a50b1869408c559dc605ef3583f/data/languages.yaml#L207

# 한글 지원이 되지 않는 듯
# 하지만 한글은 크게 쓸모가 없음
dateparser.parse('2020년 3월 2일', 
date_formats=['%Y년 %m월 %d일'], languages=['ko'])#, locales=['ko-KR'])
dateparser.parse('Mars 01 2020', 
date_formats=['%A %m %Y'], languages=['fr'])#, locales=['ko-KR'])

import parsedatetime as pdt # $ pip install parsedatetime pyicu
# pyicu 설치가 쉽지 않음

calendar = pdt.Calendar(pdt.Constants(localeID='fr', usePyICU=True))
for date_string in [u"Aujourd'hui", "3 juillet", u"4 Août", u"Hier"]:
    dt, success = calendar.parseDT(date_string)
    if success:
       print(date_string, dt.date())

# https://stackoverflow.com/questions/26294333/parse-french-date-in-python
for date_string in [u"Aujourd'hui", "3 juillet", u"4 Août", u"Hier"]:
    print(dateparser.parse(date_string).date())

#as.Date('Mars 01 2020', format='%B %d %Y')
#as.Date('March 01 2020', format='%B %d %Y')
#mdy('March 01 2020')
#mdy('Mars 01 2020')

locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
#locale.setlocale(locale.LC_ALL, "")
datetime.datetime(2022, 3,1).strftime('%Y-%B(%b)-%d %A %a')
datetime.datetime.strptime('mars 01 2022', '%B %d %Y')
dateparser.parse('Mars 01 2020', languages=['fr'])
# https://dateparser.readthedocs.io/en/latest/

# timezone도 가능
dateparser.parse('March 01 2020 EST', languages=['en'])
dateparser.parse('March 01 2020 KST', languages=['en'])
dateparser.parse('March 01 2020 17:00:00+09:00', languages=['en'])

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
datetime.datetime(2022, 3,1).strftime('%Y-%B(%b)-%d %A %a')
datetime.datetime.strptime('March 01 2022', '%B %d %Y')
dateparser.parse('March 01 2020')

locale.setlocale(locale.LC_ALL, "ko_KR.UTF-8")
datetime.datetime(2022, 3,1).strftime('%Y-%B(%b)-%d %A %a')
datetime.datetime.strptime('3월 01 2022', '%B %d %Y')
dateparser.parse('2020년 3월 01일') # None!
dateparser.parse('2020 3월 01')

#Sys.setlocale("LC_ALL", "Korean") %>% strsplit(";")
#mdy('Mars 01 2020', locale='French_France.1252')

#wday(today(), label = TRUE, abbr = FALSE, locale = "German")
#wday(today(), label = TRUE, abbr = FALSE, locale = "French")
#month(today(), label = TRUE, abbr = FALSE, locale = "German")
#month(today(), label = TRUE, abbr = FALSE, locale = "French")
locale.setlocale(locale.LC_ALL, "") # default
locale.getlocale()
today = datetime.datetime.today()
today.weekday() # 1
# %U : Week number of the year(Sunday as the first day, w00 for the days before the first Sunday)
# %W : Week number(Monday as the first day)
# %w : Week day(0-6, 0=Sunday)
# %u : Week day(1-7, 1=Monday)
# %w와 %u는 일요일이 0이냐, 7이냐만 다르다.

for x in pd.date_range('2021-12-25', '2022-01-05'):
    #print(x)
    #print(type(x))
    #print(x.to_pydatetime())
    x2 = x.to_pydatetime()
    print(x2.strftime('%Y-%m-%d %Y %B %d(%A) %Y-%U-%w %Y-%W-%u %G-W%V-%u(ISO 8601)'))
    
#today.strftime('%Y-%U-%w %Y-%W-%u %G-W%V-%u(ISO 8601)')

today.strftime('%A')
today.month

from babel.dates import format_date

format_date(today, locale = 'ko')
format_date(today, locale = 'en')
format_date(today, locale = 'ja')
format_date(today, locale = 'zh')
format_date(today, locale = 'es')
format_date(today, locale = 'fr')
format_date(today, locale = 'de')

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


format_date(today, format = 'LLL LLLL LLLLL', locale='ko')
format_date(today, format = 'LLL LLLL LLLLL', locale='ja')
format_date(today, format = 'LLL LLLL LLLLL', locale='zh')
format_date(today, format = 'LLL LLLL LLLLL', locale='en')
format_date(today, format = 'LLL LLLL LLLLL', locale='es')
format_date(today, format = 'LLL LLLL LLLLL', locale='fr')
format_date(today, format = 'LLL LLLL LLLLL', locale='de')

#Sys.setlocale("LC_ALL", "English") %>% strsplit(";")
#as.POSIXct('March 01 2020 11:13:22', format='%B %d %Y %H:%M:%S')
#strptime('March 01 2020 11:13:22', format='%B %d %Y %H:%M:%S')
#mdy_hms('March 01 2020 11:13:22')
#mdy_hms('March 01 2020 11:13:22', tz='Asia/Seoul')
locale.setlocale(locale.LC_ALL, 'en_US')
datetime.datetime.strptime('March 01 2022 11:14:44', '%B %d %Y %H:%M:%S')
pytz.timezone('Asia/Seoul').localize(
    datetime.datetime.strptime('March 01 2022 11:14:44', '%B %d %Y %H:%M:%S'))

#Sys.setlocale("LC_ALL", "French") %>% strsplit(";")
#as.POSIXct('Mars 01 2020 11:13:22', format='%B %d %Y %H:%M:%S')
#strptime('Mars 01 2020 11:13:22', format='%B %d %Y %H:%M:%S')
#mdy_hms('Mars 01 2020 11:13:22')
#mdy_hms('Mars 01 2020 11:13:22', tz='Asia/Seoul')

#Sys.setlocale("LC_ALL", "Korean") %>% strsplit(";")

## 6.4

#t0 <- Sys.time()
#t1 <- as.POSIXct("2030-01-01 00:00:00")
#t1-t0
#difftime(t1, t0, units='weeks')
#difftime(t1, t0, units='hours')

t0 = datetime.datetime.now()
t1 = datetime.datetime(2030,1,1)
t1-t0
(t1-t0).days % 7
(t1-t0).total_seconds() / (60*60)  # 60*60 seconds = 1 hour

# ???
#t0s <- format(t0, format="%Y-%m-%d %H:%S:%M")
#t1s <- format(t1, format="%Y-%m-%d %H:%S:%M")
#t1s-t0s
#difftime(t1s, t0s, units='weeks')
#difftime(t1s, t0s, units='hours')


##6.5

## 함수                       의미                              지역설정
## julian(x)                1970년 1월 1일 이후 몇번째의 일     "Korean"
## julian(x, origin = )     origin 이후 몇번째 일               "Korean"
## quartes(x)               분기(Q1, Q2, Q3, Q4)                "Korean"
## months(x)                월(1월, 2월, 3월, ...)              "Korean"
## months(x)                월(January, Februrary, March, ...)  "English"
## months(x, abbr = TRUE)   월(1, 2, 3, ...)                    "Korean"
## months(x, abbr = TRUE)```월(Jan, Feb, Mar, ...)              "English"
## weekdays(x)              요일(월요일, 화요일, 수요일,..)     "Korean"
## weekdays(x)              요일(Monday, Tuesday, Wednesday, ...)"English"
## weekdays(x, abbr =TRUE)  요일(월, 화, 수, ...)               "Korean"
## weekdays(x, abbr =TRUE)  요일(Mon, Tue, Wed,...)             "English"


## 6.6

## 함수     의미              
## year()   년
## month()  월
## week()   주
## yday()   (년 중) 일(1-366)
## mday()   (월 중) 일(1-31)
## day()    (월 중) 일
## yday()   (주 중) 일(1-7, 1:일)
## hour()   시
## minute() 분
## second() 초
## tz()     타임존
## dst()    써머타임(Daylight Saving Time)의 여부

## Daylight-Saving Time?
## https://stackoverflow.com/questions/12203676/daylight-savings-time-in-python



#t <- Sys.time()
#t
#year(t); year(t) <- 2030; t
#month(t); month(t) <- 1; t
#week(t); week(t) <- 2; t
#day(t); day(t) <- 2; t

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
# %U : Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
# %W : Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
# %V : ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4.
t.day
t = t.replace(day=2)

#yday(t); yday(t) <- 1; t
#yday(t); yday(t) <- 366; t
#mday(t); mday(t) <- 2; t # same as day(t)
#wday(t); wday(t) <- 3; t
#wday(t, label=TRUE); wday(t); 
#wday(t) <- 1; t 

t.strftime('%j')

#hour(t); hour(t) <- 12; t
#minute(t); minute(t) <- 41; t
#second(t); second(t) <- 12; t
#tz(t) ; tz(t) <- "GMT"; t
#dst(t)
#dst(t) <- TRUE
#t

t = t.astimezone(pytz.timezone('Asia/Seoul'))
t.hour; t2 = t.replace(hour=12); t2
t.minute; t2 = t.replace(minute=41); t2
t.second; t2 = t.replace(second = 12); t2
t.tzinfo; t2 = t.replace(tzinfo=None).astimezone(pytz.timezone('GMT')); t2
#pytz.timezone('GMT').localize(t.replace(tzinfo=None))
t.dst() # ??? dst는 시간과 timezone에 의해 결정되므로 바꿀 수 없을 듯??? 

#format(as.Date(parse_iso_8601('2020-W53-6')), "%A")
#options('lubridate.week.start'=1) 
#wday(as.Date(parse_iso_8601('2020-W53-6'))) 
#options('lubridate.week.start'=2) 
#wday(as.Date(parse_iso_8601('2020-W53-6')))


#t <- Sys.time()
#t
#tz(t) <- "GMT" # 또는 force_tz(t, tzone="GMT")
#t
#with_tz(t, "Asia/Seoul")

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

tzKST = pytz.timezone('Asia/Seoul')  # Korea Standard Time
tzKST.localize(t) == \
    datetime.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second, t.microsecond, 
                  tzinfo = datetime.timezone(datetime.timedelta(hours=9)))

t.replace(tzinfo = tzKST)
t.replace(tzinfo = datetime.timezone(datetime.timedelta(hours=9)))
t.replace(tzinfo = tzKST) == \
    t.replace(tzinfo = datetime.timezone(datetime.timedelta(hours=9)))
# !!! False 
# !!! Bug?  LMT+8:28:00

# https://stackoverflow.com/questions/11473721/weird-timezone-issue-with-pytz?noredirect=1&lq=1
# https://en.wikipedia.org/wiki/Tz_database#Example_zone_and_rule_lines

t.astimezone(tzKST)
t.astimezone(datetime.timezone(datetime.timedelta(hours=9)))

t2a = t.astimezone(tzKST)
t2b = t.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
t2a == t2b
# !!! True

t2a.astimezone(pytz.timezone('UTC'))
t2b.astimezone(datetime.timezone(datetime.timedelta(hours=0)))
t2b.astimezone(datetime.timezone.utc)
# 참고 : https://brownbears.tistory.com/356

# strftime.org 

# source의 확장성
datetime.datetime.now() # 그 지역의 날짜로 표시
datetime.datetime.utcnow().astimezone(tzKST) # 어디에서도 한국 시간

# last friday?
# iso format에서 다시 iso format으로???

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
t3.hour = t3.hour + 7 # ERROR
t3.replace(hour = t3.hour + 7) # possibly ERROR
t3 = t3 + datetime.timedelta(hours = 7)
t3
t4 = t3.astimezone(pytz.timezone('Asia/Seoul'))
t4

print(t1)
print(t2)
t1 == t2
t1.strftime('%Y-%m-%d %H:%M:%S %Z')
t2.strftime('%Y-%m-%d %H:%M:%S %Z') # CET : Central Europe Time?

## pandas

t = pd.to_datetime(0, origin='2020/01/01', unit='D')
## type(t) == <class 'pandas._libs.tslibs.timestamps.Timestamp'>
t.isoweekday()
t.dayofweek

ser = pd.Series(t)
[x for x in set(dir(t)) - set(dir(ser)) if not x.startswith('_')]
# ['isoformat', 'dayofyear', 'year', 'to_julian_date', 'normalize', 'now', 'weekday', 'to_datetime64', 'value', 'daysinmonth', 'day', 'today', 'timestamp', 'timetuple', 'isocalendar', 'fromisoformat', 'day_of_week', 'tzinfo', 'month', 'strftime', 'day_name', 'resolution', 'microsecond', 'week', 'second', 'is_year_start', 'tz', 'strptime', 'asm8', 'utcoffset', 'days_in_month', 'timetz', 'astimezone', 'is_quarter_end', 'fromtimestamp', 'freq', 'weekofyear', 'is_quarter_start', 'dst', 'to_pydatetime', 'time', 'utcfromtimestamp', 'fromisocalendar', 'isoweekday', 'is_year_end', 'dayofweek', 'is_month_start', 'utctimetuple', 'toordinal', 'ctime', 'floor', 'month_name', 'fold', 'date', 'nanosecond', 'is_leap_year', 'fromordinal', 'utcnow', 'ceil', 'freqstr', 'tzname', 'quarter', 'hour', 'minute', 'day_of_year', 'is_month_end']
[x for x in set(dir(ser)) - set(dir(t)) if not x.startswith('_')]

[x for x in set(dir(ser.dt)) - set(dir(t)) if not x.startswith('_')]
# []
[x for x in set(dir(t)) - set(dir(ser.dt)) if not x.startswith('_')]
# ['isoformat', 'max', 'to_julian_date', 'fold', 'now', 'resolution', 'fromordinal', 'to_datetime64', 'utcnow', 'combine', 'value', 'min', 'today', 'dst', 'freqstr', 'strptime', 'tzname', 'timestamp', 'timetuple', 'asm8', 'utcfromtimestamp', 'utcoffset', 'to_numpy', 'fromisocalendar', 'replace', 'isoweekday', 'fromisoformat', 'tzinfo', 'utctimetuple', 'toordinal', 'astimezone', 'ctime', 'fromtimestamp']
[x for x in set(dir(t)).intersection(set(dir(ser.dt))) if not x.startswith('_')]
# ['month_name', 'dayofyear', 'year', 'freq', 'normalize', 'date', 'nanosecond', 'weekday', 'day_name', 'is_leap_year', 'weekofyear', 'round', 'microsecond', 'daysinmonth', 'day', 'week', 'second', 'is_quarter_start', 'is_year_start', 'tz', 'ceil', 'to_pydatetime', 'time', 'isocalendar', 'tz_convert', 'to_period', 'quarter', 'is_year_end', 'dayofweek', 'tz_localize', 'day_of_week', 'is_month_start', 'month', 'days_in_month', 'hour', 'minute', 'timetz', 'strftime', 'day_of_year', 'is_month_end', 'is_quarter_end', 'floor']
[x for x in set(dir(t)).intersection(set(dir(ser.dt))) if x.startswith('day')]

ser = pd.Series(pd.date_range('2021-08-13', '2021-08-17'))
ser.dt.month_name()
t.month_name()
ser.dt.day_name()

ser.dt.dayofyear   # ser.dt.day_of_year
ser.dt.daysinmonth # ser.dt.days_in_month
ser.dt.dayofweek   # ser.dt.day_of_week
ser.dt.day         # day of month


# tz_localize('KST')가 아니라 tz_localize('Asia/Seoul')로 써야 함
# holiday 확인하기?
# gregorian and julian calendar : https://keisan.casio.com/exec/system/1227757509
# 

def without_underbar(s):
    return [x for x in s if not x.startswith('_')]

## Reference
# Reference
# https://stackoverflow.com/questions/17976063/how-to-create-tzinfo-when-i-have-utc-offset
# https://www.kite.com/python/docs/pytz.FixedOffset
# https://www.programcreek.com/python/example/50095/pytz.FixedOffset
# https://stackoverflow.com/questions/3305413/python-strptime-and-timezones
# https://stackoverflow.com/questions/1703546/parsing-date-time-string-with-timezone-abbreviated-name-in-python
# https://stackoverflow.com/questions/13707545/linux-convert-timefor-different-timezones-to-utc/13713813#13713813






## timedelta에서 왜 days, seconds, microseconds밖에 없는가?
## 분, 시간은 항상 60seconds, 60*60seconds가 아니다?

for iyear in range(1990, 2030):
    delT = datetime.datetime(iyear+1, 1, 4, 14, 2,2, 142) - \
        datetime.datetime(iyear, 1, 4, 14, 2,2, 142)
    if delT != datetime.timedelta(days=365) and delT != datetime.timedelta(days=366):
        print(iyear)

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

ser = pd.Series(delTs)
ser.value_counts()

# leap second : 2015-06-30
# does not account for leap second!!!
# https://stackoverflow.com/questions/9306328/why-python-time-has-61-seconds
# https://stackoverflow.com/questions/21027639/python-datetime-not-accounting-for-leap-second-properly
datetime.datetime(2015, 7, 1, 0, 0)-datetime.datetime(2015, 6, 30, 23,0)
datetime.datetime(2015, 6, 30, 23, 0)-datetime.datetime(2015, 6, 30, 22,0)


## pandas datetime의 강점

import pandas as pd
d = pd.to_datetime(['2021-01-04', '2022-04-01'])
d >= '2022'  # 그냥 이렇게 쓸 수 있다! d가 datetime이고 '2022'이 문자열이지만!
d >= pd.to_datetime('2022-01-01')
# datetime이 index일 때도 비슷하게 사용 가능...
# slicing도 가능

# .resample
# .groupby 를 datetime에 특수한 방법으로 사용
# 
# ex) df.resample('D').agg({'Close':'mean', 'High':'max', 'Low':'min', 'Volume':'sum'})

