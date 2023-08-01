#Program for Demonstrating Keyword Args
#KwdArgsEx2.py
def  dispstudinfo(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t\t{}\t\t{}\t\t{}".format(sno, sname, marks, crs))


print("-"*50)
print("\tStno\tName\tMarks\t\tCourse")
print("-"*50)
dispstudinfo(10,"RS",34.56)  # Function Call with positional args
dispstudinfo(sname="TR",marks=45.67,sno=20)# Function Call with keyword args
dispstudinfo(crs="Java",sname="TR",marks=45.67,sno=20)# Function Call with keyword args
dispstudinfo(30,crs="DSA",sname="DR",marks=45.89)# Function Call with Positional and keyword args
dispstudinfo(40,"MC",crs="HTML",marks=56.89) # Function Call with Positional and keyword args
#dispstudinfo(50,"DR",crs="C++",56.89) SyntaxError: positional argument follows keyword argument
dispstudinfo(50,"DR",58.78,crs="C++",)#  # Function Call with Positional and keyword args

print("-"*50)