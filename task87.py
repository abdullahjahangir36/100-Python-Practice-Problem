# Write a function that accepts a number and returns it’s factorial. You can not use any loop
def factorial(n):
    """Compute the factorial of a number using recursion."""
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: ").strip())
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is {result}.")
