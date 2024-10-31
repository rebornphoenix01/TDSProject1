import pandas as pd
import statsmodels.api as sm

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Step 2: Calculate the length of the bio in words
# Ignore users without bios
users_df['bio_word_count'] = users_df['bio'].apply(lambda x: len(x.split()) if pd.notnull(x) else 0)

# Filter out users with no bio
filtered_users_df = users_df[users_df['bio_word_count'] > 0]

# Step 3: Prepare the data for regression
X = filtered_users_df['bio_word_count']  # Independent variable
y = filtered_users_df['followers']        # Dependent variable

# Add a constant to the independent variable (for the intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the slope for bio_word_count
slope = model.params['bio_word_count']

# Step 4: Print the slope rounded to 3 decimal places
print(f"Regression slope of followers on bio word count: {slope:.3f}")
