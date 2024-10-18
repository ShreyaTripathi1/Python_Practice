# Function to take matrix input from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the values for the {rows}x{cols} matrix, row by row, space-separated:")
    for i in range(rows):
        row = list(map(int, input().split()))  # Take input for each row
        matrix.append(row)
    return matrix

# Function to calculate the transpose of a matrix
def transpose_matrix(matrix, rows, cols):
    # Create an empty matrix with dimensions cols x rows (transposed dimensions)
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Transpose logic: swap rows and columns
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose

# Main Program
if __name__ == "__main__":
    # Input dimensions for the matrix
    rows, cols = map(int, input("Enter the number of rows and columns, separated by a space: ").split())

    # Input the matrix
    matrix = input_matrix(rows, cols)

    # Calculate the transpose
    transposed_matrix = transpose_matrix(matrix, rows, cols)

    # Print the transposed matrix
    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(" ".join(map(str, row)))
