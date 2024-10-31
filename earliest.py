import pandas as pd

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Convert 'created_at' to datetime format if it's not already
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Sort by 'created_at' in ascending order and select the top 5
earliest_users = users_df.sort_values(by='created_at').head(5)

# Get the login names as a comma-separated list
earliest_user_logins = ','.join(earliest_users['login'].tolist())
print(earliest_user_logins)
