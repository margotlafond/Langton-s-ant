# First party
from .dir import Dir
from .tile import Tile


class Ant:
    """The ant."""

    def __init__(self, x: int, y: int, direction: Dir) -> None:
        self._x = x
        self._y = y
        self._dir = direction

    @property
    def dir(self) -> Dir:
        """Ant direction."""
        return self._dir

    @dir.setter
    def dir(self, direction: Dir) -> None:
        self._dir = direction

    def turn_right(self) -> None:
        if self._dir == Dir.UP:
            self._dir = Dir.RIGHT
        elif self._dir == Dir.RIGHT:
            self._dir = Dir.DOWN
        elif self._dir == Dir.DOWN:
            self._dir = Dir.LEFT
        elif self._dir == Dir.LEFT:
            self._dir = Dir.UP

    def turn_left(self) -> None:
        if self._dir == Dir.UP:
            self._dir = Dir.LEFT
        elif self._dir == Dir.RIGHT:
            self._dir = Dir.UP
        elif self._dir == Dir.DOWN:
            self._dir = Dir.RIGHT
        elif self._dir == Dir.LEFT:
            self._dir = Dir.DOWN

    @property
    def x(self) -> int:
        """The x coordinate (i.e.: column index) of the ant."""
        return self._x
    
    @property
    def y(self) -> int:
        """The x coordinate (i.e.: line index) of the ant."""
        return self._y

    def move(self, tile: Tile) -> None:
        """Moves the ant : first checks the tile color, then turns, then changes the tile color, and then moves forward."""
        if tile.color == (0, 0, 0):
            self.turn_left()
            tile.color = (255, 255, 255)
        else:
            self.turn_right()
            tile.color = (0, 0, 0) 
        self._x += self._dir[0]
        self._y += self._dir[1]