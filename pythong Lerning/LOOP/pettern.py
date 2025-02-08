# # Result
#     *
#    ***
#   *****
#  *******
# *********

n = int(input("Enter Number : "))

for i in range(1,n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end= "")
    print("")


# # result
# *
# **
# ***

n = int(input("Enter Number : "))

for i in range(1,n+1):
    # print("" * i-n)
    print("*" * i)

# reverse table

n = int(input("Enter Number : "))

for i in range(10,0,-1):
    print(f"{n} * {i} = { n * i}")
    