#Define a function for cal addition of two numbers
#ApproachEx4.py

#INPUT: Inside of Function Body
#PROCESS: Inside of Function Body
#OUTPUT : to Function Call
def addop():
    #Taking INPUT in Function Body
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    #doing PROCESS
    c=a+b
    #give result back to Function Call
    return a,b,c# a return kwd can return one or more values

#main program
x,y,z=addop() # Function call with Multi Line assigment
print("Sum({},{})={}".format(x,y,z))
print("-------------OR--------------------")
res=addop() # Function call with Single Line assigment
#here res is an object of <class,tuple>
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("-------------OR--------------------")
print("sum({},{})={}".format(res[-3],res[-2],res[-1]))
print("**********************************")
print("sum({},{})={}".format(res[0:1],res[1:2],res[2:3]))
print("-------------OR--------------------")
print("sum({},{})={}".format(res[-3:-2],res[-2:-1],res[-1:]))
print("**********************************")