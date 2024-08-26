# Write a program that will take three digits from the user and add the square of each digit.
def sum_of_squares(digit1, digit2, digit3):
    return digit1**2 + digit2**2 + digit3**2

try:
    # Input from the user
    digit1 = int(input("Enter the first digit: "))
    digit2 = int(input("Enter the second digit: "))
    digit3 = int(input("Enter the third digit: "))

    # Check if the inputs are single digits
    if 0 <= digit1 <= 9 and 0 <= digit2 <= 9 and 0 <= digit3 <= 9:
        # Calculate the sum of squares
        result = sum_of_squares(digit1, digit2, digit3)
        print(f"The sum of the squares of the digits is: {result}")
    else:
        print("Please enter valid single digits (0-9).")

except ValueError:
    print("Please enter valid integer digits.")
