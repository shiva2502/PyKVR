#Program for finding max from list of values by using reduce()
#ReduceEx3.py

import functools
lst1=[10,34,23,56,78,12,47]
maxv=functools.reduce(lambda a,b:a if a>b else b,lst1)
print("Max({})={}".format(lst1,maxv))