#Abdullah Jahangir , Task 11
# Write a program to find the simple interest when the 
# value of principle,rate of interest and time period is given.
principal = int(input("Enter Principal amount of Interest: "))
rate = int(input("Enter Rate amount of Interest: "))
time = int(input("Enter Time amount of Interest: "))

#simple interest formula
interest= (principal*rate*time)/100

print(f"The simple interest for a {principal} Principle Amount , {rate} Rate Amount, {time} Time Amount is: {interest}")