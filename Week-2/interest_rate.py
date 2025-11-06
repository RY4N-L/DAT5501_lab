# Create a function that calculates the compound interest on a savings account.
def CompoundInterestCalculator(savings, annualInterestRate, years):
    """
    Calculate the compound interest on a savings account.

    Returns:
    string: A summary of the savings after the specified number of years and the time to double the savings.
    """

    multiply = annualInterestRate/100
    for i in range (years):
        savings *= 1 + multiply
        #text1 = "Your savings after " + str(i+1) + " years is " + str(savings)
        #print(text1)
    number_of_years_to_double = 72/annualInterestRate

    text = f"Your savings after {years} years is {savings} Your savings will double in {number_of_years_to_double} years"
    return text

print(CompoundInterestCalculator(10000, 3.5, 10))