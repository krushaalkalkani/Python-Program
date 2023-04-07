class Employee:

    # init is constrctor 

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

krushal = Employee('Krushal', 'Das', 44000)
parth = Employee('Parth', 'Bodar', 1000000000)

print(krushal.fname, parth.salary)


