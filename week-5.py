records = []
uid = 1

def add():
    global uid
    name = input("Name: ")
    city = input("City: ")
    rec = {"id": uid, "name": name, "city": city}
    records.append(rec)
    uid += 1

def search_city():
    c = input("City: ")
    for r in records:
        if r["city"] == c:
            print(r)

add()
add()
search_city()
