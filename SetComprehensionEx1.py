#SetComprehensionEx1.py
lst=[10,-23,45,67,-45,-23,0]
pslist={val for val in lst if val>0}  # Set Comprehension
print("Given Elements={}".format(lst))
print("Possitive Elements={} and type={}".format(pslist,type(pslist)))