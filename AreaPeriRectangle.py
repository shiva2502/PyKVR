# Write a Python program which will calculate Area and Perimeter of Rectangle by using functions
# AreaPeriRectangle.py

def arearecthangle():

    l=float(input("Enter Length of Rectangle: "))
    b=float(input("Enter Breadth of Rectangle: "))
    print("Enter Breadth: ")
    ar=(l*b)                             #A=lb
    print("Area of Rectangle: {}".format(ar))

def areaperimeter():
    l = float(input("Enter Length of Rectangle: "))
    b = float(input("Enter Breadth of Rectangle: "))
    ap=2*(l+b)                           #P=2(l+b)
    print("Perimeter of Rectangle: {}".format(ap))

#main program
while(True):
    print("============================")
    print("\tRectangle Calculations")
    print("============================")
    print("\tA:Area of Rectangle")
    print("\tP:Perimeter of Rectangle")
    print("\tE:Exit")
    print("============================")
    ch=input("Enter Ur Choice:")
    if(ch.isalpha()):
        match(ch):
            case "AR"|'ar':
                arearecthangle() # Function Call
            case "PR"|'pr':
                areaperimeter()  # Function Call
            case "E"|'e':
                print("Tq for this program")
                break
            case _:
                print("Your Selection of Operation is wrong-try again")
    else:
        print("Don't enter Digits and Symbols")
