# # 1. Multiplication table of a number
# a = int(input("Enter Number : "))
# for i in range(1,11):
#     print(f'{a} X {i} = {a * i}')



# 2. Find number is prime or not

# n = int(input("Enter the limit: ")) #9
# for num in range(2, n + 1): # 2, 3+1 =4
#     is_prime = True #
#     for i in range(2, num): 
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")

# With Math
# import math

# n = int(input("Enter the limit: "))
# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")

# 3. Factorial 

# 7 * 6* 5* 4*3*2*1

# n=int(input("Enter Number of facto : "))

# fact=1

# for i in range(1, n+1):
#     fact = fact * i

# print(fact)

# 4. fibbonacci series

# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# print(a, b, end=" ")
# for _ in range(2, n):
#     a, b = b, a + b
#     print(b, end=" ")

# data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# for x, _, z in data:
#     print(x, z)

# 



