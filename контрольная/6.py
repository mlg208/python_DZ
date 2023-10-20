import random


N = 5  
M = 4  


matrix = [[random.randint(-10, 10) for _ in range(M)] for _ in range(N)]

for row in matrix:
    print(row)

sums_in_rows = [0] * N
sums_in_columns = [0] * M

for i in range(N):
    for j in range(M):
        if matrix[i][j] % 2 != 0:  
            sums_in_rows[i] += matrix[i][j]
            sums_in_columns[j] += matrix[i][j]

for i in range(N):
    print(f"Сумма нечетных элементов в строке {i + 1}: {sums_in_rows[i]}")

for j in range(M):
    print(f"Сумма нечетных элементов в столбце {j + 1}: {sums_in_columns[j]}")
