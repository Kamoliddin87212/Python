## Exercise 1:
import pandas as pd
df = pd.read_csv('task\\stackoverflow_qa.csv')
print(df[df['creationdate'] < '2014-01-01'])
print(df[df['score'] > 50])
print(df[(df['score'] >= 50) & (df['score'] <= 100)])
print(df[df['ans_name'] == 'Scott Boston'])
users = ['user1', 'user2', ...]  # 5 users
print(df[df['ans_name'].isin(users)])
print(df[(df['creationdate'] >= '2014-03-01') & (df['creationdate'] <= '2014-10-31') & (df['ans_name'] == 'Unutbu') & (df['score'] < 5)])
print(df[(df['score'].between(5,10)) | (df['viewcount'] > 10000)])
print(df[df['ans_name'] != 'Scott Boston'])

## Exercise 2:
import pandas as pd
df = pd.read_csv("task\\titanic.csv")
print(df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & (df['Age'].between(20,30))])
print(df[df['Fare'] > 100])
print(df[(df['Survived'] == 1) & (df['SibSp'] == 0) & (df['Parch'] == 0)])
print(df[(df['Embarked'] == 'C') & (df['Fare'] > 50)])
print(df[(df['SibSp'] > 0) & (df['Parch'] > 0)])
print(df[(df['Age'] <= 15) & (df['Survived'] == 0)])
print(df[df['Cabin'].notna() & (df['Fare'] > 200)])
print(df[df['PassengerId'] % 2 == 1])
print(df.drop_duplicates(subset='Ticket'))
print(df[(df['Name'].str.contains('Miss')) & (df['Pclass'] == 1)])
