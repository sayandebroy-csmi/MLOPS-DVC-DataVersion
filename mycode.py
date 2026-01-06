import pandas as pd
import os

# Create a sample DataFrame with columns 'Name', 'Age', and 'City'
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# # Add new row to df for v2
new_row_loc = {'Name': 'v2', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df)] = new_row_loc

# # Addding another row for v3
# new_row_loc2 = {'Name': 'v3', 'Age': 26, 'City': 'Seattle'}
# df.loc[len(df.index)] = new_row_loc2

# Ensure the "data" dictory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path to save the CSV file
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)

print(f"CSV saved to {file_path}")