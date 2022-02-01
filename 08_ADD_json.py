# -*- coding: utf-8 -*-
import json

datJsonOrig = {'a':'b', 'num':[1,2,3],
               'dict':{'a':24, 'c':[2,4,5], '숫자들':['하나', '둘', '셋']}}
with open('f.json', 'wt') as f:
    f.write(json.dumps(datJsonOrig, indent=2))

with open('f.json', 'rt') as f:
    datJson = json.loads(f.read())

json.dumps(datJsonOrig) == json.dumps(datJson)
# list comparison???

with open('f.json', 'rt') as f:
    print(f.readlines())
# ['{"a": "b", "num": [1, 2, 3], "dict": {"a": 24, "c": [2, 4, 5], "\\uc22b\\uc790\\ub4e4": ["\\ud558\\ub098", "\\ub458", "\\uc14b"]}}']

# if indent = 2
# ['{\n', '  "a": "b",\n', '  "num": [\n', '    1,\n', '    2,\n', '    3\n', '  ],\n', '  "dict": {\n', '    "a": 24,\n', '    "c": [\n', '      2,\n', '      4,\n', '      5\n', '    ],\n', '    "\\uc22b\\uc790\\ub4e4": [\n', '      "\\ud558\\ub098",\n', '      "\\ub458",\n', '      "\\uc14b"\n', '    ]\n', '  }\n', '}']


# json.dumps(obj, *, ensure_ascii=True, indent=2)

datJsonOrig = {'가':'나', '숫자':[1,2,3],
               '사전':{'ㄱ':24, 'ㄷ':[2,4,5], '숫자들':['하나', '둘', '셋']}}
with open('f.json', 'wt') as f:
    f.write(json.dumps(datJsonOrig, 
                       ensure_ascii=False,
                       indent = 2))

with open('f.json', 'rt') as f:
    datJson = json.loads(f.read())

with open('f.json', 'rt') as f:
    #print(f.readlines())
    [print(x, end='') for x in f.readlines()]
# '가'를 '\uc790'으로 바꾸진 않지만
