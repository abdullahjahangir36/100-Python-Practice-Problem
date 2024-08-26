#Abdullah Jahangir , Task 8
# Write a program to find the euclidean distance between two coordinates.
import math
x1 = float(input("Enter x-coordinate of First point: "))
y1 = float(input("Enter y-coordinate of First point: "))

x2 = float(input("Enter x-coordinate of Second point: "))
y2 = float(input("Enter y-coordinate of Second point: "))

#Euclidean Distance Formula
euc_distance= math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"The euclidean distance between ({x1},{y1}) and ({x2},{y2}) is: {euc_distance}")