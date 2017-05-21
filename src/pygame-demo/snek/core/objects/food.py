import pygame
from .drawable import Drawable
from random import randint
from .gameobject import GameObject
from core.colors import COLORS
from core.eventlistener import EventListener

class Food(Drawable, GameObject, EventListener):

    def __init__(self, game):
        self.grid_division = game.grid_division
        self.game = game
        self.coords = self.randomCoords()
        self.node_width = game.window.width / self.grid_division
        self.node_height = game.window.height / self.grid_division

    def randomCoords(self):
        possibilities = []
        for i in range(0, self.grid_division):
            for j in range(0, self.grid_division):
                snake = self.game.elements['snake']
                if snake.x != j and snake.y != i:
                    possibilities.append((j, i))

        return possibilities[randint(0, len(possibilities))]

    def setRandomCoords(self):
        self.coords = self.randomCoords()

    def draw(self):
        pygame.draw.rect(self.game.window.screen,
                         COLORS['black'],
                         (self.coords[0]*self.node_width,
                         self.coords[1]*self.node_height,
                         self.node_width,
                         self.node_height))


