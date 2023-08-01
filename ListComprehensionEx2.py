#Find the sqaures of +ve numbers by using List Comprehension
#ListComprehensionEx2.py

lst=[2,5,-6,12,-13,9,0,-21]
lst1=[val**2 for val in lst if val>0 ] # List Comprehension
pselements=[val for val in lst if val>0]   # List Comprehension
print("Given Elements={}".format(lst))
print("+Ve Elements={}".format(pselements))
print("Squares of +Ve Numbers={}".format(lst1))
