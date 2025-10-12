def CalendarPrinter():
    while True: # Loop until user enters a q after printing calendar
        row_counter = int(0)
        first_row = True
        days_dict = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 0
        }

        while True: # Loop until user enters a valid number of days
            try:
                days_in_month = int(input("\nPlease enter the number of days in the month:"))
                break
            except ValueError as e:
                print("\nInvalid input, please enter an integer e.g. 31 or 100")

        while True: # Loop until user enters a valid day of the week
            try:
                starting_day = str(input("\nPlease enter the day of the week the month starts on:" )).lower()
                gaps_to_leave = int(days_dict[starting_day])
                row_counter += gaps_to_leave
                break
            except KeyError as e:
                print("\nInvalid input, please enter the full name of the day e.g. 'monday' or 'Sunday'")


        for i in range (days_in_month):
            row_counter += 1
            current_day = str(i+1)

            if first_row == True: # Runs if this is the first row - to print the dashed spaces
                print ("\nS  M  T  W  T  F  S")
                print ("-- " * gaps_to_leave, end="")
                first_row = False

            if row_counter == 7 or int(current_day) == days_in_month: # If we are at the end of the week or month print and create a new line
                row_counter = 0
                print(current_day)

            elif int(current_day) < 10: # If the date is <10th print an extra sace (for better alignment)
                print(current_day + "  ", end="")

            else: print(current_day + " ", end="")

        exit = str(input("\nPlease press r to retry or q to quit"))

        if exit == 'q':
            print("CALENDAR PRINTER CLOSED")
            break

CalendarPrinter()