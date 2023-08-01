#AnonymousFunEx2.py

palindrome=lambda val: val.lower()==val[::-1].lower()

#main program
val=input("Enter a any value:")
if(palindrome(val)):
    print("{} is PALINDROME".format(val))
else:
    print("{} is NOT PALINDROME".format(val))