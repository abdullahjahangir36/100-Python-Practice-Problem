# Count the number of vowels in a string provided by the user.
def count_vowels(string):
    # Define a set of vowel characters
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # Initialize vowel count
    count = 0
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
    
    return count

def main():
    # Input string from the user
    string = input("Enter a string: ")
    
    # Count the number of vowels
    num_vowels = count_vowels(string)
    
    # Print the result
    print(f"The number of vowels in the string is: {num_vowels}")

if __name__ == "__main__":
    main()
