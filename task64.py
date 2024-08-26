# Write a program that can reverse words of a given string.
# Eg if the input is Hello how are you
# Output should be you are how Hello
def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a single string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

def main():
    # Input string from the user
    input_string = input("Enter a string: ")
    
    # Reverse the words in the string
    reversed_string = reverse_words(input_string)
    
    # Print the reversed string
    print(f"The reversed string is: {reversed_string}")

if __name__ == "__main__":
    main()
