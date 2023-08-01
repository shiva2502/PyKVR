#Program for finding Square of Every Value of List
#MapEx2.py

square=lambda n: n*n # Anonymous Function
#main program
lst=[2,-3,14,25,6,9,-4,0]
sqlist=tuple(map(square,lst))
print("------------------------------------")
print("Given List:{}".format(lst))
print("Square List:{}".format(sqlist))
print("------------------------------------")