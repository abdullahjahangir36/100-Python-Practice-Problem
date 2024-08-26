#Abdullah Jahangir , Task 10
# Write a program that will take user input of cost price and 
# selling price and determines whether its a loss or a profit
cost = float(input("Enter Cost in Rs.: "))
sold = float(input("Enter Sold Price in Rs: "))

if cost>sold:
    print(f"It's loss and the loss is Rs. {cost-sold}")
else:
    print(f"It's Profit and the Profit is Rs. {sold-cost}")