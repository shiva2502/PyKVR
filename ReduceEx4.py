#Program for concatnating  list of words as line of text by using reduce()
#ReduceEx4.py

import functools
lst=["Apple","is","red","in","color"]
line=functools.reduce(lambda x,y:x+" "+y,lst)
print("------------------------------------")
print("Given Words={}".format(lst))
print("Line={}".format(line))
print("------------------------------------")
lst=["Python","is","an","OOP","LANG"]
line=functools.reduce(lambda x,y:x+" "+y,lst)
print("------------------------------------")
print("Given Words={}".format(lst))
print("Line={}".format(line))
print("--------------OR----------------------")
line=" ".join(lst)
print("Given Words={}".format(lst))
print("Line={}".format(line))
print("------------------------------------")