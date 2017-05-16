import pygame
import form
import color

class Case:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.color = color.BLACK
        self.rect = pygame.Rect(self.x, self.y, self.game.case_width, (self.game.case_width * 3))
        self.next = None

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)

class Game:
    def __init__(self, width, case_width=10):
        self.cases = []
        self.width = width
        self.case_width = case_width
        self.screen_width = self.case_width * self.width
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_width))
        self._initialize_grill()

    def _initialize_grill(self):
        for i in range(0, self.width):
            self.cases.append([])
            for j in range(0, self.width):
                case = Case(self, i * self.case_width, j * self.case_width)
                if last_case is not None:
                    last_case.next = case
                self.cases[i].append(case)
                last_case = case

    def draw(self):
        for cases in self.cases:
            for case in cases:
                case.draw()


    def play(self):
        clock = pygame.time.Clock()
        running = True
        self.draw()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    print('fall')
                    ll.fall()
            pygame.display.flip()
            clock.tick(10)

Game(50).play()
