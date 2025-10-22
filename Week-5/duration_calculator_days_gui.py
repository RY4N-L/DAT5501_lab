import numpy as np
import tkinter as tk
from tkcalendar import DateEntry

today = np.datetime64('today', 'D').astype(str)  # Get today's date as a string in 'YYYY-MM-DD' format

def calculate_duration():
    # Calculate the duration in days between start and end dates
    start_date = np.datetime64(start_calendar.get_date(), 'D')
    use_today = use_today_var.get()

    if use_today: # If checkbox is selected, use today's date
        end_date = np.datetime64(today, 'D')
    else: # Otherwise, get the date from the end date calendar
        end_date = np.datetime64(end_calendar.get_date(), 'D')

    duration = (end_date - start_date).astype(int)
    result_label.config(text=f"Duration: {duration} days")

def toggle_end_date():
    # Enable or disable end date selection based on checkbox
    if use_today_var.get():
        # Set end date to today and disable calendar if checkbox is selected
        end_calendar.set_date(today)
        end_calendar.config(state='disabled')
    else:
        # Enable calendar for manual selection if checkbox is not selected
        end_calendar.config(state='normal')

# GUI setup
root = tk.Tk() # Create the main window
root.title("Date Duration Calculator")

# Start Date
tk.Label(root, text="Start Date:").grid(row=0, column=0, padx=10, pady=5)
start_calendar = DateEntry(root, date_pattern='yyyy-mm-dd', width=50)
start_calendar.grid(row=0, column=1, padx=10, pady=5)

# End Date (Checkbox)
use_today_var = tk.BooleanVar(value=True)
check_box = tk.Checkbutton(root, text="Use today's date as end date", variable=use_today_var, command=toggle_end_date) # Checkbox to use today's date, runs toggle_end_date on change
check_box.grid(row=1, columnspan=2, padx=10, pady=5) 

# End Date
tk.Label(root, text="End Date:").grid(row=2, column=0, padx=10, pady=5)
end_calendar = DateEntry(root, date_pattern='yyyy-mm-dd', width=50)
end_calendar.grid(row=2, column=1, padx=10, pady=5)

# Calculate Button
tk.Button(root, text="Calculate Duration", command=calculate_duration, width=50).grid(row=3, columnspan=2, pady=10) # runs calculate_duration on click

# Result Label
result_label = tk.Label(root, text="Duration: ")
result_label.grid(row=4, columnspan=2, pady=5)

# Initially set to today and disabled
end_calendar.set_date(today)
end_calendar.config(state='disabled')

root.mainloop() # Start the GUI event loop
