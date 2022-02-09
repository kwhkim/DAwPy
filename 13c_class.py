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
#     display_name: rtopython3-pip
#     language: python
#     name: rtopython3-pip
# ---

# %% [markdown]
# ## 클래스
#
# * 참고 자료 : https://docs.python.org/3.8/tutorial/classes.html

# %% [markdown]
# 파이썬에서 함수는 입력되는 데이터 타입을 가리지 않는다. 이는 약간 의도적인데, 여러 데이터 타입에 적용되는 함수를 만들 수 있기 때문이다. 다음을 보자.

# %%
def add(x,y):
    return(x+y)


# %% [markdown]
# 위에서 정의한 함수 `add`는 두 숫자 입력에 대해 두 수를 합친다.

# %%
add(3,5)

# %% [markdown]
# 그런데 문자열도 입력이 가능하다.

# %%
add('a', 'b')

# %% [markdown]
# 리스트도 입력이 가능하다.

# %%
add([3,2,'five'], ['b', 5])

# %% [markdown]
# 왜냐하면 `+`가 입력되는 변수의 타입에 따라 다르게 작동하기 때문이다. 하지만 다음을 보자.

# %%
add([3,2,5], 5)

# %% [markdown]
# 위에서 리스트 `[3,2,5]`에 마지막 원소로 `5`를 추가하기 위해서 `add([3,2,5], 5)`를 시도해보았다. 그런데 이렇게 특정한 변수 타입을 가정하고 함수를 정의할 필요가 있는 경우가 있다. 이렇게 특정한 타입을 전제하고 만들어진 함수를 메소드라고 한다. 

# %% [markdown]
# 사실 앞에서 **타입**이라고 했지만 리스트는 보통 **클래스**라고 불린다. 파이썬에서 거의 모든 것이 **객체**라고 한다. **객체**란 인스턴스(instance)라고도 하는데, 객체는 클래스의 구체적인 실현이다. 예를 들어 사람이 클래스라면, 특정인 홍길동은 인스턴스라고 생각할 수 있다.

# %% [markdown]
# 리스트에는 이미 `.append()`라는 메소드가 있어서 우리가 앞에서 하고자 했던 기능을 한다.

# %%
lst = [3,2,5]
lst.append(5)
lst

# %% [markdown]
# 여기서 `append(lst, 5)`는 불가능함을 유의하자.

# %%
append(lst, 5)


# %%

# %%

# %%
class Student():
    def __init__(self, name, scoreA, scoreB):
        self.name = name
        self.scores = [scoreA, scoreB]
        
    
    def mean_score(self):
        return (self.scores[0] + self.scores[1])/2

# %%
a = Student('Kim', 90,80)
b = Student('Park', 85,75)

# %%
a.scores  # Attribute

# %%
a.mean_score() # Method


# %%
## Monkey-patching Class method

def f(self, identity):
    #print("제 이름은 "+self.name + "입니다.\n 저는 "+x+" 입니다.")
    print(f"제 이름은 {self.name}입니다.\n저는 {identity} 입니다.")


# %%
Student.intro = f

# %%
a.intro('2학년')


# %%
class Free():
    pass


# %%

# %%
b = Free()

# %%
b.name = '철수'

# %%
Free.intro = f

# %%
b.intro('전학생')

# %%
