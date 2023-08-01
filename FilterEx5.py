#FilterEx5.py

lst=[12,13,56,53,78,0,34,33,-34,-23]
evenlist=list(filter(lambda n:n%2==0 and n>=0,lst))
oddlist=list(filter(lambda n: n%2!=0 and n>0,lst))
print("------------------------------------------")
print("Given Elements={}".format(lst))
print("Even Elements={}".format(evenlist))
print("Odd Elements={}".format(oddlist))
print("------------------------------------------")
