import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, func):
        self.__rect = pygame.Rect(x, y, width, height)
        self.__width = width
        self.__height = height
        self.__text = text
        self.__color = color
        self.__hover_color = hover_color
        self.__text_color = text_color
        self.__action = func
        self.__hovered = False

    def get_rect(self) -> pygame.Rect:
        return self.__rect
    
    def activate(self) -> None:
        self.__action()

    def on_mouse_over(self) -> None:
        self.__hovered = True
    def on_mouse_exit(self) -> None:
        self.__hovered = False

    def draw(self, surface):
        if self.__hovered:
            pygame.draw.rect(surface, self.__hover_color, self.__rect, border_radius=5)
        else:
            pygame.draw.rect(surface, self.__color, self.__rect, border_radius=5)
        font = pygame.font.Font(None, 28)
        font_surf = font.render(self.__text, True, self.__text_color)
        surface.blit(font_surf, font_surf.get_rect(center=self.__rect.center))