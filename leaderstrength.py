import pandas as pd

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Calculate leader_strength
users_df['leader_strength'] = users_df['followers'] / (1 + users_df['following'])

# Sort by leader_strength in descending order and select the top 5
top_leaders = users_df.sort_values(by='leader_strength', ascending=False).head(5)

# Get the login names as a comma-separated list
top_leader_logins = ','.join(top_leaders['login'].tolist())
print(top_leader_logins)
