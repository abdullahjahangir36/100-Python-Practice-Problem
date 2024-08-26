# Write a program to merge two given dictionary.
def merge_dicts(dict1, dict2):
    # Merge two dictionaries using the merge operator
    merged_dict = dict1 | dict2
    return merged_dict

def main():
    # Define two dictionaries
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'d': 4, 'e': 5, 'f': 6}
    
    # Merge the dictionaries
    result = merge_dicts(dict1, dict2)
    
    # Print the merged dictionary
    print("Merged dictionary:", result)

if __name__ == "__main__":
    main()
