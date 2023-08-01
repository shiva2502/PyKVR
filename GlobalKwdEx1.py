#GlobalKwdEx1.py

a=10 # here a is called Global Variable
def increment():
    global a
    a=a+1
def multiply():
    global a
    a=a*2
def modifyval():
    c=a-2 # No Need to write global kwd bcoz we are not modifying the value of a, but we are just accessing

#main program
print("Val of a in main program before incrment()=",a) # 10
increment()
print("Val of a in main program after increment()=",a) # 10
multiply()
print("Val of a in main program after multyiply()=",a) # 22
modifyval()
print("Val of a in main program after modifyval()=",a) # 22