#Define a function for cal addition of two numbers
#ApproachEx3.py

#INPUT: From Function Call
#PROCESS: Inside of Function Body
#OUTPUT : Inside of Function Body
def addop(a,b):
    #Doing the PROCESS
    c=a+b
    #Display the RESULT
    print("sum({},{})={}".format(a,b,c))

#main program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
addop(a,b) # Function call
