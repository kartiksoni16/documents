# To check the String is present in the file or not.

# with open("/home/kartik/Desktop/lerning/Learning-main/Learning-Learning_py_css/pythong Lerning/FILE io/PracticeSet/poem.txt",'w') as f:
#     f.write("Hello How Are you, I am kartik Soni, And I am 24 year old")


with open("/home/kartik/Desktop/lerning/Learning-main/Learning-Learning_py_css/pythong Lerning/FILE io/PracticeSet/poem.txt", 'r') as f1:

    c = f1.read()

    if(("kartik" or "Kartik") in c):

        print("The kartik is present")
    else:
        print("Kartik Is not Present")


