#Program for demonstrating globals()
#In This Program local and global variable are Same-- need to use globals()
#GlobalsFunEx2.py
a=10
b=20 # Here a and b are called global variables
def operation():
    a=100
    b=200 # here a and b are called Local Variables
    #In This Program local and global variable are SAME
    print("-" * 50)
    print("Val of a--Global Variable={}".format(globals()['a']))
    print("Val of b--Global Variable={}".format(globals()['b']))
    print("Val of a--Local Variable={}".format(a))
    print("Val of b--Local Variable={}".format(b))
    print("-" * 50)
    res=a+b+globals()['a']+globals()['b']
    print("sum=",res)

#main program
operation()
