#Program for finding Square of Every Value of List
#MapEx3.py

lst=[2,-3,14,25,6,9,-4,0]
sqlist=tuple(map(lambda val: val**2,lst))
print("------------------------------------")
print("Given List:{}".format(lst))
print("Square List:{}".format(sqlist))
print("------------------------------------")