#Program for finding Length of words which are in list
#WordLengthCount.py

def findwordslength(lst):
    dictobj={}
    for word in lst:
        l1=len(word)
        dictobj[word]=l1
    return dictobj

#main program
lst=["Apple","Kiwi","Mango","Python","Java"]
obj=findwordslength(lst)
for word,length  in obj.items():
    print("\t{}\t{}".format(word,length))