#DictComprehensionEx4.py

def kvrfact(n):
    if(n<0):
        return "No Factorial"
    else:
        f=1
        for val in range(1,n+1):
            f*=val
        return f
#main program
lst=[2,3,1,0,-3,6,7,-8]
dobj=dict([(val,kvrfact(val)) for val in lst ])
print("---------------------------")
print("Given List of Values={}".format(lst))
print("Dict of Factorials={}".format(dobj))
print("---------------------------")