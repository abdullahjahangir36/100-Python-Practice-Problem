# Write a python program to search a given number from a list.
def search_number(input_list, number_to_search):
    # Iterate through the list to find the number
    for index, item in enumerate(input_list):
        if item == number_to_search:
            return index  # Return the index if the number is found
    return -1  # Return -1 if the number is not found

def main():
    # Input list from the user
    input_string = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string to a list of integers
    input_list = list(map(int, input_string.split()))
    
    # Input number to search for
    number_to_search = int(input("Enter the number to search for: "))
    
    # Search for the number in the list
    index = search_number(input_list, number_to_search)
    
    if index != -1:
        print(f"The number {number_to_search} is found at index {index}.")
    else:
        print(f"The number {number_to_search} is not found in the list.")

if __name__ == "__main__":
    main()
