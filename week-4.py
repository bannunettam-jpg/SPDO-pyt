records = []

def add_record():
    name = input("Name: ")
    records.append(name)

def display():
    for r in records:
        print(r)

def menu():
    while True:
        print("\n1.Add 2.Show 3.Exit")
        ch = input()
        if ch == "1":
            add_record()
        elif ch == "2":
            display()
        else:
            break

menu()
