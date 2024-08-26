# Write a program that will check whether the number is armstrong number or not.
# Armstrong number has 3 digits.
def is_armstrong_number(number):
    # Convert the number to a string to iterate over digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

try:
    # Input from the user
    number = int(input("Enter a number: "))

    # Check if the number is an Armstrong number
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

except ValueError:
    print("Please enter a valid integer.")
