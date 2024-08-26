# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
def compute_value(n):
    # Convert the integer to a string
    str_n = str(n)
    
    # Form nn and nnn
    nn = int(str_n + str_n)
    nnn = int(str_n + str_n + str_n)
    
    # Calculate the result
    result = n + nn + nnn
    return result

try:
    # Input from the user
    n = int(input("Enter an integer: "))
    
    # Compute and print the result
    value = compute_value(n)
    print(f"The value of {n} (n) + {n}{n} (nn) + {n}{n}{n} (nnn) is: {value}")

except ValueError:
    print("Please enter a valid integer.")