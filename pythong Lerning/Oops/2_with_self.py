class first:
    name = "Kartik"
    emploee = "Computer"
    age = 20


    def getInfo(self):
        print(f"I am {self.name} and Working in {self.emploee} and i am {self.age} old")

name = first()
name.emploee = "Machenical"
print(name.emploee,name.age)

name.getInfo()



