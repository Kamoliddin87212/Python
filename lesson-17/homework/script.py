## Exercise 1:
import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
df = df.rename(columns={"First Name": "first_name", "Age": "age"})
print(df.head(3))
print(df['age'].mean())
print(df[['first_name', 'City']])
df['Salary'] = np.random.randint(50000, 100000, len(df))
print(df.describe())

## Exercise 2:
import pandas as pd
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 'Sales': [5000,6000,7500,8000], 'Expenses': [3000,3500,4000,4500]}
df = pd.DataFrame(data)
print(df['Sales'].max(), df['Expenses'].max())
print(df['Sales'].min(), df['Expenses'].min())
print(df['Sales'].mean(), df['Expenses'].mean())

## Exercise 3:
import pandas as pd
data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
        'January': [1200,200,300,150], 'February': [1300,220,320,160], 'March': [1400,240,330,170], 'April': [1500,250,350,180]}
df = pd.DataFrame(data).set_index('Category')
print(df.max(axis=1))
print(df.min(axis=1))
print(df.mean(axis=1))
