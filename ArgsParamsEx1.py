# Write a python program which will calculate factorial of a given number by using functions
# ArgsParamsEx1.py
def factcal(n): # Here n is called Formal Parameter
    if(n<0):
        print("{} Is Invalid Input".format(n))
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        else:
            print("Fact({})={}".format(n,fact))
#main program
n=int(input("Enter a Number for cal Factorial:"))
factcal(n) # Function call--here n is called argument