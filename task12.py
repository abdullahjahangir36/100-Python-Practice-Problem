#Abdullah Jahangir , Task 12
# Write a program to find the volume of the cylinder.
# Also find the cost when ,when the cost of 1litre milk is 40Rs
#Volume of Cylinder
import math
r=int(input("Enter Cylinder Radius: "))
h=int(input("Enter Cylinder Height: "))

volume= math.pi*(r**2)*h
print(f"Volume of Cylinder is: {volume}")

#Milk Cost
litre_milk=int(input("Enter litres of Milk: "))
#1 litre milk = 40 Rs.

cost_milk = litre_milk * 40
print(f"{litre_milk} litre Milk Cost is Rs. {cost_milk}")