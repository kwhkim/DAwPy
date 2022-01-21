# -*- coding: utf-8 -*-
# %%
import types

def assign(varname, value):
	# 전역 변수만 가능
    globals()[varname] = value
	
def globals_user(dict_ = False):
	# 편의 함수 : _로 시작하는 이름 제외
    varnames = globals().keys()
    varnames2 = [varname for varname in varnames if not varname.startswith('_')]
    if dict_:
        return {k:globals()[k] for k in varnames2}
    else:
        return varnames2
	
def del_all(types_skip=(type, types.FunctionType, types.ModuleType)):
	# 함수, 모듈 제외 변수 지우기
    #print(types_skip)
    #print(type(types_skip))
    if types_skip is not None and not isinstance(types_skip, tuple):
        raise ValueError("types should be either 'all' or tuple of types to skip")
    varnames = set(globals().keys()) # 제거할 변수
    # 맥락에 따라 globals().keys()를 locals().keys(), dir() 등으로 교체할 수 있다.
    #varnames = varnames.difference({'exit', 'quit', 'get_ipython', 'delall', 'globals_user', 'builtins', 'In', 'Out'})
    varnames_underbar = [varname for varname in varnames if varname.startswith('_')]    
    varnames = varnames.difference(set(varnames_underbar))    
    if types_skip is None:
        for varname in varnames:
            del globals()[varname]
    else:
        for varname in varnames:
            if not isinstance(globals()[varname], types_skip):
                del globals()[varname]   
				
def ordered(categories):
    #print(categories)
    from pandas.api.types import CategoricalDtype
    return CategoricalDtype(categories=categories, ordered=True)
	
def lsf(module):
	# 모듈의 함수 나열    
    if not isinstance(module, (types.ModuleType, type)):
        raise ValueError("argument should be module type")
    return [k for k, v in vars(module).items() 
            if not k.startswith('_') and callable(v) and not isinstance(v, type)] 
    # '_'로 시작하지 않는 함수 종류만 출력
	
def lsf_doc(module):
	# 모듈의 함수와 doc
    funcs = lsf(module)
    funcs_dic = {func:vars(module)[func].__doc__ for func in funcs}
    for k,v in funcs_dic.items():
        #print(k,v.split('\n')[0])
        try:
            dochead = v.split('\n')[0]
            print(f"{k:10}: {dochead:30}")
            # SyntaxError: f-string expression part cannot include a backslash
            # 왜 backslash는 포함하지 못하나?
        except Exception as e:
            print(f"{k:10}:")
			
def xor(x, y):
    return (x and not y) or (not x and y)

def imported():
    import sys
    #import types
    modules = list(sys.modules.keys())
    aliasnames = {}
    filenames = {}
    b_builtins = {}
    for name, val in globals().items():
        #if isinstance(val, types.ModuleType):
        if isinstance(val, type(__builtins__)): 
        # __builtins__은 언제라도 수정될 수 있으므로 불확실하지만,
        # types 역시 마찬가지...
            if val.__name__ not in aliasnames:
                aliasnames[val.__name__] = [name]                
                filenames[val.__name__] = getattr(val, '__file__', None)                
                if hasattr(val, '__file__'):
                    b_builtins[val.__name__] = False
                    #filenames[val.__name__] = val.__file__                    
                else:
                    b_builtins[val.__name__] = val.__name__ in sys.builtin_module_names
                    #filenames[val.__name__] = val.__file__
            else:
                aliasnames[val.__name__].append(name)                 
        
    # module object name(alias), 파일, 빌트인 모듈 여부
    return aliasnames, filenames, b_builtins 

# listing available packages
# from https://stackoverflow.com/questions/5632980/list-of-all-imports-in-python-3
import shutil
import pkgutil

def show_acceptable_modules():
    line = '-' * 100
    print('{}\n{:^30}|{:^20}\n{}'.format(line, 'Module', 'Location', line))
    for entry in pkgutil.iter_modules():
        print('{:30}| {}'.format(entry[1], entry[0].path))


# =====
# From Ax_rutils.py

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: rtopython2-pip
#     language: python
#     name: rtopython2-pip
# ---

# %% [markdown]
# ## R의 함수 대용
#
# * `c`
# * `seq`
# * `pdDataFrame`
#

# %%
import numpy as np
a = np.array([1,3,2])
a

# %%
type(a)

# %%
a


# %%
class rarray(np.ndarray):
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        np.array(*args,**kwargs)
        


# %%
# ?np.ndarray

# %%
import inspect
#inspect.getsource(np.array)

# %%
## rarray([[1,3,2],[2,4,5]])

# %%
a

# %% [markdown]
# R의 `seq()` 함수는 `seq(from, to, by, length.out)`의 형태이며, 만약 `from`, `to`, `by`가 정해지면, `to`를 적절히 조정한다.
# 그리고 `from`, `to`, `by`, `length.out`는 다음의 관계식을 만족한다.
#
# $$\textrm{to} = \textrm{from} + \textrm{by} \times (\textrm{length.out} -1)$$ 

# %%
import numpy as np

