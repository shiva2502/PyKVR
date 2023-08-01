#Program for Filtering List of +Ve  and -Ve Elements from List of Values
#FilterEx3.py

pos=lambda n: n>0 # Anonymous Function
neg=lambda n: n<0 # Anonymous Function

#main program
lst=[10,-23,45,-46,-67,0,12,89]
pslist=list(filter(pos,lst))
nglist=tuple(filter(neg,lst))
print("------------------------------------------")
print("Given Elements={}".format(lst))
print("Possitive Elements={}".format(pslist))
print("Negative Elements={}".format(nglist))
print("------------------------------------------")