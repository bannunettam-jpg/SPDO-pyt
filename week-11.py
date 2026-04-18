import pandas as pd

data = {
    "name": ["User1", "User2", "User3"],
    "city": ["CityA", "CityB", "CityA"]
}

df = pd.DataFrame(data)

print(df)

print("\nCity-wise count:")
print(df.groupby("city").count())
