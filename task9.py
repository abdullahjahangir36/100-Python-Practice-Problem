#Abdullah Jahangir , Task 9
# Write a program that take a user input of three angles and
# will find out whether it can form a triangle or not.
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

if ((angle1+angle2+angle3==180) and (angle1>0) and (angle2>0) and (angle3>0)):
    print("This can form a Triangle")
else:
    print("This can not form a Triangle")