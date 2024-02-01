def matrix_multiply(matrix_a, matrix_b):
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    if cols_a != rows_b:
        return "Error: Matrices A and B are not multipliable."
    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix
def get_matrix_from_user(rows, cols, matrix_name):
    print(f"Enter elements for Matrix {matrix_name}:")
    return [[int(input(f"Enter element for Matrix {matrix_name}[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
# Get user input for matrix A
matrix_a_rows = int(input("Enter the number of rows for Matrix A: "))
matrix_a_cols = int(input("Enter the number of columns for Matrix A: "))
matrix_a = get_matrix_from_user(matrix_a_rows, matrix_a_cols, 'A')
# Get user input for matrix B
matrix_b_rows = int(input("Enter the number of rows for Matrix B: "))
matrix_b_cols = int(input("Enter the number of columns for Matrix B: "))
matrix_b = get_matrix_from_user(matrix_b_rows, matrix_b_cols, 'B')
# Perform matrix multiplication
result_matrix = matrix_multiply(matrix_a, matrix_b)
# Print the result or error message
print("Matrix Multiplication Result:")
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    for row in result_matrix:
        print(row)
