#DictComprehensionEx2.py

import math
lst=[2,3,1,0,-3,6,7,-8]
dobj=dict([(val,math.factorial(val)) for val in lst if val>=0])
print("---------------------------")
print("Given List of Values={}".format(lst))
print("Dict of Factorials={}".format(dobj))
print("---------------------------")