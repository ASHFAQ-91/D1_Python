# Reading CSV Files using Pandas.
# Can read CSV, Excel, Html, json.
import pandas as pd

df = pd.read_csv('Concept_2/28DATA.csv')    # give relative_path
print(df)

#$ Selecting Specific Columns:-
abc = pd.read_csv('Concept_2/28DATA.csv', usecols=('order_id', 'order_status', 'city'))
print(f"\n\n\t\t***Selecting Specific Columns:***\n{abc}\n\n");

#$ Select All Delivered Orders:-
delivered_orders = df[df['order_status'] == "Delivered"]
print(delivered_orders, "\n\n");

#$ Select All Delivered Orders from Bangalore:-
dofb = df[(df['order_status'] == 'Delivered') & (df['city'] == 'Jaipur')]
print(dofb);