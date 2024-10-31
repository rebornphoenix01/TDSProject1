import pandas as pd
import statsmodels.api as sm

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Prepare the data for regression
X = users_df['public_repos']  # Independent variable
y = users_df['followers']      # Dependent variable

# Add a constant to the independent variable (for the intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the slope for public_repos
slope = model.params['public_repos']

# Print the slope rounded to 3 decimal places
print(f"Regression slope of followers on public repositories: {slope:.3f}")
