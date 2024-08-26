# Write a program that will take user input of (4 digits number) and 
# check whether the number is narcissist number or not.
# Narcissistic number is bascially Armstrong number but has 4 digits.
def is_narcissistic_number(number):
    # Convert the number to a string to iterate over digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

try:
    # Input from the user
    number = int(input("Enter a 4-digit number: "))

    # Check if the number is a 4-digit number
    if 1000 <= number <= 9999:
        # Check if the number is a narcissistic number
        if is_narcissistic_number(number):
            print(f"{number} is a narcissistic number.")
        else:
            print(f"{number} is not a narcissistic number.")
    else:
        print("Please enter a valid 4-digit number.")

except ValueError:
    print("Please enter a valid integer.")
