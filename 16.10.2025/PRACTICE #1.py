from os.path import expanduser


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.experience = 0
        self.coefficient = 1

    def salary(self):
        return self.coefficient * (self.experience + 1) * 4600

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

dev = Developer("", 25, 15)
print(dev.salary())