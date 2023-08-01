#Program for Demonstrating Variable length args
#PureVarArgsEx3.py
def disp(sno,sname,*a): # Here *a is called Var Length arg and whose type is tuple
    s=0
    print("-----------------------")
    print("Student ID:{}".format(sno))
    print("Student Name:{}".format(sname))
    for val in a:
        print("\t{}".format(val))
        s+=val
    print("\tSum={}".format(s))
    print("-----------------------")

#main program
disp(100,"Rossum",10,20,30,40,50) # Function call-1 with 5 args
disp(200,"KVR",10,20,30,40) # Function call-2 with 4 args
disp(300,"NRaju",10,20,30) # Function call-3 with 3 args
disp(400,"Shahoo",20) # Function call-4 with 2 args
disp(500,"Himansu",10) # Function call-5 with 1 arg
disp(600,"Avinash") #Function call-6 without  args
disp(700,"Jaynanth",2.3,3.4,5.6) #Function call-7 with 3  args