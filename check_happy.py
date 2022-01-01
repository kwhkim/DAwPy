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

# %%
def question1():
    return input("Are you happy today?")
 
def question2():
    return input("Are you happy yesterday?")
    
if __name__ == "__main__":
    a1 = question1()
    a2 = question2()
    
    if a1=='Y' and a2=='Y':
        print('Good. You seems to be happy all the time')
    else:
        print("It's okay. keep it up.")
