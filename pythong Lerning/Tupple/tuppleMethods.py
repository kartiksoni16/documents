t=(3,2,5,"Badshah","Boss")

print(len(t))

temp=list(t)
temp.append(40)
print(temp)

temp.pop(2) #Using this we can remove the data from specific portion.

print(temp)

t = tuple(temp)
print(t)

k=(3,2,1)
l=(1,2,3)

print(k+l)

m=k+l
print(m)

n = m.count(2)
print(n)

print(m.count(2))