# Write a python program which will calculate factorial of a given number by using functions
# ArgsParamsEx2.py

def factcal(n): # Here n is called Formal Parameter
    if(n<0):
        return ("{} Is Invalid Input".format(n))
    else:
        fact=1  # Here Fact is called Local Variable
        for i in range(1,n+1):
            fact*=i
        else:
            return("Fact({})={}".format(n,fact))
#main program
n=int(input("Enter a Number for cal Factorial:"))
res=factcal(n) # Function call--here n is called argument
print(res)