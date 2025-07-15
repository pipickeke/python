"""
测试使用 Counter
"""

from collections import Counter

c = Counter(['apple','banana','apple','orange'])
print(c)

char_counter = Counter('abracadabra')
print(char_counter)


list(c.elements())

c.update(['apple','hello'])
print(c)


c.subtract(['apple', 'banana'])
print(c)

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)

print(c1 - c2)
print(c1 & c2)
print(c1 | c2)