# %%
c = lambda v: eval(f'np.r_[{v}]')
c("1,3,2,4:6")
# 이 방법의 문제는 다른 변수는 포함시키지 못한다?

# %%
a = c("1, 3, 2, 4:6")

# %%
c("1,3,2,a")


# %%

# %% [raw]
# def c(*arg):
#     return np.concatenate([np.array([x]).flatten() for x in arg])

# %% [raw]
# def c(*args):
#     l = []
#     for x in args:
#         l.append(x)
#     return l

# %%
def ac(*args):
    res = []
    for x in args:
        if isinstance(x, np.ndarray):
            res.append(x.flatten())
        else:
            res.append(np.array([x]))
    return np.concatenate(res)

def lc(*args):
    res = []
    for x in args:
        if isinstance(x, list):
            res.extend(x)
        else:
            res.append(x)
    return res

# %%
#v[c(seq(np.where(v.index == "Mary")[0], \
#        np.where(v.index == "Suzi")[0]), \
#    np.where(v.index=="Angus")[0])]
def ac(*args, dtype=None):
    res = []
    for x in args:
        if isinstance(x, np.ndarray):
            res.append(x.flatten())
        else:
            res.append(np.array([x]))
    if dtype is None:
        return np.concatenate(res)
    else:
        return np.concatenate(res).astype(dtype)


# %% [raw]
# def seq1(from_, to, lengthout):
#     by=(to-from_)/(lengthout-1)
#     return np.arange(from_, to+by, by)

# %% [raw]
# def seq(from_, to, by=1, lengthout=None):
#     if lengthout is None:
#         lengthout = int((to -from_)/by + 1)
#         to2 = from_ + by*(lengthout-1)
#         return seq1(from_, to2, lengthout)
#     else:
#         return seq1(from_, to, lengthout)

# %% [raw]
# def seq(from_, to, lengthout):
#     return np.r_[from_:to:lengthout*1j]

# %% [raw]
# def seq(from_, to, step, lengthout=None):
#     lengthout = int((to-from_)//step) + 1  # 정수에만 적용?    
#     to = from_ + (step)*(lengthout-1)
#     #print(lengthout)
#     return np.linspace(start=from_, stop=to, num=lengthout, endpoint=True)

