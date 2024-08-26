#Abdullah Jahangir , Task 7
# Write a program that will tell whether the given year is a leap year or not.
year=int(input("Enter Year to check whether it's leap or not: "))
if (year%4==0 and year%100!=0) or (year %400==0):
    print(f"{year} Year is Leap Year")
else:
    print(f"{year} Year is not Leap Year")