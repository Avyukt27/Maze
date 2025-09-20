import pygame

from maze.cell import Cell
from maze.generator import generate_maze
from maze.solver import astar

WINDOW_WIDTH: int = 1001


def update_window(
    window: pygame.Surface, grid: list[list[Cell]], path: list[Cell]
) -> None:
    for cell in path:
        cell.highlighted = True

    for row in grid:
        for cell in row:
            if not path:
                cell.highlighted = False
            cell.draw(window)

    pygame.display.update()


def main() -> None:
    _ = pygame.init()

    window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
    pygame.display.set_caption("Maze")

    clock: pygame.Clock = pygame.Clock()

    rows: int = 250
    columns: int = 250
    tile_size: int = (WINDOW_WIDTH - 1) // rows

    grid: list[list[Cell]] = [
        [Cell(x, y, tile_size) for y in range(columns)] for x in range(rows)
    ]

    generate_maze(grid)
    path: list[Cell] = astar(grid)

    show_path: bool = False

    running: bool = True
    while running:
        _ = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys: pygame.key.ScancodeWrapper = pygame.key.get_just_pressed()
        if keys[pygame.K_s]:
            show_path = not show_path

        update_window(window, grid, path if show_path else [])

    pygame.quit()


if __name__ == "__main__":
    main()
