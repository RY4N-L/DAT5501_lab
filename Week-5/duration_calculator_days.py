import numpy as np




def calculate_duration():
    """
    Calculate the duration in days between two dates.

    Returns:
    int: The duration in days between the two dates.
    """
    today = np.datetime64('today', 'D')
    while True:
    # Loop until valid start date is entered
        try:
            start_date_str = input("Please enter the start date (YYYY-MM-DD): ")
            
            # Validate date format (important to note that np.datetime64 will accept invalid dates like 202300230 and convert them to valid dates by reading all digits except for the last 4 as the year e.g. 202300230 -> 20230-02-30)
            start_date = np.datetime64(start_date_str, 'D')
            
            # Exit loop if start date is valid
            break
        
        except ValueError: # Catch invalid date format
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
            
    
    while True:
    # Loop until valid end date is entered
        try:
            end_date_str = input(f"Please enter the end date (YYYY-MM-DD) or press enter to use today's date [{today}]: ") or str(today) # Default to today's date if input is empty/user presses enter
            
            # Validate date format
            end_date = np.datetime64(end_date_str, 'D')
            
            # Exit loop if end date is valid
            break

        except ValueError: # Catch invalid date format
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")

    duration = (end_date - start_date).astype(int) # Calculate duration in days
    return duration

# Example usage
print(calculate_duration())
