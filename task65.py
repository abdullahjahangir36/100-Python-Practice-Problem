# Write a program that can count the number of words in a given string.
def count_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Count the number of words
    word_count = len(words)
    
    return word_count

def main():
    # Input string from the user
    input_string = input("Enter a string: ")
    
    # Count the number of words in the string
    word_count = count_words(input_string)
    
    # Print the word count
    print(f"The number of words in the string is: {word_count}")

if __name__ == "__main__":
    main()
