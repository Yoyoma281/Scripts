import os
import pandas as pd
file_path_1 = input("file 1")
file_path_2 = input("file 2")

file_path_1 = os.path.abspath(file_path_1)  # Convert to absolute path
file_path_2 = os.path.abspath(file_path_2)  # Convert to absolute path

# Read both Excel files
df1 = pd.read_excel(file_path_1, engine='openpyxl')
df2 = pd.read_excel(file_path_2, engine='openpyxl')

# Compare DataFrames and find differences
diff = df1.compare(df2)

if diff.empty:
    print("The Excel files are identical.")
else:
    print("Differences found:")
    print(diff)

    # Save differences to an Excel file for review
    diff.to_excel("differences.xlsx")
    print("Differences saved to 'differences.xlsx'.")