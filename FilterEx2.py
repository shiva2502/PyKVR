#Program for Filtering List of -Ve Elements from List of Values
#FilterEx2.py

def negative(n):
    if(n<0):
        return True
    else:
        return False

#main program
lst=[10,-23,-46,45,-46,-67,0,12,89]
filobj=filter(negative,lst)
#Convert filter object into list
nglist=tuple(filobj)
print("------------------------------------------")
print("Given Elements={}".format(lst))
print("Negative Elements={}".format(nglist))
print("------------------------------------------")