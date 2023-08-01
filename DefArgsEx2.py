#Program for Demonstrating Default Args
#DefArgsEx2.py

def studinfo1(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))

def studinfo2(sno,sname,marks,crs="JAVA",cnt="INDIA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("-"*50)
print("\tStno\tName\tMarks\t\tCourse\t\tCountry")
print("-"*50)
studinfo1(10,"RS",34.56)  # Function Call
studinfo1(20,"SB",24.56)  # Function Call
studinfo1(30,"TR",44.56)  # Function Call
studinfo1(40,"DR",74.56)  # Function Call
studinfo1(60,"DT",14.22,cnt="USA")  # Function Call
studinfo1(sname="KV",marks=0.0,cnt="AP",crs="DSA",sno=35)
studinfo1(15,"JM",24.12,crs="JAVA-PYTHON")  # Function Call
print("-"*50)
print("\tStno\tName\tMarks\t\tCourse\t\tCountry")
print("-"*50)
studinfo2(50,"NR",64.22,"JAVA")  # Function Call
studinfo2(70,"RC",24.12,"JAVA")  # Function Call
studinfo2(80,"KR",34.52,"JAVA")  # Function Call
studinfo2(90,"PT",14.52,cnt="RSA")  # Function Call
studinfo2(85,"KM",14.12,cnt="NK",crs="PHP")  # Function Call
studinfo2(15,"JM",24.12,cnt="USA",crs="JAVA-PYTHON")  # Function Call
print("-"*50)