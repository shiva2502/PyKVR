#Program for Demonstrating Variable length args
#Non-VarArgsEx1.py
def disp1(a,b,c,d,e): # Function Def-1
    print(a,b,c,d,e)

def disp2(a,b,c,d): # Function Def-2
    print(a,b,c,d)

def disp3(a,b,c): # Function Def-3
    print(a,b,c)

def disp4(a,b): # Function Def-4
    print(a,b)

def disp5(a): # Function Def-5
    print(a)

#main program
print("-"*50)
disp1(10,20,30,40,50) # Function call-1 with 5 args
disp2(10,20,30,40) # Function call-2 with 4 args
disp3(10,20,30) # Function call-3 with 3 args
disp4(10,20) # Function call-4 with 2 args
disp5(10) # Function call-5 with 1 arg
print("-"*50)