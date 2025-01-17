# Write a program to print whether a given number is prime number or not
def is_prime(number):
    # Check for negative numbers, 0, and 1
    if number <= 1:
        return False
    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    # Input from the user
    num = int(input("Enter a number: "))
    
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

except ValueError:
    print("Please enter a valid integer.")
