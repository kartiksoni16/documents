a = int(input("Enter Number in Python : "))

match a:
    case 1:
        print("Case 1 is executed.")
    case 4:
        print("case 4 is execusted.")
    case 5:
        print( "Case 5 is executed.1")
    case _ if a>20:
        print(a,"Case default is executed")
    case _:
        print(a)