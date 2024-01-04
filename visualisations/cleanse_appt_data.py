import pandas as pd

df = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\attp_data.xlsx")

#Data Cleansing
# Replace the specified value in the 'Ethnic Group' column
df['Ethnic Group'] = df['Ethnic Group'].replace('Black/African/Caribbean/Black British', 'Black/Black British')
df['Ethnic Group'] = df['Ethnic Group'].replace('Mixed/ Multiple Ethnic Group', 'Mixed/Multiple')

df.to_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\attp_data.xlsx", index=False)

print(df)