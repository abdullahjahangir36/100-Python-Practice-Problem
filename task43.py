# Write  a program to print the following pattern
#         *
#       * * *
#     * * * * *
#    * * * * * * *
# * * * * * * * * *
def print_pattern(n):
    for i in range(1, n + 1):
        # Calculate number of spaces before the asterisks
        spaces = ' ' * (2 * (n - i))
        # Create a string with `i` asterisks separated by spaces
        stars = ' '.join(['*'] * (2 * i - 1))
        # Print the row with leading spaces and asterisks
        print(spaces + stars)

# Number of rows for the pattern
rows = 5
# Print the pattern
print_pattern(rows)
