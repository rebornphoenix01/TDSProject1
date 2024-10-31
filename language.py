import pandas as pd

# Load the repositories data from 'repositories.csv'
repos_df = pd.read_csv('repositories.csv')

# Drop rows where 'language' is missing (NaN)
repos_df = repos_df.dropna(subset=['language'])

# Count occurrences of each language and find the most common one
most_popular_language = repos_df['language'].value_counts().idxmax()
print(most_popular_language)
