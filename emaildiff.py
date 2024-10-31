import pandas as pd

# Load the user data from the CSV file (assuming you already have this file)
users_df = pd.read_csv('users.csv')

# Step 1: Calculate the fraction of users with email addresses for hireable users
hireable_users = users_df[users_df['hireable'] == True]
fraction_hireable_with_email = hireable_users['email'].notnull().sum() / len(hireable_users) if len(hireable_users) > 0 else 0

# Step 2: Calculate the fraction for non-hireable users
non_hireable_users = users_df[users_df['hireable'] == False]
fraction_non_hireable_with_email = non_hireable_users['email'].notnull().sum() / len(non_hireable_users) if len(non_hireable_users) > 0 else 0

# Step 3: Calculate the difference
email_difference = fraction_hireable_with_email - fraction_non_hireable_with_email

# Print the result rounded to three decimal places
print(f"Email difference (hireable - non-hireable): {email_difference:.3f}")
