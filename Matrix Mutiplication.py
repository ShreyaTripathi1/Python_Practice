# Function to take matrix input from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the values for the {rows}x{cols} matrix, row by row, space-separated:")
    for i in range(rows):
        row = list(map(int, input().split()))  # Take input for each row
        matrix.append(row)
    return matrix

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2, rows1, cols1, cols2):
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Matrix multiplication logic
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Main Program
if __name__ == "__main__":
    # Input dimensions for the first matrix
    rows1, cols1 = map(int, input("Enter number of rows and columns for Matrix 1, separated by a space: ").split())

    # Input the first matrix
    print("Matrix 1:")
    matrix1 = input_matrix(rows1, cols1)

    # Input dimensions for the second matrix (rows of matrix 2 must match cols of matrix 1)
    rows2, cols2 = map(int, input("Enter number of rows and columns for Matrix 2, separated by a space: ").split())

    if cols1 != rows2:
        print("Matrix multiplication is not possible. The number of columns in Matrix 1 must equal the number of rows in Matrix 2.")
    else:
        # Input the second matrix
        print("Matrix 2:")
        matrix2 = input_matrix(rows2, cols2)

        # Perform matrix multiplication
        result_matrix = multiply_matrices(matrix1, matrix2, rows1, cols1, cols2)

        # Print the result
        print("\nResult of Matrix Multiplication:")
        for row in result_matrix:
            print(" ".join(map(str, row)))
