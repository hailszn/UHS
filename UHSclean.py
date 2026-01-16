import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel(r'c:\Users\lilbi\OneDrive\Documents\UHS\UHS1.xlsx')

#null check
print(df.isnull().sum())
print(df.info())
# Save the cleaned data to a new Excel file
#df.to_excel('UHS1_cleaned.xlsx', index=False)