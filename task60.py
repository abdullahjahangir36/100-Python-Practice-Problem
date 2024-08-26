# Write a python program to find the max item from a list without using the max function
def find_maximum(input_list):
    # Check if the list is empty
    if not input_list:
        raise ValueError("The list is empty")
    
    # Initialize the maximum with the first element of the list
    max_item = input_list[0]
    
    # Iterate through the list to find the maximum item
    for item in input_list:
        if item > max_item:
            max_item = item
    
    return max_item

def main():
    # Input list from the user
    input_string = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string to a list of integers
    input_list = list(map(int, input_string.split()))
    
    try:
        # Find the maximum item in the list
        max_item = find_maximum(input_list)
        print(f"The maximum item in the list is: {max_item}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
