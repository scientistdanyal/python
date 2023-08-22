class Employee:


    num_of_empl = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_empl +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Dnayal','Ahmed',7000000)

emp_2 = Employee('Ali', 'Khan',899090)


emp_1.raise_amount = 1.05
# print(emp_2.fullname())
print(emp_1.__dict__)

print(emp_1.raise_amount)
print(emp_1.__dict__)
print(Employee.num_of_empl)