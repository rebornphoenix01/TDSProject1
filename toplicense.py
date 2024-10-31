import pandas as pd

# Load the repositories data from 'repositories.csv'
repos_df = pd.read_csv('repositories.csv')

# Filter out rows with missing license names
licensed_repos = repos_df.dropna(subset=['license_name'])

# Count the occurrences of each license and get the top 3
top_licenses = licensed_repos['license_name'].value_counts().head(3)

# Get the license names as a comma-separated list
top_license_names = ','.join(top_licenses.index.tolist())
print(top_license_names)
