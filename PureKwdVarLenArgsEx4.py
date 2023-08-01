#PureKwdVarLenArgsEx4.py
def findtotalmarks(sno,sname,cls,*vals, city="HYD",**submarks):
    print("*"*50)
    print("Var length Args")
    for val in vals:
        print("{}".format(val),end=" ")
    print()
    print("*" * 50)
    print("-"*50)
    print("\tStudent Details")
    print("-" * 50)
    print("\tStudent Number:{}".format(sno))
    print("\tStudent Name:{}".format(sname))
    print("\tStudent Class:{}".format(cls))
    print("\tStudent Living City:{}".format(city))
    print("-" * 50)
    print("\tSubject Names\tSubject Marks")
    totmarks=0
    print("-" * 50)
    for sub,marks in submarks.items():
        print("\t{}\t\t\t{}".format(sub,marks))
        totmarks=totmarks+marks
    print("-" * 50)
    print("\tTotal Marks={}".format(totmarks))
    print("-" * 50)

#main program
findtotalmarks(10,"Rajesh","X",10,20,30,40,Telugu=60,Hindi=68,English=69,Maths=99,Science=89,Social=77)
findtotalmarks(20,"Rakesh","XII",100,200,Maths=75,Physics=60,Chemistry=59)
findtotalmarks(30,"Rajinish","B.Tech(CSE)",1.2,2.3,4.5,C=30,DBMS=35,OS=15,SRT=50)
findtotalmarks(40,"Rossum","Research","NL",110,210)
findtotalmarks(50,"Ritche","Scientist",C=100,CPP=90,city="USA")
findtotalmarks(60,"Trump","Politician",3.5,4.5,6.5,7.5,city="USA",Poly=20,Eco=15)