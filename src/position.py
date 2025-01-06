from color import Color

class Position:
    def __init__(self, pos_x: float, pos_y: float):
        self.__x = pos_x
        self.__y = pos_y

    @property
    def x(self) -> float:
        return self.__x
    @property
    def y(self) -> float:
        return self.__y
    
    @x.setter
    def x(self, pos_x) -> None:
        self.__x = pos_x
    @y.setter
    def y(self, pos_y) -> None:
        self.__y = pos_y
    
    def __str__(self) -> str:
        return f"Position at ({self.__x}, {self.__y})"
    