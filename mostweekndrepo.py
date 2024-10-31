import pandas as pd

# Load the repositories data from 'repositories.csv'
repos_df = pd.read_csv('repositories.csv')

# Step 2: Convert the 'created_at' column to datetime format
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])

# Step 3: Extract the day of the week (0=Monday, 6=Sunday)
repos_df['day_of_week'] = repos_df['created_at'].dt.dayofweek

# Step 4: Filter for weekend days (Saturday=5, Sunday=6)
weekend_repos = repos_df[repos_df['day_of_week'].isin([5, 6])]

# Step 5: Group by user login and count the number of repositories
weekend_counts = weekend_repos.groupby('login')['full_name'].count().reset_index()

# Rename columns for clarity
weekend_counts.columns = ['login', 'repo_count']
print(weekend_counts)

# Step 6: Sort by the number of repositories and get the top 5
top_weekend_users_print = weekend_counts.sort_values(by='repo_count', ascending=False).head(10)
print(top_weekend_users_print)
top_weekend_users = weekend_counts.sort_values(by='repo_count', ascending=False).head(5)

# Step 7: Extract the logins and join them as a comma-separated string
top_user_logins = ', '.join(top_weekend_users['login'])

# Print the result
print(f"Top 5 users who created the most repositories on weekends: {top_user_logins}")

# import pandas as pd

# # Load the repository data from 'repositories.csv'
# repos_df = pd.read_csv('repositories.csv')

# # Step 2: Convert 'created_at' to datetime
# repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])

# # Debugging: Check if the 'created_at' conversion was successful
# print("First few entries of 'created_at':")
# print(repos_df['created_at'].head())

# # Step 3: Filter for repositories created on weekends (Saturday and Sunday)
# # dayofweek: Monday=0, Sunday=6; hence we check for 5 (Saturday) and 6 (Sunday)
# weekend_repos = repos_df[repos_df['created_at'].dt.dayofweek.isin([5, 6])]

# # Debugging: Check the weekend repositories
# print(f"Number of repositories created on weekends: {len(weekend_repos)}")
# print("First few weekend repositories:")
# print(weekend_repos.head())

# # Step 4: Count the number of repositories created by each user on weekends
# # Ensure 'login' is in the DataFrame; this may need to be extracted from the repository's full_name.
# top_users = weekend_repos['login'].value_counts().head(5)  # Get top 5 users

# # Debugging: Check top users
# print("Top users by weekend repository count:")
# print(top_users)

# # Step 5: Prepare the result
# top_user_logins = ','.join(top_users.index)

# # Output the result
# print(f"Top 5 users who created the most repositories on weekends: {top_user_logins}")


