records = []

def add():
    name = input("Name: ").strip()
    records.append(name)

def search():
    key = input("Search name: ").lower()
    for r in records:
        if key in r.lower():
            print("Found:", r)

while True:
    print("\n1.Add 2.Search 3.Show 4.Exit")
    ch = input()

    if ch == "1":
        add()
    elif ch == "2":
        search()
    elif ch == "3":
        print(records)
    else:
        break
