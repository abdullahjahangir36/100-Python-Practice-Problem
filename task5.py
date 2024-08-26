#Abdullah Jahangir , Task 5
# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
number = input("Enter Four Digit Number: ")
if len(number)!=4:
    print("Please enter a valid 4-Digit Number.")
else:
    reverse=number[::-1]
    print(f"The Reverse of {number} is {reverse}")