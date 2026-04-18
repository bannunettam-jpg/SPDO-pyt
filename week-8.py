import json

records = [
    {"name": "User1", "city": "CityA"},
    {"name": "User2", "city": "CityB"}
]

# Save to file
with open("data.json", "w") as f:
    json.dump(records, f)

# Load from file
with open("data.json", "r") as f:
    data = json.load(f)

print(data)
