from matric_multiplication import Square_matrix_mult

"""
Q12. The product of two lower triangular matrices is again lower triangular (all its entries
above the main diagonal are zero). Confirm this with a 3 by 3 example, and then
explain how it follows from the laws of matrix multiplication.

"""

L = []
for i in range(3):
    M = []
    for j in range(3):
        if i < j :
            M.append(0)
            continue
        M.append(i+j)
    L.append(M)
        
N = []
for i in range(3):
    M = []
    for j in range(3):
        if i < j :
            M.append(0)
            continue
        M.append((-1)**(i+j))
    N.append(M)
    
print(Square_matrix_mult(L,N))