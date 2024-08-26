# Write a program that can find the factorial of a given number provided by the user.
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    # Input from the user
    number = int(input("Enter a non-negative integer: "))
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate factorial using the iterative method
        result = factorial_iterative(number)
        print(f"The factorial of {number} is: {result}")

except ValueError:
    print("Please enter a valid integer.")
