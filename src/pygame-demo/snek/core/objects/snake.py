import pygame
from .drawable import Drawable
from .gameobject import GameObject
from core.colors import COLORS
from core.eventlistener import EventListener

class Snake(Drawable, GameObject, EventListener):
    def __init__(self, game):
        self.grid_division = game.grid_division
        self.x = self.grid_division / 2
        self.y = self.grid_division / 2
        self.tail = []
        self.tail_length = 3
        self.velocity = (0, -1)
        self.node_width = game.window.width / self.grid_division
        self.node_height = game.window.height / self.grid_division

        self.game = game
        self.alive = True


    def draw(self):
        pygame.draw.rect(self.game.window.screen,
                         COLORS['red'],
                         (self.x*self.node_width,
                          self.y*self.node_height,
                          self.node_width,
                          self.node_height))
        for coord in self.tail:
            pygame.draw.rect(self.game.window.screen,
                             COLORS['red'],
                             (coord[0]*self.node_width,
                              coord[1]*self.node_height,
                              self.node_width,
                              self.node_height))


    def tick(self):
        self.move_head_to_tail()
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.game.elements['food'].coords == (self.x, self.y):
            self.game.elements['food'].setRandomCoords()
            self.tail_length += 1

        if (self.x, self.y) in self.tail:
            self.alive = False

        if self.out_of_bounds():
            self.alive = False

    def move_head_to_tail(self):
        self.tail.append((self.x, self.y))
        if len(self.tail) > self.tail_length:
            self.tail.pop(0)

    def out_of_bounds(self):
        if self.x < 0 or self.y < 0 or self.x >= self.grid_division or self.y >= self.grid_division:
            return True
        return False

    def arrow_up(self):
        self.velocity = (0, -1)

    def arrow_down(self):
        self.velocity = (0, 1)

    def arrow_left(self):
        self.velocity = (-1, 0)

    def arrow_right(self):
        self.velocity = (1, 0)
