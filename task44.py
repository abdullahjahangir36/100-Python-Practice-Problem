# Write a program to print the following pattern
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
def print_pattern(n):
    for i in range(1, n + 1):
        # Create the increasing part of the row
        increasing_part = list(range(1, i + 1))
        # Create the decreasing part of the row
        decreasing_part = list(range(i - 1, 0, -1))
        # Combine both parts
        row = increasing_part + decreasing_part
        # Print the row with spaces between numbers
        print(' '.join(map(str, row)))

# Number of rows for the pattern
rows = 5
# Print the pattern
print_pattern(rows)
