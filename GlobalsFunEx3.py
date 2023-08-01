#Program for demonstrating globals()
#In This Program local and global variable are Same-- need to use globals()
#GlobalsFunEx3.py

a=10
b=20 # Here  and b are called globals variables
def  operation():
    a=100
    b=200
    #To get the global variables inside of function body
    gv=globals() # gv contains GVN:GVV--dict type
    #Here gv contains Present program global variables and Invisible Global variables
    print("---------------------------")
    print("type of gv=",type(gv))
    print("---------------------------")
    for gvn,gvv in gv.items():
        print("\t{}---->{}".format(gvn,gvv))
    print("---------------------------")
    print("Total Globals=",len(gv))
    print("---------------------------")
    print("Programmer-Defined Global Variables--Way-1")
    print("---------------------------")
    print("Global Variable a=",gv['a'])
    print("Global Variable b=",gv['b'])
    print("---------------------------")
    print("Programmer-Defined Global Variables--Way-2")
    print("---------------------------")
    print("Global Variable a=", gv.get('a'))
    print("Global Variable b=", gv.get('b'))
    print("---------------------------")
    print("Programmer-Defined Global Variables--Way-3")
    print("---------------------------")
    print("Global Variable a=", globals()['a'])
    print("Global Variable b=", globals()['b'])
    print("---------------------------")
    print("Programmer-Defined Global Variables--Way-4")
    print("---------------------------")
    print("Global Variable a=", globals().get('a'))
    print("Global Variable b=", globals().get('b'))
    print("---------------------------")

#Main program
operation()