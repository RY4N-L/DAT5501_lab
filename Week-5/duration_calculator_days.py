import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date

def calculate_duration():
    start_date = np.datetime64(start_calendar.get_date(), 'D')
    use_today = use_today_var.get()

    if use_today:
        end_date = np.datetime64('today', 'D')
    else:
        end_date = np.datetime64(end_calendar.get_date(), 'D')

    duration = (end_date - start_date).astype(int)
    result_label.config(text=f"Duration: {duration} days")

def toggle_end_date():
    if use_today_var.get():
        # Set end date to today and disable calendar
        end_calendar.set_date(date.today())
        end_calendar.config(state='disabled')
    else:
        # Enable calendar for manual selection
        end_calendar.config(state='normal')

# GUI setup
root = tk.Tk()
root.title("Date Duration Calculator")

tk.Label(root, text="Start Date:").grid(row=0, column=0, padx=10, pady=5)
start_calendar = DateEntry(root, date_pattern='yyyy-mm-dd')
start_calendar.grid(row=0, column=1, padx=10, pady=5)

use_today_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Use today's date as end date", variable=use_today_var, command=toggle_end_date).grid(row=1, columnspan=2, padx=10, pady=5)

tk.Label(root, text="End Date:").grid(row=2, column=0, padx=10, pady=5)
end_calendar = DateEntry(root, date_pattern='yyyy-mm-dd')
end_calendar.grid(row=2, column=1, padx=10, pady=5)

# Initially set to today and disabled
end_calendar.set_date(date.today())
end_calendar.config(state='disabled')

tk.Button(root, text="Calculate Duration", command=calculate_duration).grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="Duration: ")
result_label.grid(row=4, columnspan=2, pady=5)

root.mainloop()
