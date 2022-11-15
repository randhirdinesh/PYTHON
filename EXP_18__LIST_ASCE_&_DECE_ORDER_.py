y={'aksa':1,'ehsan':4,'savy':3,'sumu':2}
l=list(y.items())
l.sort()
print("ascending",l)
l=list(y.items())
l.sort(reverse=True)

print("decending",l)
dict=dict(l)
print("dict",dict)
