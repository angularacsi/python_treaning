class Employee:
    raise_amount=1.04
   
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@gmail.com'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
    
emp_1 = Employee('Walelign', 'Balew', 5000)
emp_2 = Employee('Adugnawu', 'addisu', 9000)


print (emp_1.raise_amount)  #accessing the variable by the class instance
print (Employee.raise_amount) #accessing the variable by class itself

print(emp_1.apply_raise())  # calling the function
