a=input("Type a line of text: ")

list1=a.split(" ")
print("\n")
for i in range(len(list1)):
    print("Occurence of word ",i+1, "(",list1[i], ") is:",list1.count(list1[i]))
