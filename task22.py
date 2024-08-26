# Write a program that will tell the number of dogs and 
# chicken are there when the user will provide the value of total heads and legs.
def solve_animals(total_heads, total_legs):
    # Since we have 2 equations:
    # x + y = total_heads
    # 2x + 4y = total_legs
    
    # We can derive the formulas:
    # y = (total_legs - 2 * total_heads) / 2
    # x = total_heads - y
    
    # Calculate number of dogs
    y = (total_legs - 2 * total_heads) / 2
    # Calculate number of chickens
    x = total_heads - y
    
    # Check if the results are valid
    if x >= 0 and y >= 0 and x.is_integer() and y.is_integer():
        return int(x), int(y)
    else:
        return None, None

try:
    # Input from the user
    total_heads = int(input("Enter the total number of heads: "))
    total_legs = int(input("Enter the total number of legs: "))

    # Solve for the number of chickens and dogs
    chickens, dogs = solve_animals(total_heads, total_legs)

    if chickens is not None and dogs is not None:
        print(f"There are {chickens} chickens and {dogs} dogs.")
    else:
        print("No valid solution. Please check the input values.")

except ValueError:
    print("Please enter valid integer values for heads and legs.")
