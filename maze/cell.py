from typing import override

import pygame


class Cell:
    NORMAL_COLOUR: pygame.Color = pygame.Color(255, 255, 255)
    HIGHLIGHTED_BOX_COLOUR: pygame.Color = pygame.Color(0, 100, 0)

    def __init__(self, row: int, col: int, tile_size: int) -> None:
        self.row: int = row
        self.col: int = col
        self.top: bool = True
        self.bottom: bool = True
        self.left: bool = True
        self.right: bool = True
        self.visited: bool = False
        self.highlighted: bool = False
        self.tile_size: int = tile_size

        self.pos: pygame.Vector2 = pygame.Vector2(
            self.col * self.tile_size, self.row * self.tile_size
        )

    def draw(self, window: pygame.Surface) -> None:
        if self.highlighted:
            _ = pygame.draw.rect(
                window,
                self.HIGHLIGHTED_BOX_COLOUR,
                pygame.Rect(self.pos.x, self.pos.y, self.tile_size, self.tile_size),
            )

        if self.top:
            _ = pygame.draw.line(
                window,
                self.NORMAL_COLOUR,
                (self.pos.x, self.pos.y),
                (self.pos.x + self.tile_size, self.pos.y),
            )

        if self.bottom:
            _ = pygame.draw.line(
                window,
                self.NORMAL_COLOUR,
                (self.pos.x, self.pos.y + self.tile_size),
                (self.pos.x + self.tile_size, self.pos.y + self.tile_size),
            )

        if self.left:
            _ = pygame.draw.line(
                window,
                self.NORMAL_COLOUR,
                (self.pos.x, self.pos.y),
                (self.pos.x, self.pos.y + self.tile_size),
            )

        if self.right:
            _ = pygame.draw.line(
                window,
                self.NORMAL_COLOUR,
                (self.pos.x + self.tile_size, self.pos.y),
                (self.pos.x + self.tile_size, self.pos.y + self.tile_size),
            )

    @override
    def __hash__(self) -> int:
        return hash((self.row, self.col))

    @override
    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Cell) and self.row == other.row and self.col == other.col
        )
