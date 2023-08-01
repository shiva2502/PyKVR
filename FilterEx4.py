#Program for Filtering List of +Ve  and -Ve Elements from List of Values
#FilterEx4.py

lst=[10,-23,45,-46,-67,0,12,89]
pslist=list(filter(lambda n:n>0,lst))
nglist=tuple(filter(lambda n:n<0,lst))
print("------------------------------------------")
print("Given Elements={}".format(lst))
print("Possitive Elements={}".format(pslist))
print("Negative Elements={}".format(nglist))
print("------------------------------------------")