# Write a program to print the following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
def print_pattern(rows):
    current_number = 1
    for i in range(1, rows + 1):
        # Create a list of numbers for the current row
        row_numbers = [str(current_number + j) for j in range(i)]
        # Print the row with spaces between numbers
        print(' '.join(row_numbers))
        # Update the current number for the next row
        current_number += i

# Number of rows for the pattern
num_rows = 4
# Print the pattern
print_pattern(num_rows)
