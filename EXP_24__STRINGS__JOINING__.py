string_1=input("Enter string 1: ")
string_2=input("\nEnter string 2: ")

string_3=string_2[:2]+string_1[2:]+" "+string_1[:2]+string_2[2:]

print("\n Result: ",string_3)
