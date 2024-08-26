# Given two rectangles, find if the given two rectangles overlap or not. 
# A rectangle is denoted by providing the x and y coordinates of two points: 
# the left top corner and the right bottom corner of the rectangle. 
# Two rectangles sharing a side are considered overlapping. 
# (L1 and R1 are the extreme points of the first rectangle and
#  L2 and R2 are the extreme points of the second rectangle).
def rectangles_overlap(L1, R1, L2, R2):
    """Determine if two rectangles overlap."""
    # Unpack coordinates for clarity
    L1_x, L1_y = L1
    R1_x, R1_y = R1
    L2_x, L2_y = L2
    R2_x, R2_y = R2
    
    # Check if one rectangle is to the left of the other
    if R1_x < L2_x or R2_x < L1_x:
        return 0
    
    # Check if one rectangle is above the other
    if L1_y < R2_y or L2_y < R1_y:
        return 0
    
    # If none of the above, the rectangles overlap
    return 1

def parse_input(prompt):
    """Parse tuple input from the user."""
    while True:
        try:
            # Get input and strip unnecessary spaces
            user_input = input(prompt).strip()
            # Remove parentheses and split by comma
            user_input = user_input.strip('()')
            x, y = map(int, user_input.split(','))
            return (x, y)
        except ValueError:
            print("Invalid input. Please enter coordinates in the format (x, y).")

if __name__ == "__main__":
    # Input coordinates
    L1 = parse_input("Enter L1 (x, y): ")
    R1 = parse_input("Enter R1 (x, y): ")
    L2 = parse_input("Enter L2 (x, y): ")
    R2 = parse_input("Enter R2 (x, y): ")
    
    # Determine if the rectangles overlap
    result = rectangles_overlap(L1, R1, L2, R2)
    print(result)
