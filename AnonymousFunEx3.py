#AnonymousFunEx3.py

palindrome=lambda val: "PALINDROME" if val.lower()==val[::-1].lower() else "NOT PALINDROME"

#main program
val=input("Enter a any value:")
res=palindrome(val)
print("{} is {}".format(val,res))