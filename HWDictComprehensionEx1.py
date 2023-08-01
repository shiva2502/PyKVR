#HWDictComprehensionEx1.py

lst=["Python","DSA","HYDERABAD","Django","Apple"]
words=[word for word in lst if len(word)>=3 and len(word)<=5]
print(words)
print("-------------------OR-----------------------------")
words=list(filter(lambda word:len(word)>=3 and len(word)<=5,lst))
print(words)
print("-------------------OR-----------------------------")
words=list(filter(lambda word:3<=len(word)<=5, lst))
print(words)
