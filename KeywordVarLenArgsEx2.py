#This Program will not execute as it is bcoz PVM remembers latest Function Def only due to ints interpretation Process.
#KeywordVarLenArgsEx2.py
def dispvalues(sno,sname,marks):
    print(sno,sname,marks)

dispvalues(sno=10,sname="RS",marks=34.56) # Function call with 3 Kwd args
#--------------------------------------------
def dispvalues(eno,ename,sal,cname):
    print(eno,ename,sal,cname)

dispvalues(eno=10,ename="RS",sal=4.56,cname="TCS") # Function call with 4 Kwd args
#--------------------------------------------
def dispvalues(sid,name,hb1,hb2,hb3):
    print(sid,name,hb1,hb2,hb3)
dispvalues(sid=10,name="Raj",hb1="Sleep",hb2="Eating",hb3="Chating") # Function call with 5 Kwd args
#--------------------------------------------
def dispvalues(a,b,c,d,e,f):
    print(a,b,c,d,e,f)
dispvalues(a=10,b=20,c=30,d=40,e=50,f=60) # # Function call with 6 Kwd args
#--------------------------------------------