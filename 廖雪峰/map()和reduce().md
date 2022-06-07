Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
```python
def prod(L):
    def mul(x,y):
        return x*y
    return reduce(mul,L)   
```

利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

```python
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    i = s.find('.')
    e = len(s)-1-i
    s = s[:i]+s[i+1:]
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s)) * 10**(-1*e)
```
