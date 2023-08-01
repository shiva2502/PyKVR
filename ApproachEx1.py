#Define a function for cal addition of two numbers
#ApproachEx1.py

#INPUT : From Function Call
#PROCESSING : Inside of Function Body
#RESULT / OUTPUT : to Function Call
def addop(a,b): # here a and b are called Formal Parameters
    c=a+b # here c is called Local Variable
    return c
#main program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
z=addop(x,y) # Function call
print("sum({},{})={}".format(x,y,z))


