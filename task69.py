# Write a program to replace an item with a different item if found in the list.
def replace_item(input_list, old_item, new_item):
    # Iterate through the list and replace old_item with new_item
    for i in range(len(input_list)):
        if input_list[i] == old_item:
            input_list[i] = new_item
    return input_list

def main():
    # Input list from the user
    input_string = input("Enter a list of items separated by spaces: ")
    # Convert the input string to a list of items
    input_list = input_string.split()
    
    # Input the item to replace and the new item
    old_item = input("Enter the item to replace: ")
    new_item = input("Enter the new item: ")
    
    # Replace the item in the list
    updated_list = replace_item(input_list, old_item, new_item)
    
    # Print the updated list
    print(f"Updated list: {updated_list}")

if __name__ == "__main__":
    main()
