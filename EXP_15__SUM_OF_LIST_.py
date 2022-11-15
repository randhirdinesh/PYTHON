xx=input("Enter The First List:\n")
yy=input("\nEnter The Second List:\n")

list1=xx.split(',')
list2=yy.split(',')

sum1=int('0')
sum2=int('0')

if len(list1)==len(list2):
    print("\n Both lists are of equal length: ",len(list1));
else:
    print("\n Length of list1:",len(list1),"\n Length of list2:",len(list2),"\n Hence, lists are not of equal length")


for i in range(len(list1)):
    sum1+=int(list1[i])

for i in range(len(list2)):
    sum2+=int(list2[i])


if sum1==sum2:
    print("\n Both lists sum up to the same value: ",sum1)
else:
    print("\n Lists don't sum up to same values. \n List1 sums up to: ",sum1,"\n List2 sums up to: ",sum2)

print("\n")
if len(list2)>len(list1):
    length=len(list2)
    for i in range(length):
        if list2[i] in list1[::]:
            print("Common element:", list2[i])
else:
    length=len(list1)
    for i in range(length):
        if list1[i] in list2[::]:
            print("Common element:", list1[i])
