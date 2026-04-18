def get_age():
    try:
        age = int("20")  # no input
        return age
    except:
        return None

print("Age:", get_age())
