import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
ucas_data = pd.read_excel(r"C:\Users\krina\OneDrive - Queen Mary, University of London\Desktop\Year2\DAT5902\final_project\visualisations\ucas_data.xlsx")

# Filter data for June deadline applications and offers
deadline_data = ucas_data[ucas_data['Entry of Application'] == 'June deadline applications']
offers_data = ucas_data[ucas_data['Entry of Application'] == 'Offers']

# Calculate the total number of applications and offers
total_applications = deadline_data['Number of Applications'].sum()
total_offers = offers_data['Number of Applications'].sum()

# Create a pie chart
labels = ['Deadline Applications', 'Offers']
sizes = [total_applications, total_offers]
colors = ['pink', 'orange']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of UCAS Deadline Applications and Offers')

plt.show()
