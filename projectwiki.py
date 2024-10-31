import pandas as pd

# Load the repositories data from 'repositories.csv'
repos_df = pd.read_csv('repositories.csv')

# Ensure that 'has_projects' and 'has_wiki' are treated as boolean values
# Assuming 'has_projects' and 'has_wiki' are represented as True/False or 1/0 in the CSV
repos_df['has_projects'] = repos_df['has_projects'].astype(bool)
repos_df['has_wiki'] = repos_df['has_wiki'].astype(bool)

# Calculate the correlation between having projects enabled and having wiki enabled
correlation = repos_df['has_projects'].corr(repos_df['has_wiki'])

# Print the correlation rounded to 3 decimal places
print(f"Correlation between projects and wiki enabled: {correlation:.3f}")
