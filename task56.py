# Write a program which can remove a particular character from a string.
def remove_character(string, char_to_remove):
    # Replace all occurrences of the character with an empty string
    modified_string = string.replace(char_to_remove, "")
    return modified_string

def main():
    # Input string and character from the user
    string = input("Enter the string: ")
    char_to_remove = input("Enter the character to remove: ")
    
    # Check if the user entered exactly one character
    if len(char_to_remove) != 1:
        print("Please enter exactly one character.")
        return
    
    # Remove the character from the string
    result = remove_character(string, char_to_remove)
    
    # Print the result
    print(f"The modified string is: {result}")

if __name__ == "__main__":
    main()
