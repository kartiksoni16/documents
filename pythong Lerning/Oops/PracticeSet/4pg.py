# Print the conpmay name of the Emploee
import random
class ticket:

    def __init__(self,ticket_no):
        self.ticket_no = ticket_no

    def book(self,fro,to):
        print(f"Enter Ticket no{self.ticket_no} and {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.ticket_no}")

    def getfare(self,fro,to):
        print(f"{self.ticket_no} {fro} {to} is {random.randint(300,300000)}")



t = ticket(345)


t.book("Baroda","AHmedabad")