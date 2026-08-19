import pandas as pd

df = pd.DataFrame({
    "name": ["Ram", "Shaam", "Mohan"],
    "age": [21,22,23],
    "class": [7,8,9]
})

print(df)

df.to_csv('30DATA.csv', index=False);