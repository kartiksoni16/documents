class first:
    name = "Kartik"
    emploee = "Computer"
    age = 20


    def getInfo(self):
        print(f"I am {self.name} and Working in {self.emploee} and i am {self.age} old")


    def __init__(self, name, emploee, email):
        self.name = name
        self.emploee = emploee
        self.email = email
        print("Using cinstructor")

name = first("Kartik","Electronics","ks@gmai,com")
# name.emploee = "Machenical"
# print(name.emploee,name.age)

print(name.name, name.emploee, name.email)


