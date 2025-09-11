## Exercise 1: Analysing Sales Data
import pandas as pd
df = pd.read_csv('task\\sales_data.csv')
grouped = df.groupby('Category').agg({'Quantity': ['sum', 'max'], 'Price': 'mean'})
print(grouped)
top = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False).groupby('Category').head(1)
print(top)
df['Total'] = df['Quantity'] * df['Price']
max_date = df.groupby('Date')['Total'].sum().idxmax()
print(max_date)

## Exercise 2: Examining Customer Orders
import pandas as pd
df = pd.read_csv('task\\customer_orders.csv')
grouped = df.groupby('CustomerID')['OrderID'].count()
customers_20plus = grouped[grouped >= 20].index
print(df[df['CustomerID'].isin(customers_20plus)])
avg_price = df.groupby('CustomerID')['Price'].mean()
high_avg = avg_price[avg_price > 120].index
print(high_avg)
product_tot = df.groupby('Product').agg({'Quantity': 'sum', 'Price': 'sum'})
print(product_tot[product_tot['Quantity'] >= 5])

## Exercise 3: Population Salary Analysis
import sqlite3
import pandas as pd
conn = sqlite3.connect('task\\population.db')
df = pd.read_sql("SELECT * FROM population", conn)
bands_df = pd.read_excel('task\\population salary analysis.xlsx')
def get_band(salary):
    for _, row in bands_df.iterrows():
        if row['Min'] <= salary < row['Max']:
            return row['Band']
    return 'Unknown'

df['Band'] = df['Salary'].apply(get_band)
perc = df['Band'].value_counts(normalize=True) * 100
avg = df.groupby('Band')['Salary'].mean()
median = df.groupby('Band')['Salary'].median()
count = df['Band'].value_counts()
print(perc, avg, median, count)
state_perc = df.groupby('State')['Band'].value_counts(normalize=True) * 100
state_avg = df.groupby(['State', 'Band'])['Salary'].mean()
