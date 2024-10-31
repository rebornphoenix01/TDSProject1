import pandas as pd

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Sort by followers in descending order and select the top 5
top_users = users_df.sort_values(by='followers', ascending=False).head(5)

# Get the login names as a comma-separated list
top_user_logins = ','.join(top_users['login'].tolist())
print(top_user_logins)
