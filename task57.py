# Write a program that can check whether a given string is palindrome or not.
def is_palindrome(string):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    cleaned_string = string.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

def main():
    # Input string from the user
    string = input("Enter a string: ")
    
    # Check if the string is a palindrome
    if is_palindrome(string):
        print(f"The string '{string}' is a palindrome.")
    else:
        print(f"The string '{string}' is not a palindrome.")

if __name__ == "__main__":
    main()
