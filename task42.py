# Write a program to print the following pattern
# *
# **
# ***
# **
# *
def print_pattern():
    # Number of lines for the increasing part
    max_stars = 3
    
    # Print the increasing part
    for i in range(1, max_stars + 1):
        print('*' * i)
    
    # Print the decreasing part
    for i in range(max_stars - 1, 0, -1):
        print('*' * i)

# Print the pattern
print_pattern()
