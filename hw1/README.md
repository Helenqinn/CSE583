## Process

First of all, to build the directory structure, I was able to quickly get them done based on what we learned in class and the previous homework.

Then to complete the python part, I mainly referred to the online tutorials of python, including <https://www.w3schools.com/python/matplotlib_pyplot.asp> and <https://www.w3schools.com/python/pandas/>. I also had to get help from Claude to help with installing packages in VScode. I initially got errors from importing the packages because I had them installed in conda but was running VScode in a separate environment.

## Converting `Date` to datetime

I converted the whole `Date` column from strings to pandas' datetime type.

### Comparing datetime formats

| Format | Library | How it's stored |
|------------------|------------------|------------------|
| `datetime.datetime` | Python standard library | One Python object per value | 
| `numpy.datetime64` | NumPy | A 64-bit integer + a time unit (e.g. `ns`) | 
| `pd.Timestamp` / `datetime64[ns]` | pandas | Built on `numpy.datetime64` | 


