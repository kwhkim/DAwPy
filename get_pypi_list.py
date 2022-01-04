### PyPI의 패키지 리스트 

# Download from https://www.kaggle.com/rtatman/list-of-pypi-packages/version/479
#import zipfile
#zip = zipfile.ZipFile(r'C:\Users\Home\Downloads\simple.zip', mode='r')
#dat = zip.read('simple')
#text_html = dat.decode('utf8')

# Url : https://pypi.org/simple/
import requests 
text_html = requests.get("https://pypi.org/simple/").text



import html

from bs4 import BeautifulSoup 
soup = BeautifulSoup(text_html)  # 'html5lib'

found = soup.findAll('a')

package_names = [x.text for x in found]

#package_names


import requests
import json
import re       
import pandas as pd

patt1 = re.compile('from\\s+([A-Za-z_][A-Za-z0-9_.]*)\\s+import\\s+([A-Za-z_][A-Za-z0-9_]*)\\s*$', re.MULTILINE)
patt2 = re.compile('(?<!from)\\s+[^\\s]+\\s+import\\s+([A-Za-z_][A-Za-z0-9_.]*)\\s*$', re.MULTILINE)

res = []

#npack = 200; mpack = 100

spack = 120000 # complete 
npack = len(package_names)
mpack = 1000

print('* npack = {} & mpack = {}'.format(npack, mpack))

for ipack, package in enumerate(package_names[spack:npack], start=spack):
    if ipack % mpack == 0 and ipack != spack:
        dat = pd.DataFrame(res)
        dat.to_csv('dat_pypi/dat_pypi_'+"{:06d}".format(ipack)+'.csv')
        print('* SAVED to '+'dat_pypi_'+"{:06d}".format(ipack)+'.csv')
        res = []
    try:
        url = requests.get('https://pypi.org/pypi/'+package+'/json')
        text = url.text
        #print(type(text))
        dat_pack = json.loads(text)
    except Exception as e:
        print(ipack, package, str(e))
        continue # 나중엔 여기도 데이터로 저장?
    
    try:
        desc = dat_pack['info']['description']
    except Exception as e:
        print(ipack, package,str(e))
        continue # 데이터?

    f1 = patt1.findall(desc)
    f2 = patt2.findall(desc)    
    #name_import = ''
    names_import1 = ''
    names_import2 = ''
    if len(f1) > 0:
        # name_import = f1[0][0].split('.')[0]
        # 문제는 https://pypi.org/project/glasses/에서 보듯이
        # glasses 패키지를 설명하는데
        # import torch가 먼저 등장!        
        names_import1 = ",".join([f1[i][0].split('.')[0] for i in range(len(f1))])
        print("{:06d}: ".format(ipack) + "from " + package + " import ...", names_import1)   
    if len(f2) > 0:
        #name_import = f2[0].split('.')[0]
        names_import2 = ",".join([f2[i].split('.')[0] for i in range(len(f2))])
        print("{:06d}: ".format(ipack) + "import " + package, names_import2)
    if len(f1) or len(f2):
        #print(ipack, package, name_import)
        #res.append((package, name_import))
        res.append((package, names_import1 + names_import2))

dat = pd.DataFrame(res)
dat.to_csv('dat_pypi/dat_pypi_'+"{:06d}".format(ipack)+'.csv')
print('* SAVED to '+'dat_pypi_'+"{:06d}".format(ipack)+'.csv')




