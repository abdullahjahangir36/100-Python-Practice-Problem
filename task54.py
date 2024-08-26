# Find the index position of a particular character in another string.
def find_character_index(string, char):
    # Find the index of the character
    index = string.find(char)
    
    # Return index if found, otherwise indicate that the character is not in the string
    if index != -1:
        return index
    else:
        return "Character not found in the string"

def main():
    # Input string and character from the user
    string = input("Enter the string: ")
    char = input("Enter the character to find: ")
    
    # Check if the user entered exactly one character
    if len(char) != 1:
        print("Please enter exactly one character.")
        return
    
    # Find the index of the character
    index = find_character_index(string, char)
    
    # Print the index position
    if isinstance(index, int):
        print(f"The index of '{char}' in the string is: {index}")
    else:
        print(index)

if __name__ == "__main__":
    main()
