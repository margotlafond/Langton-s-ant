import pygame
from pathlib import Path

from .ant import Ant
from .board import Board

class Game:
    """The main class of the game."""

    def __init__(self, nb_steps: int, tile_size: int, # noqa: PLR0913
                 fps: int,
                 ant_color: tuple,
                 score_file: Path,
                 gui: bool,
                 logger_obj,
                 width: int, height: int,
                 ) -> None:
        """Object initialization."""
        # Given arguments
        self._tile_size = tile_size
        self._fps = fps
        self._ant_color = ant_color
        self._score_file = score_file
        self._nb_steps = nb_steps
        self._gui = gui
        self._logger = logger_obj
        self._logger.info("test")

        # News parameters and objects
        screen_size = (width*self._tile_size,
                       height*self._tile_size)
        self._screen = pygame.display.set_mode(screen_size)
        self._nb_lines = height // self._tile_size
        self._nb_cols = width // self._tile_size
        self._board = Board(self._screen, self._nb_lines, self._nb_cols, tile_size)
        self._ant = Ant.create_random(self._board)
        

        # Create the clock
        self._clock = pygame.time.Clock()

    def start(self) -> None:
        """Start the game."""
        self._logger.info("Game started.")
        # Initialize pygame
        pygame.init()

        # Initialize game
        #self._init() # à coder ?
        i = 0

        # Start pygame loop
        while i < self._nb_steps:

            # Wait 1/FPS second
            self._clock.tick(self._fps)

            # Update object
            tile = self._board.get_tile(self._ant.x, self._ant.y)
            self._ant.move(tile)

            # Display
            if self._gui:
                self._board.draw_board(self._ant, self._ant_color)
                pygame.display.update()

            # Output file

            # Increase number of steps
            i += 1

        # Terminate pygame
        pygame.quit()