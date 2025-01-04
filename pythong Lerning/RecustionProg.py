def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

# fobimacci series

s = int(input("Enter Value : "))
def febo(n):
    if(n == 0):
        return 0
    elif(n==1):
        return 1
    else:
        return febo(n-1) + febo(n-2)
for i in range(s):  
        print(febo(i))

# 5-1 = 4 + 5-2 =3 7
#  4-1 =3 + 4-2 =2  5
# 3-1 =2 + 3-2 = 1  3
# 2 -1 =1 + 2-2 = 0 1
# 1