# %%
def aseq(from_, to, by=None, lengthout=None):
    if lengthout is None:
        if by is None:
            by = 1
        lengthout = int((to-from_)//by) + 1  # 정수에만 적용?    
        to = from_ + by*(lengthout-1)        
        #print("np.linspace")
        #print(from_)
        #print(to)
        #print(lengthout)
        if isinstance(from_, int) and isinstance(to, int) and isinstance(by, int):
            return np.linspace(start=from_, stop=to, num=lengthout, endpoint=True, dtype=int).flatten()
        else:
            return np.linspace(start=from_, stop=to, num=lengthout, endpoint=True).flatten()

        #dtype : dtype, optional
        #The type of the output array.  If `dtype` is not given, the data type
        #is inferred from `start` and `stop`. The inferred dtype will never be
        #an integer; `float` is chosen even if the arguments would produce an
        #array of integers.
    else:
        if by is not None:
            lengthout2 = int((to-from_)//by) + 1  # 정수에만 적용?    
            if lengthout2 != lengthout:            
                raise ValueError('lengthout should be {} or modify step'.format(lengthout2))
        else:
            #print("np.r_")
            #print(from_)
            #print(to)
            #print(lengthout)
            return np.r_[from_:to:lengthout*1j].flatten()
            


# %%
def aseq2(from_, to, by=None, lengthout=None):
    
    if lengthout is None and by is None:
        by = abs(to-from_)/(to-from_)
    if lengthout is not None and by is not None:
        raise ValueError('by and lengthout can not both be determined')
        
    if by is None:
        if not isinstance(lengthout, int):
            raise ValueError('lengthout should be interger number!')
        elif lengthout == 0:
            return np.array([])
        if lengthout == 1:
            return np.array([from_])
        else:
            #by = (to-from_)/lengthout
            by = (to-from_)/(lengthout-1)
    else: # by is specified
        lengthout = int((to-from_)/by + 1) # lenghout shoud be integer
        to = from_ + by*(lengthout-1)
        
    res = np.arange(from_, to+by, by)
    return res

def lseq(*args, **kwargs):
    return list(seq(*args, **kwargs))

#def lc(*args):
#    return list(ac(*args))


# %%

# %%
aseq(1,10,3)

# %%
aseq2(1,10,3)

# %%
aseq(1,4,2)

# %%
aseq2(1,4,2)

# %%
aseq(1,10,lengthout=5)

# %%
aseq2(1,10,lengthout=5)

# %%
# R과 비교했을 때 차이가 나는 곳???

# %%

# %%
import numpy as np
isinstance(np.array([1,3,2]), np.ndarray)

# %%
seq = aseq
c = ac

# %%
aseq(1,14,lengthout=1)

# %%
aseq2(1,14,lengthout=1)

# %%
aseq(1,14,lengthout=0)

# %%
aseq2(1,14,lengthout=0)

# %%
aseq(14,1, lengthout=3)

# %%
aseq2(14,1,lengthout=3)

# %%
aseq(14,3,by=-2)

# %%
aseq2(14,3,by=-2)

# %%
c(c(1,3,2),2,4)

# %%
aseq(15,25)

# %%

# %%
c = ac
seq = aseq

# %%
import pandas as pd

def pdDataFrame(**kwargs):
    return pd.DataFrame(kwargs)

def pdDataFrame(**kwargs):
    ar_opt = {}
    ar_data = {}    
    for k in kwargs:
        #print(k)
        if k.startswith('_'):
            ar_opt[k[1:]] = kwargs[k]
        else:
            ar_data[k] = kwargs[k]

    return pd.DataFrame(ar_data, **ar_opt)

# pd.date_range('11/27/2016') 대신에
#   seq('11/27/2016', periods=5, freq='D')을 쓸 수 있다면?
#   pd.date_rage(start, end, periods, freq, tz, normalize, bool, Hashable, closed)


import dateparser

# aseq + pd.date_range
# seq(6,9) -> ERROR???
def seq(from_, to=None, by=None, lengthout=None, **kwargs):
    if isinstance(from_, str):
        if to is None:
            from_ = dateparser.parse(from_)
            if not 'periods' in kwargs.keys():
                raise ValueError('periods ?')
            if not 'freq' in kwargs.keys():
                freq = 'D'
            else:
                freq = kwargs['freq']
                kwargs.pop('freq')
            return pd.date_rage(from_, periods=kwargs['periods'], freq=freq, **kwargs)
        else:
            return pd.date_range(from_, to, **kwargs).values
        # 문제는 pd.date_range의 결과가 DatetimeIndex()라는 특수한 꼴...
        # 결과를 list로? np.array의 dtype='datetime64[ns]'
        # https://ellun.tistory.com/320

    if lengthout is None:
        if by is None:
            by = 1
        lengthout = int((to-from_)//by) + 1  # 정수에만 적용?    
        to = from_ + by*(lengthout-1)        
        #print("np.linspace")
        #print(from_)
        #print(to)
        #print(lengthout)
        if isinstance(from_, int) and isinstance(to, int) and isinstance(by, int):
            return np.linspace(start=from_, stop=to, num=lengthout, endpoint=True, dtype=int).flatten()
        else:
            return np.linspace(start=from_, stop=to, num=lengthout, endpoint=True).flatten()

        #dtype : dtype, optional
        #The type of the output array.  If `dtype` is not given, the data type
        #is inferred from `start` and `stop`. The inferred dtype will never be
        #an integer; `float` is chosen even if the arguments would produce an
        #array of integers.
    else:
        if by is not None:
            lengthout2 = int((to-from_)//by) + 1  # 정수에만 적용?    
            if lengthout2 != lengthout:            
                raise ValueError('lengthout should be {} or modify step'.format(lengthout2))
        else:
            #print("np.r_")
            #print(from_)
            #print(to)
            #print(lengthout)
            return np.r_[from_:to:lengthout*1j].flatten()

seq('2011-03-01', '2011-03-04')


def rep(x, n_rep, each=1):
    return np.tile(np.repeat(x, each), n_rep)
    
def rep(x, times = 1, length_out = None, each = 1):
    if length_out is None:
        return np.tile(np.repeat(x, each), times)
    elif times != 1:
        if length_out <= len(x)*times:
            return np.tile(x, times)[:length_out]
        else:
            each = length_out / (len(x)*times)
            return np.repeat(np.tile(x,times), each)[:length_out]
    elif each != 1:
        if length_out <= len(x)*each:
            return np.repeat(x, each)[:length_out]
        else:
            times = length_out / (len(x)*each)
            return np.repeat(np.tile(x,times), each)[:length_out]

def np_apply(arr, axes_remain, fun, *args, **kwargs):
    axes_remain = tuple(set(axes_remain))
    arr_shape = arr.shape
    axes_to_move = set(range(len(arr.shape)))
    for axis in axes_remain:
        axes_to_move.remove(axis)
    axes_to_move = tuple(axes_to_move)
    #arr, axes_to_move
    
    if arr.flags.c_contiguous:
        arr2 = np.moveaxis(arr, axes_to_move, [-x for x in list(range(1,len(axes_to_move)+1))]).copy()
        arr2 = arr2.reshape([arr_shape[x] for x in axes_remain]+[-1])
        return np.apply_along_axis(fun, -1, arr2, *args, **kwargs)
    elif arr.flags.f_contiguous:
        arr2 = np.moveaxis(arr, axes_to_move, [x for x in list(range(0,len(axes_to_move)))]).copy()
        arr2 = arr2.reshape([-1]+[arr_shape[x] for x in axes_remain])
        return np.apply_along_axis(fun, 0, arr2, *args, **kwargs)
    else:
        raise ValueError('The array is neither c_contiguous nor f_contiguous')

## Testing
x = np.random.normal(0,1,(3,3,3))
np_apply(x, (0,), sum)
y = x.copy(order='F')
np_apply(y, (0,), sum)

np_apply(x, (1,2), sum)
np_apply(y, (1,2), sum)
