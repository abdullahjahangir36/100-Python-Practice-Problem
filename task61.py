# Write a python program to reverse a list
def reverse_list_reverse_method(input_list):
    input_list.reverse()
    return input_list

def main():
    # Input list from the user
    input_string = input("Enter a list of items separated by spaces: ")
    
    # Convert the input string to a list of items
    input_list = input_string.split()
    
    # Reverse the list using the reverse() method
    reversed_list = reverse_list_reverse_method(input_list.copy())  # Using copy() to preserve original list
    
    # Print the reversed list
    print(f"The reversed list is: {reversed_list}")

if __name__ == "__main__":
    main()
