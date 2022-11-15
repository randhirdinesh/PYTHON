
b=input("Enter a list of integer values:\n")

list_1=b.split(',')

for i in range(len(list_1)):
    if int(list_1[i])>100:
        list_1[i]="over"

print("\n",list_1)
