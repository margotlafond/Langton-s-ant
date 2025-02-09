# First party
from .dir import Dir


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

    @property
    def x(self) -> int:
        """The x coordinate (i.e.: column index) of the ant."""
        return self._x
    
    @property
    def y(self) -> int:
        """The x coordinate (i.e.: line index) of the ant."""
        return self._y

    def move(self) -> None:
        self._x += self._dir[0]
        self._y += self._dir[1]