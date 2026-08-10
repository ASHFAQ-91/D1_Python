import pandas as pd

data = {"name": ["Ali", "Sara", "John"],
        "marks": [75, 90, 80]
        }

df = pd.DataFrame(data);
print(df, "\n")
print(df["marks"])