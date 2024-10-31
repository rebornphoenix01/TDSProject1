import pandas as pd

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Step 2: Calculate the number of hireable and non-hireable users
total_hireable = users_df[users_df['hireable'] == True]
total_non_hireable = users_df[users_df['hireable'] == False]

# Count users with email for hireable
hireable_with_email = total_hireable['email'].notnull().sum()
fraction_hireable_with_email = hireable_with_email / len(total_hireable) if len(total_hireable) > 0 else 0

# Count users with email for non-hireable
non_hireable_with_email = total_non_hireable['email'].notnull().sum()
fraction_non_hireable_with_email = non_hireable_with_email / len(total_non_hireable) if len(total_non_hireable) > 0 else 0

# Step 3: Compute the difference
difference = fraction_hireable_with_email - fraction_non_hireable_with_email

# Step 4: Print the result rounded to 3 decimal places
print(f"Difference in email sharing: {difference:.3f}")
