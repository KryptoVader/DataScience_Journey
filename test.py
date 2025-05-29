"""
Define Vector class and Matrix class and add some functionalities to it.
"""

class Vector:
    def __init__(self):
        self.__a = 0
        self.__b = 0
        
    def __init__(self,num):
        self.__a = num
        self.__b = 0
        
    def __init__(self, num1, num2):
        self.__a = num1
        self.__b = num2
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
        
    def __str__(self):
        return '[' + str(self.__a) + ',' + str(self.__b) + ']' 
    
    def __add__(self, v):
        return Vector(self.__a + v.getA(), self.__b + v.getB())
    
    def __sub__(self, v):
        return Vector(self.__a - v.getA(), self.__b - v.getB())
    
    def dot(self, v):
        return self.__a * v.getA() + self.__b * v.getB()
        
v1 = Vector(2,5)
print(v1)

v2 = Vector(3,7)
print(v2)

print(v1 + v2)
print(v2 - v1)
print(v1.dot(v2))

#========================================Matrix=================================================

class Matrix:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            self.__matrix = args[0]
        else:
            self.__matrix = list(args)
            
    def __str__(self):
        shape = self.getShape()

        def format_matrix(mat, depth=0):
            if not isinstance(mat, list):
                return str(mat)

            if not mat:  # Empty list
                return "[]"

            indent = "  " * depth
            if all(not isinstance(el, list) for el in mat):
                return indent + "[" + ", ".join(map(str, mat)) + "]"
            else:
                return "[\n" + ",\n".join(format_matrix(row, depth + 1) for row in mat) + "\n" + indent + "]"

        return format_matrix(self.__matrix)
    
    def getMatrix(self):
        return self.__matrix
    
    def getShape(self):
        def shape_recursive(matrix):
            try:
                length = len(matrix)
                return (length,) + shape_recursive(matrix[0])
            except TypeError:
                return ()
            except IndexError:
                return (0,)

        return shape_recursive(self.__matrix)

    def __add__(self, matrix):
        if (self.getShape() != matrix.getShape()):
            print("Cannot be added")
            pass
        
        (m,n) = self.getShape()
        arr = []
        for i in range(m):
            list1 = []
            for j in range(n):
                list1.append(self.__matrix[i][j] + matrix.getMatrix()[i][j])
            arr.append(list1)
            
        return Matrix(arr)
    
m1 = Matrix([[1,2,3],[4,5,6]])
print(m1)

m2 = Matrix([[10,11,12],[13,14,15]])
print(m2)

print(m1 + m2)