#PureKwdVarLenArgsEx.py

def dispvalues(**vals): # **vals is calle Kwd var len args and type dict
    print(vals,type(vals))

#main program
dispvalues(sno=10,sname="RS",marks=34.56) # Function call with 3 Kwd args
dispvalues(eno=10,ename="RS",sal=4.56,cname="TCS") # Function call with 4 Kwd args
dispvalues(sid=10,name="Raj",hb1="Sleep",hb2="Eating",hb3="Chating") # Function call with 5 Kwd args
dispvalues(a=10,b=20,c=30,d=40,e=50,f=60) # # Function call with 6 Kwd args