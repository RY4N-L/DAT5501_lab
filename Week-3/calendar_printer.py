#days_in_month = int(input("Please enter the number of days in the month:"))
#starting_day = str(input("Please enter the day of the week the month starts on:" ))

days_in_month = int(30)
starting_day = str("Sunday")
row_counter = int(0)
first_row = True

days_dict = {
  "Monday": 1,
  "Tuesday": 2,
  "Wednesday": 3,
  "Thursday": 4,
  "Friday": 5,
  "Saturday": 6,
  "Sunday": 0
}

gaps_to_leave = int(days_dict[starting_day])
row_counter += gaps_to_leave


for i in range (days_in_month):
    row_counter += 1
    current_day = str(i+1)

    if first_row == True: # Runs if this is the first row - to print the dashed spaces
        print ("S  M  T  W  T  F  S")
        print ("-- " * gaps_to_leave, end="")
        first_row = False

    if row_counter == 7: # If we are at the end of the week print and create a new line
        row_counter = 0
        print(current_day)

    elif int(current_day) < 10: # If the date is <10th print an extra sace (for better alignment)
        print(current_day + "  ", end="")

    else: print(current_day + " ", end="")