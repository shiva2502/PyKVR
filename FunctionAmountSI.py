# Write a python program to calculate simple interest and total amount to pay by using functions
# FunctionAmountSI.py

#p = float(input("Enter Principle Amount: "))
#r = float(input("Enter Rate of Interest: "))
#t = int(input("Enter Time Period"))

def simpleinterest():
    p = float(input("Enter Principle Amount: "))
    t = int(input("Enter Time Period: "))
    r = float(input("Enter Rate of Interest: "))

    si = (p*t*r)/100
    print("Simple Interest: {}".format(si))

def totalamount():
    p = float(input("Enter Principle Amount: "))
    t = int(input("Enter Time Period: "))
    r = float(input("Enter Rate of Interest: "))

    si = (p * t * r) / 100
    ta = p+si
    print("Total Amount to be Paid: {}".format(ta))

#main program
while(True):
    print("============================")
    print("\tSimple Interest and Total Amount Calculations")
    print("============================")
    print("\tSI:Simple Interest")
    print("\tTA:Total Amount to be Paid")
    print("\tE:Exit")
    print("============================")
    ch=input("Enter Ur Choice:")
    if(ch.isalpha()):
        match(ch):
            case "SI"|'si':
                simpleinterest() # Function Call
            case "TA"|'ta':
                totalamount()  # Function Call
            case "E"|'e':
                print("Tq for this program")
                break
            case _:
                print("Your Selection of Operation is wrong-try again")
    else:
        print("Don't enter Digits and Symbols")
