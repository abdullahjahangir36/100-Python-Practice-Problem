# Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
# n will be provided by the user
import math

def calculate_series_sum(n):
    series_sum = 0
    for i in range(1, n + 1):
        # Calculate i / i!
        term = i / math.factorial(i)
        # Add the term to the series sum
        series_sum += term
    return series_sum

try:
    # Input from the user
    n = int(input("Enter the value of n: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        # Calculate and print the series sum
        result = calculate_series_sum(n)
        print(f"The sum of the series up to the {n}th term is: {result:.5f}")

except ValueError:
    print("Please enter a valid integer.")
