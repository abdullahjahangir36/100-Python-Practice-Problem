# Write a program that can perform union and intersection on 2 given list.
def union_lists(list1, list2):
    # Convert lists to sets and perform union operation
    return list(set(list1).union(set(list2)))

def intersection_lists(list1, list2):
    # Convert lists to sets and perform intersection operation
    return list(set(list1).intersection(set(list2)))

def main():
    # Input two lists from the user
    input_string1 = input("Enter the first list of items separated by spaces: ")
    input_string2 = input("Enter the second list of items separated by spaces: ")
    
    # Convert input strings to lists of integers
    list1 = list(map(int, input_string1.split()))
    list2 = list(map(int, input_string2.split()))
    
    # Compute union and intersection
    union_result = union_lists(list1, list2)
    intersection_result = intersection_lists(list1, list2)
    
    # Print the results
    print(f"Union of the lists: {union_result}")
    print(f"Intersection of the lists: {intersection_result}")

if __name__ == "__main__":
    main()
