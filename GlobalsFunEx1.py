#Program for demonstrating globals()
#In This Program local and global variable are different--no need to use globals()
#GlobalsFunEx1.py

def operation():
    x=100
    y=200 # here x and y are called Local Variables
    #In This Program local and global variable are different
    res=a+b+x+y
    print("-"*50)
    print("Val of a--Global Variable={}".format(a))
    print("Val of b--Global Variable={}".format(b))
    print("Val of x--Local Variable={}".format(x))
    print("Val of y--Local Variable={}".format(y))
    print("-" * 50)
    print("sum={}".format(res))

#main program
a=10
b=20 # Here  and b are called globals variables
operation()
