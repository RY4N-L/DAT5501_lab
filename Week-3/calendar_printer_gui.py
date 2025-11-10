import tkinter as tk
from tkinter import messagebox

# Dictionary to map the day of the week to the number of spaces to leave in the first row of the calendar
days_dict = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 0
}

def generate_calendar(days_entry, day_var, calendar_inner_frame): 
    
    """
    Generate a calendar structure based on user input.

    parameters:
    days_entry (tk.Entry): Entry widget for number of days in the month.
    day_var (tk.StringVar): Variable holding the starting day of the week.
    calendar_inner_frame (tk.Frame): Frame to display the generated calendar.

    Returns:
    None
    """

    # Get user inputs from GUI widgets
    try: 
        days_in_month = int(days_entry.get())
        starting_day = day_var.get()
        gaps_to_leave = days_dict[starting_day]

    # Error handling for invalid input (non-integer or blank days)
    except ValueError:
        messagebox.showerror("Invalid input, please enter a valid number of days.")
        return

    # Clear previous calendar to prevent stacking
    for widget in calendar_inner_frame.winfo_children():
        widget.destroy()

    # Create calendar headers
    headers = ["S", "M", "T", "W", "T", "F", "S"]
    for i, day in enumerate(headers):
        tk.Label(calendar_inner_frame, text=day, width=10, borderwidth=1, relief="solid").grid(row=0, column=i)

    # Fill in the calendar days in grid cells
    row = 1
    col = gaps_to_leave
    for day in range(1, days_in_month + 1):
        colour = "white"
        
        match col:
            case 0: # Sunday
                colour = "lightgrey"
            case 6: # Saturday
                colour = "lightgrey"

        tk.Label(calendar_inner_frame, text=str(day), width=10, borderwidth=1, relief="solid", bg=colour).grid(row=row, column=col)

        col += 1
        if col > 6: # Move to the next row after Saturday
            col = 0
            row += 1

def setup_calendar_gui():

    """
    Set up the main GUI window for the calendar printer and run the event loop.

    Returns:
    None
    """

    root = tk.Tk() # Create main window
    root.title("Calendar Printer")

    # Input for number of days in month
    tk.Label(root, text="Number of days in month:").pack() 
    days_entry = tk.Entry(root)
    days_entry.pack()

    # Dropdown for starting day
    tk.Label(root, text="Starting day of the week:").pack() 
    day_var = tk.StringVar(root)
    day_var.set("Monday")  # Default value to monday
    day_dropdown = tk.OptionMenu(root, day_var, *days_dict.keys())
    day_dropdown.pack()

    # Button that runs function to create calendar
    tk.Button(
        root,
        text="Generate Calendar",
        command=lambda: generate_calendar(days_entry, day_var, calendar_inner_frame)).pack(pady=10)

    # Scrollable calendar frame setup
    canvas = tk.Canvas(root, height=300, width=515)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind("<Configure>",lambda e: canvas.configure( scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


    # Inner frame to hold the calendar
    calendar_inner_frame = tk.Frame(scrollable_frame)
    calendar_inner_frame.pack()

    root.mainloop() # Start the GUI infinite event loop

if __name__ == "__main__":
    setup_calendar_gui()