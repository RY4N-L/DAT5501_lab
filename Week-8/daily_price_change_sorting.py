import pandas as pd
import matplotlib.pyplot as plt
import time

# Load the CSV 
asset_price_data_df = pd.read_csv('DAT5501_lab/Week-8/asset_price_data.csv')
# Sort the dates in ascending order
asset_price_data_df['Date'] = pd.to_datetime(asset_price_data_df['Date'], format='%m/%d/%Y')
asset_price_data_df = asset_price_data_df.sort_values(by='Date', ascending=True)

# Setting to show all rows when printing the dataframe
pd.set_option('display.max_rows', None)

print (asset_price_data_df)

# Calculate daily price change
asset_price_data_df['Close/Last'] = asset_price_data_df['Close/Last'].replace('[\$,]', '', regex=True).astype(float) # Remove dollar signs and convert to float

asset_price_data_df['Daily Price Change'] = asset_price_data_df['Close/Last'].diff()
print (asset_price_data_df)