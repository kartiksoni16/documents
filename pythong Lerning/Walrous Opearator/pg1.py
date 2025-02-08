text = "Hello, Python!"

le = len(text)
if (le > 10):
    print(f"Text is too long: {le} characters")


text = "Hello, Python!"

if (length := len(text)) > 10:
    print(f"Text is too long: {length} characters")



l = input("Enter value : ")
k = "kartik"

if (n := k == l):
    print(n)