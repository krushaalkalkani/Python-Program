class Employee:

    Increment = 1.5

    # init is constrctor 

    def __init__(self, fname, lname, salary):
        # instant variable 
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.Increment)

krushal = Employee('Krushal', 'Das', 44000)
parth = Employee('Parth', 'Bodar', 1000000000)

print(krushal.__dict__) # To see the all variable of intance
print(krushal.salary)
krushal.increase()
print(krushal.salary)


