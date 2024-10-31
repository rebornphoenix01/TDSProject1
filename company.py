import pandas as pd

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Clean up the company names: trim whitespace, remove leading '@', and convert to uppercase
users_df['company'] = users_df['company'].str.strip().str.lstrip('@').str.upper()

# Count occurrences of each company and find the most common one
most_common_company = users_df['company'].value_counts().idxmax()
print(most_common_company)
