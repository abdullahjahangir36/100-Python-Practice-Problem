# Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user
def calculate_series_sum(x, n):
    series_sum = 0
    for i in range(1, n + 1):
        # Calculate x^i / i
        term = (x ** i) / i
        # Add the term to the series sum
        series_sum += term
    return series_sum

try:
    # Input values from the user
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))
    
    if n <= 0:
        print("Please enter a positive integer for n.")
    else:
        # Calculate and print the series sum
        result = calculate_series_sum(x, n)
        print(f"The sum of the series up to the {n}th term is: {result:.5f}")

except ValueError:
    print("Please enter valid numbers for x and n.")
