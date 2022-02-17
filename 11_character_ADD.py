# -*- coding: utf-8 -*-
# %% [markdown]
# # font dependent character width and height

# %%
import matplotlib as mpl
from pathlib import Path
afm_path = Path(mpl.get_data_path(), 'fonts', 
'afm', 'ptmr8a.afm')

# %%
fp = r'D:\Fonts\_LinuxUpload\Menlo.ttf'
fp = Path(r'D:\Fonts\_LinuxUpload\Menlo.ttf')
# font path

# %%
fp = Path(r'D:\Fonts\_LinuxUpload\Menlo.ttf')
# generated from fontforge 
# 화일 - 폰트를출력(G) - SVG폰트 
#                     - 옵션 - [v] AFM을 출력
#                     - 생성(G)
fp = Path(r'D:\Fonts\_LinuxUpload\Menlo.afm')
from matplotlib.afm import AFM

# %%
with open(fp, 'rb') as f:
#with fp.open('rb') as f:
    afm = AFM(f)
# RuntimeError: Not an AFM file

# %%
afm.string_width_height('Hi!')

# %% [markdown]
# # afm is necessary
# # generate afm with fontforge

# %% [markdown]
# # FontForge(window), BirdFont(win, mac, linux)
# # 를 통해 unicode와 폰트 맵핑을 확인할 수 있다.

# %% [markdown]
# # 


# %% [markdown]
# https://stackoverflow.com/questions/32555015/how-to-get-the-visual-length-of-a-text-string-in-python
# Use a graphic / font library like ImageFont. Draw the string and then use the getsize to get the width.
# Note that some text like "AWAY" may be narrower than the sum of the individual letters due to kerning. So it would be difficult to lookup widths of each letter and add them.


# %% [markdown]
# Unicode strings
# https://docs.python.org/3/howto/unicode.html
# https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
#

# %%

# %%
# Adopted from https://docs.python.org/ko/3.8/howto/unicode.html
print("no let. UNICODE category  num letter name")
print("=========================================")
for i, c in enumerate(u):
    #print(i, c, '%04x' % ord(c), unicodedata.category(c), end=" ")
    #print(f'{i:02d} {c:2s} {ord(c):04x}') 
    # 완벽히 맞출 수 없을 듯... GUI의 역할이라서??? # tab을 쓰면?
    print(f'{i:02d} {c:2s} \t{ord(c):06x}\t{unicodedata.category(c):4s} ', end='') 
    try:
        print('%8.2f ' % unicodedata.numeric(c), end='')
    except:
        print(' '*(8+1), end='')
    print(unicodedata.name(c))
    #print(unicodedata.east_asian_width(c))
# Get numeric value of second character
#print(unicodedata.numeric(u[1]))

# %%
