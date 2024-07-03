import pandas as pd

df = pd.read_csv('train.csv')

# Remove all rows that have 'NaN' in at least one column
# Another solution: is to add averages
df = df.dropna()

# Print the cleaned DataFrame
print("All DataFrames cleaned of NaN")
print(df.to_string())

# Add family count
print("Family Count")
df['Family Count'] = df['SibSp'] + df['Parch']
print(df)


print("Age Interpreter")
df['AgeInterpreter'] = pd.cut(df['Age'], bins=[0, 18, 65, 200], labels=['Underage', 'Adult', 'Senior'])
print(df)


# Extract surname from the 'Name' column
df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0].strip())

# Initialize the 'IsAlone' column
df['IsAlone'] = True

# Loop over each row to determine if the passenger was alone or with relatives
for index, row in df.iterrows():
    surname_count = df[df['Surname'] == row['Surname']].shape[0]
    if surname_count > 1:
        df.at[index, 'IsAlone'] = False

# Print the DataFrame with the new 'IsAlone' column
print(df)



# Average class age
print(df.groupby('Pclass')['Age'].mean())


# Remove all rows that have 'NaN' in the 'Fare' or 'Survived' columns
df_cleaned = df.dropna(subset=['Fare', 'Survived'])

# Does the price of the ticket make higher chances of survival?
mean_fare_by_survival = df_cleaned.groupby('Survived')['Fare'].mean()

print("Mean Fare by Survival Status:")
print(mean_fare_by_survival)


# Compute the correlation matrix

df_cleaned = df.dropna()


# Select only the numeric columns
numeric_df = df_cleaned.select_dtypes(include=['number'])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# df_cleaned['isWithNany'] = (df_cleaned['Family Count'] < 1) & (df_cleaned['Age'] < 18)
# df_cleaned['isWithNany'] = df_cleaned['isWithNany'].astype(int)
# print(df_cleaned)

# # Compute the correlation between 'isWithNany' and 'Survived'
# correlation = df_cleaned[['isWithNany', 'Survived']].corr()

# # Print the correlation matrix
# print("Correlation between 'isWithNany' and 'Survived':")
# print(correlation)

# # Average port price
# mean_fare_by_port = df_cleaned.groupby('Embarked')['Fare'].mean()
# print(mean_fare_by_port)