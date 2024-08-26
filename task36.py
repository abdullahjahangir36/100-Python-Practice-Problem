# Write a program to find the compound interest
def calculate_compound_interest(principal, rate, times_compounded, years):
    # Convert rate from percentage to decimal
    rate_decimal = rate / 100
    # Calculate the amount of money accumulated
    amount = principal * (1 + rate_decimal / times_compounded) ** (times_compounded * years)
    # Calculate compound interest
    compound_interest = amount - principal
    return compound_interest

try:
    # Input from the user
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    times_compounded = int(input("Enter the number of times interest is compounded per year: "))
    years = float(input("Enter the number of years the money is invested for: "))

    # Calculate compound interest
    interest = calculate_compound_interest(principal, rate, times_compounded, years)
    print(f"The compound interest is: {interest:.2f}")

except ValueError:
    print("Please enter valid numbers.")