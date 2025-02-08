
def multi_table(a):
    result = ""
    for i in range(1,11):
        result = result + f"{a} X {i} = {a * i} \n"
        
    with open(f"/home/kartik/Desktop/lerning/Learning-main/Learning-Learning_py_css/pythong Lerning/FILE io/PracticeSet/tables{a}.csv",'w') as w:
        print(w.write(result))


for i in range(2,21):
    multi_table(i)

