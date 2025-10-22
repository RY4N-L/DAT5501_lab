import numpy as np

def calculate_duration(start_date_str, end_date_str):
    """
    Calculate the duration in days between two dates.

    Parameters:
    start_date_str (str): The start date in 'YYYY-MM-DD' format.
    end_date_str (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    int: The duration in days between the two dates.
    """
    start_date = np.datetime64(start_date_str, 'D')
    end_date = np.datetime64(end_date_str, 'D')
    duration = (end_date - start_date).astype(int)
    return duration

# Example usage
print(calculate_duration('2023-01-01', '2023-01-31'))  # Returns 30
