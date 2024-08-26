# Write a program that can convert an integer to string.
def integer_to_string(number):
    # Convert integer to string
    return str(number)

def main():
    # Input integer from the user
    number = int(input("Enter an integer: "))
    
    # Convert the integer to string
    result = integer_to_string(number)
    
    # Print the result
    print(f"The integer as a string is: {result}")

if __name__ == "__main__":
    main()
