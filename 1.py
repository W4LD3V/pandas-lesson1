import pandas as pd
import numpy as np

# Generate a DataFrame with random data
# Uniform - float, randint - integers
np.random.seed(1)
data = {
    'Temperature': np.random.uniform(low=-10, high=30.0, size=5),
    'Humidity': np.random.uniform(low=40.0, high=60.0, size=5),
    'Pressure': np.random.uniform(low=1000.0, high=1020.0, size=5)
}

df = pd.DataFrame(data)

print(df)


# Print 1st and 4th rows
print(df.iloc[[0, 3]])

# Filter out the results where temp is negative
minus_temp = df[df['Temperature'] < 0]
print(minus_temp)

temp_sum = df['Temperature'].sum()
print(temp_sum)

# Add a new column 'Wind Speed'
df['WindSpeed'] = np.random.uniform(low=0.0, high=30.0, size=5)

# Adding risk of catching cold column
df['ColdRisk'] = df['Temperature'].apply(lambda x: 'Yes' if x < 0 else 'No')
print(df)

# def wind_to_string(wind):
#     if wind > 20:
#         return 'STRONG'
#     elif wind > 10:
#         return 'MODERATE'
#     else:
#         return 'WEAK'

# df['WindSpeed'] = df['WindSpeed'].apply(wind_to_string)
    
# mappings = {
#     '0.0': 'WEAK',
#     '10.0': 'MODERATE',
#     '20.0': 'STRONG'  # For wind speeds > 20, we assume it's strong
# } 

# df['WindSpeed'] = df['WindSpeed'].map(mappings)

# pd.cut(df['WindSpeed'], bins=[0,10,20,30], labels=['WEAK', 'MODERATE', 'STRONG'])

df['WindSpeed'] = pd.cut(df['WindSpeed'], bins=[0,10,20,30], labels=['WEAK', 'MODERATE', 'STRONG'])
print(df)


# Group by 'ColdRisk' and print the mean temperature of each group
print("Temp mean values grouped by 'ColdRisk'")
print(df.groupby('ColdRisk')['Temperature'].mean())


# Sort by temperature
# Be inplace kitaip nesortina
df.sort_values(by="Temperature", ascending=True, inplace=True)
print(df)



data1 = {
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Temperature': np.random.uniform(low=-10, high=30.0, size=5)
}

data2 = {
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'WindSpeed': np.random.uniform(low=-0.0, high=20.0, size=5)
}

# Convert dictionaries to DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the DataFrames on the 'Date' column
merged_df = pd.merge(df1, df2, on='Date')

print(merged_df)