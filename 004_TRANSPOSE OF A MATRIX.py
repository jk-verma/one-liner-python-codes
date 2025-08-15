# TRANSPOSE OF A MATRIX

#The transpose_matrix function computes
# the transpose of a given matrix.

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print("\n".join(", ".join(map(str, row)) for row in
                transpose_matrix(matrix)))
# Output:
# 1, 4, 7
# 2, 5, 8
# 3, 6, 9