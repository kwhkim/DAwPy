# -*- coding: utf-8 -*-
# ## 흐름제어
#

# 1. 분기
#     - if/else, if/elif/elif/else
#     - switch
# 2. 반복
#     - while
#     - for
#

# ### 1. 분기
# #### if/elif/else

import sys

# +
choice = input('choose y to proceed, n to quit')

if choice == 'y':
    print('Thank you. Going to do ...')
elif choice == 'n':
    print('Going to quit')
    sys.exit()  
    # exit() -> Kernel shuts down
else:
    print('I do not know what you mean')    
    
# -

# #### switch
#
# 파이썬에는 일반적인 프로그래밍 언어의 switch에 해당하는 statement가 없다. switch 문을 꼭 사용하고 싶다면, 딕셔너리를 활용해보라.

# +
msg = {'y':'Thank you. Going to ...', 
       'n':'Going to quit'}

choice = input('choose y to proceed, n to quit')
print(msg.get(choice, 'I do not know what you mean'))


# -

# 위의 방법으로는 복잡한 statement를 사용할 수 없다. 좀 더 복잡한 결과가 필요하다면 함수를 만들어 쓸 수 있다.

# +
def func_y():
    print('Thank you. Going to do ...')
def func_n():
    print('Going to quit')
    sys.exit()  
def func_default():
    print('I do not know what you mean')
    
branch = {'y':func_y,
          'n':func_n}

choice = input('choose y to proceed, n to quit')

(branch.get(choice, func_default))()
# -

# ### 2. 반복

# #### while
#
# while문은 조건이 성립하는 동안에 반복한다. 다음은 변수 `i`가 10보다 작을 때, `i`를 출력한 후 1만큼 증가시킨다.

i = 0
while i<10:    
    print(i, end=',')
    i = i + 1


# while문을 쓰는 전형적인 방법을 알아두면 좋다. 뭔가를 n번 반복하려면 다음을 쓴다.

# +
def do_something():
    print(i, end=',')
    
n = 10    
i = 0
while i < n:
    do_something()
    i = i + 1
# -

# `n=10`일 때, `i`는 0부터 9까지 변하고, 10이 되었을 때 `do_something()`을 실행하지 않고 나와버린다. 이는 리스트의 슬라이싱과 비슷하다.

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
x[0:10]

i = 0
while i < 10:
    print(x[i], end=', ')
    i = i + 1

# 실제로 왜 파이썬에서 인덱싱이 0부터이며, 슬라이싱은 마지막 원소를 포함시키지 않는가에 대해 동일한 역할을 하는 가장 단순한 `while`과 비교하기도 한다.

x[3:10:2]

i = 3
while i < 10:
    print(x[i], end=', ')
    i = i + 2

x[-7:2:-3]

# 만약 음의 step까지 포함한다면 다음과 같이 쓸 수 있다. 

i = len(x)-7
step = -3
sign = step/abs(step)
while i*sign < 2*sign:
    print(x[i], end=', ')
    i = i + step

# 위의 `while`이 이해하기 어렵다면 다음과 같이 풀어 쓸 수도 있다.

# +
start = len(x)-7
stop = 2
step = -3
sign = step/abs(step)

i = start
if sign > 0:
    while i < stop:
        print(x[i], end=', ')
        i = i + step
else:
    while i > stop:
        print(x[i], end=', ')
        i = i + step
# -

x[20:-8:-3]

# 만약 Index가 범위에서 벗어나는 경우까지 포함하면 다음과 같이 쓸 수 있다. 범위에서 벗어나는 부분은 모두 제거한 후 슬라이싱을 한다고 생각할 수 있다

# +
i = 20
step = -3
sign = step/abs(step)

if i >= len(x):
    i = len(x)-1

if i < 0:
    i = 0

while i*sign<(len(x)-8)*sign:
    print(x[i], end=', ')
    i = i + step
# -

#

# #### 조건이 만족될 때까지 실행

