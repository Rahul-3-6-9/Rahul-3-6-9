#change the board value with the board to be solved
board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return [i,j]
    return None

def allowed_no(board,x,y,n):
    for i in range(9):
        if board[x][i] == n and i!=y:
            return False
        if board[i][y] == n and i!=x:
            return False
    for i in range(3):
        for j in range(3):
            if board[i+3*(x//3)][j+3*(y//3)] == n and i+3*(x//3) != x and j+3*(y//3) != y:
                return False
    return True

def solve(board):
    pos = find_empty(board)
    if not pos:
        return True
    row = pos[0]
    col = pos[1]
    for n in range(1, 10):
        if allowed_no(board,row,col,n):
            board[row][col] = n
            if solve(board):
                return True
            board[row][col]=0
    return False

def print_final():
    if solve(board):
        print(board)

