a=input("Enter a list of +ve & -ve numbers:\n")

l1=map(int,a.split(','))

l2=[i for i in l1 if i>0]

print("The +ve numbers are: \n",l2)
