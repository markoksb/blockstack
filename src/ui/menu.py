import pygame
from .button import Button

SPACE = 5
SPACE_TOP = 50
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 30
BUTTON_COLOR = (47, 47, 47, 255)
BUTTON_HOVER_COLOR = (47, 47, 127, 255)
BUTTON_TEXT_COLOR = (255, 255, 255, 255)

class Menu:
    def __init__(self, parent, name: str) -> None:
        self.__active: bool = True
        self.__parent = parent
        self.__width: int = 300
        self.__height: int = 175
        self.__msg: str = name
        self.__surface = pygame.Surface((self.__width, self.__height), pygame.SRCALPHA, 32)
        #self.__surface.fill( (0,0,0,0) )
        self.__buttons: list = []
        self.__buttons.append(Button(self.__width // 2 - BUTTON_WIDTH // 2, SPACE_TOP, BUTTON_WIDTH, BUTTON_HEIGHT, "Play", BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR, self.start_game))
        self.__buttons.append(Button(self.__width // 2 - BUTTON_WIDTH // 2, SPACE_TOP + BUTTON_HEIGHT + SPACE, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit", BUTTON_COLOR, BUTTON_HOVER_COLOR, (191, 0, 0), self.__parent.quit))

    def get_surface(self):
        return self.__surface
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def get_x(self):
        return self.__parent.width // 2 - self.get_width() // 2
    def get_y(self):
        return self.__parent.height // 2 - self.get_height() // 2
    def get_buttons(self):
        return self.__buttons
    
    def draw(self, surface):
        """ ui render """
        menu_rect = pygame.Rect(0, 0, self.__width, self.__height)
        menu_color = pygame.Color(91, 63, 91, 175)
        pygame.draw.rect(self.__surface, menu_color, menu_rect, border_radius=2)
        pygame.font.init()
        font = pygame.font.Font(None, 28)
        font_surf = font.render(self.__msg, True, (255, 255, 255))
        self.__surface.blit(font_surf, (self.__width // 2 - font_surf.get_width() // 2, 10))
        for button in self.__buttons:
            button.draw(self.__surface)

        surface.blit(self.get_surface(), (self.get_x(), self.get_y(), self.get_width(), self.get_height()) )

    def show(self) -> None:
        """show the ui"""
        self.__msg = f"pause"
        self.__active = True
        
    def hide(self) -> None:
        """hide the ui"""
        self.__active = False

    def is_active(self) -> bool:
        """is the ui active?"""
        return self.__active
    
    def start_game(self):
        self.__active = False
        if self.__msg != f"pause":
            self.__parent.reset()
    
    def reset(self, points) -> None:
        self.__active = True
        self.__msg = f"Game Over! You got {points} points!"
        