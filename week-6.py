class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display(self):
        print(f"Name: {self.name}, City: {self.city}")


records = []

p1 = Person("User1", "CityA")
p2 = Person("User2", "CityB")

records.append(p1)
records.append(p2)

for r in records:
    r.display()
