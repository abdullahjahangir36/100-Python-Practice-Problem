# Write a program to print all the unique combinations of 1,2,3 and 4
from itertools import combinations

def print_combinations(numbers):
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            print(combo)

# List of numbers
numbers = [1, 2, 3, 4]

# Print all unique combinations
print_combinations(numbers)
