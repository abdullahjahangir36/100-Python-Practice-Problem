#Abdullah Jahangir , Task 1
# User will input (3ages).Find the oldest one
a=int(input("Enter Age1: "))
b=int(input("Enter Age2: "))
c=int(input("Enter Age3: "))
if (a>b and a>c):
    print("Age1 is older: ",a)
elif (b>a and b>c):
    print("Age2 is older: ",b)
else:
    print("Age3 is older: ",c)