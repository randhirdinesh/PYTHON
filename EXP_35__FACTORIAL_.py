def factorial(n):
    f = n
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
        
num = int(input("Enter a number:"))

for i in range(1,num+1):
    f = factorial(i)
print("Factorial of the number:",f)
