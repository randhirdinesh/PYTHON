number = int(input("Enter a Number"))

if number > 1:
    for i in range(2,int(number/2)+1):
        if (number % i == 0):
            print(number, "is not a Prime Number")
            break
    else:
        print(number,"is a Prime number")

else:
    print(number,"is not a Prime number")
