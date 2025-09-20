import random

import pygame

WINDOW_WIDTH: int = 801

WHITE = pygame.Color(255, 255, 255)


class Cell:
    def __init__(self, row: int, col: int, tile_size: int) -> None:
        self.row: int = row
        self.col: int = col
        self.top: bool = True
        self.bottom: bool = True
        self.left: bool = True
        self.right: bool = True
        self.visited: bool = False
        self.tile_size: int = tile_size

        self.pos: pygame.Vector2 = pygame.Vector2(
            self.col * self.tile_size, self.row * self.tile_size
        )

    def draw(self, window: pygame.Surface) -> None:
        if self.top:
            _ = pygame.draw.line(
                window,
                WHITE,
                (self.pos.x, self.pos.y),
                (self.pos.x + self.tile_size, self.pos.y),
            )
        if self.bottom:
            _ = pygame.draw.line(
                window,
                WHITE,
                (self.pos.x, self.pos.y + self.tile_size),
                (self.pos.x + self.tile_size, self.pos.y + self.tile_size),
            )
        if self.left:
            _ = pygame.draw.line(
                window,
                WHITE,
                (self.pos.x, self.pos.y),
                (self.pos.x, self.pos.y + self.tile_size),
            )
        if self.right:
            _ = pygame.draw.line(
                window,
                WHITE,
                (self.pos.x + self.tile_size, self.pos.y),
                (self.pos.x + self.tile_size, self.pos.y + self.tile_size),
            )


def get_unvisited_neighbors(cell: Cell, grid: list[list[Cell]]) -> list[Cell]:
    neighbors: list[Cell] = []
    row, col = cell.row, cell.col

    if row > 0 and not grid[row - 1][col].visited:
        neighbors.append(grid[row - 1][col])
    if row < len(grid) - 1 and not grid[row + 1][col].visited:
        neighbors.append(grid[row + 1][col])
    if col > 0 and not grid[row][col - 1].visited:
        neighbors.append(grid[row][col - 1])
    if col < len(grid[0]) - 1 and not grid[row][col + 1].visited:
        neighbors.append(grid[row][col + 1])

    return neighbors


def remove_walls(current_cell: Cell, next_cell: Cell) -> None:
    row_change: int = current_cell.row - next_cell.row
    col_change: int = current_cell.col - next_cell.col

    if row_change == 1:
        current_cell.top = False
        next_cell.bottom = False
    if row_change == -1:
        current_cell.bottom = False
        next_cell.top = False
    if col_change == 1:
        current_cell.left = False
        next_cell.right = False
    if col_change == -1:
        current_cell.right = False
        next_cell.left = False


def generate_maze(grid: list[list[Cell]]) -> None:
    stack: list[Cell] = []
    current_cell: Cell = grid[0][0]
    current_cell.visited = True
    stack.append(current_cell)

    while stack:
        current_cell = stack[-1]
        unvisited_neighbors: list[Cell] = get_unvisited_neighbors(current_cell, grid)
        if unvisited_neighbors:
            next_cell: Cell = random.choice(unvisited_neighbors)
            remove_walls(current_cell, next_cell)
            next_cell.visited = True
            stack.append(next_cell)
        else:
            _ = stack.pop()


def update_window(window: pygame.Surface, grid: list[list[Cell]]) -> None:
    for row in grid:
        for cell in row:
            cell.draw(window)

    pygame.display.update()


def main() -> None:
    _ = pygame.init()

    window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
    pygame.display.set_caption("Maze")

    clock: pygame.Clock = pygame.Clock()

    rows: int = 40
    columns: int = 40
    tile_size: int = (WINDOW_WIDTH - 1) // rows

    grid: list[list[Cell]] = [
        [Cell(x, y, tile_size) for y in range(columns)] for x in range(rows)
    ]

    generate_maze(grid)

    running: bool = True
    while running:
        _ = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_window(window, grid)

    pygame.quit()


if __name__ == "__main__":
    main()
