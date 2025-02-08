
def pettern(n):
    if (n == 0):
        return
    
    print("*" * n)
    pettern((n-1))


pettern(3)


youstr = input("Enter Value")
m = { 
    'a':1,
    'b' : 2,
    'c':3
}
you = m[youstr]

print(you)