# Write a function that accepts a string and 
# returns the number of upper case chars and lower case chars as a dictionary
def count_case_chars(s):
    # Initialize counters for uppercase and lowercase characters
    upper_count = 0
    lower_count = 0
    
    # Iterate through each character in the string
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    # Create a dictionary with counts
    result = {
        'uppercase': upper_count,
        'lowercase': lower_count
    }
    
    return result

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    counts = count_case_chars(input_string)
    print("Character counts:", counts)
