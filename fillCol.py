import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'contractor': ['Alice', 'Bob', 'Carol'], 'cost': [25, 30, 35]})

# Export the DataFrame to a CSV file, matching the data with the column names
df.to_csv('data.csv', index=False, header=False)
