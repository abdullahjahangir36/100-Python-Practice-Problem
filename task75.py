# Write a program that can check if you can perform matrix multiplication on 2 matrices.
def can_multiply(matrix1, matrix2):
    # Get the dimensions of matrix1
    rows1 = len(matrix1)
    cols1 = len(matrix1[0]) if rows1 > 0 else 0
    
    # Get the dimensions of matrix2
    rows2 = len(matrix2)
    cols2 = len(matrix2[0]) if rows2 > 0 else 0
    
    # Check if the number of columns in matrix1 equals the number of rows in matrix2
    return cols1 == rows2

def main():
    # Input first matrix
    input_string1 = input("Enter the first matrix (rows separated by semicolons, items separated by spaces): ")
    matrix1 = [list(map(int, row.split())) for row in input_string1.split(';')]
    
    # Input second matrix
    input_string2 = input("Enter the second matrix (rows separated by semicolons, items separated by spaces): ")
    matrix2 = [list(map(int, row.split())) for row in input_string2.split(';')]
    
    # Check if multiplication is possible
    if can_multiply(matrix1, matrix2):
        print("Matrix multiplication can be performed.")
    else:
        print("Matrix multiplication cannot be performed.")

if __name__ == "__main__":
    main()
