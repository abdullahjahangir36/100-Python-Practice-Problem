# Take a number from the user and find the number of digits in it.
def count_digits(number):
    # Convert the number to a string and strip any negative sign
    number_str = str(abs(number))
    # Count the number of characters in the string representation
    return len(number_str)

try:
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Find and print the number of digits
    num_digits = count_digits(num)
    print(f"The number of digits in {num} is: {num_digits}")

except ValueError:
    print("Please enter a valid integer.")