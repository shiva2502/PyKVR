# Write a Python program which will calculate Area and Perimeter of Square by using functions
# AreaPeriSquare.py

def areasquare():

    l=float(input("Enter Length of Square: "))
    a=l*l                             #A=s*s
    print("Area of Rectangle: {}".format(a))

def perimetersquare():

    l=float(input("Enter Length of Square: "))
    ps=4*l                         #P=4s
    print("Perimeter of Square: {}".format(ps))

#main program
while(True):
    print("============================")
    print("\tSquare Calculations")
    print("============================")
    print("\tA:Area of Square")
    print("\tP:Perimeter of Square")
    print("\tE:Exit")
    print("============================")
    ch=input("Enter Ur Choice:")
    if(ch.isalpha()):
        match(ch):
            case "A"|'a':
                areasquare() # Function Call
            case "PS"|'ps':
                perimetersquare()  # Function Call
            case "E"|'e':
                print("Tq for this program")
                break
            case _:
                print("Your Selection of Operation is wrong-try again")
    else:
        print("Don't enter Digits and Symbols")
