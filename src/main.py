import pygame
from board import Board
from ui.menu import Menu

class App:
    def __init__(self, name: str, width: int = 720, height: int = 1080): #640 x 360
        self.__running: bool = False
        self.__display_surface = None
        self.__name: str = name
        self.__width: int = width
        self.__height: int = height
        self.__size = (self.__width, self.__height)
        self.__game_objects: list = []
        self.__board: Board = None
        self.__menu: Menu = None
        self.__ft: int = 0
        self.__update_timer: int = 300

    def on_init(self):
        pygame.init()
        self.__display_surface = pygame.display.set_mode( self.__size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SRCALPHA, 32 )
        self.__caption = pygame.display.set_caption(self.__name)
        self.__clock = pygame.time.Clock()
        self.__board = Board(self)
        self.__menu = Menu(self, self.__name)
        self.running = True

    def on_keypress(self, key):
        if key == pygame.K_a or key == pygame.K_LEFT:
            self.board.move_shape(-1, 0)
        if key == pygame.K_d or key == pygame.K_RIGHT:
            self.board.move_shape(1, 0)
        if key == pygame.K_w or key == pygame.K_UP:
            self.board.rotate_shape(1)
        if key == pygame.K_s or key == pygame.K_DOWN:
            self.board.move_shape(0, 1)
        if key == pygame.K_ESCAPE:
            if self.__menu.is_active():
                self.__menu.hide()
            else:
                self.__menu.show()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return
        
        if event.type == pygame.KEYDOWN:
            self.on_keypress(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.menu.is_active():
                for button in self.menu.get_buttons():
                    if button.get_rect().left + self.menu.get_x() < pos[0] and button.get_rect().right + self.menu.get_x() > pos[0] and\
                        button.get_rect().top + self.menu.get_y() < pos[1] and button.get_rect().bottom + self.menu.get_y() > pos[1]:
                        button.activate()

    def update(self, dt: int) -> None:
        if self.board.game_over():
            self.__menu.reset(0)
            return
        
        if self.menu.is_active():
            return

        self.__ft += dt
        if self.__ft >= self.__update_timer:
            self.__ft = 0
            self.board.update(self.__ft)

    def render(self) -> None:
        # fill the background
        self.window.fill((16,16,16))

        # render game objects
        for item in self.game_objects:
            item.render()

        # render ui
        if self.menu.is_active():
            self.menu.draw(self.__display_surface)

        # present
        pygame.display.update()

    def cleanup(self) -> None:
        pygame.quit()

    def run(self) -> None:
        """ initialization and loop """
        self.on_init()

        while self.running:
            dt = self.__clock.tick(120)
            for event in pygame.event.get():
                self.on_event(event)
            self.update(dt)
            self.render()
        self.cleanup()

    def quit(self) -> None:
        """ exiting gameloop """
        self.__running = False
    
    def reset(self) -> None:
        """ start new game """
        self.__board = Board(self)

    def register_game_object(self, obj) -> None:
        """ register object to renderqueue """
        self.__game_objects.append(obj)

    @property
    def game_objects(self) -> list:
        return self.__game_objects    

    @property
    def board(self) -> Board:
        return self.__board
    
    @property
    def menu(self) -> Menu:
        return self.__menu    

    @property
    def window(self) -> pygame.Surface:
        return self.__display_surface
    
    @property
    def running(self) -> bool:
        return self.__running
    @running.setter
    def running(self, running: bool) -> None:
        self.__running = running

    @property
    def width(self) -> int:
        return self.__width
    @property
    def height(self) -> int:
        return self.__height


if __name__ == "__main__":
    app = App("BlockStack")
    app.run()
