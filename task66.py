# Write a program to check if a list is in ascending order or not.
def is_ascending(input_list):
    # Check if the list is empty or has one item (trivially sorted)
    if len(input_list) < 2:
        return True
    
    # Iterate through the list and check if each element is less than or equal to the next element
    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i + 1]:
            return False  # Return False if any element is greater than the next one
    
    return True  # Return True if all elements are in ascending order

def main():
    # Input list from the user
    input_string = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string to a list of integers
    input_list = list(map(int, input_string.split()))
    
    # Check if the list is in ascending order
    if is_ascending(input_list):
        print("The list is in ascending order.")
    else:
        print("The list is not in ascending order.")

if __name__ == "__main__":
    main()
