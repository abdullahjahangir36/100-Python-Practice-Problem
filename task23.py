# Write a program that will swap numbers
# Using a temporary variable
def swap_using_temp(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swapping: a = {a}, b = {b}")
    return a, b

# Input from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Swap the numbers
swap_using_temp(a, b)