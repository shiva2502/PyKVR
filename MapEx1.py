#Program for finding Square of Every Value of List
#MapEx1.py

def square(n):
    return (n**2)

#main program
lst=[2,-3,14,25,6,9,-4,0]
obj=map(square,lst)
print("Type of obj=",type(obj)) # <class 'map'>
print("Content of obj=",obj) # <map object at 0x00000197FEDBA5F0>
#Convert mao object into list
sqlist=list(obj)
print("------------------------------------")
print("Given List:{}".format(lst))
print("Square List:{}".format(sqlist))
print("------------------------------------")