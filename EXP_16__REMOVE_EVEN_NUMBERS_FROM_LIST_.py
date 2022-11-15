zz=input("Enter a list of numbers:\n")

l1=zz.split(',')
l2=[]

for i in range(len(l1)):
    if int(l1[i])%2!=0:
        l2.append(l1[i])

print("\n The list after removing even numbers: \n",l2)
