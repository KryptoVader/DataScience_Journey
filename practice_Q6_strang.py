from matric_multiplication import Square_matrix_mult

"""
Q6) Write down the 2 by 2 matrices A and B that have entries ai j = i+ j and bi j = (−1)
i+j.Multiply them to find AB and BA
"""

A,B = [],[]
for i in range(1,3):
    L = []
    for j in range(1,3):
        L.append(i+j)
    A.append(L)
    
for i in range(1,3):
    L = []
    for j in range(1,3):
        L.append((-1)**(i+j))
    B.append(L)

print("AB is: ")
print(Square_matrix_mult(A, B))

print("====================================")

print("BA is: ")
print(Square_matrix_mult(B, A))