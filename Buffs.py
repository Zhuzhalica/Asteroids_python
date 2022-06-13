from enum import Enum
import pygame


class Buff_Item:
    def __init__(self, image):
        self.image = image


class Buffs(Enum):
    Shield = Buff_Item(pygame.transform.scale(pygame.image.load("assets/image/space-ship-protected.png"), (50, 50)))
    HP = Buff_Item(pygame.transform.scale(pygame.image.load("assets/image/space-ship.png"), (30, 30)))
    Triple_Gun = Buff_Item(pygame.transform.scale(pygame.image.load("assets/image/bullet.png"), (30, 30)))