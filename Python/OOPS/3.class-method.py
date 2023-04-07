class Employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1


    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod #this is a decorator
    def change_increment(cls, amount):
        cls.increment = amount

harry = Employee('harry', 'jacson', 44000)

rohan = Employee('rohan', 'das', 74000)

print(harry.salary)
Employee.change_increment(3)
harry.increase()
print(harry.salary)