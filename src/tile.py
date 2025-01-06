import pygame
from position import Position
from color import Color

class Tile:
    def __init__(self, position: Position, color: Color, size: int = 1, falling: bool = True) -> None:
        self.__position: Position = position
        self.__color: Color = color
        self.__size: int = size

    @property
    def position(self) -> Position:
         return self.__position
    def set_pos(self, x: int, y: int) -> None:
        self.__position.x = x
        self.__position.y = y
    
    def change_pos(self, x_offset: int, y_offset: int) -> None:
        self.__position.x += x_offset
        self.__position.y += y_offset
    
    @property
    def color(self) -> Color:
        return self.__color

    def render(self, surface) -> None:
        size = surface.window.get_height() // surface.board.height
        board_offset = surface.width // 2 - ( surface.board.width * surface.board.tile_size) // 2
        rect = pygame.Rect(board_offset + self.position.x * size, self.position.y * size, size, size)
        pygame.draw.rect(surface.window, self.color.pgc, rect)
        