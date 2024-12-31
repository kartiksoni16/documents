a = "Kartik"
for x in a:
    print(x)
    # if(x=="K"):
    #     # print("Value is matach")
    #     y= x.replace("K","tHis is new one")
    #     print(y)
       
a = "Kartik"
new_string = ""
for x in a:
    if x == "K":
        new_string += "tHis is new one"
    else:
        new_string += x

print(new_string)