# 만약 조건이 만족될 때까지 어떤 일을 수행해야 한다면, 다음의 형식을 사용할 수 있다.

# + active=""
# while True:
#     do_something()
#     if condition_is_met:
#         break
# -

# 만약 입력을 받아 y면 `print('Good')`, n이면 `print('You said no')`하려고 한다면, 다음과 같이 할 수 있다.

# +
while True:
    choice = input('y or n')
    if choice in ['y', 'n']:
        break

if choice == 'y':
    print('Good')
elif choice == 'n':
    print('You said no')
# -

# #### for

i = 0; n=10
while i < n:
    do_something()
    i = i + 1

# 위의 전형적인 while은 너무 자주 사용되기 때문에 다음과 같이 for문을 활용할 수 있다.

for i in range(n):
    do_something()

# 위에서 `range(n)`은 0부터 n 직전까지를 의미한다.

list(range(n))

# 다음과 같이 불규칙적인 `i`에 대해 반복하는 것도 가능하다

for i in [2,3,5,7]:
    do_something()

# 위의 `for`문은 특정한 리스트의 "모든 원소에 대해, 그 원소를 출력하라."라고 말할 수 있다.

# 여기서는 가장 자주 쓰이는 두 가지 변주를 소개한다. 

lst = [2,3,5,7]
for x in lst:
    print(x, end=', ')

# `enumerate()`을 사용하면 원소의 위치를 확인할 수 있다.

lst = [2,3,5,7]
for i,x in enumerate(lst):
    print(i, x)

# `zip()`을 사용하면, 두 리스트에 대해 한꺼번에 일을 진행할 있다.

# +
lstA = [2,3,5,7]
lstB = [10,9,8,7]

for x,y in zip(lstA, lstB):
    print(x,y)
# -

# 이 둘을 합쳐 보자.

# +
lstA = [2,3,5,7]
lstB = [10,9,8,7]

for i, (x,y) in enumerate(zip(lstA, lstB)):
    print(i,x,y)
# -

# 다음도 가능하다.

# +
lstA = [2,3,5,7]
lstB = [10,9,8,7]
lstC = ['a', 'b', 'c', 'd']

for i, (x,y, z) in enumerate(zip(lstA, lstB, lstC)):
    print(i,x,y, z)
# -

# ### 반복(`while`/`for`) 내에서의 분기

# `for`와 `while`은 특정한 횟수, 또는 특정 조건이 만족하는 동안 스크립트의 동일한 부분이 반복된다. 만약 반복되는 스크립트 안에서 분기가 필요하다면, `continue` 또는 `break`를 사용할 수 있다.

# ####  continue
#
# `continue`는 반복되는 스크립트의 나머지 부분을 건너뛰고, 반복의 처음으로 가라는 의미이다. 보통 해당 반복에서 할 일을 모두 마쳤을 때 실행한다.

for i in range(10):
    if i in [2,3,5,7]:
        continue
    print(i, end=',')

# 0부터 9까지의 숫자에서 2,3,5,7에 해당하는 경우는 출력을 하지 않는다.

# break의 경우는 반복을 완전히 빠져 나올 때 사용한다. 앞에서 `y` 또는 `n`을 입력받기 위해 `while True`, `if` ~ `break`에서 사용되었다.

# 그리고 `break`없이 반복스크립트가 모두 마쳤을 때는 `else:` 이후가 실행된다.

lst = input('input numbers')
lst2 = lst.split(',')
lst2 = [int(x.strip()) for x in lst2]
print("Your numbers are ", lst2)

for i in lst2:
    if i == 10:
        print('number 10 means break out!')
        break
    print(i, end=',')    
else:
    print('all done')

# 아래를 실행하고 `1,2,3`과 `1,10,3`을 입력해보자.

lst = input('input numbers')
lst2 = lst.split(',')
lst2 = [int(x.strip()) for x in lst2]
print("Your numbers are ", lst2)
for i in lst2:
    if i == 10:
        print('number 10 means break out!')
        break
    print(i, end=',')    
else:
    print('all done')


