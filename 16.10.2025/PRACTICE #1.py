class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.experience = 0
        self.coefficient = 1

    def salary(self):
        return int(self.coefficient * (self.experience/10 + 1) * 30000)

class Manager(Employee):
    def __init__(self, name, age, experience):
        Employee.__init__(self, name, age)
        self.experience = experience
        self.coefficient = 1.5

class Developer(Employee):
    def __init__(self, name, age, experience):
        Employee.__init__(self, name, age)
        self.experience = experience
        self.coefficient = 1.2

dev = Developer("Antony", 27, 6)
man = Manager("John", 31, 11)
print(dev.salary())
print(man.salary())