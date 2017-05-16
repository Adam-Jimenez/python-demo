import pygame
import color

class Ll:
    def __init__(self, cases):
        self.cases = cases
        self.set_color(color.BLACK)

    def set_color(self, color):
        for case in self.cases:
            case.color = color

    def fall(self):
        for case in self.cases:
            case = case.next
