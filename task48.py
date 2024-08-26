# The natural logarithm can be approximated by the following series.
# If x is input through the keyboard, 
# write a program to calculate the sum of the first seven terms of this series.
def approximate_ln(x, num_terms=7):
    series_sum = 0
    for n in range(1, num_terms + 1):
        # Calculate the term using the series formula
        term = ((-1) ** (n + 1)) * (x ** n) / n
        # Add the term to the series sum
        series_sum += term
    return series_sum

try:
    # Input value from the user
    x = float(input("Enter the value of x (where -1 < x <= 1): "))
    
    if x <= -1 or x > 1:
        print("The value of x should be in the range -1 < x <= 1.")
    else:
        # Calculate and print the natural logarithm approximation
        result = approximate_ln(x)
        print(f"The approximation of ln(1 + {x}) using the first 7 terms is: {result:.5f}")

except ValueError:
    print("Please enter a valid number for x.")
