import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('Group-Presentation/meat_co2_data.csv')

# Clean column names (remove extra spaces)
df.columns = [col.strip() for col in df.columns]

# Prepare data
years = df['Year']
meat = df['Total meat per year']
co2 = df['Annual CO2 emissions (tonnes)']

# Plotting
fig, ax1 = plt.subplots(figsize=(10,6))
color1 = 'tab:blue'
ax1.set_xlabel('Year', fontsize=15)
ax1.set_ylabel('CO₂ Emissions (tonnes)', color=color1, fontsize=15)

line1, = ax1.plot(years, co2, color=color1, label='Global CO₂ Emissions')
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
color2 = 'tab:red'
line2, = ax2.plot(years, meat, color=color2, label='Global Meat Consumption', linestyle=':')
ax2.set_ylabel('Meat Consumption (kg/person)', color=color2, fontsize=15)
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('Global Annual CO₂ Emissions and Meat Consumption (1990-2022)', fontsize=20)
# Combine both lines in one legend
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper left')
fig.tight_layout()
plt.show()

# Calculate percentage change per year
co2_pct = df['Annual CO2 emissions (tonnes)'].pct_change() * 100
meat_pct = df['Total meat per year'].pct_change() * 100

# Bar chart for percentage change
x = np.arange(len(years))
bar_width = 0.4

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(x - bar_width/2, co2_pct, width=bar_width, label='CO₂ % Change', color='tab:blue')
ax.bar(x + bar_width/2, meat_pct, width=bar_width, label='Meat % Change', color='tab:red')
ax.set_xticks(x)
ax.set_xticklabels(years, rotation=45)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage Change (%)')
ax.set_title('Year-on-Year Percentage Change: CO₂ Emissions vs Meat Consumption (1990-2022)')
ax.legend()
fig.tight_layout()
plt.show()
