#DictComprehensionEx1.py

lst=["Python","DSA","HYDERABAD","Django"]
dobj=dict([(word,len(word))  for word in lst]) # List Comprehension
print(dobj,type(dobj))