#Program for Demonstrating Possitonal Args
#PosArgsEx2.py

def studinfo(sno,sname,marks,crs):
    print("\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs))

#main program
print("-"*50)
print("\tStno\tName\tMarks\t\tCourse")
print("-"*50)
studinfo(10,"RS",34.56,"PYTHON")  # Function Call
studinfo(20,"SB",24.56,"PYTHON")  # Function Call
studinfo(30,"TR",44.56,"PYTHON")  # Function Call
studinfo(40,"DR",74.56,"PYTHON")  # Function Call
print("-"*50)