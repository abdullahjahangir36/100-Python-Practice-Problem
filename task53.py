# Count the frequency of a particular character in a provided string.
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.
def count_character_frequency(string, char):
    # Initialize frequency count
    count = 0
    
    # Iterate through each character in the string
    for c in string:
        # Increment count if character matches
        if c == char:
            count += 1
    
    return count

def main():
    # Input string and character from the user
    string = input("Enter the string: ")
    char = input("Enter the character to count: ")
    
    # Check if the user entered exactly one character
    if len(char) != 1:
        print("Please enter exactly one character.")
        return
    
    # Count the frequency of the character
    frequency = count_character_frequency(string, char)
    print(f"The frequency of '{char}' in the string is: {frequency}")

if __name__ == "__main__":
    main()
