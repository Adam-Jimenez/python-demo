import pygame

class Window:
    def __init__(self,
                 width=400,
                 height=400,
                 caption="Snek"):
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

    @property
    def screen(self):
        return self._screen

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def update(self):
        pygame.display.flip()
