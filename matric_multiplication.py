"""
Matrix Multiplication: C = A × B

Given two matrices:
- A of size (m × n)
- B of size (n × p)

The resulting matrix C will have dimensions (m × p).
Each element C[i][j] is computed as:
    C[i][j] = sum(A[i][k] * B[k][j]) for k in range(n)

Rules:
1. The number of columns in the first matrix (A) must equal the number of rows in the second matrix (B).
2. This works for both square and non-square matrices.
    - Square matrix case: A and B both have the same number of rows and columns (e.g., 3×3 × 3×3 → 3×3)
    - Non-square matrix case: A is m×n and B is n×p (e.g., 4×3 × 3×4 → 4×4)

Loop Structure:
- i iterates over rows of A (m)
- j iterates over columns of B (p)
- k iterates over shared dimension (n), which is columns of A and rows of B

Make sure to:
- Initialize result matrix C with size m×p
- Use M[0] to get the number of columns in B
"""

"""
Example for Non Square Matrix
"""
def Nonsquare_matrix_mult(L, M):
    multi_matrix = [[ 0 for _ in range(len(M[0]))] for _ in range(len(L))]

    for i in range(len(L)):
        for j in range(len(M[0])):
            for k in range(len(L[0])):
                multi_matrix[i][j] += L[i][k] * M[k][j]

    return multi_matrix

"""
Example for Sqaure Matrix
"""

def Square_matrix_mult(L, M):
    multi_matrix = [[ 0 for _ in range(len(L))] for _ in range(len(L))]

    for i in range(len(L)):
        for j in range(len(M[0])):
            for k in range(len(L[0])):
                multi_matrix[i][j] += L[i][k] * M[k][j]

    return multi_matrix