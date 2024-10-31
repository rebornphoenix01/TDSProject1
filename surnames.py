import pandas as pd
from collections import Counter

# Load the users data from 'users.csv'
users_df = pd.read_csv('users.csv')

# Step 2: Extract surnames
def extract_surname(name):
    if pd.isna(name):  # Check for missing names
        return None
    # Trim and split by whitespace, then take the last element as surname
    return name.strip().split()[-1]

# Apply the function to extract surnames
users_df['surname'] = users_df['name'].apply(extract_surname)

# Step 3: Count occurrences of each surname
surname_counts = Counter(users_df['surname'].dropna())

# Step 4: Identify the most common surname(s)
if surname_counts:
    most_common_count = max(surname_counts.values())
    most_common_surnames = [surname for surname, count in surname_counts.items() if count == most_common_count]
    
    # Step 5: Sort the surnames alphabetically
    most_common_surnames.sort()
    
    # Output the result
    result = ', '.join(most_common_surnames)
    print(f"Most common surname(s): {result}")
else:
    print("No surnames found.")
