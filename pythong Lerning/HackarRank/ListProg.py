#  to find the runner-up from the list. 

# a = [1,2,5,4,3,8,6]
# b = sorted(a)
# print(b)

# print(b[-2])

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr1 = set(arr)
    print(arr1)
    arr1 = sorted(arr)
    print(arr1[-2])

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
    
#     arr1=sorted(arr)
#     print(arr1)
#     # print(arr1[-2])