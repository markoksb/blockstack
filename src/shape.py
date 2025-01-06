from tile import Tile
from color import Color
from position import Position

class Shape:
    def __init__(self, type: int = 0, falling: bool = True) -> None:
        self.__tiles: list[Tile] = []
        self.__falling: bool = falling
        self.__index: int = 0
        self.__set_type(type)

    @property
    def tiles(self) -> list[Tile]:
        return self.__tiles
    
    def change_pos(self, x_offset: int, y_offset: int) -> None:
        for tile in self.__tiles:
            tile.change_pos(x_offset, y_offset)
    
    def rotate(self, direction: int = 1) -> None:
        anchor = Position(min(t.position.x for t in self.tiles), min(t.position.y for t in self.tiles))
        relative = [ Position(t.position.x - anchor.x, t.position.y - anchor.y) for t in self.tiles ]
        if direction == 1:
            new_positions = [ Position(p.y, -p.x) for p in relative ]
        else:
            new_positions = [ Position(-p.y, p.x) for p in relative ]

        for i, new_pos in enumerate(new_positions):
            self.__tiles[i].set_pos(new_pos.x + anchor.x, new_pos.y + anchor.y)

    @property
    def left_most(self) -> int:
        return min(t.position.x for t in self.tiles)
    
    @property
    def right_most(self) -> int:
        return max(t.position.x for t in self.tiles)
    
    @property
    def lowest(self) -> int:
        return max(t.position.y for t in self.tiles)
    
    @property
    def is_falling(self) -> bool:
        return self.__falling
    
    def stop(self) -> None:
        self.__falling = False
    
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index >= len( self.__tiles ):
            raise StopIteration
        item = self.__tiles[self.__index]
        self.__index += 1
        return item
        
    def __set_type(self, type: int = 0) -> None:
        match type:
            case 0:
                self.__tiles.append( Tile( Position(4, 1), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(5, 1), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(6, 1), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(5, 0), Color.set_color(255, 0, 0) ) )
            case 1:
                self.__tiles.append( Tile( Position(4, 0), Color.set_color(255, 255, 0) ) )
                self.__tiles.append( Tile( Position(4, 1), Color.set_color(255, 255, 0) ) )
                self.__tiles.append( Tile( Position(5, 0), Color.set_color(255, 255, 0) ) )
                self.__tiles.append( Tile( Position(5, 1), Color.set_color(255, 255, 0) ) )
            case 2:
                self.__tiles.append( Tile( Position(4, 0), Color.set_color(0, 127, 255) ) )
                self.__tiles.append( Tile( Position(5, 0), Color.set_color(0, 127, 255) ) )
                self.__tiles.append( Tile( Position(6, 0), Color.set_color(0, 127, 255) ) )
                self.__tiles.append( Tile( Position(6, 1), Color.set_color(0, 127, 255) ) )
            case 3:
                self.__tiles.append( Tile( Position(5, 0), Color.set_color(0, 255, 127) ) )
                self.__tiles.append( Tile( Position(6, 0), Color.set_color(0, 255, 127) ) )
                self.__tiles.append( Tile( Position(7, 0), Color.set_color(0, 255, 127) ) )
                self.__tiles.append( Tile( Position(5, 1), Color.set_color(0, 255, 127) ) )
            case 4:
                self.__tiles.append( Tile( Position(4, 0), Color.set_color(191, 191, 191) ) )
                self.__tiles.append( Tile( Position(5, 0), Color.set_color(191, 191, 191) ) )
                self.__tiles.append( Tile( Position(5, 1), Color.set_color(191, 191, 191) ) )
                self.__tiles.append( Tile( Position(6, 1), Color.set_color(191, 191, 191) ) )
            case 5:
                self.__tiles.append( Tile( Position(4, 1), Color.set_color(191, 127, 191) ) )
                self.__tiles.append( Tile( Position(5, 1), Color.set_color(191, 127, 191) ) )
                self.__tiles.append( Tile( Position(5, 0), Color.set_color(191, 127, 191) ) )
                self.__tiles.append( Tile( Position(6, 0), Color.set_color(191, 127, 191) ) )
            case 6:
                self.__tiles.append( Tile( Position(3, 0), Color.set_color(255, 255, 255) ) )
                self.__tiles.append( Tile( Position(4, 0), Color.set_color(255, 255, 255) ) )
                self.__tiles.append( Tile( Position(5, 0), Color.set_color(255, 255, 255) ) )
                self.__tiles.append( Tile( Position(6, 0), Color.set_color(255, 255, 255) ) )
            case _:
                self.__tiles.append( Tile( Position(0, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(1, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(2, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(3, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(4, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(5, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(6, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(7, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(8, 0), Color.set_color(255, 0, 0) ) )
                self.__tiles.append( Tile( Position(9, 0), Color.set_color(255, 0, 0) ) )
    

