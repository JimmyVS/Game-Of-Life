# Made by Jim Grysmpolakis.
# Please do not claim as yours.

# Conway's Game of Life Implementation with Pygame

# This implementation showcases Conway's Game of Life, a cellular automaton devised by mathematician John Conway.
# The game consists of a grid of cells, each of which can be alive (populated) or dead (unpopulated).
# The state of each cell evolves over time based on simple rules, creating interesting patterns and behaviors.

# To play, press left click to place cells in the grid. You can also press space to play or pause the simulation.
# With right click, you can place a pre-placed cells, called "glider".

# Pygame is used for visualization and user interaction in this implementation.

import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 80
CELL_SIZE = 10

# Colors
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Function to initialize an empty grid
def initialize_grid():
    return [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Function to draw the grid
def draw_grid():
    for x in range(GRID_SIZE + 1):
        pygame.draw.line(screen, GRAY, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT))
    for y in range(GRID_SIZE + 1):
        pygame.draw.line(screen, GRAY, (0, y * CELL_SIZE), (WIDTH, y * CELL_SIZE))

# Function to draw the cells
def draw_cells(grid):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            color = WHITE if grid[x][y] else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to update the grid based on the rules of Conway's Game of Life
def update_grid(grid):
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            alive_neighbors = count_alive_neighbors(grid, x, y)
            # Apply rules of Conway's Game of Life
            if grid[x][y] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                new_grid[x][y] = 0
            elif grid[x][y] == 0 and alive_neighbors == 3:
                new_grid[x][y] = 1
            else:
                new_grid[x][y] = grid[x][y]
    return new_grid

# Function to get the number of alive neighbors for a given cell
def count_alive_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_x, new_y = x + i, y + j
            # Check if neighbor is within the grid bounds and is alive
            if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and grid[new_x][new_y] == 1:
                count += 1
    return count

# Function to add a glider at a specific position
def add_glider(grid, x, y):
    glider_pattern = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]
    # Place glider pattern in the grid
    for i, row in enumerate(glider_pattern):
        grid[x + i][y:y + len(row)] = row

# Function to display the status indicator
def draw_status_indicator(paused):
    font = pygame.font.Font(None, 36)
    status_text = "Playing" if not paused else "Paused"
    color = GREEN if not paused else RED
    text = font.render(status_text, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 20))
    screen.blit(text, text_rect)

# Function to count the number of alive cells
def count_alive_cells(grid):
    count = sum(row.count(1) for row in grid)
    return count

# Function to draw the cell count
def draw_cell_count(count):
    font = pygame.font.Font(None, 36)
    count_text = f"Alive Cells: {count}"
    text = font.render(count_text, True, WHITE)
    text_rect = text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(text, text_rect)

# Main loop
running = True
paused = True
grid = initialize_grid()

# Keep track of mouse state
left_mouse_pressed = False
right_mouse_pressed = False

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Toggle between paused and playing
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                left_mouse_pressed = True
            elif event.button == 3:  # Right mouse button
                right_mouse_pressed = True
                x, y = event.pos
                grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
                # Add glider pattern where right mouse button is clicked
                add_glider(grid, grid_x, grid_y)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_mouse_pressed = False
            elif event.button == 3:
                right_mouse_pressed = False

    # Add cells continuously when left mouse button is held down
    if left_mouse_pressed:
        x, y = pygame.mouse.get_pos()
        grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
        grid[grid_x][grid_y] = 1

    # Update the grid if not paused
    if not paused:
        grid = update_grid(grid)

    # Draw the cells
    draw_cells(grid)

    # Draw the grid lines
    draw_grid()

    # Draw the status indicator
    draw_status_indicator(paused)

    # Count and draw the number of alive cells
    alive_cell_count = count_alive_cells(grid)
    draw_cell_count(alive_cell_count)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()
sys.exit()
