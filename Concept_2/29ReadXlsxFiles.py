# Reading Excel Files using Pandas. 
# Can read CSV, Excel, Html, json.
import pandas as pd

#$ Read a specific sheet:
df = pd.read_excel('Concept_2/29DATA.xlsx', sheet_name="Badmos")    #Sheet1 & Badmos
# print(df)

#$ List all sheet names:-
print(pd.ExcelFile('Concept_2/29DATA.xlsx').sheet_names)