# Create 2 lists from a given list where 1st list 
# will contain all the odd numbers from the original list 
# and the 2nd one will contain all the even numbers.
def split_odd_even(input_list):
    # Create two lists: one for odd numbers and one for even numbers
    odd_numbers = [num for num in input_list if num % 2 != 0]
    even_numbers = [num for num in input_list if num % 2 == 0]
    return odd_numbers, even_numbers

def main():
    # Input list from the user
    input_string = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string to a list of integers
    input_list = list(map(int, input_string.split()))
    
    # Split the list into odd and even numbers
    odd_numbers, even_numbers = split_odd_even(input_list)
    
    # Print the results
    print(f"Odd numbers: {odd_numbers}")
    print(f"Even numbers: {even_numbers}")

if __name__ == "__main__":
    main()
