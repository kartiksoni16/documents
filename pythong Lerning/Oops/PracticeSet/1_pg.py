# Print the conpmay name of the Emploee

class emploee:

    def __init__(self,name, em_no, em_email, em_department):

        self.name = name
        self.em_no = em_no
        self.m_email = em_email
        self.em_department = em_department
        

k = emploee("Khushi",23,"abc@gmai.com","Computer")

print(f"Emploee Name is {k.name} his no is {k.em_no} and the email is {k.em_email} and thier deparment is {k.em_department}")