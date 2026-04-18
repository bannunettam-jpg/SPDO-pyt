class Record:
    def display(self):
        print("Base Record")

class Person(Record):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Person Name: {self.name}")


p = Person("User1")
p.display()
