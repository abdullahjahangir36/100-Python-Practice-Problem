# Write a program that can sort a given unsorted list. Dont use any built in function for sorting.
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Track if any swap was made in this pass
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, then break
        if not swapped:
            break

def main():
    # Input list from the user
    input_string = input("Enter a list of numbers separated by spaces: ")
    arr = list(map(int, input_string.split()))
    
    # Sort the list
    bubble_sort(arr)
    
    # Print the sorted list
    print("Sorted list:", arr)

if __name__ == "__main__":
    main()
