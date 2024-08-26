# Write a program to find histogram of a given set of numbers. 
# Take bin size from user. Print the result in the form of a dictionary.
def calculate_histogram(numbers, bin_size):
    # Find the minimum and maximum values
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Initialize the dictionary to store histogram data
    histogram = {}
    
    # Iterate over the range of bins
    for start in range(min_value, max_value + bin_size, bin_size):
        end = start + bin_size
        # Count the numbers that fall into the current bin
        count = sum(1 for number in numbers if start <= number < end)
        # Store the count in the histogram dictionary
        histogram[f"{start}-{end - 1}"] = count
    
    return histogram

def main():
    try:
        # Input numbers from the user
        numbers_str = input("Enter a list of numbers separated by commas (e.g., 1,2,3,4,5): ")
        numbers = [int(num.strip()) for num in numbers_str.split(',')]
        
        # Input bin size from the user
        bin_size = int(input("Enter the bin size: "))
        
        # Validate bin size
        if bin_size <= 0:
            raise ValueError("Bin size must be a positive integer.")
        
        # Calculate the histogram
        histogram = calculate_histogram(numbers, bin_size)
        
        # Print the histogram
        print("Histogram:", histogram)
    
    except ValueError as e:
        print(f"Error: {e}. Please ensure your inputs are valid.")

if __name__ == "__main__":
    main()
