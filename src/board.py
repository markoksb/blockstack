import pygame
from tile import Tile
from color import Color
from shape import Shape
from random import randint

class Board:
    def __init__(self, surface, width: int = 10, height: int = 24, tile_size: int = 15):
        self.__width: int = width
        self.__height: int = height
        self.__grid: list[list] = [[Color.set_color(31, 31, 31) for _ in range(self.__width)] for _ in range(self.__height)] 
        self.__surface = surface
        self.__tile_size: int = surface.window.get_height() // self.__height
        self.__surface.register_game_object(self)
        self.__over: bool = False

        self.__next_shape = Shape(randint(0, 6))
        self.generate_shape()

    @property
    def width(self) -> int:
        return self.__width
    @property
    def height(self) -> int:
        return self.__height
    @property
    def tile_size(self) -> int:
        return self.__tile_size
    
    def game_over(self) -> bool:
        return self.__over
            
    def rotate_shape(self, direction: int = 1):
        self.__current_shape.rotate(direction)

        while self.__current_shape.left_most < 0:
            self.__current_shape.change_pos(1, 0)
        while self.__current_shape.right_most > self.width - 1:
            self.__current_shape.change_pos(-1, 0)
    
    def move_shape(self, pos_x, pos_y):
        if pos_x == 0 and pos_y > 0 and pos_y + self.__current_shape.lowest < self.height:
            for tile in self.__current_shape:
                if type(self.__grid[tile.position.y][tile.position.x]) == Tile:
                    pos_y -= 2
                    break
            self.__current_shape.change_pos(pos_x, pos_y)
        
        x_left = self.width
        x_right = 0
        for tile in self.__current_shape:
            x_left = min(x_left, tile.position.x)
            x_right = max(x_right, tile.position.x)

        if pos_x + x_left >= 0 and pos_x < 0 or pos_x + x_right < self.width and pos_x > 0:
            self.__current_shape.change_pos(pos_x, pos_y)

    def stop_shape(self) -> None:
        self.__current_shape.stop()
        for tile in self.__current_shape:
            self.__grid[tile.position.y][tile.position.x] = tile
        self.generate_shape()

    def check_shape_pos(self) -> bool:
        for tile in self.__current_shape:
            if type( self.__grid[min( tile.position.y + 1, self.height - 1 )][tile.position.x] ) == Tile:
                self.stop_shape()
                return False
                        
            if tile.position.y >= self.height - 1:
                self.stop_shape()
                return False
        return True
    
    def clear_row(self, col: int) -> None:
        for row in range( len(self.__grid[col]) ):            
            self.__grid[col][row] = Color.set_color(31, 31, 31)
        for col in range( col, 0, -1 ):
            for row in range( len(self.__grid[col]) ):
                self.__grid[col][row] = self.__grid[col - 1][row]     

    def generate_shape(self) -> None:
        self.__current_shape = self.__next_shape
        for tile in self.__current_shape:
            if type( self.__grid[min( tile.position.y + 1, self.height - 1 )][tile.position.x] ) == Tile:
                self.__over = True
        self.__next_shape = Shape(randint(0, 6))   
        
    def update(self, dt: int) -> None:
        if self.check_shape_pos():
            if self.__current_shape.is_falling:
                self.__current_shape.change_pos(0, 1)

        for col in range( len(self.__grid) ):
            if all(isinstance(row, Tile) for row in self.__grid[col]):
                self.clear_row(col)
                       
    
    def render(self):
        draw_width = self.__tile_size * self.__width 
        draw_height = self.__tile_size * self.__height
        pos_x = self.__surface.width / 2 - draw_width / 2
        pos_y = 0
        rect = pygame.Rect(pos_x, pos_y, draw_width, draw_height)
        pygame.draw.rect(self.__surface.window, (255,0,255), rect)

        board_offset = self.__surface.width // 2 - ( self.width * self.tile_size) // 2

        for col in range( len(self.__grid) ):
            for row in range( len(self.__grid[col]) ):
                pos_x = row * self.__tile_size + board_offset
                pos_y = col * self.__tile_size
                if type(self.__grid[col][row]) != Color:
                    pygame.draw.rect(self.__surface.window, self.__grid[col][row].color.pgc, pygame.Rect(pos_x, pos_y, self.tile_size, self.tile_size))
                else:
                    pygame.draw.rect(self.__surface.window, self.__grid[col][row].pgc, pygame.Rect(pos_x, pos_y, self.tile_size, self.tile_size))

        for tile in self.__current_shape:
            tile.render(self.__surface)


if __name__ == "__main__":
    board = Board(None)
