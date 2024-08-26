# Write a program to print the shape of a matrix.
def print_matrix_shape(matrix):
    # Get the number of rows
    num_rows = len(matrix)
    # Get the number of columns (assuming all rows have the same number of columns)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    
    print(f"The shape of the matrix is: {num_rows} rows x {num_cols} columns")

def main():
    # Input matrix from the user
    input_string = input("Enter the matrix (rows separated by semicolons, items separated by spaces): ")
    
    # Convert the input string to a matrix (list of lists)
    matrix = [list(map(int, row.split())) for row in input_string.split(';')]
    
    # Print the shape of the matrix
    print_matrix_shape(matrix)

if __name__ == "__main__":
    main()
