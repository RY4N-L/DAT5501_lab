import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV 
population_data_df = pd.read_csv('DAT5501_lab/Week-8/population_data_owid.csv')

# Setting to show all rows when printing the dataframe
pd.set_option('display.max_rows', None)

# Create a sub sample without the last 10 years for fitting
sample_population_data_df = population_data_df[(population_data_df['Year'] > 1900) & (population_data_df['Year'] <= population_data_df['Year'].max() - 10)]

def n_polynomial_fit(order):
    # Fit a polynomial of given order to the sample data
    coefficients = np.polyfit(sample_population_data_df['Year'], sample_population_data_df['Population'], order)
    polynomial = np.poly1d(coefficients)
    
    # Generate x values for plotting the fitted curve
    x_values = np.linspace(sample_population_data_df['Year'].min(), population_data_df['Year'].max(), 100)
    y_values = polynomial(x_values)
    
    # Plot the original data and the fitted curve
    plt.scatter(sample_population_data_df['Year'], sample_population_data_df['Population'], color='blue', label='Sample Data')
    plt.plot(x_values, y_values, color='red', label=f'Polynomial Fit (Order {order})')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(f'Polynomial Fit of Order {order}')
    plt.legend()
    plt.show()
    
    return polynomial


# Example usage: Fit a polynomial of order 3
polynomial_model = n_polynomial_fit(1)

print (sample_population_data_df)