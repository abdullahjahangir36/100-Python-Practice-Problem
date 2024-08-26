# Write a program that can multiply 2 numbers provided by the user without using the * operator
def multiply_without_asterisk(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    
    # Adjust the result for negative numbers
    if b < 0:
        result = -result
    
    return result

try:
    # Input from the user
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # Multiply the numbers without using *
    result = multiply_without_asterisk(a, b)
    print(f"The result of {a} multiplied by {b} is: {result}")

except ValueError:
    print("Please enter valid integers.")
