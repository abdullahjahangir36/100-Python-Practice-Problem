# Write a program to find the sum of first n numbers, 
# where n will be provided by the user. Eg if the user provides n=10 the output should be 55.
def sum_of_first_n_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

# Input from the user
n = int(input("Enter the value of n: "))

# Calculate the sum of the first n numbers
result = sum_of_first_n_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")