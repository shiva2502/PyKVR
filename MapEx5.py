#MapEx5.py

def sumlist(x,y):
    return (x+y)

#main program
lst1=[10,20,30,40,50]
lst2=[100,200,300,400,500]
lst3=list(map(sumlist,lst1,lst2))
print("List1={}".format(lst1))
print("List2={}".format(lst2))
print("Sum List={}".format(lst3))
