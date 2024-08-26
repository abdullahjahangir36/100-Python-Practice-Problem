# Write a program to swap the key value pair for max and min values
# Eg if the dict is like this {‘a’:1,’b’:2,’c’:3}
# Output should be {a:3,b:2,c:1}
def swap_max_min(dict):
    # Check if the dictionary is empty
    if not dict:
        return dict
    
    # Find the maximum and minimum values
    max_value = max(dict.values())
    min_value = min(dict.values())
    
    # Find the corresponding keys for these values
    max_key = [key for key, value in dict.items() if value == max_value][0]
    min_key = [key for key, value in dict.items() if value == min_value][0]
    
    # Swap the key-value pairs for the maximum and minimum values
    dict[max_key], dict[min_key] = min_value, max_value
    
    return dict

def main():
    # Input from the user
    input_str = input("Enter a dictionary (e.g., {'a':1,'b':2,'c':3}): ")
    
    try:
        # Convert the input string to a dictionary
        user_dict = eval(input_str)
        
        # Check if the input is a valid dictionary
        if not isinstance(user_dict, dict):
            raise ValueError("Input is not a valid dictionary.")
        
        # Swap the maximum and minimum values
        updated_dict = swap_max_min(user_dict)
        
        # Print the updated dictionary
        print("Updated dictionary:", updated_dict)
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
