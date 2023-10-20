import random

N = 4  
M = 5  


matrix = [[random.randint(-10, 10) for _ in range(M)] for _ in range(N)]


for row in matrix:
    print(row)

for i, row in enumerate(matrix):
    min_in_row = min(row)
    max_in_row = max(row)
    print(f"В строке {i+1}: Минимальный элемент: {min_in_row}, Максимальный элемент: {max_in_row}")

transposed_matrix = list(map(list, zip(*matrix)))

for j, column in enumerate(transposed_matrix):
    min_in_column = min(column)
    max_in_column = max(column)
    print(f"В столбце {j+1}: Минимальный элемент: {min_in_column}, Максимальный элемент: {max_in_column}")
