# Tuple Comprehension is not possible directly but we can convert generator object into tuple
#TupleComprehensionEx1.py

lst=[10,-23,45,67,-45,-23,0]
pslist=(val for val in lst if val>0)  # tuple Comprehension
print(type(pslist)) # <class 'generator'>
print("Content=",pslist) # <generator object <genexpr> at 0x00000167A18D9BD0>
#Convert Generator into tuple
tpl=tuple(pslist)
print("Given Elements={}".format(lst))
print("Possitive Elements={} and type={}".format(tpl,type(tpl)))