print("Square: \n")
s=int(input("Enter length of side: "))
x=lambda s: s*s

print("\n Area of square is ",x(s)," square units")

print("Rectangle: \n")
l=int(input("Enter length: "))
w=int(input("Enter width: "))
y=lambda l,w: l*w

print("\n Area of rectangle is ",y(l,w)," square units")

print("Triangle: \n")
b=int(input("Enter base: "))
h=int(input("Enter height: "))
z=lambda b,h: 0.5*b*h

print("\n Area of triangle is ",z(b,h)," square units")
