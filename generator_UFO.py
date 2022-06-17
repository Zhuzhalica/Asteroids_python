import pygame
import random
from pygame.sprite import Group

from UFO import UFO


class Generator_UFO:
    def __init__(self, screen=pygame.display.set_mode((800, 450)),
                 frequency_min=0, frequency_max=0):
        self.screen = screen
        self.frequency_min = frequency_min
        self.frequency_max = frequency_max
        self.frequency = random.randint(frequency_min, frequency_max)
        self.ufos = Group()
        self.count = 0

    def draw_asteroid(self):
        """Отрисовка всех астероидов"""
        for ufo in self.ufos:
            ufo.draw()

    def make_UFO(self):
        start_position = (
            pygame.Vector2(
                0,
                random.randint(0,
                               self.screen.get_rect().bottom)),
            pygame.Vector2(
                self.screen.get_rect().right,
                random.randint(0,
                               self.screen.get_rect().bottom)))

        self.ufos.add(UFO(self.screen, random.choice(start_position)))

    def update(self):
        if self.count > self.frequency:
            self.make_UFO()
            self.frequency = random.randint(self.frequency_min, self.frequency_max)
            self.count = 0
        self.count += 1

        self.ufos.update()
