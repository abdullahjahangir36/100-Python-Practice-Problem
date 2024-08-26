# Print all factors of a given number provided by the user.
def find_factors(number):
    factors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return sorted(factors)

try:
    # Input from the user
    num = int(input("Enter a number: "))
    
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        # Find and print the factors
        factors = find_factors(num)
        print(f"The factors of {num} are: {factors}")

except ValueError:
    print("Please enter a valid integer.")