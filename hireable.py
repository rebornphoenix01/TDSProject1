import pandas as pd

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Calculate the average following for hireable users
avg_following_hireable = users_df[users_df['hireable'] == True]['following'].mean()

# Calculate the average following for non-hireable users
avg_following_non_hireable = users_df[users_df['hireable'] == False]['following'].mean()

# Calculate the difference
following_difference = avg_following_hireable - avg_following_non_hireable

# Print the result rounded to 3 decimal places
print(f"Difference in average following: {following_difference:.3f}")
