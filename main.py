import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 15
ROWS = SCREEN_HEIGHT // CELL_SIZE
COLS = SCREEN_WIDTH // CELL_SIZE
ALIVE_COLOR = (0, 255, 0)
DEAD_COLOR = (0, 0, 0)
GRID_COLOR = (128, 128, 128)

def initialize_grid():
    # init frame with the Gosper's Glider gun pattern

    grid = [[0 for x in range(COLS)] for y in range(ROWS)]
    
    grid[5][1] = 1; grid[5][2] = 1; grid[6][1] = 1; grid[6][2] = 1

    grid[3][13] = 1; grid[3][14] = 1; grid[4][12] = 1; grid[4][16] = 1
    grid[5][11] = 1; grid[5][17] = 1; grid[6][11] = 1; grid[6][15] = 1
    grid[6][17] = 1; grid[6][18] = 1; grid[7][11] = 1; grid[7][17] = 1
    grid[8][12] = 1; grid[8][16] = 1; grid[9][13] = 1; grid[9][14] = 1

    grid[1][25] = 1; grid[2][23] = 1; grid[2][25] = 1; grid[3][21] = 1
    grid[3][22] = 1; grid[4][21] = 1; grid[4][22] = 1; grid[5][21] = 1
    grid[5][22] = 1; grid[6][23] = 1; grid[6][25] = 1; grid[7][25] = 1

    grid[3][35] = 1; grid[3][36] = 1; grid[4][35] = 1; grid[4][36] = 1
    
    return grid

def draw_grid_lines(screen):
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))
 
def draw_cells(grid, screen):
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                color = ALIVE_COLOR
            else:
                color = DEAD_COLOR
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def count_neighbors(grid, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= row+i < len(grid) and 0 <= col+j < len(grid[0]):
                count += grid[row+i][col+j]
    return count

def update_cells(grid):
    new_grid = [[0] * COLS for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            neighbors = count_neighbors(grid, row, col)
            if grid[row][col] == 1 and neighbors in (2, 3):
                new_grid[row][col] = 1
            elif grid[row][col] == 0 and neighbors == 3:
                new_grid[row][col] = 1
    return new_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    
    grid = initialize_grid()
    draw_grid_lines(screen)
    draw_cells(grid, screen)
    pygame.display.update()

    running = True
    paused = False
    delay = 100

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN and paused:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0] // CELL_SIZE
                row = mouse_pos[1] // CELL_SIZE
                grid[row][col] = 1 - grid[row][col]
        
        if not paused:
            grid = update_cells(grid)
            pygame.display.set_caption("Conway's Game of Life")
        else:
            pygame.display.set_caption("Conway's Game of Life - (Paused)")

        screen.fill(DEAD_COLOR)
        draw_cells(grid, screen)
        draw_grid_lines(screen)
        pygame.display.flip()
        
        pygame.time.wait(delay)
    
if __name__ == "__main__":
    main()
