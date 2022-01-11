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
	
