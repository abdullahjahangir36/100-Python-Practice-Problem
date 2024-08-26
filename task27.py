# Write a program to print the first 25 odd numbers
def print_first_n_odd_numbers(n):
    count = 0
    num = 1
    while count < n:
        print(num, end=' ')
        num += 2
        count += 1
    print()  # for newline

# Print the first 25 odd numbers
print_first_n_odd_numbers(25)
