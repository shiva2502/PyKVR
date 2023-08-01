#Program for Demonstrating Keyword Args
#KwdArgsEx1.py
def disp(a,b,c):
    print("\t{}\t{}\t{}".format(a,b,c))


#main program
print("="*50)
print("\tA\tB\tC")
print("="*50)
disp(10,20,30) # Function call with Positional args
disp(c=30,b=20,a=10) # Function call with Keyword args
disp(10,c=30,b=20) # Function call with Positional  and Keyword args
#disp(b=20,a=10,30)---SyntaxError: Positional argument follows keyword argument
disp(b=20,a=10,c=30) # Function call with Keyword args
print("="*50)