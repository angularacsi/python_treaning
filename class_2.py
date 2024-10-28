class Employee:
    num_of_emps=0
    raise_amount=1.04
   
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@gmail.com'
        Employee.num_of_emps+=1
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
print(Employee.num_of_emps)    # this prints zero b/c not created the class instance
emp_1 = Employee('Walelign', 'Balew', 5000)
emp_2 = Employee('Adugnawu', 'addisu', 9000)
print(Employee.num_of_emps) # this prints 2 b/c we created two instance of the class


Employee.raise_amount=1.05 #this changes the whole value to 1.05
emp_1.raise_amount=1.06 #this changes only its instance to 1.06


print (emp_1.raise_amount)  #accessing the variable by the class instance
print (Employee.raise_amount) #accessing the variable by class itself

print(emp_1.apply_raise())  # calling the function

print(Employee.__dict__)