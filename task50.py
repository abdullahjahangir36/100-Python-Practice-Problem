# Write a program that accepts 2 numbers from the user a numerator 
# and a denominator and then simplifies it
# Eg if the num = 5, den = 15 the answer should be ⅓
# Eg if the num = 6, den = 9 the answer should be ⅔
import math

def simplify_fraction(numerator, denominator):
    # Calculate the greatest common divisor (GCD)
    gcd = math.gcd(numerator, denominator)
    
    # Simplify the fraction
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    
    return simplified_numerator, simplified_denominator

def main():
    try:
        # Input numerator and denominator from the user
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        # Check if the denominator is zero
        if denominator == 0:
            print("The denominator cannot be zero.")
            return

        # Simplify the fraction
        simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
        
        # Print the result in the form of a fraction
        print(f"The simplified fraction is: {simplified_numerator}/{simplified_denominator}")

    except ValueError:
        print("Please enter valid integers for numerator and denominator.")

if __name__ == "__main__":
    main()
