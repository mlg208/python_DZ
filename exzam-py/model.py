class XoModel:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def is_empty(self, row, col):
        return self.grid[row][col] ==  ' '
    
    def set(self, row, col, char):
        self.grid[row][col] = char

    def row(self, row):
        return tuple(self.grid[row])
    
    def col(self, col):
        return tuple(self.grid[i][col] for i in range(self.size))
    
    def diag(self, direction):
        if direction == 1:
            return tuple(self.grid[i][i] for i in range(self.size))
        else: 
            direction == -1
            return tuple(self.grid[i][self.size -1 -i] for i in range(self.size))
        
    def __str__(self):
        board = []
        for i in range(self.size):
            board_row = ' | '.join (self.grid[i])
            board.append(f'{i + 1} | {board_row} |')
        col_numbers = ' ' + ' '.join(str(i + 1) for i in range(self.size))
        separator = '\n +---' + '---' * (self.size -1) + '---+'
        return f'   {col_numbers}\n{separator}\n{separator}\n{separator}'.join(board)
        