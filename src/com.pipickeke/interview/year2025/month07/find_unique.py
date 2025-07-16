"""

找出列表中不重复的元素
"""


def find_unique(lst):
    return [x for x in lst if lst.count(x) == 1]


lst = [1,2,3,1,2]
print(find_unique(lst))