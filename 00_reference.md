## R vs. 파이썬


* https://heads0rtai1s.github.io/2020/11/05/r-python-dplyr-pandas/
* [R reticulate](https://heads0rtai1s.github.io/2019/10/03/reticulate-intro/)

```python

```

## R `reticulate`

<!-- #raw -->
conda create -n rtopython3 python=3.8

conda activate rtopython3
conda install numpy pandas matplotlib seaborn
# conda install -c conda-forge jupyterlab
conda install notebook jupytext -c conda-forge
<!-- #endraw -->

<!-- #raw -->
Sys.setenv(RETICULATE_PYTHON = "/home/master/miniconda3/envs/rtopython3/bin")
library(reticulate)
<!-- #endraw -->

### 참고

```python
# 이렇게 해도 잘 안 됨.
# # https://stackoverflow.com/questions/59986841/requested-version-of-python-cannot-be-used-as-another-version-has-been-initializ
# 
# # When you run library(reticulate), the reticulate package will try to initialize a version of Python, which may not be the version that you intend to use. To avoid this, (in a new R session) run your set-up commands without importing the full reticulate library with the :: syntax like this:
# 
# reticulate::virtualenv_create(envname = 'python_environment', 
#                               python= 'python3')
# reticulate::virtualenv_install("python_environment", 
#                                packages=c('pandas','catboost'))
# reticulate::use_virtualenv("python_environment",required = TRUE)
```

### python 확인

```python magic_args="R"
reticulate::repl_python() # python version 확인
```

```python
foo = [1,2,3]
print(foo[0])
import pandas as pd
print(r.iris.loc[:5, ["Sepal.Length", "Species"]])
```
