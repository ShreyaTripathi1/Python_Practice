# Function to take matrix input from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the values for the {rows}x{cols} matrix, row by row, space-separated:")
    for i in range(rows):
        row = list(map(int, input().split()))  # Take input for each row
        matrix.append(row)
    return matrix

# Function to add two matrices
def add_matrices(matrix1, matrix2, rows, cols):
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Main Program
if __name__ == "__main__":
    # Get matrix dimensions
    rows, cols = map(int, input("Enter number of rows and columns, separated by a space: ").split())

    # Input the first matrix
    print("Matrix 1:")
    matrix1 = input_matrix(rows, cols)

    # Input the second matrix
    print("Matrix 2:")
    matrix2 = input_matrix(rows, cols)

    # Perform matrix addition
    result_matrix = add_matrices(matrix1, matrix2, rows, cols)

    # Print the result
    print("\nSum of the two matrices:")
    for row in result_matrix:
        print(" ".join(map(str, row)))
