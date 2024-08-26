# Write a python program to convert a string to title case without using the title()
def to_title_case(string):
    # Split the string into words
    words = string.split()
    
    # Capitalize the first letter of each word and lowercase the rest
    title_case_words = [word[0].upper() + word[1:].lower() for word in words]
    
    # Join the words back into a single string with spaces in between
    title_case_string = ' '.join(title_case_words)
    
    return title_case_string

def main():
    # Input string from the user
    string = input("Enter a string: ")
    
    # Convert the string to title case
    title_case_string = to_title_case(string)
    
    # Print the result
    print(f"The string in title case is: {title_case_string}")

if __name__ == "__main__":
    main()
