import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Load the shapefile
england_map = gpd.read_file(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\gb_shapefile.shp")

# Load your Excel data into a DataFrame
appt_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\attp_data.xlsx")

plt.figure(figsize=(15, 8))

# Select three industries of interest
selected_industries = ['Agriculture, Horticulture and Animal Care', 'Arts, Media and Publishing', 'Business, Administration and Law']

# Filter the data for the selected industries
filtered_data = appt_data[appt_data['Industry'].isin(selected_industries)]

# Group by Industry and Geographical Location and count the occurrences
industry_geo_counts = filtered_data.groupby(['Industry', 'Geographical Location of Applicant']).size().unstack().reset_index()

# Merge with the England map data
merged_data = england_map.merge(industry_geo_counts, left_on='Area_Name', right_on='Geographical Location of Applicant', how='left')

# Plotting the heatmap on the map
fig, ax = plt.subplots(1, 1, figsize=(15, 8))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

merged_data.plot(column='Agriculture, Horticulture and Animal Care', cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, cax=cax)
ax.set_title('Number of Applicants - Agriculture, Horticulture and Animal Care')
plt.show()
