import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np

# Load the CSV 
asset_price_data_df = pd.read_csv('DAT5501_lab/Week-8/asset_price_data.csv')

# Sort the dates in ascending order
asset_price_data_df['Date'] = pd.to_datetime(asset_price_data_df['Date'], format='%m/%d/%Y')
asset_price_data_df = asset_price_data_df.sort_values(by='Date', ascending=True)

# Setting to show all rows when printing the dataframe
pd.set_option('display.max_rows', None)
#print (asset_price_data_df)

# Calculate daily price change and add it as a new column in the dataframe
asset_price_data_df['Close/Last'] = asset_price_data_df['Close/Last'].replace('[\$,]', '', regex=True).astype(float) # Remove dollar signs and convert to float
asset_price_data_df['Daily Price Change'] = asset_price_data_df['Close/Last'].diff()
#print (asset_price_data_df)

# Move the price changes column to an array for plotting and remove NaN values
price_changes = asset_price_data_df['Daily Price Change'].dropna().to_numpy()
times = []

# Measure sorting time for increasing sizes of the array from 7 to the full length of array
for i in range(7, len(price_changes)):
    
    array_to_sort = price_changes[:i] # Get the sub-array to sort (increases by 1 each iteration)
    

    # Sort the array and measure the time taken
    start_time = time.perf_counter()
    sorted_array = sorted(array_to_sort)
    end_time = time.perf_counter()
    
    time_taken = end_time - start_time
    times.append(time_taken) # Store the time taken

# Create x-axis values
x_values = np.arange(7, len(times)+7)

# Calculate n log n values for comparison
n_log_n = x_values * np.log(x_values) 

# Plot figure
plt.figure(figsize=(8, 4))


plt.plot(x_values, times, linestyle='-', color='blue') # Plot line graph
#plt.scatter(x_values, times, marker='o', linestyle='-', color='blue') # Plot scatter  
#plt.plot(x_values, n_log_n, label='n log n', color='red') # Plot n log n for comparison
#plt.legend()

plt.title('Daily Price Changes to Sort vs Sorting Time')
plt.xlabel('Number of Price Changes Sorted')
plt.ylabel('Time')
plt.grid(True)
plt.tight_layout()
plt.show()