import pygame

from maze.cell import Cell
from maze.generator import generate_maze
from maze.solver import astar

WINDOW_WIDTH: int = 801


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
    astar(grid)

    running: bool = True
    while running:
        _ = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_window(window, grid)

    pygame.quit()


if __name__ == "__main__":
    main()
