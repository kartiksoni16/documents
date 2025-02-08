# Write the program that use enter value in ist

k = input("Enter Value in list").split()
print(k)

# Enter & student name store them in  ascending order

list_lst = []

p = input("Enter Marks")
list_lst.append(p)

p2 = input("Enter Marks")
list_lst.append(p2)

p3 = input("Enter Marks")
list_lst.append(p3)

p4 = input("Enter Marks")
list_lst.append(p4)

p5 = input("Enter Marks")
list_lst.append(p5)

p6 = input("Enter Marks")
list_lst.append(p6)

print(list_lst)

# print(sorted(list_lst))

list_lst.sort()
print(list_lst)