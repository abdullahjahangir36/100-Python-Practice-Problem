# User will provide 2 numbers you have to find the HCF of those 2 numbers
def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

try:
    # Input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculate HCF
    hcf = find_hcf(num1, num2)
    print(f"The HCF of {num1} and {num2} is: {hcf}")

except ValueError:
    print("Please enter valid integers.")