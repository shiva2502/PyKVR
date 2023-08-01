#Program for Demonstrating Possitonal Args
#PosArgsEx1.py

def studinfo(sno,sname,marks):
    print("\t{}\t\t{}\t\t{}".format(sno,sname,marks))


#main program
print("-"*50)
print("\tStno\tName\tMarks")
print("-"*50)
studinfo(10,"RS",34.56)  # Function Call
studinfo(20,"SB",24.56)  # Function Call
studinfo(30,"TR",44.56)  # Function Call
studinfo(40,"DR",74.56)  # Function Call
print("-"*50)