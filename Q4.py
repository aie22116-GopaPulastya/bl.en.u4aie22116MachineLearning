def transpose_matrix(input_matrix):
    return [[input_matrix[j][i] for j in range(len(input_matrix))] for i in range(len(input_matrix[0]))]
# Get user input for the matrix
num_rows = int(input("Enter the number of rows for the matrix: "))
num_cols = int(input("Enter the number of columns for the matrix: "))
matrix = [[int(input(f"Enter element for matrix[{i}][{j}]: ")) for j in range(num_cols)] for i in range(num_rows)]
# Call the function to get the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)
# Print the result
print("Original Matrix:")
for row in matrix:
    print(row)
print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
