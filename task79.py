# Assume a list with numbers from 1 to 10 and then convert it 
# into a dictionary where the key would be the numbers of the list
# and the values would be the square of those numbers.
def list_to_dict(lst):
    # Create a dictionary with keys as numbers and values as their squares
    return {num: num**2 for num in lst}

def main():
    # Define the list of numbers from 1 to 10
    numbers = list(range(1, 11))
    
    # Convert the list to a dictionary
    number_dict = list_to_dict(numbers)
    
    # Print the resulting dictionary
    print("Dictionary with numbers and their squares:")
    print(number_dict)

if __name__ == "__main__":
    main()
