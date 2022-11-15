a=input("Enter list of words seperated by ',':")
a=a.split(",")
l=len(a)
lar=0
wid=0
for i in range(l):
    temp=len(a[i])
    if temp>lar:
        lar=temp
        wid=i
print("the longest word is: "+a[wid]+" with length ",lar)
