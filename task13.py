#Abdullah Jahangir , Task 13
# Write  a program that will tell whether the given number is divisible by 3 & 6.
number = int(input("Enter Number to Check whether it's divisible by 3 & 6 or not: "))
if number %3==0 and number%6==0:
    print(f"{number} is divisible by 3 & 6")
else:
    print(f"{number} is not divisible by 3 & 6")