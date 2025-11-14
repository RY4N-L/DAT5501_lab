import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dictionary to store the chi-squared values for different polynomial orders
chi_squared_values = {}

# Load the CSV 
population_data_df = pd.read_csv('DAT5501_lab/Week-8/population_data_owid.csv')

# Setting to show all rows when printing the dataframe
pd.set_option('display.max_rows', None)

# Create a sub sample without the last 10 years for fitting
sample_population_data_df = population_data_df[(population_data_df['Year'] > 1900) & (population_data_df['Year'] <= population_data_df['Year'].max() - 10)]

def n_polynomial_fit(order, colour, linestyle):
    # Fit a polynomial of given order to the sample data
    coefficients = np.polyfit(sample_population_data_df['Year'], sample_population_data_df['Population'], order)
    polynomial = np.poly1d(coefficients)
    
    # Generate x values for plotting the fitted curve
    x_values = np.linspace(sample_population_data_df['Year'].min(), population_data_df['Year'].max(), 100)
    y_values = polynomial(x_values)
    
    # Plot the original data and the fitted curve
    plt.plot(x_values, y_values, color=colour, label=f'Polynomial Fit (Order {order})', linestyle=linestyle)
    
    # Calculate chi-squared value for the fit
    residuals = sample_population_data_df['Population'] - polynomial(sample_population_data_df['Year'])
    chi_squared = np.sum((residuals ** 2) / polynomial(sample_population_data_df['Year']))
    chi_squared_values[order] = chi_squared

    return polynomial


# Example usage: Fit a polynomial of order 3
n_polynomial_fit(1, 'red', 'dashed')
n_polynomial_fit(2, 'green', 'dotted')
n_polynomial_fit(3, 'orange', 'dashdot')
n_polynomial_fit(4, 'purple', 'solid')

n_polynomial_fit(5, 'brown', 'dashed')
n_polynomial_fit(6, 'pink', 'dotted')
n_polynomial_fit(7, 'gray', 'dashdot')
n_polynomial_fit(8, 'cyan', 'solid')
n_polynomial_fit(9, 'magenta', 'dashed')


plt.scatter(sample_population_data_df['Year'], sample_population_data_df['Population'], color='blue', label='Sample Data')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Polynomial Fit of Order')
plt.legend()
plt.show()

# plot a graph of chi-squared values
plt.plot(list(chi_squared_values.keys()), list(chi_squared_values.values()), marker='o')
plt.xlabel('Polynomial Order')
plt.ylabel('Chi-Squared Value')
plt.title('Chi-Squared Values for Different Polynomial Orders')
plt.show()


print (sample_population_data_df)