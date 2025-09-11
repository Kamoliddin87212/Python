## Exercise 1: Customer Purchases Analysis
import sqlite3
import pandas as pd
conn = sqlite3.connect('chinook.db')
df = pd.read_sql("""
SELECT c.CustomerId, c.FirstName || ' ' || c.LastName as Name, SUM(i.Total) as Total
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY Total DESC
LIMIT 5
""", conn)
print(df)

## Exercise 2: Album vs. Individual Track Purchases
df = pd.read_sql("SELECT * FROM invoice_items", conn)
