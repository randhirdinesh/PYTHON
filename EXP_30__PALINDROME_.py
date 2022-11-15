str=input("Enter a String\n")
strstr=str.casefold()
rev=reversed(str)
if(list(str)==list(rev)):
    print(str,"is a Palindrome String")
else:
    print(str,"is not a Palindrome String")
