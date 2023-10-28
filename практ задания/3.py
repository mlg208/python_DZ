import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def transposed(self):
        transposed_matrix = Matrix(self.cols, self.rows)
        transposed_matrix.data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return transposed_matrix

class IdMatrix(Matrix):
    def __init__(self, rows, cols):
        if rows != cols:
            raise ValueError("Identity matrix must be square (rows = cols)")
        super().__init__(rows, cols)
        for i in range(rows):
            for j in range(cols):
                if i == j:
                    self.data[i][j] = 1
                else:
                    self.data[i][j] = 0


# Создание и отображение матрицы
matrix = Matrix(3, 4)
print("Matrix:")
print(matrix)

# Создание и отображение единичной матрицы
id_matrix = IdMatrix(3, 3)
print("Identity Matrix:")
print(id_matrix)

# Сложение 
matrix2 = Matrix(3, 4)
print("Matrix 2:")
print(matrix2)

sum_matrix = matrix + matrix2
print("Sum of Matrices:")
print(sum_matrix)

# Транспонирование 
transposed = matrix.transposed()
print("Transposed Matrix:")
print(transposed)
