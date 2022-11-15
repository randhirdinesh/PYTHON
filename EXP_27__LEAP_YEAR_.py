y=int(input("enter an year:\n"))
if(y % 4 == 0 and y % 100 != 0):
    print("year is a leap year")
elif (y % 400 == 0):
    print("leap year")
else:
    print("not leap ye")
