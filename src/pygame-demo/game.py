import pygame

colors = {
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'black': (0, 0, 0),
    'gray': (50, 50, 50),
    'lightgray': (230, 230, 230)
}

class Window:
    def __init__(self,
             width=400,
             height=400,
             background='white',
             caption='Snek'):
        # Create window
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

        # Set background
        self.screen.fill(colors[background])

    def update(self):
        pygame.display.flip()

class Snake:
    def __init__(self, x=0, y=0, velocity=(0, -1)):
        self.x = x
        self.y = y
        self._velocity = velocity

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        self._velocity = velocity

    def tick(self):
        self.x += self._velocity[0]
        self.y += self._velocity[1]

class Grid:
    def __init__(self,
             window,
             snake,
             scale):
        self.grid = []
        self.window = window
        self.scale = scale
        self.snake = snake
        for x in range(window.width // scale):
            row = []
            for y in range(window.height // scale):
                row.append((x*scale, y*scale, scale, scale))
            self.grid.append(row)

    def draw(self):
        pygame.draw.rect(self.window.screen, colors['red'], (self.snake.x*self.scale, self.snake.y*self.scale, self.scale, self.scale))

        for row in self.grid:
            for rect in row:
                pygame.draw.rect(self.window.screen, colors['gray'], rect, 1)



class GameLoop:
    def __init__(self):
        self.window = Window()
        scale = 20
        self.snake = Snake(self.window.width / 2 / scale, self.window.height / 2 / scale)
        self.grid = Grid(self.window, self.snake, scale)
        self.running = True
        self.iteration_count = 0

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.velocity = (-1, 0)
                    if event.key == pygame.K_RIGHT:
                        self.snake.velocity = (1, 0)
                    if event.key == pygame.K_UP:
                        self.snake.velocity = (0, -1)
                    if event.key == pygame.K_DOWN:
                        self.snake.velocity = (0, 1)
            if self.iteration_count % 100 == 0:
                self.snake.tick()
            self.grid.draw()
            self.window.update()
            self.iteration_count += 1

game_loop = GameLoop()
game_loop.run()
