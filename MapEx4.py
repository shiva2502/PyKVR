#Program for finding new sal list by giving 50% hike to old sal list
#MapEx4.py

oldsal=[1000,2000,1500,3000,4000,100]
newsal=list(map(lambda sal: sal+sal*(50/100),oldsal))
print("======================================")
print("Old Salary\t\tNew Salary")
print("======================================")
for osl,nsl in zip(oldsal,newsal):
    print("\t{}\t\t{}".format(osl,nsl))
print("======================================")