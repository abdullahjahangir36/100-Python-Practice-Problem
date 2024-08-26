# User will provide 2 numbers you have to find the by LCM of those 2 numbers
def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_hcf(a, b)

try:
    # Input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculate LCM
    lcm = find_lcm(num1, num2)
    print(f"The LCM of {num1} and {num2} is: {lcm}")

except ValueError:
    print("Please enter valid integers.")
