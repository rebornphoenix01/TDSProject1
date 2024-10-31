import pandas as pd

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Calculate the correlation between 'followers' and 'public_repos'
correlation = users_df['followers'].corr(users_df['public_repos'])

# Print the correlation rounded to 3 decimal places
print(f"Correlation between followers and public repositories: {correlation:.3f}")
