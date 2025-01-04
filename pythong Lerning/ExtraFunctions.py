import time

n = "kartik soni"
for i in n:
    print(i)


# set separator between multiple arguments in a single
print("My","Name", "is", "Kartik", sep='-')

# flush parameter, when set to True, forces the output to be written to the stream immediately.

# st="My Name is Kartik"
# print("Loading",end='')
# for i in range(2):
#     time.sleep(2)
#     print('.',end='',flush=True)


# Return Index and value both of the variable.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Combines two or more iterables into a single iterator of tuples.
names = ['Alice', 'Bob']
ages = [25, 30]
# print(names + ages)
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")


