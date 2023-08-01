#Program for Filtering List of +Ve Elements from List of Values
#FilterEx1.py

def pos(n):
    if(n>0):
        return True
    else:
        return False

#main program
lst=[10,-23,45,-46,-67,0,12,89]
filobj=filter(pos,lst)
print("type of filobj=",type(filobj)) # <class 'filter'>
print("content of filobj=",filobj) # <filter object at 0x000002E341AB9D50>
#Convert filter object into list
pslist=list(filobj)
print("------------------------------------------")
print("Given Elements={}".format(lst))
print("Possitive Elements={}".format(pslist))
print("------------------------------------------")