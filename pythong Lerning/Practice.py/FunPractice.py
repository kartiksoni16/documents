# 1. To check no is Plaidram or not.
# def is_palim(s):
#     s= s.lower()
#     return s == s[::-1]

# s=input("Enter Value ")
# print(is_palim(s))


# 2. Reverse a string without using slicing.

# def reverse_string(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s
#     return reversed_s

# # Test
# print(reverse_string("hello"))

# a="Hello"
# reverse_ss = ""
# for i in a:
#     reverse_ss = i + reverse_ss
#     print(reverse_ss)

# 3. Count the frequency of each character in a string.

# a = "Kartik"
# for i in enumerate(a, start=1):
#     print(i, end='')


# 4. Check if two strings are anagrams.

# s=input("Enter first value : ")
# s2=input("Enter first value : ")
# if(sorted(s) == sorted(s2)):
#     print(True)
# else:
#     print(False)

# def to_check_angram(s,s1):
#     return (sorted(s1) == sorted(s1))



# print (to_check_angram('abcdefgh', 'dbeacfgh'))


# 5. Find the longest word in a string.

# s = "My Name is Kartik Soni"

# word = s.split(" ")

# s= max(word,key=len)
# print(s)

# Without function

# s = "My mom is making food"

# word = s.split(" ")
# print(word)

# long =""
# for words in word:
#     if len(words) > len(long):
#         long = words

# print(long)

# word1 = s.strip("")

# 11. Remove spaces from a string.
# s = "The quick brown fox"
# no_spaces = ""
# for char in s:
#     if char != " ":
#         no_spaces = no_spaces + char
# print(no_spaces)  # Output: "Thequickbrownfox"

# print("Result of the 11the q : " ,len(no_spaces))

# 6.  Replace all vowels in a string with '*'.

# s = "Kartik"
# vovel="aeiouAEIOU"
# replace = ""
# for char in s:
#     if char in vovel:
#         replace = replace + '*'
#         # print(replace)
#     else:
#         replace = replace + char
# print(replace)

# 7. Count the number of words in a string.

# s = "Kartik Is My name"
# count = 0
# for i in s.split():
#     count = count + 1
# print(count)

# 8. Check string is substing
s = "Kartik"
s1 = "My name is Kartik"

s3 = s1 in s2
print(s3)







