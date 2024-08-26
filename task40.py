# Find the reverse of a number provided by the user(any number of digit) 
def reverse_number(number):
    # Convert number to string and reverse the string
    reversed_str = str(number)[::-1]
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    return reversed_num

try:
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Find and print the reversed number
    reversed_num = reverse_number(num)
    print(f"The reverse of {num} is: {reversed_num}")

except ValueError:
    print("Please enter a valid integer.")
