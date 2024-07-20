def generate_sudoku():
    # taken from https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
    base  = 3
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    squares = side*side
    empties = squares * 1//2
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0
    return board


def print_sudoku(sudoku):
    for row in sudoku:
        print(' '.join([str(x) if x != 0 else '.' for x in row]))
    print()

sudoku = generate_sudoku()
print_sudoku(sudoku)

def check(sudoku, row, col, num):
        for i in range(9):
            if sudoku[row][i] == num or sudoku[i][col] == num:
                return False
        for i in range(3):
            for j in range(3):
                if sudoku[(row//3)*3 + i][(col//3)*3 + j] == num:
                    return False
        return True

def solve(sudoku):
    
    def dfs(sudoku, row, col):
        # if col is 8 go to next row
        if col == 8:
            next_col = 0
            next_row = row + 1
        else:
            next_col = col + 1
            next_row = row

        # skip 
        if sudoku[row][col] != 0:
            if col == 8 and row == 8:
                return True
            return dfs(sudoku, next_row, next_col)
                    
        # try out the numbers
        for x in range(1,10):                
            if check(sudoku, row, col, x):
                sudoku[row][col] = x
                if col == 8 and row == 8:
                    return True
                if not dfs(sudoku, next_row, next_col):
                    # undo
                    sudoku[row][col] = 0
                else: 
                    return True
        return False
    
    solvable = dfs(sudoku, 0,0)
    
    return sudoku if solvable else None

print_sudoku(solve(sudoku))
