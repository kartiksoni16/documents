# Print the conpmay name of the Emploee

class emploee:

    
    def __init__(self,n):
        self.n = n
    
    def squre(self):
        print(f"Sqare root of {self.n} = {self.n*self.n}")

    def qube(self):
        print(f"Cube of {self.n} = {self.n*self.n*self.n}")

    def squreRoot(self):
        print(f"Sqareroot of {self.n} = {self.n**1/2}")

    def add(self):
        return 20 + 30
        

# k = emploee("Khushi",23,"abc@gmai.com","Computer")

cal = emploee(25)

cal.squre()
cal.squreRoot()
cal.qube()

cal.add()

