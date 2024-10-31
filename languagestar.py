import pandas as pd

# Load the repositories data from 'repositories.csv'
repos_df = pd.read_csv('repositories.csv')

# Drop rows where 'language' or 'stargazers_count' is missing (NaN)
repos_df = repos_df.dropna(subset=['language', 'stargazers_count'])

# Group by 'language' and calculate the average number of stars
average_stars_per_language = repos_df.groupby('language')['stargazers_count'].mean()

# Identify the language with the highest average number of stars
highest_average_language = average_stars_per_language.idxmax()
highest_average_value = average_stars_per_language.max()

print(f"Language with highest average stars: {highest_average_language} ({highest_average_value:.2f} stars)")
