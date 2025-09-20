import random

from maze.cell import Cell


def _get_unvisited_neighbors(cell: Cell, grid: list[list[Cell]]) -> list[Cell]:
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


def _remove_walls(current_cell: Cell, next_cell: Cell) -> None:
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
        unvisited_neighbors: list[Cell] = _get_unvisited_neighbors(current_cell, grid)
        if unvisited_neighbors:
            next_cell: Cell = random.choice(unvisited_neighbors)
            _remove_walls(current_cell, next_cell)
            next_cell.visited = True
            stack.append(next_cell)
        else:
            _ = stack.pop()
