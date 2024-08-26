# Write a python program to remove all the duplicates from a list
def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates, then back to a list
    unique_list = list(set(input_list))
    return unique_list

def main():
    # Input list from the user
    input_string = input("Enter a list of items separated by spaces: ")
    
    # Convert the input string to a list of items
    input_list = input_string.split()
    
    # Remove duplicates from the list
    unique_list = remove_duplicates(input_list)
    
    # Print the list without duplicates
    print(f"The list without duplicates is: {unique_list}")

if __name__ == "__main__":
    main()