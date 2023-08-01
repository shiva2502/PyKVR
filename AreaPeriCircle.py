# Write a python program which will calculate Area and Perimeter of circle by using functions
# AreaPeriCircle.py

def area():
    r=float(input("Enter Radius of Circle for Area: "))
    ac=3.14*r**2
    print("Area of Circle={}".format(ac))
def perimeter():
    r = float(input("Enter Radius of Circle for Perimter: "))
    pc =2*3.14 * r
    print("Perimeter of Circle={}".format(pc))

#main program
while(True):
    print("============================")
    print("\tCircle Calculations")
    print("============================")
    print("\tA:Area of Circle")
    print("\tP:Perimeter of Circle")
    print("\tE:Exit")
    print("============================")
    ch=input("Enter Ur Choice:")
    if(ch.isalpha()):
        match(ch):
            case "A"|'a':
                area() # Function Call
            case "P"|'p':
                perimeter()  # Function Call
            case "E"|'e':
                print("Tq for this program")
                break
            case _:
                print("Ur Selection of Operation is wrong-try again")
    else:
        print("Don't enter Digits and Symbols")