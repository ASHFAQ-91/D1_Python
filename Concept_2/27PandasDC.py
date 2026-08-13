# Selecting, Filtering and Data Cleaning with Pandas
import pandas as pd

df = pd.DataFrame({
    "Product name": ["iPhone 15", "Samsung 25", "Pixel 7", "Poco f7", None] * 200,
    "price": [999, 799, 749, 349, None] * 200,
    "category": ["mobile", "Mobile", "ELECTRONICS", "electronics", None] * 200,
    "rating": [4.5, 4.3, 4, 4.5, None] * 200,
    "reviews": [8000, 6000, 3000, 4500, 150] * 200,
    "in_stock": ["Yes", "No", "no", "yes", None] * 200,
    "launch_year": ["2023", "2025", "2022", "2026", None] * 200
})

# print(df)
# print(df["price"])                  # print single_column.
# print(df[["price", "launch_year"]]) # print multi_columns

#$ conditions:-
# print(df[df['in_stock']== "Yes"])
# print(df[df['reviews'] > 5000])
# print(df[(df['reviews'] <> 6000) & (df['in_stock'] == "Yes")])

#$ Handling Missing Values:-
# print(df.isna());
# print(df.isna().sum());

#$ Remove Missing values:-
# print(df.dropna()); 

#$ Rename Columns:-
# df = df.rename(columns={"Product name": "product_name"})
# print(df)

#$ data types:-
print(df.dtypes)