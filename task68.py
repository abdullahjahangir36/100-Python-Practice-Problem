# Write a program to merge 2 list without using the + operator.
def merge_lists(list1, list2):
    # Create a copy of list1 to avoid modifying the original list
    merged_list = list1.copy()
    
    # Extend the copied list with elements from list2
    merged_list.extend(list2)
    
    return merged_list

def main():
    # Input two lists from the user
    input_string1 = input("Enter the first list of numbers separated by spaces: ")
    input_string2 = input("Enter the second list of numbers separated by spaces: ")
    
    # Convert input strings to lists of integers
    list1 = list(map(int, input_string1.split()))
    list2 = list(map(int, input_string2.split()))
    
    # Merge the two lists
    merged_list = merge_lists(list1, list2)
    
    # Print the merged list
    print(f"Merged list: {merged_list}")

if __name__ == "__main__":
    main()
