#AnonymousFunEx1.py

def sumop(a,b): # Normal Function Definition
    c=a+b
    return c

addop=lambda k,v: k+v # Anonymous Function Definition

#main program
print("-----------------------")
print("Type of sumop=",type(sumop)) # <class 'function'>
res=sumop(10,20)
print("sum=",res)
print("-----------------------")
print("-----------------------")
print("Type of addop=",type(addop)) # <class 'function'>
res=addop(100,200)
print("sum=",res)
print("-----------------------")