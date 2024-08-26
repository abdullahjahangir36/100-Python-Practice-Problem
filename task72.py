# the max item of each row of a matrix
def max_in_rows(matrix):
    # Find the maximum item of each row
    max_items = [max(row) for row in matrix]
    return max_items

def main():
    # Input matrix from the user
    input_string = input("Enter the matrix (rows separated by semicolons, items separated by spaces): ")
    
    # Convert the input string to a matrix (list of lists)
    matrix = [list(map(int, row.split())) for row in input_string.split(';')]
    
    # Find the maximum item of each row
    max_items = max_in_rows(matrix)
    
    # Print the results
    print(f"Maximum item of each row: {max_items}")

if __name__ == "__main__":
    main()
