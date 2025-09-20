import heapq
from itertools import count

from maze.cell import Cell


def _heuristic(cell_a: Cell, cell_b: Cell) -> int:
    return abs(cell_a.row - cell_b.row) + abs(cell_a.col - cell_b.col)


def _get_open_neighbors(cell: Cell, grid: list[list[Cell]]) -> list[Cell]:
    neighbors: list[Cell] = []
    row, col = cell.row, cell.col

    if not cell.top and row > 0:
        neighbors.append(grid[row - 1][col])
    if not cell.bottom and row < len(grid) - 1:
        neighbors.append(grid[row + 1][col])
    if not cell.left and col > 0:
        neighbors.append(grid[row][col - 1])
    if not cell.right and col < len(grid[0]) - 1:
        neighbors.append(grid[row][col + 1])

    return neighbors


def astar(grid: list[list[Cell]]) -> list[Cell]:
    start: Cell = grid[0][0]
    end: Cell = grid[-1][-1]

    counter: count[int] = count()
    open_set: list[tuple[int, int, Cell]] = []
    heapq.heappush(open_set, (0, next(counter), start))

    came_from: dict[Cell, Cell] = {}
    g_score: dict[Cell, int] = {start: 0}
    f_score: dict[Cell, int] = {start: _heuristic(start, end)}

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if current == end:
            path: list[Cell] = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor in _get_open_neighbors(current, grid):
            tentative_g: int = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + _heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], next(counter), neighbor))

    return []
