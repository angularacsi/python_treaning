class Employee:

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

        
emp_1 = Employee('Walelign', 'Balew', 5000)
emp_2 = Employee('Adugnawu', 'addisu', 9000)

print(emp_1.fullname())
print(emp_2.email)














