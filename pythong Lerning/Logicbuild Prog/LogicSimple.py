#  Hello World 

print("Hello, World")

# 2. Sum of the two number

a= 20
b=30
print(a+b)

# c=int(input("Enter Number of the C "))
# d = int(input("Enter Number of the D "))
# print( c + d)

# 3.Check Even or Odd

# a = int(input("Enter Number : "))
# if (a%2 == 0):
#     print("Number is even")
# else:
#     print("Number is odd")

# 4. Find Largest Number

# a = int(input("Enter Number a "))            
# b = int(input("Enter Number b"))
# c= int(input("Enter Number c"))
# if a > b and a > c:
#     print(" a is larger")
# elif b>a and b>c:
#     print("b is grater")
# else:
#     print("c is grater")

# print("The Largest number", max(a,b,c))

# 5. Print Numbers from 1 to N

# n = int(input("Enter Number : "))

# for i in range(1, n+1):
#     print(i)

# 6. Calculate the Factorial of a Number

# n = int(input("Enter Number : "))
# fact =1
# for i in range(1, n+1):
#     fact = fact * i

# print(fact)

# 7. revese string.

st = "Badshah"
# print(st[::-1])

reversed = ""

for i in st:
    reversed = i + reversed 
    print(reversed)
    