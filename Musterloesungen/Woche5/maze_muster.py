import stddraw
import random


def create_maze(n):
    maze = [['#'] * (n * 2 + 1) for _ in range(n * 2 + 1)]

    last = (-1,-1)
    def carve(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < n * 2 and 1 <= ny < n * 2 and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[ny - dy//2][nx - dx//2] = ' '
                last = (nx-1, ny - 1)
                carve(nx, ny)
                

    maze[1][0] = 'S'
    carve(1, 1)
    maze[-2][-1] = 'E'
    return maze



with open('sheet05/maze2.txt', 'r') as f:
    maze = [list(line) for line in f.read().split("\n") if line]



def draw_maze(maze):
    width = len(maze[0])
    height = len(maze)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(0.01)
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            stddraw.setPenColor(stddraw.BLACK)
            if cell == 'E':
                stddraw.setPenColor(stddraw.RED)
            if cell == 'S':
                stddraw.setPenColor(stddraw.GREEN)
            if cell == 'X':
                stddraw.setPenColor(stddraw.BLUE)
            if cell != ' ':
                stddraw.filledRectangle(x / width, 1 - (y + 1) / height, 1 / width, 1 / height)

def find_start(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                return (x, y)

def is_free_cell(maze, x, y):
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and (maze[y][x] == ' ' or maze[y][x] == 'E')

def show_path(maze, prev, x, y):
    while prev[y][x] != (-1,-1):
        x, y = prev[y][x]
        if maze[y][x] == 'S':
            break
        maze[y][x] = 'X'
    draw_maze(maze)

def is_solvable(maze):
    x, y = find_start(maze)
    prev = [[(-1,-1) for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visit_queue = [(x, y)]
    while visit_queue:
        cx, cy = visit_queue.pop(0)
        if maze[cy][cx] == 'E':
           show_path(maze, prev, cx, cy)
           return True
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if is_free_cell(maze, cx + dx, cy + dy) and prev[cy + dy][cx + dx] == (-1,-1):
                visit_queue.append((cx + dx, cy + dy))
                prev[cy + dy][cx + dx] = (cx, cy)
    
    return False
    
draw_maze(maze)

if is_solvable(maze):
    stddraw.show()
