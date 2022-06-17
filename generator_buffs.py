import pygame
import random
from pygame.sprite import Group

from Buffs import Buff_Item, Buffs


class Generator_Buffs:
    def __init__(self, screen=pygame.display.set_mode((800, 450)),
                 frequency_min=0, frequency_max=0):
        self.screen = screen
        self.frequency_min = frequency_min
        self.frequency_max = frequency_max
        self.frequency = random.randint(frequency_min, frequency_max)
        self.enums = (Buffs.HP, Buffs.Shield, Buffs.Triple_Gun)
        self.buffs = Group()
        self.count = 0

    def draw_buffs(self):
        """Отрисовка всех астероидов"""
        for buff in self.buffs:
            buff.draw()

    def make_buff(self):
        x = random.randint(10, self.screen.get_rect().width - 10)
        y = random.randint(10, self.screen.get_rect().height - 10)
        position = pygame.Vector2(x, y)

        enum = random.choice(self.enums)

        self.buffs.add(Buff_Item(enum, screen=self.screen, position=position))

    def update(self):
        if self.count > self.frequency:
            self.make_buff()
            self.frequency = random.randint(self.frequency_min,
                                            self.frequency_max)
            self.count = 0
        self.count += 1
