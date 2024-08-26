# Write a program to perform matrix multiplication on 2 matrices.
def matrix_multiply(matrix1, matrix2):
    # Get dimensions of matrix1
    rows1 = len(matrix1)
    cols1 = len(matrix1[0]) if rows1 > 0 else 0
    
    # Get dimensions of matrix2
    rows2 = len(matrix2)
    cols2 = len(matrix2[0]) if rows2 > 0 else 0
    
    # Check if multiplication is possible
    if cols1 != rows2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    
    # Initialize result matrix with zeros
    result = [[0] * cols2 for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1))
    
    return result

def main():
    # Input first matrix
    input_string1 = input("Enter the first matrix (rows separated by semicolons, items separated by spaces): ")
    matrix1 = [list(map(int, row.split())) for row in input_string1.split(';')]
    
    # Input second matrix
    input_string2 = input("Enter the second matrix (rows separated by semicolons, items separated by spaces): ")
    matrix2 = [list(map(int, row.split())) for row in input_string2.split(';')]
    
    # Perform matrix multiplication
    try:
        result = matrix_multiply(matrix1, matrix2)
        print("Result of matrix multiplication:")
        for row in result:
            print(' '.join(map(str, row)))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
