# à faire : fonctions pour : de quelle couleur est la tile x, y
# faire défiler défiler board
# draw

import pygame

from .tile import Tile

WHITE = (255, 255, 255)

class Board:
    """The board."""

    def __init__(self, screen: pygame.Surface, nb_lines: int, nb_cols: int,
                 tile_size: int) -> None:
        self._screen = screen
        self._nb_lines = nb_lines
        self._nb_cols = nb_cols
        self._tile_size = tile_size
        self._tiles = [[Tile(x, y, WHITE) for y in range(self._nb_lines)] for x in range(self._nb_cols)]

    @property
    def nb_lines(self):
        """Gives how many lines the board counts."""
        return self._nb_lines
    
    @property
    def nb_cols(self):
        """Gives how many columns the board counts."""
        return self._nb_cols
    
    def get_tile(self, x: int, y: int) -> Tile:
        """Gives the tile at given coordinates."""
        return self._tiles[y][x]