# Find the length of a given string without using the len() function.
def find_string_length(s):
    # Initialize a counter to zero
    count = 0
    
    # Iterate through each character in the string
    for char in s:
        count += 1
    
    return count

def main():
    # Input a string from the user
    string = input("Enter a string: ")
    
    # Find and print the length of the string
    length = find_string_length(string)
    print(f"The length of the string is: {length}")

if __name__ == "__main__":
    main()