#Program for adding list of values by using reduce()
#ReduceEx2.py

import functools
lst1=[10,34,23,56,78,12,47]
res=functools.reduce(lambda a,b:a+b,lst1)
print("sum({})={}".format(lst1,res))
lst2=[1.2,3.4,4.5,6.7]
res=functools.reduce(lambda x,y:x+y,lst2)
print("sum({})={}".format(lst2,res))