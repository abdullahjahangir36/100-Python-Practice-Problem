# Print all the armstrong numbers in the range of 100 to 1000
def is_armstrong(number):
    # Extract digits
    digits = [int(d) for d in str(number)]
    # Calculate the sum of cubes of its digits
    sum_of_cubes = sum(d ** 3 for d in digits)
    # Check if the sum of cubes equals the original number
    return sum_of_cubes == number

# Print all Armstrong numbers in the range 100 to 1000
print("Armstrong numbers in the range 100 to 1000 are:")
for num in range(100, 1000):
    if is_armstrong(num):
        print(num)
