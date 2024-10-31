import pandas as pd

# Load the users data from 'users.csv' and repositories data from 'repositories.csv'
users_df = pd.read_csv('users.csv')
repos_df = pd.read_csv('repositories.csv')

# Convert 'created_at' to datetime
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Filter users who joined after 2020
recent_users = users_df[users_df['created_at'] > '2020-01-01']

# Drop rows where 'language' is missing in repositories
repos_df = repos_df.dropna(subset=['language'])

# Filter repositories to include only those owned by recent users
recent_repos = repos_df[repos_df['login'].isin(recent_users['login'])]

# Count occurrences of each language among the filtered repositories
language_counts = recent_repos['language'].value_counts()

# Get the second most popular language
second_most_popular_language = language_counts.index[1]  # Index 1 corresponds to the second most popular
print(second_most_popular_language)
