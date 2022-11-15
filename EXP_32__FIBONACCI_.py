a=int(input("Enter a number:"))
b=[]
i=1
while i<=(a//2):
    if a%i==0:
        b.append(i)
    i=i+1
b.append(a)
print(b)
