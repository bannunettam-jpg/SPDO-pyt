records = []

while True:
    print("\n1. Add Record\n2. Display Records\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        records.append((name, age))
    elif choice == "2":
        for r in records:
            print(r)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
