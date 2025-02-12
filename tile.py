# Third party
import pygame

class Tile:
    """A square tile in the game. Includes a color."""
    
    def __init__(self, x: int, y: int, color: pygame.Color) -> None:
        """Object initialization."""
        self._x = x # Column index
        self._y = y # Line index
        self._color = color

    @property
    def x(self) -> int:
        """The x coordinate (i.e.: column index) of the tile."""
        return self._x
    
    @property
    def y(self) -> int:
        """The y coordinate (i.e.: line index) of the tile."""
        return self._y

    @property
    def color(self) -> pygame.Color:
        """The color of the tile."""
        return self._color
    
    @color.setter
    def color(self, color: pygame.Color) -> None:
        """Change the color of the tile."""
        self._color = color