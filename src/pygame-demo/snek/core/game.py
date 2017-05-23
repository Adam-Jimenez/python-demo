import pygame
from .window import Window
from .objects.snake import Snake
from .objects.food import Food
from .colors import COLORS


class Game:

    def __init__(self):
        self.window = Window()
        self.elements = {}
        self.running = False
        self.fps = 10
        self.grid_division = 40

        self.elements['snake'] = Snake(self)
        self.elements['food'] = Food(self)


    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            self.handleEvents()
            self.tick()
            self.render()
            clock.tick(self.fps)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                # TODO: check if elem listens to certain events
                if event.key == pygame.K_LEFT:
                    for key, elem in self.elements.items():
                        elem.arrow_left()
                if event.key == pygame.K_RIGHT:
                    for key, elem in self.elements.items():
                        elem.arrow_right()
                if event.key == pygame.K_UP:
                    for key, elem in self.elements.items():
                        elem.arrow_up()
                if event.key == pygame.K_DOWN:
                    for key, elem in self.elements.items():
                        elem.arrow_down()

    def tick(self):
        for key, elem in self.elements.items():
            elem.tick()

        if not self.elements['snake'].alive:
            self.running = False


    def render(self):
        self.window.screen.fill(COLORS['white'])

        for key, elem in self.elements.items():
            elem.draw()

        self.window.update()
