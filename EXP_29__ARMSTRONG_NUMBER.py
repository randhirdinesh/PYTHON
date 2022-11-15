num=int(input("Enter The Number:"))

summ=int('0')
temp=num

while(temp>0):
    digit=temp%10
    summ+=digit**3
    temp//=10

if num==summ:
     print(num,"is an Armstrong number")
else:
     print(num,"is Not an Armstrong number")
