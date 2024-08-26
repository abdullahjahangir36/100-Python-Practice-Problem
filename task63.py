# Write a program that can create a new list from a given list where
# each item in the new list is square of the item of the old list
def square_list(input_list):
    # Create a new list with squares of each item in the original list
    squared_list = [item ** 2 for item in input_list]
    return squared_list

def main():
    # Input list from the user
    input_string = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string to a list of integers
    input_list = list(map(int, input_string.split()))
    
    # Create a new list with the squares of the items
    squared_list = square_list(input_list)
    
    # Print the original and the new list
    print(f"Original list: {input_list}")
    print(f"Squared list: {squared_list}")

if __name__ == "__main__":
    main()
