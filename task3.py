#Abdullah Jahangir , Task 3
# User will input (2numbers).Write a program to swap the numbers
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

temp = num1 #for storing num1
num1 = num2
num2 = temp

print("Number 1: ", num1)
print("Number 2: ", num2)