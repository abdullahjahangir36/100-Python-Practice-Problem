# Write a program that can convert a 2D list to 1D list, Write a program that can print.
def flatten_2d_list(two_d_list):
    # Flatten the 2D list using a list comprehension
    one_d_list = [item for sublist in two_d_list for item in sublist]
    return one_d_list

def main():
    # Input 2D list from the user
    input_string = input("Enter a 2D list (rows separated by semicolons, items separated by spaces): ")
    
    # Convert the input string to a 2D list
    two_d_list = [list(map(int, row.split())) for row in input_string.split(';')]
    
    # Flatten the 2D list to a 1D list
    one_d_list = flatten_2d_list(two_d_list)
    
    # Print the flattened 1D list
    print(f"Flattened 1D list: {one_d_list}")

if __name__ == "__main__":
    main()
