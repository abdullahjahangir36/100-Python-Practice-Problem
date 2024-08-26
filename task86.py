# Write a program that accepts neighbors(set of 2D co-ordinates) and
# a point(single 2D co-ordinate) and tells nearest neighbor(in terms of euclidean distance)
import math

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two 2D points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_nearest_neighbor(neighbors, point):
    """Find the nearest neighbor to the given point."""
    nearest_neighbor = None
    min_distance = float('inf')
    
    for neighbor in neighbors:
        distance = euclidean_distance(neighbor, point)
        if distance < min_distance:
            min_distance = distance
            nearest_neighbor = neighbor
    
    return nearest_neighbor

def main():
    # Input neighbors
    neighbors = []
    print("Enter neighbors (format: x y) one by one, type 'done' when finished:")
    
    while True:
        user_input = input().strip()
        if user_input.lower() == 'done':
            break
        try:
            x, y = map(float, user_input.split())
            neighbors.append((x, y))
        except ValueError:
            print("Invalid input. Please enter coordinates in the format: x y")

    # Input point
    print("Enter the point (format: x y):")
    while True:
        try:
            x, y = map(float, input().strip().split())
            point = (x, y)
            break
        except ValueError:
            print("Invalid input. Please enter coordinates in the format: x y")

    # Find and display the nearest neighbor
    nearest = find_nearest_neighbor(neighbors, point)
    if nearest:
        print(f"The nearest neighbor to the point {point} is {nearest}")
    else:
        print("No neighbors provided.")

if __name__ == "__main__":
    main()
