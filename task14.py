# Calculate the angle between the hour hand and minute hand.
# Constraints:
# 1 ≤ H ≤ 12
# 0 ≤ M < 60
# H and M are Integers
import math

def getAngle(H, M):
    """Calculate the smallest angle between the hour and minute hands."""
    # Calculate the angle of the minute hand from 12:00
    minute_angle = M * 6
    
    # Calculate the angle of the hour hand from 12:00
    hour_angle = (H % 12) * 30 + M * 0.5
    
    # Calculate the absolute difference between the two angles
    angle = abs(hour_angle - minute_angle)
    
    # Find the minimum angle between the two possible angles
    min_angle = min(angle, 360 - angle)
    
    # Return the floor of the minimum angle
    return math.floor(min_angle)

if __name__ == "__main__":
    # Take input from the user
    H = int(input("Enter the hour (1-12): ").strip())
    M = int(input("Enter the minute (0-59): ").strip())
    
    # Validate the input
    if H < 1 or H > 12:
        print("Error: Hour should be between 1 and 12.")
    elif M < 0 or M > 59:
        print("Error: Minute should be between 0 and 59.")
    else:
        # Compute and print the angle
        angle = getAngle(H, M)
        print(f"The minimum angle between the hour and minute hands is: {angle} degrees.")
