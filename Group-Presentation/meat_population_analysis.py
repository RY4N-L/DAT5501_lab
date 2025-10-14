import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- CONFIGURABLE TIME INTERVAL ---
START_YEAR = 1990
END_YEAR = 2013

# --- READ DATA ---
# Update the filename and column names as needed
df = pd.read_csv('Group-Presentation/meat_population_data.csv')
df.columns = [col.strip() for col in df.columns]

# --- FILTER DATA BY YEAR ---
filtered = df[(df['Year'] >= START_YEAR) & (df['Year'] <= END_YEAR)]
years = filtered['Year']
population = filtered['World population'] / 1e9  # Convert to billions
meat = filtered['Total Meat Consumption Per Year (tonnes)'] / 1e6

# --- PLOT ---

fig, ax1 = plt.subplots(figsize=(10,6))
color1 = 'tab:blue'
ax1.set_xlabel('Year', fontsize=15)
ax1.set_ylabel('Population (billions)', color=color1, fontsize=15)

line1, = ax1.plot(years, population, color=color1, label='Population Growth', linestyle=':')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

ax2 = ax1.twinx()
color2 = 'tab:red'
line2, = ax2.plot(years, meat, color=color2, label='Meat Consumption Growth')
ax2.set_ylabel('Meat Consumption (million tonnes)', color=color2, fontsize=15)
ax2.tick_params(axis='y', labelcolor=color2)

plt.title(f'Population and Global Meat Consumption Growth ({START_YEAR}-{END_YEAR})', fontsize=20)
# Combine both lines in one legend
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper left')
fig.tight_layout()
plt.show()


# Calculate percentage change per year (filtered)
population_pct = filtered['World population'].pct_change() * 100
meat_pct = filtered['Total Meat Consumption Per Year (tonnes)'].pct_change() * 100

# Bar chart for percentage change
x = np.arange(len(years)-1)
bar_width = 0.4

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(x - bar_width/2, population_pct[1:], width=bar_width, label='Population % Change', color='tab:blue', hatch = '//')
ax.bar(x + bar_width/2, meat_pct[1:], width=bar_width, label='Meat Consumption % Change', color='tab:red')
ax.set_xticks(x)
ax.set_xticklabels(years[1:], rotation=45)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Percentage Change (%)', fontsize=15)
ax.set_title('Year-on-Year Percentage Change: World Population vs Global Meat Consumption', fontsize=20)
ax.legend()
fig.tight_layout()
#plt.show()

pop_2000 = df[df['Year'] == 2000]['World population'].values[0]
pop_2050 = df[df['Year'] == 2050]['World population'].values[0]
pct_change_pop = ((pop_2050 - pop_2000) / pop_2000) * 100
print(f"Projected growth in World Population from 2000 to 2050: {pct_change_pop:.1f}%")

meat_2000 = df[df['Year'] == 2000]['Total Meat Consumption Per Year (tonnes)'].values[0]
meat_2050 = df[df['Year'] == 2050]['Total Meat Consumption Per Year (tonnes)'].values[0]
pct_change_meat = ((meat_2050 - meat_2000) / meat_2000) * 100
print(f"Projected growth in Global Meat Consumption from 2000 to 2050: {pct_change_meat:.1f}%")