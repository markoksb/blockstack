import pygame.color

class Color:
    def __init__(self, color: int):
        # if isinstance(color, Color):
        #     self.__color == color.value
        # else:
            self.__color: int = color

    @property
    def value(self) -> int:
        return self.__color
    
    # @value.setter
    # def value(self, color: int) -> None:
    #     self.__color: int = color

    @property
    def pgc(self):
        return pygame.Color(self.r, self.g, self.b)

    @property
    def r(self) -> int:
        return (self.value >> 16) & 0xFF
              
    @property
    def g(self) -> int:
        return (self.value >> 8) & 0xFF
    
    @property
    def b(self) -> int:
        return self.value & 0xFF
    
    @r.setter
    def r(self, r: int) -> None:
        self.__color = (self.__color & 0xFF00FFFF) | (( r & 0xFF ) << 16)
    @g.setter
    def g(self, g: int) -> None:
        self.__color = (self.__color & 0xFFFF00FF) | (( g & 0xFF ) << 8)
    @b.setter
    def b(self, b: int) -> None:
        self.__color = (self.__color & 0xFFFFFF00) | ( b & 0xFF )
    
    @classmethod
    def set_color(cls, r: int, g: int, b: int):
        c = ( (( r & 0xFF ) << 16) | (( g & 0xFF ) << 8) | ( b & 0xFF ) )
        return cls( c )

    def __str__(self) -> str:
        return f"Color is ({self.r}, {self.g}, {self.b})"
