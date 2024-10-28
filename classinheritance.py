class Employee:
    num_of_emps=0
    raise_amount=1.04
   
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@gmail.com'
        Employee.num_of_emps+=1
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
class developer(Employee): # this class inherits from the main class Employee
    raise_amount =1.10 # changing the amount of the developers only 
    
    def __init__(self,firstname,lastname,pay,proglang): 
        super().__init__(firstname, lastname, pay) # calling the parent class constructor
        self.proglang = proglang # adding a new attribute to the developer class
 
class Manager(Employee):

    def __init__(self, firstname,lastname,pay,employees=None):
        super().__init__(firstname,lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()