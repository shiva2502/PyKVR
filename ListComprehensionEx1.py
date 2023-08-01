#ListComprehensionEx1.py

lst=[2,5,6,12,13,9]
lst1=[val**2  for val in lst] # List Comprehension
print("------------------------------")
print("Given Elements={}".format(lst))
print("Squares={}".format(lst1))
print("------------------------------")
lst2=[round(val**0.5,2) for val in lst] # List Comprehension
print("Given Elements={}".format(lst))
print("Square Roots={}".format(lst2))
print("------------------------------")