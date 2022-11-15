import math
a=int(input("enter the first value"))
b=int(input("enter the second value"))

print("before swap a=",a," b=",b)
a=a+b
b=a-b
a=a-b
print("after swap a=",a," b=",b)
