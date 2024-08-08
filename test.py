import pandas as pd

# Read the CSV file into a DataFrame
# df = pd.read_csv('myfile.csv')


# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

print("/////")

print(s[2])
print(s.iloc[3])

print("/////")
print(s[1:4])

print("/////")

# Creating a DataFrame from a dictionary
data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df2 = pd.DataFrame(data2)
print(df2)

print("/////")

print(df2['Name'])
print("Tipo ",type(df2))

print("/////")

print(df2[['Name', 'Age']])  # Select specific columns
print("/////")
print(df2[1:4])             # Select specific rows

print("/////")
unique_dates = df2['Age'].unique()
print(unique_dates)

print("/////")
high_above_25 = df2[df2['Age'] > 25]
print(high_above_25)

print("/////")

df2.to_csv('trading_data.csv', index=False)
print("/////")


print(df2.iloc[0, 2])   # With index
print("/////")
print(df2.loc[2, 'Age'])  # With name

print("/////")

df3=df2
# It sets the names as index
df3=df3.set_index("Name")
print(df3)
print("/////")

# It shows the first 5 rows
print(df2.head())

print("/////")

print(df3.loc['David', 'City'])

print("/////")
print(df2.iloc[0:2, 0:3])
print("/////")
print(df2.loc[0:2,'Age':'City'])
print("/////")
print(df3.loc['Bob':'David', 'Age':'City'])
print("/////")
print("/////")
