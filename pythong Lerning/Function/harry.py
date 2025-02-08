
def greet(name):
    print("Good Day,",name)

greet("Harry")


# Recursion

def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n - 1)


print(fact(5))

n = int(input("Enter Number "))

print(f'Factoria of {n} = {fact(n)}')