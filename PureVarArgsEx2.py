#Program for Demonstrating Variable length args
#PureVarArgsEx2.py
def disp(*a): # Here *a is called Var Length arg and whose type is tuple
    print("-----------------------")
    for val in a:
        print(val,end=" ")
    print()
    print("-----------------------")

#main program
print("-"*50)
disp(10,20,30,40,50) # Function call-1 with 5 args
disp(10,20,30,40) # Function call-2 with 4 args
disp(10,20,30) # Function call-3 with 3 args
disp(10,20) # Function call-4 with 2 args
disp(10) # Function call-5 with 1 arg
disp() #Function call-6 without  args
print("-"*50)