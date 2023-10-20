import random

N = 5  
M = 4 

matrix = [[random.randint(-10, 10) for _ in range(M)] for _ in range(N)]

for row in matrix:
    print(row)
